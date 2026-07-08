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
| **Waitress / Waiter** | View all live orders, serve any table/room, update order status, collect payment, resolve guest requests |
| **Manager** | Monitor all live orders, table status, staff roster, stock alerts, daily operations; access historical revenue only if owner grants permission |
| **Owner** | View analytics, projections, feedback, manage subscription/billing, generate promo QR codes |
| **Platform Admin** (Korvia team) | Onboard venues, moderate marketplace, manage payouts, feature venues |

### 3.1 Permission matrix (high level)

| Resource | Guest | Staff | Waiter | Manager | Owner | Admin |
|----------|-------|-------|--------|---------|-------|-------|
| View menu | own venue only | own venue | own venue | own venue | own venue | all |
| Place order | own session | no | no | no | no | no |
| Update menu | no | yes | no | yes | yes | no |
| View all live orders | no | kitchen only | yes | yes | yes | read-only |
| Update order status | no | kitchen only | yes (serve/collect) | yes | yes | no |
| View historical orders | no | no | no | owner-granted | yes | read-only |
| View revenue / payouts | no | no | no | owner-granted | yes | admin only |
| Manage staff | no | no | no | yes | yes | no |
| Billing | no | no | no | no | yes | admin only |
| Feature in Client Hub | no | no | no | no | opt-in | yes |

### 3.2 Cross-venue isolation and sensitive data

#### Order visibility rule

Waiters and waitresses can **view all live orders**, not only their assigned tables. This prevents missed orders and avoids blame when an assigned waiter does not see an order that another staff member could have handled. However, they can only update status on orders they are serving or collecting payment for.

#### Sensitive financial data

