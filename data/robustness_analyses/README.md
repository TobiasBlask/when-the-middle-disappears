# Robustness Analyses (Revision)

This folder contains the three quantitative robustness analyses added during the
revision of *"When the Middle Disappears: Three Orders of AI-Driven Economic
Transformation from a Multi-LLM Delphi Analysis."* They correspond to the
Methodological Properties section of the revised manuscript and to major concerns
M3 (inter-model dependence), M4 (threshold sensitivity), and M5 (inter-coder
reliability) raised in review.

## Files

- **`analysis_results.json`** — machine-readable summary of all three analyses
  (inter-coder reliability, HC-zone robustness, threshold sensitivity, inter-model
  dependence) plus recorded data-integrity flags.
- **`coding_pkg.json`** — the full input package used for the reliability analysis:
  the Round-1 corpus, the codebook, and the original (coder-1) binary coding matrix.
  This is the material the independent coders re-coded.
- **`fig_R1_reliability.png`** — pairwise Cohen's kappa among the original coding and
  four independent re-coders; dumbbell of paper vs independent-majority HC zones.
- **`fig_R2_dependence.png`** — 7x7 pairwise model-agreement heatmap; within-US /
  within-CN / cross-bloc mean agreement.
- **`fig_R3_threshold.png`** — number of high-consensus zones surviving at cut-offs
  of 4/7, 5/7, 6/7, and 7/7.

## Key results

**1. Inter-coder reliability (M5).**
Four independent coders re-coded all 11 themes x 7 models from the raw corpus using
the published codebook. Agreement *among the four independent coders* is substantial
(mean pairwise Cohen's kappa = 0.71). The original coding sits at the lower-moderate
edge (mean kappa vs independent coders = 0.44), i.e. the codebook is applied
reproducibly while the paper's own coding is conservative. Under majority vote of the
independent coders, **five of the six headline high-consensus zones reproduce**
(labor market bifurcation, infrastructure bottleneck, regulatory divergence,
disintermediation, trust premium); only AI-feedback concentration drops from HC to
MC. The independent coders in fact find *more* consensus, not less.

**2. Inter-model dependence (M3).**
Pairwise agreement does not track geopolitical provenance: within-US mean agreement
(0.62) is essentially equal to cross-bloc agreement (0.62), and within-CN is lower
(0.46). The highest-agreement pair (GPT-Gemini, 0.91) and the lowest (Claude-Grok,
0.27) are *both* within the US bloc. A marginal-matched permutation test is
underpowered given only 11 themes (p = 0.32); we therefore do **not** claim that
convergence exceeds chance, only that it is not structured by regional provenance.

**3. Threshold sensitivity (M4).**
High-consensus zone counts at successive cut-offs: 8 zones at 4/7, 6 at 5/7, 3 at 6/7
(labor, infrastructure, regulatory), and 1 at 7/7 (labor only). The six headline
zones use the 5/7 (majority-plus-one) threshold; three are robust to the stricter 6/7.

## Reproduction

`analysis_results.json` is the computed output. The reliability analysis re-codes the
corpus in `coding_pkg.json` with the codebook in `../codebook.md`; dependence and
threshold analyses operate on `../consensus_matrix_r1.csv`. Independent coding was
performed by separate large-language-model coders, which provides a scalable
reliability probe and a partial check on the generate-and-code circularity noted in
review; it is not a substitute for multiple trained human coders, which remains the
standard for confirmatory work.

## Data-integrity note

During the revision, the originally submitted Figure 4 was found to render three rows
(infrastructure bottleneck, concentration, biological-digital) with cell counts that
did not match Table 3, the consensus matrices, or the main text. Figure 4 has been
regenerated directly from `../consensus_matrix_r1.csv` so that figure, table, and text
now agree exactly. The `data_integrity_flags` field in `analysis_results.json` records
this and two related documentation fixes.
