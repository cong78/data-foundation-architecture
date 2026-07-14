# Architecture Dashboard

<div class="decision-brief"><div><small>Use when</small><strong>Reviewing foundation capability and control evidence.</strong></div><div><small>Decision</small><strong>Which measured gap should be addressed next?</strong></div><div><small>Owner</small><strong>Foundation sponsor and capability owners.</strong></div><div><small>Output</small><strong>Prioritized improvement backed by current evidence.</strong></div></div>

Use this page to discuss maturity with evidence. Values are illustrative; replace them with real portal, catalog, and observability data.

<div class="metric-strip">
  <div class="metric-card"><strong>9</strong>Foundation services</div>
  <div class="metric-card"><strong>9</strong>Go-live gates</div>
  <div class="metric-card"><strong>27</strong>Foundation maturity checks</div>
  <div class="metric-card"><strong>OTel</strong>Telemetry standard</div>
</div>

<div class="blue-callout">
  Review what exists, which gates are enforced, and where implementation is still thin.
</div>

## Capability Maturity

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Illustrative maturity by foundation service.",
  "data": {
    "values": [
      {"service": "Portal", "maturity": 70},
      {"service": "AI Assistant", "maturity": 50},
      {"service": "Ingestion", "maturity": 65},
      {"service": "Product Creation", "maturity": 60},
      {"service": "Consumption", "maturity": 58},
      {"service": "Sharing", "maturity": 45},
      {"service": "Platform Enablement", "maturity": 54},
      {"service": "Observability", "maturity": 55},
      {"service": "Operations", "maturity": 52}
    ]
  },
  "mark": {"type": "bar", "cornerRadiusEnd": 3},
  "encoding": {
    "x": {"field": "maturity", "type": "quantitative", "title": "Maturity score", "scale": {"domain": [0, 100]}},
    "y": {"field": "service", "type": "nominal", "title": null, "sort": "-x"},
    "color": {"value": "#0F238C"},
    "tooltip": [
      {"field": "service", "type": "nominal"},
      {"field": "maturity", "type": "quantitative", "title": "Score"}
    ]
  }
}
```

## Go-Live Gate Coverage

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Illustrative product go-live gate coverage.",
  "data": {
    "values": [
      {"gate": "Ownership", "status": "Implemented", "count": 1},
      {"gate": "Purpose", "status": "Implemented", "count": 1},
      {"gate": "Contract", "status": "In progress", "count": 1},
      {"gate": "Quality", "status": "In progress", "count": 1},
      {"gate": "Security", "status": "Implemented", "count": 1},
      {"gate": "Lineage", "status": "In progress", "count": 1},
      {"gate": "Observability", "status": "In progress", "count": 1},
      {"gate": "Documentation", "status": "Implemented", "count": 1},
      {"gate": "Portability", "status": "In progress", "count": 1}
    ]
  },
  "mark": {"type": "arc", "innerRadius": 55},
  "encoding": {
    "theta": {"field": "count", "type": "quantitative"},
    "color": {
      "field": "status",
      "type": "nominal",
      "scale": {"range": ["#0F238C", "#7C87C0"]}
    },
    "tooltip": [
      {"field": "gate", "type": "nominal"},
      {"field": "status", "type": "nominal"}
    ]
  },
  "view": {"stroke": null}
}
```

## AI-Ready Control Coverage

```vegalite
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "Illustrative AI-ready control coverage.",
  "data": {
    "values": [
      {"control": "Lineage", "coverage": 80},
      {"control": "Quality", "coverage": 72},
      {"control": "Access Policy", "coverage": 76},
      {"control": "AI Usage Approval", "coverage": 48},
      {"control": "Retrieval Governance", "coverage": 42},
      {"control": "Model-to-Data Trace", "coverage": 35}
    ]
  },
  "mark": {"type": "line", "point": true, "strokeWidth": 3},
  "encoding": {
    "x": {"field": "control", "type": "nominal", "title": null},
    "y": {"field": "coverage", "type": "quantitative", "title": "Coverage", "scale": {"domain": [0, 100]}},
    "color": {"value": "#0F238C"},
    "tooltip": [
      {"field": "control", "type": "nominal"},
      {"field": "coverage", "type": "quantitative"}
    ]
  }
}
```
