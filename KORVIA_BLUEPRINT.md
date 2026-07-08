# Korvia Blueprint

> Single source of truth for the Korvia QR hospitality ecosystem.  
> Status: prototype complete, backend pending server availability.

---

## 1. Overview

**Korvia** is a QR-first hospitality operating system for restaurants, hotels, and events in East Africa. It replaces printed menus, manual order taking, and fragmented payment workflows with a single mobile-first platform.

**Tagline:** *Karibu, tukuhudumie* — Welcome, let us serve you.

### 1.1 Vision

Become the default digital infrastructure for hospitality venues in emerging markets: low setup cost, no hardware required, and a marketplace that brings venues new customers.

### 1.2 Why it wins

- **Zero-friction ordering:** customers scan a QR, order, and pay without downloading an app or waiting for staff.
- **Operations control:** staff, managers, and owners each get a focused dashboard.
- **Discovery channel:** the Client Hub marketplace helps venues be found by new customers.
- **Localized:** built for mobile money, multi-vendor events, and Swahili-market service culture.

---

## 2. Product Verticals

Korvia runs one core engine with three vertical faces:

| Vertical | Spot type | Primary use case |
|----------|-----------|------------------|
| **Restaurants** | `table` | QR menus, table ordering, kitchen display, tips |
| **Hotels** | `room` | Room service, amenities, guest requests |
| **Events** | `stall` | Multi-vendor ordering, fast checkout, crowd payments |

A single venue can operate in one or more verticals. For example, a hotel may have a restaurant (tables) and guest rooms (rooms) under the same account.

---

## 3. User Roles & Permissions

| Role | Capabilities |
|------|--------------|
| **Guest / Customer** | Browse menu, order, pay, split bill, tip, rate, request help |
| **Staff / Cook** | Edit menu in Menu Studio, manage item availability, view kitchen display |
| **Waitress / Waiter** | Serve assigned tables/rooms, update order status, collect payment, resolve guest requests |
| **Manager** | Monitor live orders, table status, staff roster, stock alerts, daily operations |
| **Owner** | View analytics, projections, feedback, manage subscription/billing, generate promo QR codes |
| **Platform Admin** (Korvia team) | Onboard venues, moderate marketplace, manage payouts, feature venues |

### 3.1 Permission matrix (high level)

| Resource | Guest | Staff | Waiter | Manager | Owner | Admin |
|----------|-------|-------|--------|---------|-------|-------|
| View menu | own venue only | own venue | own venue | own venue | own venue | all |
| Place order | own session | no | no | no | no | no |
| Update menu | no | yes | no | yes | yes | no |
| Manage orders | no | kitchen only | assigned spots | yes | yes | read-only |
| View analytics | no | no | no | partial | full | all |
| Manage staff | no | no | no | yes | yes | no |
| Billing | no | no | no | no | yes | admin only |
| Feature in Client Hub | no | no | no | no | opt-in | yes |

---

## 4. User Journeys

### 4.1 Customer journey

1. **Discovery** — finds venue on Client Hub or walks in and scans a printed QR code.
2. **Menu access** — QR opens a menu scoped to a specific `spot` (Table 5, Room 203, Stall 12).
3. **Ordering** — adds items, selects modifiers, applies promo codes.
4. **Checkout** — chooses payment method, can split bill with others at the same spot.
5. **Tracking** — sees real-time order status (`new` → `preparing` → `ready` → `served` → `paid`).
6. **Post-order** — tips staff, receives digital receipt, leaves feedback.

### 4.2 Staff / operations journey

1. **Venue onboarding** — owner registers, selects vertical(s), configures branding and payment methods.
2. **Menu setup** — staff/owner builds categories and items in the Menu Studio, uploads photos.
3. **QR deployment** — manager/owner generates and prints QR codes for each spot.
4. **Order flow** — customer order appears on kitchen display; staff updates status as it progresses.
5. **Service** — waitress gets notified when order is ready, serves it, marks served, collects payment.
6. **Management** — manager monitors table turnover, stock alerts, and staff workload in real time.
7. **Growth** — owner reviews sales analytics, top items, projected income, and runs promo QR campaigns.

---

## 5. Data Model

### 5.1 Core entities

