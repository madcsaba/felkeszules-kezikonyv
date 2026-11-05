/* Felkészülés vészhelyzetekre – interaktív elemek (függőség nélkül) */
(function () {
  "use strict";

  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) {} },
    del: function (k) { try { localStorage.removeItem(k); } catch (e) {} }
  };

  /* ---------- Téma ---------- */
  var root = document.documentElement;
  var themeBtn = document.getElementById("theme-toggle");
  var savedTheme = store.get("kh-theme");
  if (savedTheme) root.setAttribute("data-theme", savedTheme);
  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var current = root.getAttribute("data-theme") ||
        (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      var next = current === "dark" ? "light" : "dark";
      root.setAttribute("data-theme", next);
      store.set("kh-theme", next);
    });
  }

  /* ---------- Mobil menü ---------- */
  var menuBtn = document.getElementById("menu-toggle");
  var scrim = document.querySelector(".scrim");
  function closeNav() {
    document.body.classList.remove("nav-open");
    if (menuBtn) menuBtn.setAttribute("aria-expanded", "false");
  }
  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      var open = document.body.classList.toggle("nav-open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }
  if (scrim) scrim.addEventListener("click", closeNav);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeNav(); });
  document.querySelectorAll(".toc a").forEach(function (a) { a.addEventListener("click", closeNav); });

  /* ---------- Nyomtatás ---------- */
  var printBtn = document.getElementById("print-btn");
  if (printBtn) printBtn.addEventListener("click", function () { window.print(); });
  var openedForPrint = [];
  window.addEventListener("beforeprint", function () {
    document.querySelectorAll("details:not([open])").forEach(function (d) {
      d.setAttribute("open", ""); openedForPrint.push(d);
    });
  });
  window.addEventListener("afterprint", function () {
    openedForPrint.forEach(function (d) { d.removeAttribute("open"); });
    openedForPrint = [];
  });

  /* ---------- Olvasási sáv + vissza a tetejére ---------- */
  var bar = document.querySelector(".progress-bar");
  var toTop = document.querySelector(".to-top");
  function onScroll() {
    var h = document.documentElement;
    var max = h.scrollHeight - h.clientHeight;
    var pct = max > 0 ? (h.scrollTop / max) * 100 : 0;
    if (bar) bar.style.width = pct + "%";
    if (toTop) toTop.classList.toggle("show", h.scrollTop > 800);
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  if (toTop) toTop.addEventListener("click", function () { window.scrollTo({ top: 0 }); });

  /* ---------- Tartalomjegyzék kiemelése ---------- */
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a"));
  var byId = {};
  tocLinks.forEach(function (a) { byId[a.getAttribute("href").slice(1)] = a; });
  var sections = tocLinks
    .map(function (a) { return document.getElementById(a.getAttribute("href").slice(1)); })
    .filter(Boolean);
  if ("IntersectionObserver" in window && sections.length) {
    var visible = {};
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { visible[en.target.id] = en.isIntersecting; });
      var current = null;
      for (var i = 0; i < sections.length; i++) {
        if (visible[sections[i].id]) { current = sections[i].id; break; }
      }
      if (current) {
        tocLinks.forEach(function (a) { a.classList.remove("active"); a.removeAttribute("aria-current"); });
        byId[current].classList.add("active");
        byId[current].setAttribute("aria-current", "true");
      }
    }, { rootMargin: "-70px 0px -60% 0px" });
    sections.forEach(function (s) { io.observe(s); });
  }

  /* ---------- Ellenőrzőlisták (helyben mentve) ---------- */
  document.querySelectorAll("[data-checklist]").forEach(function (box) {
    var key = "kh-list-" + box.getAttribute("data-checklist");
    var inputs = Array.prototype.slice.call(box.querySelectorAll('input[type="checkbox"]'));
    var meter = box.querySelector(".meter > span");
    var label = box.querySelector(".meter-label");
    var reset = box.querySelector("[data-reset]");
    var saved = {};
    try { saved = JSON.parse(store.get(key) || "{}"); } catch (e) { saved = {}; }

    inputs.forEach(function (inp, i) { inp.checked = !!saved[i]; });

    function update() {
      var done = 0, state = {};
      inputs.forEach(function (inp, i) { if (inp.checked) { done++; state[i] = 1; } });
      if (meter) meter.style.width = (inputs.length ? (done / inputs.length) * 100 : 0) + "%";
      if (label) label.textContent = done + " / " + inputs.length;
      if (done) store.set(key, JSON.stringify(state)); else store.del(key);
      if (box.classList.contains("quiz")) updateQuiz(box);
    }
    inputs.forEach(function (inp) { inp.addEventListener("change", update); });
    if (reset) reset.addEventListener("click", function () {
      inputs.forEach(function (inp) { inp.checked = false; });
      update();
    });
    update();
  });

  function updateQuiz(box) {
    var total = 0;
    box.querySelectorAll('input[type="checkbox"]').forEach(function (inp) {
      if (inp.checked) total += parseInt(inp.getAttribute("data-points") || "0", 10);
    });
    var val = box.querySelector(".score .val");
    var verdict = box.querySelector(".score .verdict");
    if (val) val.textContent = total + " / 10";
    if (!verdict) return;
    var text, cls;
    if (total <= 2) { text = "nagyon gyengén felkészült"; cls = "l1"; }
    else if (total <= 5) { text = "gyengén felkészült"; cls = "l2"; }
    else if (total <= 7) { text = "felkészült"; cls = "l3"; }
    else { text = "jól felkészült"; cls = "l4"; }
    if (total === 0) { text = "jelöld be, ami igaz rád"; cls = ""; }
    verdict.textContent = text;
    verdict.className = "verdict " + cls;
  }
})();
