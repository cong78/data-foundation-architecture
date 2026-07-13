var mermaidInitialized = false;

document$.subscribe(async function () {
  if (window.mermaid) {
    if (!mermaidInitialized) {
      window.mermaid.initialize({
        startOnLoad: false,
        securityLevel: "strict",
        theme: "base",
        themeVariables: {
          primaryColor: "#e8f1fb",
          primaryTextColor: "#102a43",
          primaryBorderColor: "#2d6ca2",
          lineColor: "#466b8a",
          secondaryColor: "#eef4fa",
          tertiaryColor: "#f7f9fc",
          fontFamily: "Inter, Arial, sans-serif"
        },
        flowchart: {
          curve: "basis",
          htmlLabels: true
        }
      });
      mermaidInitialized = true;
    }

    await window.mermaid.run({ querySelector: ".mermaid" });
  }

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