- **Owner** has full access to revenue, payouts, projections, and historical analytics by default.
- **Manager** sees only operational numbers needed to run the shift (active orders, occupied tables, today's sales).
- **Historical revenue, profit margins, and payout data** are owner-only by default.
- Owner can grant managers expanded financial access in venue settings if needed.
- **Sensitive actions** — refunds, price changes, payout requests, staff role changes — can require owner OTP approval.

#### Cross-venue login prevention

1. **Global account, per-venue access.** One `Account` per email/phone. A user can have multiple `StaffProfile` records, each tied to a different venue and role.
2. **Invitation-only access.** Staff cannot self-register for a venue. The owner or manager invites them by email/phone and assigns a role. The invitation is tied to a single venue.
3. **JWT contains `venue_id`.** After login, if the user belongs to multiple venues, they pick one. Every API request enforces `WHERE venue_id = jwt.venue_id`.
4. **Role-based filtering.** Even within a venue, endpoints filter data by role. A waiter cannot view billing or manage staff.
5. **No URL guessing.** Direct object references (e.g., `/orders/123`) verify both ownership and role before returning data.

#### Staff onboarding and owner approval

Staff cannot join a venue without explicit owner approval. The flow ensures every staff member is tied to a real restaurant and approved by the owner.

1. **Owner or manager invites staff.** They enter:
   - Full name (e.g., Anna)
   - Email or phone
   - Role (waiter, manager, kitchen, etc.)
   - Venue (always the current venue)
   - Optional: assigned spots

2. **System sends approval request to the restaurant's owner email.** For management roles (manager, owner-level permissions), the owner must approve via OTP sent to the restaurant's registered email.

3. **Staff receives invitation.** After owner approval, the invited person gets an email/SMS with a secure link to accept the invitation and set their own password.

4. **Staff creates password and account.** Their `Account` is created and linked to the venue via a `StaffProfile`.

5. **Staff logs in.** They use their email/phone + password. The JWT is scoped to the venue they were invited to.

6. **Manager vs owner approval.**
   - Managers can invite waiters and kitchen staff.
   - Only owners can invite other managers or approve management-level invites.
   - All manager invites require owner OTP approval via the restaurant email.

7. **Revocation.** Owners can revoke staff access at any time, which invalidates the `StaffProfile` and JWTs.

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
├── id, email, phone, name (e.g., Anna)
├── password_hash, email_verified, phone_verified
├── role (super_admin)
├── created_at, updated_at
└── has many StaffProfiles (one per venue)

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
├── id, account_id, venue_id
├── role (owner | manager | waiter | staff | kitchen)
├── worker_handle: "anna" (unique per venue, used at staff login)
├── permissions: ["view:all_orders", "edit:menu", "view:revenue"]
├── assigned_spots (optional)
├── tips_earned
├── invitation_status (pending | active | revoked)
├── created_by_owner_id
├── approved_by_owner_id
└── is_active

Invitation
├── id, venue_id, email, phone, role
├── worker_handle (suggested login handle)
├── invited_by, token, expires_at
└── status (pending | accepted | expired | revoked)

WorkerAuthAttempt
├── id, venue_id, staff_profile_id
├── worker_handle, restaurant_username, restaurant_email
├── manager_or_owner_id, otp_code, otp_sent_to
├── ip_address, device_fingerprint
├── status (pending | approved | denied | expired)
└── created_at, resolved_at

Shift
├── id, venue_id, staff_profile_id
├── started_at, ended_at
├── start_auth_attempt_id, end_auth_attempt_id
├── device_fingerprint
└── orders_served_count, tips_earned

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
| POST | `/staff-auth/lookup` | Look up worker by handle + venue + email |
| POST | `/staff-auth/otp` | Request manager/owner OTP |
| POST | `/staff-auth/verify` | Verify OTP, issue JWT, start shift |
| POST | `/staff-auth/logout` | End shift and invalidate token |
| GET | `/venues/:id/shifts` | List shifts |
| POST | `/shifts/:id/end` | Force-end shift |

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

- **Email + password** — every staff member, manager, and owner has a personal account with name, email, and password.
- **Phone OTP** — for quick staff onboarding and guest checkout.
- **Magic link** — optional for owners.

Every login identifies **who** the person is (e.g., Anna), **which venue** they belong to, and **what role** they have there. A user can work at multiple venues with the same identity but different roles.

### 8.2 Login flow

1. User enters email/phone + password (or requests OTP).
2. System authenticates the `Account` and looks up active `StaffProfile` records.
3. If no venue is found, access is denied.
4. If one venue, the JWT is issued with `venue_id`, `staff_profile_id`, `role`, and `name`.
5. If multiple venues, the user picks a venue and receives a token scoped to that venue.

### 8.3 Multi-venue switching

- A user can belong to multiple venues (e.g., Anna works at two restaurants).
- To switch venues, the user selects from a venue list; a new scoped JWT is issued.
- No token can access data outside its `venue_id`.

### 8.4 JWT claims

```json
{
  "sub": "account_id",
  "name": "Anna",
  "venue_id": "venue_id",
  "venue_name": "Sunset Bistro",
  "staff_profile_id": "staff_profile_id",
  "role": "owner | manager | waiter | staff | admin",
  "permissions": ["read:orders", "write:menu", "view:revenue"]
}
```

### 8.5 Middleware

- `requireAuth` — valid JWT.
- `requireRole(...roles)` — role-based access.
- `requireVenueAccess` — user's `StaffProfile` belongs to the requested venue.
- `requirePermission(...permissions)` — fine-grained permission check (e.g., `view:revenue`).
- `requireOwnerApproval` — triggers OTP challenge for sensitive actions.

---

## 8.6 Staff hub login and shift tracking

Staff, waiters, waitresses, and kitchen workers do **not** log in with the same screen as owners. They use a separate **staff hub login** that binds their identity to a specific venue and creates an auditable shift record.

### Why a separate flow

- A worker can work at multiple venues with the same personal email but a different `worker_handle` per venue.
- The venue owner or manager must explicitly approve each staff login attempt with an OTP.
- Every successful login starts a tracked `Shift`, so owners know **who was on duty, when, and on which device**.

### Staff login fields

| Field | Purpose | Example |
|-------|---------|---------|
| Worker handle | Short unique name inside the venue | `anna` |
| Restaurant username | Venue slug / owner username | `sunset-bistro` |
| Restaurant email | Registered venue email for verification | `owner@sunsetbistro.co.tz` |
| Manager/owner OTP | One-time code sent to the approving manager or owner | `739201` |

### Staff login flow

1. **Worker opens staff hub** and enters:
   - Worker handle (e.g., `anna`)
   - Restaurant username / venue slug (e.g., `sunset-bistro`)
   - Restaurant email (e.g., `owner@sunsetbistro.co.tz`)

2. **System looks up** the `StaffProfile` where:
   - `worker_handle` matches
   - `Venue.slug` matches
   - `Venue.contact.email` matches
   - `StaffProfile.is_active` is true

3. **OTP request.** If the profile exists, the system sends an OTP to the venue owner or an on-duty manager. The worker cannot proceed without approval.

4. **Manager/owner approves.** The approving person receives the OTP and shares it with the worker (in person or via a trusted channel). For higher security, the approver can also see the worker's device fingerprint before confirming.

5. **Worker enters OTP.** The system creates a `WorkerAuthAttempt` record with status `approved` and issues a short-lived JWT scoped to the venue.

6. **Shift starts.** A `Shift` record is created with `started_at` and the approved `WorkerAuthAttempt`. The worker is now on duty.

7. **Shift ends.** When the worker logs out, closes the tab, or the shift timeout fires, the `Shift` is closed and `ended_at` is recorded.

### Shift rules

- A worker can only have **one active shift per venue at a time**.
- JWTs issued to staff are short-lived (e.g., 4 hours or the configured shift length).
- Owners can force-end any active shift from the owner dashboard.
- Orders updated by a worker are tagged with the active `shift_id` for audit.

### Security benefits

- Stolen credentials alone are not enough; the owner/manager OTP is required.
- Each worker is bound to one venue per login, preventing cross-venue data leaks.
- The audit trail proves **who served which order** during which shift.
- Device fingerprinting helps detect suspicious logins (new phone, new location).

### API endpoints for staff auth and shifts

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/staff-auth/lookup` | Look up venue by worker handle + restaurant username + restaurant email |
| POST | `/staff-auth/otp` | Request owner/manager OTP for a staff login attempt |
| POST | `/staff-auth/verify` | Verify OTP and issue staff JWT + start shift |
| POST | `/staff-auth/logout` | End current shift and invalidate token |
| GET | `/venues/:id/shifts` | List shifts for a venue (owner/manager) |
| GET | `/shifts/:id` | Get shift details |
| POST | `/shifts/:id/end` | Force-end a shift (owner/manager) |
| GET | `/venues/:id/worker-auth-attempts` | Audit log of staff login attempts (owner) |

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
- [ ] Staff hub login with worker handle + venue + manager/owner OTP + shift tracking
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