```
Account
├── id, email, phone, name, role
├── created_at, updated_at
└── belongs_to Venue (optional for platform admins)

Venue
├── id, name, slug, type (restaurant | hotel | event | mixed)
├── location: { address, city, country, lat, lon }
├── contact: { phone, email, social_links }
├── branding: { logo, primary_color, accent_color }
├── settings: { currency, tax_rate, service_charge, tips_enabled }
├── payment_methods: [mpesa, card, cash]
├── subscription_tier
├── is_active, is_verified, is_featured
└── has many Spots, Menus, Staff, Orders

Spot
├── id, venue_id, label, type (table | room | stall)
├── qr_code_url, qr_code_image_url
├── status (free | occupied | cleaning | out_of_order)
├── capacity, assigned_staff_id
└── current_session_id (nullable)

Menu
├── id, venue_id, name, is_active
└── has many Categories

Category
├── id, menu_id, name, sort_order
└── has many MenuItems

MenuItem
├── id, category_id, name, description, price
├── photo_url, is_available, is_featured
├── modifiers: [{ name, options: [{ label, price }] }]
├── allergens, dietary_tags, prep_time_minutes
└── stock_count (optional)

Order
├── id, venue_id, spot_id, session_id
├── customer: { name, phone, device_id }
├── items: [OrderItem]
├── status (new | preparing | ready | done | paid | cancelled)
├── payment_status (pending | paid | failed | refunded)
├── total, tax, service_charge, discount, tip
├── payment_method, transaction_reference
├── promo_code_id
├── created_at, updated_at
└── belongs_to Staff (assigned, optional)

OrderItem
├── id, menu_item_id, name, quantity, unit_price
├── modifiers: [{ name, option, price }]
└── subtotal

Payment
├── id, order_id, amount, method, status
├── provider_reference, provider_response
├── paid_at, refunded_at

StaffProfile
├── id, account_id, venue_id, role
├── assigned_spots, shift_start, shift_end
├── tips_earned
└── is_active

Feedback
├── id, venue_id, order_id, rating, comment, tags
├── created_at

Promo
├── id, venue_id, code, discount_type, discount_value
├── usage_limit, used_count, valid_from, valid_until
├── qr_code_url

CustomerRequest
├── id, venue_id, spot_id, type (help | bill | refill | custom)
├── message, status (open | resolved), created_at

ClientHubListing
├── venue_id, display_name, description, photos
├── tags, average_rating, review_count
├── is_featured, featured_until
└── search_index
```

### 5.2 Key relationships

- A `Venue` has many `Spots`, `Menus`, `StaffProfiles`, and `Orders`.
- A `Spot` belongs to one `Venue` and has many `Orders` over time.
- An `Order` belongs to a `Spot` and contains many `OrderItems`.
- A `MenuItem` belongs to a `Category`, which belongs to a `Menu`.
- `Payments` are linked to `Orders`.
- `Feedback` is optionally linked to an `Order`.

---

## 6. API Specification

Base URL: `https://api.korvia.io/v1`

Authentication: JWT in `Authorization: Bearer <token>` header.

### 6.1 Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Create account |
| POST | `/auth/login` | Email/phone + password or OTP |
| POST | `/auth/refresh` | Refresh access token |
| POST | `/auth/otp` | Request OTP login |
| POST | `/auth/verify-otp` | Verify OTP and issue tokens |

### 6.2 Venues

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/venues` | Create venue (owner/admin) |
| GET | `/venues/:id` | Get venue details |
| PATCH | `/venues/:id` | Update venue settings |
| GET | `/venues/:id/stats` | Get dashboard stats |
| GET | `/venues/:id/analytics` | Sales analytics |

### 6.3 Spots & QR codes

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/venues/:id/spots` | Create spot |
| GET | `/venues/:id/spots` | List spots |
| PATCH | `/spots/:id` | Update spot status |
| POST | `/spots/:id/qr` | Generate/regenerate QR code |
| GET | `/spots/:id/menu` | Public menu for a spot |

### 6.4 Menus

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/venues/:id/menus` | Create menu |
| GET | `/venues/:id/menus` | List menus |
| PATCH | `/menus/:id` | Update menu |
| POST | `/menus/:id/categories` | Add category |
| POST | `/categories/:id/items` | Add menu item |
| PATCH | `/items/:id` | Update item / availability |
| DELETE | `/items/:id` | Delete menu item |

### 6.5 Orders

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/spots/:id/orders` | Create order from customer session |
| GET | `/venues/:id/orders` | List venue orders (with filters) |
| GET | `/orders/:id` | Get order details |
| PATCH | `/orders/:id/status` | Update order status |
| PATCH | `/orders/:id/assign` | Assign staff to order |
| POST | `/orders/:id/pay` | Initiate payment |
| POST | `/orders/:id/split` | Split bill |

