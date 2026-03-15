# When the Middle Disappears: Three Orders of AI-Driven Economic Transformation from a Multi-LLM Delphi Analysis

**Author:** Tobias-Benedikt Blask, Harz University of Applied Sciences

## About

This repository contains the data, coding documentation, and analytical materials for the paper "When the Middle Disappears: Three Orders of AI-Driven Economic Transformation from a Multi-LLM Delphi Analysis." The study applies a two-round modified Delphi method using seven frontier large language models as structured surrogate expert panelists to map AI-driven economic transformation across eight industry verticals, four adoption stages, three bounding scenarios, and three orders of effects.

## Repository Structure

```
.
├── README.md                          # This file
├── data/
│   ├── codebook.md                    # Formal codebook with category definitions,
│   │                                  # inclusion/exclusion criteria, and decision rules
│   ├── consensus_matrix_r1.csv        # Round 1 consensus scoring (11 themes x 7 models)
│   ├── consensus_matrix_r2.csv        # Round 2 consensus scoring after Delphi iteration
│   ├── coding_examples.md            # Worked examples of the coding procedure
│   └── prompts/
│       ├── round1_prompt.txt          # Round 1 prompt description
│       └── round2_prompt_template.txt # Round 2 prompt structure
├── ModelAnswers_Input/                # Raw model responses (Round 1 + Round 2)
└── outputs/                           # Analysis outputs, figures, and compiled paper
```

## Reproducing the Analysis

### 1. Review the Codebook

Start with `data/codebook.md` to understand the six thematic categories and the consensus scoring rules (HC/MC/CF/BS) used throughout the analysis.

### 2. Examine the Coding Procedure

See `data/coding_examples.md` for worked examples showing how raw model text was classified into thematic categories, including borderline cases and exclusion decisions.

### 3. Inspect the Consensus Matrices

- `data/consensus_matrix_r1.csv` contains the Round 1 binary scoring (1 = theme substantively present, 0 = absent) for each of the 7 models across 11 identified themes.
- `data/consensus_matrix_r2.csv` contains the Round 2 scoring after models received anonymized Round 1 consensus summaries and were prompted to revise, adopt, contest, or extend.

### 4. Review Prompts

The `data/prompts/` directory describes the prompt structure used in each Delphi round. Full prompt texts are available in the paper's supplementary materials.

## Models Used

| Model | Provider | HQ Region | Role |
|-------|----------|-----------|------|
| Claude Opus 4.6 | Anthropic | US | Safety-aligned, longest output |
| GPT-5.4 Pro | OpenAI | US | Data-anchored reasoning |
| Gemini 3.1 Pro | Google DeepMind | US | Provocative scenarios |
| Grok 4.2 | xAI | US | Contrarian, terse |
| DeepSeek R2 | DeepSeek | China | Most rigorous causal chains |
| Qwen 4.5 Max | Alibaba Cloud | China | Industrial policy lens |
| Mistral Large 3 | Mistral AI | EU (France) | Regulatory-equity focus |

## License

This work is licensed under [Creative Commons Attribution 4.0 International (CC-BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

You are free to share and adapt this material for any purpose, provided appropriate credit is given.

## Citation

```bibtex
@article{blask2026middle,
  title={When the Middle Disappears: Three Orders of AI-Driven Economic Transformation from a Multi-LLM Delphi Analysis},
  author={Blask, Tobias-Benedikt},
  journal={Technological Forecasting and Social Change},
  year={2026}
}
```
