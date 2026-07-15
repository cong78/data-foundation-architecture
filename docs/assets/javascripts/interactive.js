var mermaidInitialized = false;
var mermaidRendering = false;

function initializeMermaid() {
  if (!window.mermaid || mermaidInitialized) return;

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

initializeMermaid();

document$.subscribe(async function () {
  if (window.mermaid && !mermaidRendering) {
    initializeMermaid();

    var diagramEntries = Array.from(document.querySelectorAll(".mermaid")).filter(function (diagram) {
      return !diagram.querySelector("svg") &&
        diagram.dataset.processed !== "true" &&
        diagram.dataset.mermaidRendering !== "true";
    }).map(function (diagram) {
      var code = diagram.querySelector("code");
      var source = code ? code.textContent : diagram.textContent;

      if (diagram.tagName === "PRE") {
        var container = document.createElement("div");
        container.className = diagram.className;
        container.textContent = source;
        diagram.replaceWith(container);
        diagram = container;
      }

      return { diagram: diagram, source: source };
    }).filter(function (entry) {
      return /^(---\s*)?(flowchart|graph|sequenceDiagram|classDiagram|stateDiagram|erDiagram|journey|gantt|pie|quadrantChart|requirementDiagram|gitGraph|mindmap|timeline|sankey-beta|xychart-beta|block-beta|packet-beta|architecture-beta)\b/.test(entry.source.trim());
    });
    var diagrams = diagramEntries.map(function (entry) { return entry.diagram; });
    var diagramSources = diagramEntries.map(function (entry) { return entry.source; });

    if (diagrams.length) {
      mermaidRendering = true;
      try {
        diagrams.forEach(function (diagram, index) {
          diagram.dataset.mermaidRendering = "true";
          diagram.textContent = diagramSources[index];
        });
        await window.mermaid.run({ nodes: diagrams });
      } catch (error) {
        diagrams.forEach(function (diagram, index) {
          delete diagram.dataset.mermaidRendering;
          if (!diagram.querySelector("svg")) diagram.textContent = diagramSources[index];
        });
        console.error("Mermaid rendering failed:", error && (error.message || error.str) || error);
      } finally {
        mermaidRendering = false;
      }
    }
  }

  document.querySelectorAll("[data-assessment]").forEach(function (assessment) {
    var checks = Array.from(assessment.querySelectorAll("input[type='checkbox']"));
    var score = assessment.querySelector("[data-score]");
    var status = assessment.querySelector("[data-status]");
    var meter = assessment.querySelector("[data-meter]");

    function labelFor(percent) {
      if (percent >= 85) return "Optimized";
      if (percent >= 65) return "Established";
      if (percent >= 40) return "Emerging";
      return "Foundational";
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
