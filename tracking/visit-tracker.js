(function () {
  "use strict";

  const endpoint = document.querySelector('meta[name="korvia-tracker"]')?.content;
  if (!endpoint || !/^https:\/\//.test(endpoint)) return;

  const params = new URLSearchParams(location.search);
  const payload = {
    recipient: params.get("for") || params.get("recipient") || "",
    visitToken: params.get("v") || "",
    path: location.pathname,
    query: location.search,
    title: document.title,
    referrer: document.referrer,
    language: navigator.language || "",
    screen: `${screen.width}x${screen.height}`,
    timezone: Intl.DateTimeFormat().resolvedOptions().timeZone || "",
  };

  const body = JSON.stringify(payload);
  if (navigator.sendBeacon) {
    navigator.sendBeacon(endpoint.replace(/\/$/, "") + "/collect", new Blob([body], {type: "application/json"}));
  } else {
    fetch(endpoint.replace(/\/$/, "") + "/collect", {
      method: "POST",
      headers: {"content-type": "application/json"},
      body,
      keepalive: true,
      mode: "cors",
    }).catch(() => {});
  }
})();
