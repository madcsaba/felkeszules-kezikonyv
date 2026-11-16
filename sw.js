/* Offline működés: az app és a teljes kézikönyv a telefonon marad.
   Új verzió kiadásakor a CACHE nevét kell átírni. */
var CACHE = "felkeszules-v2";
var FILES = [
  "./", "./index.html", "./style.css", "./script.js", "./img/hero.svg",
  "./app/", "./app/index.html", "./app/manifest.webmanifest",
  "./app/icon.svg", "./app/icon-192.png", "./app/icon-512.png",
  "./assets/fonts.css", "./assets/fonts/inter-latin-wght-normal.woff2",
  "./assets/fonts/inter-latin-ext-wght-normal.woff2"
];

self.addEventListener("install", function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(FILES); }).then(function () { return self.skipWaiting(); }));
});

self.addEventListener("activate", function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k.indexOf("felkeszules-") === 0 && k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});

/* Saját fájlok: először a hálózat (friss tartalom), ha nincs net, a tárolt másolat.
   Külső kéréseket (pl. petíció) nem tárolunk. */
self.addEventListener("fetch", function (e) {
  var req = e.request;
  if (req.method !== "GET" || !req.url.startsWith(self.registration.scope)) return;
  e.respondWith(
    fetch(req).then(function (res) {
      if (res.ok) { var copy = res.clone(); caches.open(CACHE).then(function (c) { c.put(req, copy); }); }
      return res;
    }).catch(function () {
      return caches.match(req, { ignoreSearch: true }).then(function (hit) {
        return hit || (req.mode === "navigate" ? caches.match("./app/index.html") : undefined);
      });
    })
  );
});
