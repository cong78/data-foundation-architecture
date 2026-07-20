(function () {
  var groupColors = {
    "Start Here": "#0f238c",
    "Architecture": "#2f67c7",
    "Services": "#00857c",
    "Standards": "#7a5a00",
    "Decisions": "#7a3e9d",
    "Runbooks": "#b5521f"
  };

  function nodeHref(container, node) {
    if (!node.url) return "";
    return (container.dataset.base || "").replace(/\/$/, "") + node.url;
  }

  function initializeGraph(container) {
    if (container.dataset.initialized === "true" || !window.d3) return;
    container.dataset.initialized = "true";

    fetch(container.dataset.src)
      .then(function (response) {
        if (!response.ok) throw new Error("Unable to load graph data");
        return response.json();
      })
      .then(function (data) { renderGraph(container, data); })
      .catch(function (error) {
        container.innerHTML = '<p class="guidance-graph-error">The documentation graph could not be loaded.</p>';
        console.error(error);
      });
  }

  function renderGraph(container, data) {
    var svgElement = container.querySelector("svg");
    var canvas = container.querySelector("[data-graph-canvas]");
    var detail = container.querySelector("[data-graph-detail]");
    var search = container.querySelector("[data-graph-search]");
    var groupSelect = container.querySelector("[data-graph-group]");
    var reset = container.querySelector("[data-graph-reset]");
    var modeButtons = Array.from(container.querySelectorAll("[data-graph-mode]"));
    var tooltip = container.querySelector("[data-graph-tooltip]");
    var metrics = data.metrics;
    var state = { mode: "structure", group: "All", query: "", selected: null };
    var simulation;
    var zoom;

    Object.keys(metrics.groupPageCounts).forEach(function (group) {
      var option = document.createElement("option");
      option.value = group;
      option.textContent = group + " (" + metrics.groupPageCounts[group] + ")";
      groupSelect.appendChild(option);
    });

    container.querySelector("[data-metric-pages]").textContent = metrics.pages;
    container.querySelector("[data-metric-links]").textContent = metrics.referenceRelationships;
    container.querySelector("[data-metric-sections]").textContent = metrics.topLevelSections;
    container.querySelector("[data-metric-architecture]").textContent = metrics.architectureRelationships;

    function setDetail(node) {
      state.selected = node || null;
      if (!node) {
        detail.innerHTML = "<strong>Select a node</strong><span>Inspect its role, relationships, and place in the guide.</span>";
        return;
      }
      var path = node.kind === "page" ? node.id : node.breadcrumbs.join(" / ");
      var facts = node.kind === "page"
        ? node.words + " words · " + node.incoming + " incoming references · " + node.architectureIncoming + " incoming architecture links"
        : node.kind + " · " + node.group;
      var link = node.url
        ? '<a href="' + nodeHref(container, node) + '">Open page <span aria-hidden="true">→</span></a>'
        : "";
      detail.innerHTML = "<strong>" + node.title + "</strong><span>" + path + "</span><small>" + facts + "</small>" + link;
    }

    function filteredGraph() {
      var nodes = data.nodes.filter(function (node) {
        if (state.group !== "All" && node.group !== state.group) return false;
        if ((state.mode === "references" || state.mode === "architecture") && node.kind !== "page") return false;
        return true;
      }).map(function (node) { return Object.assign({}, node); });
      var ids = new Set(nodes.map(function (node) { return node.id; }));
      var links = data.links.filter(function (link) {
        if (!ids.has(link.source) || !ids.has(link.target)) return false;
        if (state.mode === "structure") return link.type === "contains";
        if (state.mode === "references") return link.type === "references";
        if (state.mode === "architecture") return link.type === "architecture";
        return true;
      }).map(function (link) { return Object.assign({}, link); });
      return { nodes: nodes, links: links };
    }

    function draw() {
      if (simulation) simulation.stop();
      var graph = filteredGraph();
      var width = Math.max(canvas.clientWidth || 860, 320);
      var height = width < 600 ? 540 : 620;
      var svg = window.d3.select(svgElement);
      svg.selectAll("*").remove();
      svg.attr("viewBox", [0, 0, width, height]);

      var root = svg.append("g");
      zoom = window.d3.zoom().scaleExtent([0.35, 4]).on("zoom", function (event) {
        root.attr("transform", event.transform);
        root.selectAll(".guidance-graph-label--page")
          .attr("opacity", event.transform.k > 1.25 || state.group !== "All" ? 1 : 0);
      });
      svg.call(zoom);

      var link = root.append("g")
        .attr("class", "guidance-graph-links")
        .selectAll("line")
        .data(graph.links)
        .join("line")
        .attr("class", function (edge) { return "guidance-graph-link guidance-graph-link--" + edge.type; });

      var node = root.append("g")
        .attr("class", "guidance-graph-nodes")
        .selectAll("g")
        .data(graph.nodes)
        .join("g")
        .attr("class", function (item) { return "guidance-graph-node guidance-graph-node--" + item.kind; })
        .attr("tabindex", 0)
        .attr("role", "button")
        .attr("aria-label", function (item) { return item.title; });

      node.append("circle")
        .attr("r", function (item) { return item.kind === "root" ? 13 : item.kind === "group" ? 10 : item.kind === "section" ? 7 : Math.min(7, 3.5 + item.incoming * 0.18); })
        .attr("fill", function (item) { return item.kind === "root" ? "#10233f" : groupColors[item.group] || "#466b8a"; });

      node.append("text")
        .attr("class", function (item) { return "guidance-graph-label guidance-graph-label--" + item.kind; })
        .attr("x", function (item) { return item.kind === "root" ? 17 : item.kind === "page" ? 7 : 13; })
        .attr("y", 3)
        .attr("opacity", function (item) { return item.kind === "page" && state.group === "All" ? 0 : 1; })
        .text(function (item) { return item.navLabel || item.title; });

      node.on("click", function (event, item) {
        event.stopPropagation();
        node.classed("is-selected", function (candidate) { return candidate.id === item.id; });
        setDetail(item);
      }).on("dblclick", function (event, item) {
        if (item.url) window.location.href = nodeHref(container, item);
      }).on("keydown", function (event, item) {
        if ((event.key === "Enter" || event.key === " ") && item.url) {
          event.preventDefault();
          window.location.href = nodeHref(container, item);
        }
      }).on("pointerenter", function (event, item) {
        tooltip.hidden = false;
        tooltip.innerHTML = "<strong>" + item.title + "</strong><span>" + item.group + (item.kind === "page" ? " · " + item.incoming + " incoming references" : "") + "</span>";
      }).on("pointermove", function (event) {
        var rect = canvas.getBoundingClientRect();
        tooltip.style.left = Math.min(event.clientX - rect.left + 12, rect.width - 210) + "px";
        tooltip.style.top = Math.max(event.clientY - rect.top - 8, 8) + "px";
      }).on("pointerleave", function () {
        tooltip.hidden = true;
      });

      node.call(window.d3.drag()
        .on("start", function (event, item) {
          if (!event.active) simulation.alphaTarget(0.2).restart();
          item.fx = item.x;
          item.fy = item.y;
        })
        .on("drag", function (event, item) {
          item.fx = event.x;
          item.fy = event.y;
        })
        .on("end", function (event, item) {
          if (!event.active) simulation.alphaTarget(0);
          item.fx = null;
          item.fy = null;
        }));

      svg.on("click", function () {
        node.classed("is-selected", false);
        setDetail(null);
      });

      simulation = window.d3.forceSimulation(graph.nodes)
        .force("link", window.d3.forceLink(graph.links).id(function (item) { return item.id; })
          .distance(function (edge) { return edge.type === "contains" ? 48 : edge.type === "architecture" ? 64 : 72; })
          .strength(function (edge) { return edge.type === "contains" ? 0.75 : edge.type === "architecture" ? 0.28 : 0.16; }))
        .force("charge", window.d3.forceManyBody().strength(function (item) { return item.kind === "root" ? -520 : item.kind === "group" ? -310 : item.kind === "section" ? -150 : -48; }))
        .force("center", window.d3.forceCenter(width / 2, height / 2))
        .force("collision", window.d3.forceCollide().radius(function (item) { return item.kind === "root" ? 24 : item.kind === "page" ? 8 : 18; }))
        .force("x", window.d3.forceX(width / 2).strength(0.035))
        .force("y", window.d3.forceY(height / 2).strength(0.035))
        .on("tick", function () {
          link
            .attr("x1", function (edge) { return edge.source.x; })
            .attr("y1", function (edge) { return edge.source.y; })
            .attr("x2", function (edge) { return edge.target.x; })
            .attr("y2", function (edge) { return edge.target.y; });
          node.attr("transform", function (item) { return "translate(" + item.x + "," + item.y + ")"; });
        });

      applySearch();
    }

    function applySearch() {
      var query = state.query.trim().toLowerCase();
      var nodes = window.d3.select(svgElement).selectAll(".guidance-graph-node");
      nodes.classed("is-match", function (item) {
        return query && (item.title + " " + item.navLabel + " " + item.breadcrumbs.join(" ")).toLowerCase().includes(query);
      }).classed("is-muted", function (item) {
        return query && !(item.title + " " + item.navLabel + " " + item.breadcrumbs.join(" ")).toLowerCase().includes(query);
      });
    }

    modeButtons.forEach(function (button) {
      button.addEventListener("click", function () {
        state.mode = button.dataset.graphMode;
        modeButtons.forEach(function (candidate) {
          candidate.setAttribute("aria-pressed", candidate === button ? "true" : "false");
        });
        setDetail(null);
        draw();
      });
    });

    groupSelect.addEventListener("change", function () {
      state.group = groupSelect.value;
      setDetail(null);
      draw();
    });

    search.addEventListener("input", function () {
      state.query = search.value;
      applySearch();
    });

    reset.addEventListener("click", function () {
      state.mode = "structure";
      state.group = "All";
      state.query = "";
      search.value = "";
      groupSelect.value = "All";
      modeButtons.forEach(function (button) {
        button.setAttribute("aria-pressed", button.dataset.graphMode === "structure" ? "true" : "false");
      });
      setDetail(null);
      draw();
    });

    setDetail(null);
    draw();
  }

  function initializeAll() {
    document.querySelectorAll("[data-guidance-graph]").forEach(initializeGraph);
  }

  if (window.document$ && window.document$.subscribe) {
    window.document$.subscribe(initializeAll);
  } else {
    document.addEventListener("DOMContentLoaded", initializeAll);
  }
})();
