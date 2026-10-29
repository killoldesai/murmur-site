// Murmur site motion. Everything here is decoration: the pages read fine without it.
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.remove("no-js");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Header border once scrolled, mobile menu
  var head = document.querySelector(".site-head");
  var onScroll = function () { head && head.classList.toggle("scrolled", window.scrollY > 8); };
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();
  var menuBtn = document.querySelector(".menu-btn");
  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      var open = doc.classList.toggle("menu-open");
      menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // Waveform bars: fill each .wave with bars shaped like a voice envelope
  document.querySelectorAll(".wave[data-bars]").forEach(function (wave) {
    var n = parseInt(wave.getAttribute("data-bars"), 10) || 60;
    var html = "";
    for (var i = 0; i < n; i++) {
      var x = i / (n - 1);
      var env = Math.pow(Math.sin(Math.PI * x), 1.4);
      var h = 12 + env * 88 * (0.45 + 0.55 * Math.abs(Math.sin(i * 1.7) * Math.cos(i * 0.37)));
      var d = -((i * 0.137) % 1.4).toFixed(2);
      html += '<i style="--h:' + h.toFixed(0) + "%;--d:" + d + 's"></i>';
    }
    wave.innerHTML = html;
  });

  // Entrance: rise + stagger
  var revealables = document.querySelectorAll("[data-reveal], .reveal-group, .progress-line, .spk-group");
  if ("IntersectionObserver" in window && !reduce) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("is-in"); io.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    revealables.forEach(function (el) { io.observe(el); });
  } else {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  }

  // Count-up numbers
  document.querySelectorAll("[data-count]").forEach(function (el) {
    var end = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduce || !("IntersectionObserver" in window)) { el.textContent = end + suffix; return; }
    var run = function () {
      var t0 = performance.now(), dur = 1400;
      var tick = function (t) {
        var p = Math.min(1, (t - t0) / dur);
        el.textContent = Math.round(end * (1 - Math.pow(1 - p, 3))) + suffix;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    };
    var o = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { run(); o.disconnect(); } }, { threshold: 0.5 });
    o.observe(el);
  });

  // Hero phone: transcript lines arrive one by one, the live line follows playback
  var phone = document.querySelector("[data-live-transcript]");
  if (phone) {
    var lines = phone.querySelectorAll(".tline");
    if (reduce) {
      lines.forEach(function (l) { l.classList.add("in"); });
    } else {
      var idx = 0;
      var step = function () {
        if (idx >= lines.length) {
          setTimeout(function () {
            lines.forEach(function (l) { l.classList.remove("in", "live"); });
            idx = 0; step();
          }, 3200);
          return;
        }
        lines.forEach(function (l) { l.classList.remove("live"); });
        var line = lines[idx];
        line.classList.add("in", "live");
        var p = line.querySelector("p");
        var full = p.getAttribute("data-text") || p.textContent;
        p.setAttribute("data-text", full);
        var words = full.split(" "), w = 0;
        p.innerHTML = '<span class="caret"></span>';
        var typer = setInterval(function () {
          w++;
          p.innerHTML = words.slice(0, w).join(" ") + (w < words.length ? '<span class="caret"></span>' : "");
          if (w >= words.length) { clearInterval(typer); idx++; setTimeout(step, 900); }
        }, 110);
      };
      setTimeout(step, 600);
    }
  }

  // Transcribe visual: words light up in time with a fake progress meter
  document.querySelectorAll(".viz-transcribe").forEach(function (viz) {
    var box = viz.querySelector(".words");
    var bar = viz.querySelector(".meter .bar i");
    var pct = viz.querySelector(".meter .pct");
    var words = box.textContent.trim().split(/\s+/);
    box.innerHTML = words.map(function (w) { return "<span>" + w + "</span>"; }).join(" ");
    var spans = box.querySelectorAll("span");
    if (reduce) { spans.forEach(function (s) { s.classList.add("on"); }); if (bar) bar.style.width = "100%"; if (pct) pct.textContent = "100%"; return; }
    var i = 0;
    setInterval(function () {
      if (i > spans.length + 8) { i = 0; spans.forEach(function (s) { s.classList.remove("on", "cur"); }); }
      spans.forEach(function (s) { s.classList.remove("cur"); });
      if (spans[i]) spans[i].classList.add("on", "cur");
      var p = Math.min(100, Math.round((i / spans.length) * 100));
      if (bar) bar.style.width = p + "%";
      if (pct) pct.textContent = p + "%";
      i++;
    }, 160);
  });

  // Record visual: running timer
  document.querySelectorAll("[data-timer]").forEach(function (el) {
    if (reduce) { el.textContent = "00:42"; return; }
    var s = 0;
    setInterval(function () {
      s = (s + 1) % 3600;
      el.textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0");
    }, 1000);
  });

  // Tabs (platform switcher)
  document.querySelectorAll("[data-tabs]").forEach(function (root) {
    var buttons = root.querySelectorAll('[role="tab"]');
    var select = function (btn) {
      buttons.forEach(function (b) {
        var on = b === btn;
        b.setAttribute("aria-selected", on ? "true" : "false");
        b.tabIndex = on ? 0 : -1;
        var panel = document.getElementById(b.getAttribute("aria-controls"));
        if (panel) { panel.classList.toggle("on", on); panel.hidden = !on; }
      });
    };
    buttons.forEach(function (b, i) {
      b.addEventListener("click", function () { select(b); });
      b.addEventListener("keydown", function (e) {
        var k = e.key === "ArrowRight" ? 1 : e.key === "ArrowLeft" ? -1 : 0;
        if (!k) return;
        var next = buttons[(i + k + buttons.length) % buttons.length];
        next.focus(); select(next);
      });
    });
  });

  // Footer year
  document.querySelectorAll("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
