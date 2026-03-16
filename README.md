# When the Middle Disappears: Three Orders of AI-Driven Economic Transformation from a Multi-LLM Delphi Analysis

**Author:** Tobias-Benedikt Blask, Harz University of Applied Sciences

**Status:** Submitted to *Technological Forecasting and Social Change*

## About

This repository contains the complete data, analytical materials, and supplementary documentation for the paper "When the Middle Disappears: Three Orders of AI-Driven Economic Transformation from a Multi-LLM Delphi Analysis." The study applies a two-round Multi-LLM Delphi method using seven frontier large language models as structured panelists to map AI-driven economic transformation across eight GICS-aligned industry verticals, four adoption stages, three bounding scenarios, and three orders of effects.

## Repository Structure

```
.
├── README.md                              # This file
├── data/
│   ├── codebook.md                        # Formal codebook with category definitions,
│   │                                      # inclusion/exclusion criteria, and decision rules
│   ├── coding_examples.md                 # Worked examples of the coding procedure
│   ├── consensus_matrix_r1.csv            # Round 1 consensus scoring (11 themes x 7 models)
│   ├── consensus_matrix_r2.csv            # Round 2 consensus scoring after Delphi feedback
│   ├── figure_specifications.md           # PaperBanana prompts for all generated figures
│   ├── prompts/
│   │   ├── round1_prompt.txt              # Round 1 prompt instrument
│   │   └── round2_prompt_template.txt     # Round 2 prompt structure with feedback template
│   └── raw_outputs/
│       ├── round1/                        # Round 1 model responses (Markdown, converted from .docx)
│       │   ├── claude.md
│       │   ├── gpt54.md
│       │   ├── gemini.md
│       │   ├── grok.md
│       │   ├── deepseek.md
│       │   ├── qwen.md
│       │   └── mistral.md
│       └── round2/                        # Round 2 model responses (Markdown, converted from .docx)
│           ├── claude.md
│           ├── gpt54.md
│           ├── gemini.md
│           ├── grok.md
│           ├── deepseek.md
│           ├── qwen.md
│           └── mistral.md
├── outputs/
│   ├── figures/                           # All paper figures (PNG)
│   ├── latex/
│   │   ├── paper.tex                      # Full manuscript (LaTeX source)
│   │   ├── paper_anonymous.tex            # Double-blind anonymized version
│   │   ├── references.bib                 # Full bibliography
│   │   ├── references_anonymous.bib       # Anonymized bibliography
│   │   └── figures/                       # Figures as used by LaTeX
│   └── submission/
│       └── cover_letter.tex               # Cover letter to editors
```

## Data and Materials

### Raw Model Outputs

The `data/raw_outputs/` directory contains the complete, unedited responses from all seven models in both Delphi rounds, converted from the original .docx exports to Markdown for readability and version control.

| Model | Round 1 Words | Round 2 Words |
|-------|--------------|--------------|
| Claude Opus 4.6 | 30,613 | ~3,000 |
| GPT-5.4 | 23,346 | ~4,500 |
| DeepSeek R2 | 22,614 | ~4,500 |
| Gemini 3.1 Pro | 16,330 | ~2,200 |
| Qwen 4.5 Max | 11,024 | ~2,700 |
| Mistral Large 3 | 8,261 | ~4,700 |
| Grok 4.2 | 2,169 | ~1,700 |
| **Total** | **~114,000** | **~23,000** |

### Codebook and Coding Procedure

- `data/codebook.md`: Formal codebook with six thematic categories, inclusion/exclusion criteria, consensus scoring rules (HC/MC/CF/BS), and decision rules for borderline cases.
- `data/coding_examples.md`: Worked examples showing how raw model text was classified into thematic categories.

### Consensus Matrices

- `data/consensus_matrix_r1.csv`: Round 1 binary scoring (1 = theme substantively present, 0 = absent) for 7 models across 11 themes.
- `data/consensus_matrix_r2.csv`: Round 2 scoring after models received anonymized Round 1 consensus summaries.

### Prompt Instruments

- `data/prompts/round1_prompt.txt`: The structured prompt used for Round 1 data collection.
- `data/prompts/round2_prompt_template.txt`: The Round 2 prompt template including feedback structure.

### Figure Generation

- `data/figure_specifications.md`: Complete PaperBanana prompts and specifications used to generate all figures, documenting the exact instructions and iteration history for each figure.

## Models Used

| Model | Provider | HQ Region | Data Collection Date |
|-------|----------|-----------|---------------------|
| Claude Opus 4.6 | Anthropic | US | March 14-15, 2026 |
| GPT-5.4 Pro | OpenAI | US | March 14-15, 2026 |
| Gemini 3.1 Pro | Google DeepMind | US | March 14-15, 2026 |
| Grok 4.2 | xAI | US | March 14-15, 2026 |
| DeepSeek R2 | DeepSeek | China | March 14-15, 2026 |
| Qwen 4.5 Max | Alibaba Cloud | China | March 14-15, 2026 |
| Mistral Large 3 | Mistral AI | EU (France) | March 14-15, 2026 |

## Transparency Note

This manuscript was produced using the [Open Academic Paper Machine](https://github.com/TobiasBlask/open-paper-machine), an AI-assisted research workflow tool. The author conceived, designed, and directed the entire study; AI tools were used for prose drafting and production under author orchestration. Full disclosure is provided in the manuscript's AI Declaration section.

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, provided appropriate credit is given.

## Citation

```bibtex
@article{blask2026middle,
  title={When the Middle Disappears: Three Orders of AI-Driven Economic Transformation
         from a Multi-LLM Delphi Analysis},
  author={Blask, Tobias-Benedikt},
  journal={Technological Forecasting and Social Change},
  year={2026},
  note={Under review}
}
```
