document$.subscribe(function () {
  document.querySelectorAll("[data-assessment]").forEach(function (assessment) {
    var checks = Array.from(assessment.querySelectorAll("input[type='checkbox']"));
    var score = assessment.querySelector("[data-score]");
    var status = assessment.querySelector("[data-status]");
    var meter = assessment.querySelector("[data-meter]");

    function labelFor(percent) {
      if (percent >= 85) return "AI-ready foundation";
      if (percent >= 65) return "Strong foundation, targeted gaps";
      if (percent >= 40) return "Emerging foundation";
      return "Early maturity";
    }

    function update() {
      var selected = checks.filter(function (check) { return check.checked; }).length;
      var percent = checks.length ? Math.round((selected / checks.length) * 100) : 0;
      if (score) score.textContent = percent + "%";
      if (status) status.textContent = labelFor(percent);
      if (meter) meter.style.width = percent + "%";
    }

    checks.forEach(function (check) {
      check.addEventListener("change", update);
    });
    update();
  });
});