### 6.6 Staff

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/venues/:id/staff` | Invite staff |
| GET | `/venues/:id/staff` | List staff |
| PATCH | `/staff/:id` | Update staff role/assignment |
| DELETE | `/staff/:id` | Remove staff |

### 6.7 Payments

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/payments/initiate` | Start payment |
| POST | `/payments/callback` | Provider callback |
| POST | `/payments/:id/refund` | Refund payment |
| GET | `/venues/:id/payouts` | Payout history |

### 6.8 Feedback & requests

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/orders/:id/feedback` | Submit feedback |
| GET | `/venues/:id/feedback` | List feedback |
| POST | `/spots/:id/requests` | Create customer request |
| GET | `/venues/:id/requests` | List customer requests |
| PATCH | `/requests/:id/resolve` | Resolve request |

### 6.9 Client Hub (marketplace)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/hub/venues` | Discover venues (search, filter, near me) |
| GET | `/hub/venues/:id` | Public venue profile |
| GET | `/hub/featured` | Featured venues |
| POST | `/hub/venues/:id/claim` | Claim a venue listing (admin) |

### 6.10 QR code generation

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/spots/:id/qr` | Generate QR image for a spot |
| GET | `/spots/:id/qr` | Retrieve existing QR image URL |
| POST | `/venues/:id/qr/bulk` | Bulk-generate QR codes for all spots |

**Implementation note:** QR codes must be generated server-side, stored in object storage (R2/S3), and linked to the spot record. The encoded URL must follow the public menu format: `https://korvia.io/m/{venue_slug}/{spot_code}`. A dedicated QR generation service/module is required.

---

## 7. Real-Time Architecture

The kitchen, waitress, and manager dashboards must update instantly when orders change.

### 7.1 Recommended approach

**Primary:** WebSockets (Socket.io or native WS) per venue room.

**Fallback:** Server-Sent Events (SSE) for simpler one-way update streams.

### 7.2 Events

```
order:created       { order }
order:updated       { order_id, status, assigned_to }
order:paid          { order_id, payment }
spot:updated        { spot_id, status }
request:created     { request }
request:resolved    { request_id }
menu:updated        { venue_id }
```

### 7.3 Room model

- Each venue has a room: `venue:<venue_id>`.
- Staff, managers, and owners join the venue room.
- Customers join a temporary session room: `session:<session_id>`.
- Auth middleware validates the token and role before allowing room joins.

---

## 8. Authentication & Authorization

### 8.1 Auth methods

- **Email + password** for owners and managers.
- **Phone OTP** for quick staff onboarding and guest checkout.
- **Magic link** optional for owners.

### 8.2 JWT claims

```json
{
  "sub": "account_id",
  "venue_id": "venue_id",
  "role": "owner | manager | waiter | staff | admin",
  "permissions": ["read:orders", "write:menu"]
}
```

### 8.3 Middleware

- `requireAuth` — valid JWT.
- `requireRole(...roles)` — role-based access.
- `requireVenueAccess` — user belongs to the requested venue.

---

## 9. Payments & Monetization

### 9.1 Revenue streams

1. **SaaS subscription** — tiered by spot count and features.
2. **Transaction fee** — percentage per paid order.
3. **Client Hub featured listings** — venues pay to be promoted.
4. **Premium add-ons** — AI menu polish, advanced analytics, loyalty program.

### 9.2 Payment providers

- **M-Pesa** — primary mobile money provider.
- **Card payments** — Stripe or Paystack.
- **Cash** — recorded manually for reporting.

### 9.3 Fee structure

- Customer pays menu price + tax/service charge.
- Korvia deducts transaction fee before settling to venue.
- Venue receives payouts to configured bank/mobile money account.

---

## 10. Client Hub Marketplace

The Client Hub is Korvia's discovery channel and long-term moat.

### 10.1 Features

- Search venues by name, cuisine, city, or current location.
- Filter by vertical: restaurants, hotels, events.
- Show live status (open now, event today).
- Display ratings, photos, and tags.
- Deep-link directly into a venue's menu.

### 10.2 Monetization

- **Free listing:** every active venue appears.
- **Featured placement:** venues pay for top placement and badges.
- **Verified badge:** optional paid verification.

### 10.3 SEO

- Public venue pages should be server-rendered or pre-rendered for search indexing.
- Each venue gets a public slug: `korvia.io/v/sunset-bistro`.

---

## 11. AI Tools

The prototype hints at an AI tools tab. Recommended AI features:

