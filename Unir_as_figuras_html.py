#!/usr/bin/env python
# coding: utf-8

# In[2]:


import webbrowser

# Lista dos arquivos gerados anteriormente
files = [
    "heatmap_invertido_tegument_more.html",
    "heatmap_invertido_tegument_less.html",
    "heatmap_invertido_esophageal_gland.html",
    "heatmap_invertido_gastrodermis_carryers.html",
    "heatmap_invertido_gastrodermis_enzymes.html",
]

# Nomes para as abas (na ordem dos arquivos acima)
names = [
    "Tegument (more reactive)",
    "Tegument (less reactive)",
    "Esophageal gland",
    "Gastrodermis (carriers)",
    "Gastrodermis (enzymes)",
]

# ── metadados da publicação ──────────────────────────────────────────────────
ARTICLE_TITLE   = "Khouri et al., 2026"
JOURNAL_NAME    = "Journal Name"
ARTICLE_DOI     = "#"          # substitua pelo DOI real
GITHUB_URL      = "#"          # substitua pela URL do repositório
DATASET_ABOUT   = (
    "This visualization displays peptide microarray reactivity profiles obtained from individuals "
    "living in a <em>Schistosoma mansoni</em> endemic area. Proteins are grouped according to "
    "their tissue localization and ranked according to the aggregated reactivity score described "
    "in the manuscript. Each row represents a protein; each column represents an individual serum "
    "sample. Color intensity encodes IgG reactivity (normalized median fluorescence intensity)."
)
# ────────────────────────────────────────────────────────────────────────────

# Ler o conteúdo de cada HTML e extrair apenas o gráfico (div + script inline)
divs = []
for i, f in enumerate(files):
    with open(f, "r", encoding="utf-8") as fh:
        html_content = fh.read()
        start = html_content.find("<div")
        end   = html_content.rfind("</div>") + 6
        div   = html_content[start:end]
        divs.append(div.replace("plotly-graph-div", f"plotly-graph-div-{i}"))

# Criar botões de aba
buttons_html = "".join(
    f'<button class="tablinks" onclick="openTab(event, \'fig{i}\')">{names[i]}</button>'
    for i in range(len(files))
)

# Criar conteúdos de aba
contents_html = "".join(
    f'<div id="fig{i}" class="tabcontent">{divs[i]}</div>'
    for i in range(len(files))
)

