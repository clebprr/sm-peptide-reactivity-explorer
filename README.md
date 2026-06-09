# *Schistosoma mansoni* Peptide Reactivity Explorer

> Interactive visualization companion for:  
> **Farias et al., 2026** · *Journal Name* · DOI: [10.xxxx/xxxxx](https://doi.org/10.xxxx/xxxxx)

🔗 **[Access the tool](https://clebprr.github.io/sm-peptide-reactivity-explorer/)**

---

## About

This tool provides an interactive visualization of peptide microarray reactivity profiles obtained from individuals living in a *Schistosoma mansoni* endemic area.

Proteins are grouped according to their tissue localization and ranked according to the aggregated reactivity score described in the manuscript. Each row represents a protein; each column represents an individual serum sample. Color intensity encodes IgG reactivity (normalized median fluorescence intensity).

### Study groups

| Code | Description |
|------|-------------|
| **RR** | Resistant to Reinfection |
| **SR** | Susceptible to Reinfection |
| **NE** | Non-endemic control |

### Tissue categories available

- Tegument (more reactive)
- Tegument (less reactive)
- Esophageal gland
- Gastrodermis (carriers)
- Gastrodermis (enzymes)

---

## Usage

Access the interactive tool directly at:

```
https://seu-usuario.github.io/sm-peptide-reactivity-explorer/
```

No installation required. The tool runs entirely in the browser.

---

## Repository structure

```
sm-peptide-reactivity-explorer/
├── index.html                        # Main interactive tool (open in browser)
├── README.md                         # This file
├── data/
│   ├── heatmap_invertido_tegument_more.html
│   ├── heatmap_invertido_tegument_less.html
│   ├── heatmap_invertido_esophageal_gland.html
│   ├── heatmap_invertido_gastrodermis_carryers.html
│   └── heatmap_invertido_gastrodermis_enzymes.html
└── scripts/
    └── heatmaps_tabs_layout.py       # Script used to generate index.html
```

---

## Reproducing the figures

The heatmaps were generated using Python with [Plotly](https://plotly.com/python/). To regenerate `index.html` from the source data:

```bash
# Install dependencies
pip install plotly pandas numpy

# Run the assembly script
python scripts/heatmaps_tabs_layout.py
```

The script reads the individual heatmap HTML files from `data/` and assembles them into `index.html`.

---

## Citation

If you use this tool or the data in your research, please cite the original article:

> Farias et al. (2026). *[Article title]*. *Journal Name*. https://doi.org/10.xxxx/xxxxx

```bibtex
@article{farias2026,
  author  = {Farias, [First name] and [co-authors]},
  title   = {[Article title]},
  journal = {Journal Name},
  year    = {2026},
  doi     = {10.xxxx/xxxxx}
}
```

---

## License

The visualization code in this repository is released under the [MIT License](LICENSE).  
The underlying data and figures are subject to the terms of the original publication.

---

## Contact

For questions about the tool or the dataset, please open an [issue](../../issues) or contact the corresponding author via the published article.