| Feature | Value |
|---------|-------|
| **Menu polish** | Rewrite item descriptions and suggest pricing |
| **Photo enhancer** | Auto-crop and improve menu photos |
| **Sales forecaster** | Predict busy hours and recommended stock levels |
| **Smart promo suggestions** | Suggest discounts based on slow-moving items |
| **Review sentiment** | Summarize customer feedback and flag issues |
| **Smart replies** | Auto-respond to common customer requests |
| **Inventory alerts** | Predict when items will run out |
| **Upsell recommendations** | Suggest pairings to increase basket size |
| **Multilingual menu** | Translate menu to English/Swahili/other |

---

## 12. Tech Stack Recommendations

### 12.1 Backend

| Layer | Recommendation | Rationale |
|-------|----------------|-----------|
| Runtime | Node.js (Express/NestJS) or Python (FastAPI/Django) | Team preference; both scale well |
| Database | PostgreSQL | Relational data with complex joins |
| Cache | Redis | Sessions, real-time presence, rate limiting |
| Real-time | Socket.io or native WebSockets | Venue room broadcasts |
| Queue | BullMQ / Celery / RabbitMQ | Payment callbacks, payouts, emails |
| Storage | Cloudflare R2 / AWS S3 | Menu photos, QR images |
| Search | PostgreSQL full-text or Meilisearch | Client Hub search |
| Auth | Custom JWT + bcrypt/Argon2 | Full control over roles |
| QR generation | `qrcode` (Node.js) or `qrcode` + Pillow (Python) | Server-side QR creation |

### 12.2 Frontend

| Layer | Recommendation |
|-------|----------------|
| Customer menu | Next.js or Remix (SEO + mobile performance) |
| Dashboards | React or Next.js with TanStack Query |
| Styling | Korvia design tokens (existing CSS) migrated to Tailwind or CSS variables |
| Mobile app | PWA first; native iOS/Android later if needed |

### 12.3 DevOps

| Layer | Recommendation |
|-------|----------------|
| Hosting | DigitalOcean, Railway, or Hetzner |
| Database | Managed PostgreSQL (Supabase, Neon, or AWS RDS) |
| CDN | Cloudflare |
| CI/CD | GitHub Actions |
| Monitoring | Sentry + UptimeRobot |

---

## 13. Security & Compliance

- All API traffic over HTTPS.
- JWTs short-lived (15 min), refresh tokens rotated.
- Passwords hashed with Argon2.
- Rate limiting on auth and payment endpoints.
- Input validation and SQL injection prevention.
- File uploads scanned and restricted to images.
- PCI-DSS awareness: avoid storing card data; use provider tokenization.
- GDPR/privacy compliance for customer data.
- Audit log for order status changes and payments.

---

## 14. Implementation Roadmap

### Phase 1: Backend foundation

- [ ] Database schema and migrations
- [ ] Auth system (register, login, OTP, roles)
- [ ] Venue and spot management
- [ ] Menu CRUD with categories and items
- [ ] QR code generation service (server-side, stored images, bulk generation)

### Phase 2: Order engine

- [ ] Order creation and lifecycle
- [ ] Real-time order updates via WebSockets
- [ ] Kitchen display integration
- [ ] Waitress and manager dashboards wired to API

### Phase 3: Payments

- [ ] M-Pesa integration
- [ ] Card payments via Paystack/Stripe
- [ ] Split bill and tips
- [ ] Payouts to venues

### Phase 4: Marketplace

- [ ] Client Hub search and discovery
- [ ] Public venue pages
- [ ] Featured listings and admin moderation

### Phase 5: Growth tools

- [ ] Feedback dashboard
- [ ] Promo QR codes
- [ ] Loyalty program
- [ ] AI tools integration

---

## 15. Migration from Prototype

The existing static prototype in `~/github-recovery/korvia` is a functional UX reference. Migration steps:

1. Keep the HTML/CSS demos as a **design reference** and ** stakeholder demo**.
2. Replace `localStorage` calls with API client functions.
3. Build the real customer menu and dashboards as React/Next.js apps.
4. Reuse `korvia.css` design tokens in the new frontend.
5. Gradually retire demo pages as real features ship.

---

## 16. Open Questions

1. Which payment provider is the priority for launch — M-Pesa, Paystack, or Stripe?
2. Should the customer menu be a PWA or a responsive web app?
3. What is the target launch region — Tanzania first, then expand?
4. Should Korvia offer a free tier, or start with a paid trial?
5. Which backend language/framework does the team prefer?

---

*Last updated: 2026-07-08*

### QR code generation reminder

A dedicated QR code generation instrument must be implemented when backend development begins. See sections 6.10 and 12.1 for requirements and tool recommendations.