# ── HTML final ───────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>S. mansoni Peptide Reactivity Explorer</title>
  <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  <style>
    /* ── reset & base ── */
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #f5f4f0;
      color: #1a1a1a;
      font-size: 14px;
      line-height: 1.6;
    }}
    a {{ color: #185FA5; text-decoration: none; }}
    a:hover {{ text-decoration: underline; }}

    /* ── page wrapper ── */
    .page-wrap {{
      max-width: 1200px;
      margin: 0 auto;
      padding: 2rem 1.5rem 3rem;
    }}

    /* ── header card ── */
    .header-card {{
      background: #ffffff;
      border: 0.5px solid rgba(0,0,0,0.12);
      border-radius: 12px;
      padding: 1.5rem 1.75rem;
      margin-bottom: 1.25rem;
    }}
    .header-top {{
      display: flex;
      align-items: flex-start;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }}
    .header-title {{
      font-size: 20px;
      font-weight: 500;
      color: #1a1a1a;
      margin-bottom: 4px;
    }}
    .header-title span {{
      font-style: italic;
      color: #533AB7;
    }}
    .header-sub {{
      font-size: 13px;
      color: #555;
      margin-bottom: 12px;
    }}
    .header-links {{
      display: flex;
      gap: 8px;
      flex-shrink: 0;
      margin-top: 4px;
    }}
    .pill-link {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 12px;
      font-weight: 500;
      padding: 5px 13px;
      border-radius: 20px;
      border: 0.5px solid rgba(0,0,0,0.2);
      color: #444;
      background: #f1f0eb;
      cursor: pointer;
      white-space: nowrap;
    }}
    .pill-link:hover {{ background: #e5e4df; color: #1a1a1a; text-decoration: none; }}

    /* ── legend badges ── */
    .badge-row {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
      margin-top: 4px;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      gap: 5px;
      font-size: 12px;
      font-weight: 500;
      padding: 4px 10px;
      border-radius: 20px;
    }}
    .badge-dot {{
      width: 8px; height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }}
    .badge-rr {{ background: #EAF3DE; color: #3B6D11; }}
    .badge-sr {{ background: #FAECE7; color: #993C1D; }}
    .badge-ne {{ background: #E6F1FB; color: #185FA5; }}

    /* ── tabs ── */
    .tab-bar {{
      display: flex;
      gap: 0;
      border-bottom: 0.5px solid rgba(0,0,0,0.12);
      margin-bottom: 1rem;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }}
    .tablinks {{
      background: transparent;
      border: none;
      border-bottom: 2px solid transparent;
      padding: 9px 18px;
      font-size: 13px;
      font-weight: 400;
      color: #666;
      cursor: pointer;
      white-space: nowrap;
      transition: color 0.15s;
    }}
    .tablinks:hover {{ color: #1a1a1a; background: rgba(0,0,0,0.03); }}
    .tablinks.active {{ color: #1a1a1a; font-weight: 500; border-bottom-color: #533AB7; }}

    /* ── main panel ── */
    .main-panel {{
      background: #ffffff;
      border: 0.5px solid rgba(0,0,0,0.12);
      border-radius: 12px;
      padding: 1.25rem 1.5rem;
    }}
    .tabcontent {{ display: none; }}

    /* ── accordion ── */
    .accordion {{
      margin-top: 1.25rem;
      border: 0.5px solid rgba(0,0,0,0.12);
      border-radius: 8px;
      overflow: hidden;
    }}
    .accordion-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 10px 14px;
      cursor: pointer;
      background: #f9f8f4;
      font-size: 13px;
      color: #555;
      font-weight: 500;
      user-select: none;
      border: none;
      width: 100%;
      text-align: left;
    }}
    .accordion-header:hover {{ color: #1a1a1a; }}
    .accordion-icon {{
      font-size: 16px;
      transition: transform 0.2s;
      line-height: 1;
    }}
    .accordion-body {{
      font-size: 13px;
      line-height: 1.7;
      color: #555;
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.25s ease, padding 0.25s ease;
      padding: 0 14px;
    }}
    .accordion-body.open {{
      max-height: 300px;
      padding: 10px 14px;
    }}

    /* ── citation footer ── */
    .citation {{
      font-size: 12px;
      color: #888;
      font-style: italic;
      margin-top: 1rem;
      padding-top: 0.75rem;
      border-top: 0.5px solid rgba(0,0,0,0.08);
    }}
    .citation a {{ color: #185FA5; }}
  </style>
</head>
<body>
<div class="page-wrap">

  <!-- ── header ── -->
  <div class="header-card">
    <div class="header-top">
      <div>
        <div class="header-title">
          <span>Schistosoma mansoni</span> Peptide Reactivity Explorer
        </div>
        <div class="header-sub">
          Interactive visualization companion for: {ARTICLE_TITLE} &middot; <em>{JOURNAL_NAME}</em>
        </div>
        <div class="badge-row">
          <span class="badge badge-rr">
            <span class="badge-dot" style="background:#3B6D11"></span>RR &mdash; Resistant to Reinfection
          </span>
          <span class="badge badge-sr">
            <span class="badge-dot" style="background:#993C1D"></span>SR &mdash; Susceptible to Reinfection
          </span>
          <span class="badge badge-ne">
            <span class="badge-dot" style="background:#185FA5"></span>NE &mdash; Non-endemic control
          </span>
        </div>
      </div>
      <div class="header-links">
        <a class="pill-link" href="{ARTICLE_DOI}" target="_blank" rel="noopener">
          &#128196; Article DOI
        </a>
        <a class="pill-link" href="{GITHUB_URL}" target="_blank" rel="noopener">
          &#128736; GitHub
        </a>
      </div>
    </div>
  </div>

  <!-- ── tabs + heatmaps ── -->
  <div class="tab-bar" role="tablist">
    {buttons_html}
  </div>

  <div class="main-panel">
    {contents_html}

    <!-- accordion sobre o dataset -->
    <div class="accordion">
      <button class="accordion-header" onclick="toggleAccordion(this)" aria-expanded="false">
        <span>&#9432;&nbsp; About this dataset</span>
        <span class="accordion-icon">&#8964;</span>
      </button>
      <div class="accordion-body">
        {DATASET_ABOUT}
      </div>
    </div>

    <!-- citação -->
    <div class="citation">
      {ARTICLE_TITLE} &middot; <em>{JOURNAL_NAME}</em> &middot;
      DOI: <a href="{ARTICLE_DOI}" target="_blank" rel="noopener">{ARTICLE_DOI}</a>
    </div>
  </div>

</div><!-- /page-wrap -->

<script>
  function openTab(evt, figName) {{
    document.querySelectorAll(".tabcontent").forEach(el => el.style.display = "none");
    document.querySelectorAll(".tablinks").forEach(el => el.classList.remove("active"));
    document.getElementById(figName).style.display = "block";
    evt.currentTarget.classList.add("active");
  }}

  function toggleAccordion(btn) {{
    var body = btn.nextElementSibling;
    var icon = btn.querySelector(".accordion-icon");
    var isOpen = body.classList.contains("open");
    body.classList.toggle("open", !isOpen);
    icon.style.transform = isOpen ? "rotate(0deg)" : "rotate(180deg)";
    btn.setAttribute("aria-expanded", String(!isOpen));
  }}

  // Abrir a primeira aba por padrão
  document.querySelector(".tablinks").click();

  // Ativar scroll zoom em todos os gráficos Plotly
  document.addEventListener("DOMContentLoaded", function() {{
    document.querySelectorAll("[id^='plotly-graph-div']").forEach(function(g) {{
      Plotly.relayout(g, {{dragmode: "zoom"}});
      Plotly.newPlot(g, g.data, g.layout, {{scrollZoom: true}});
    }});
  }});
</script>
</body>
</html>
"""

with open("heatmaps_tabs.html", "w", encoding="utf-8") as f:
    f.write(html)

print("✅ Arquivo combinado gerado: heatmaps_tabs.html")
webbrowser.open("heatmaps_tabs.html")


# In[ ]:





# In[ ]:




