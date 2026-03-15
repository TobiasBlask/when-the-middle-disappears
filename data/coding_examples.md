# Coding Examples: From Raw Model Output to Thematic Classification

This document provides worked examples demonstrating how raw LLM responses were coded into the thematic categories defined in the codebook. Each example includes the original quote, the assigned thematic code, and the reasoning behind the classification decision.

---

## Example 1: Clear Single-Category Assignment

**Source:** GPT-4o, Round 1 response

**Original quote:**
> "The most significant near-term economic disruption will be the hollowing out of middle-skill knowledge work. Legal paralegals, junior financial analysts, radiologists-in-training, and entry-level consultants face displacement not because AI replaces their entire role, but because AI allows one senior professional to do the work previously requiring a team of five. This creates a barbell-shaped labor market: high demand at the top for those who orchestrate AI systems, high demand at the bottom for physical tasks AI cannot perform, and a collapsing middle."

**Assigned code:** Labor Market Displacement / Bifurcation

**Reasoning:** This passage directly addresses workforce restructuring through AI automation. The "barbell-shaped labor market" metaphor maps precisely to the bifurcation concept. The passage names specific occupations and describes a mechanism (senior professionals leveraging AI to replace teams). No secondary code was assigned because the passage focuses entirely on labor market structure rather than, for example, market concentration or disintermediation.

---

## Example 2: Borderline Case Requiring Category Prioritization

**Source:** Claude 3.5 Sonnet, Round 1 response

**Original quote:**
> "As AI systems become capable of autonomously negotiating contracts, executing trades, and managing supply chains, we will see the emergence of economic agents that operate without direct human oversight. These autonomous agents will accelerate market concentration because firms with superior AI agents will compound advantages faster than human-led competitors can respond, creating a new form of winner-take-all dynamic driven not by network effects but by algorithmic superiority."

**Assigned code (primary):** Market Concentration / Platform Dynamics
**Assigned code (secondary, noted but not counted):** Autonomous Economic Agents (sub-theme)

**Reasoning:** This passage contains two interwoven themes. The first sentence describes autonomous economic agents, while the second explains how these agents drive market concentration. Following the codebook decision rule for thematic overlap, the primary code was assigned based on the dominant mechanism -- the passage ultimately makes a claim about market structure (winner-take-all dynamics) rather than about the nature of autonomous agents per se. The autonomous agent concept was noted as a contributing sub-theme and tracked separately in the consensus matrix.

---

## Example 3: Exclusion Decision (Passing Mention)

**Source:** Grok-2, Round 1 response

**Original quote:**
> "Several infrastructure challenges will need to be addressed, including energy consumption and chip supply, as AI scales further."

**Coding decision:** NOT coded as Infrastructure Bottleneck / Compute

**Reasoning:** This sentence was excluded from the Infrastructure Bottleneck category because it constitutes a passing mention rather than a substantive engagement. Per the codebook decision rules, a theme requires at least one full paragraph or a specific predictive claim. This single sentence in a list format does not meet the threshold. By contrast, other models that received a "1" for this theme provided detailed predictions about energy consumption percentages, semiconductor geopolitics, or compute resource economics.

---

## Example 4: Round 2 Adoption vs. Acknowledgment

**Source:** Mistral Large 2, Round 2 response (regarding Apprenticeship Crash theme)

**Round 2 quote (after being shown Claude's R1 prediction about apprenticeship collapse):**
> "The observation about apprenticeship pathways is well-taken and represents a critical second-order effect of AI displacement that deserves serious attention. If junior positions are automated, the traditional pipeline through which professionals develop expertise -- by performing supervised low-complexity tasks before graduating to more complex ones -- will be fundamentally broken. This suggests we may face a future expertise crisis: a generation of would-be experts who never had the opportunity to develop their skills through progressive responsibility. Organizations and educational institutions will need to radically redesign professional development pathways."

**Assigned code:** Labor Market Displacement / Bifurcation (Apprenticeship Crash sub-theme)
**Adoption status:** Adopted (coded as 1 in R2 matrix)

**Reasoning:** This response goes well beyond simple acknowledgment. Mistral elaborates on the mechanism ("traditional pipeline... will be fundamentally broken"), introduces a novel consequence ("future expertise crisis"), and proposes institutional responses. This meets the codebook criteria for adoption: the model integrates the theme into its revised analysis with substantive elaboration, rather than merely acknowledging it as "an interesting point."
