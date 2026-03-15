# Codebook: Multi-LLM Delphi Analysis of AI-Driven Economic Transformation

## Overview

This codebook documents the deductive coding procedure used to analyze responses from seven large language models (Claude 3.5 Sonnet, GPT-4o, Gemini 1.5 Pro, Grok-2, DeepSeek-V3, Qwen 2.5 72B, Mistral Large 2) across two Delphi rounds. The coding framework was developed iteratively: an initial set of thematic categories was derived from Round 1 responses, then applied systematically to both rounds.

---

## Thematic Categories

### 1. Labor Market Displacement / Bifurcation

**Definition:** Predictions concerning the restructuring of labor markets due to AI automation, including job displacement, the emergence of a two-tier workforce (AI-augmented vs. non-augmented workers), wage polarization, and shifts in the nature of human work.

**Inclusion criteria:**
- Explicit mention of job losses, displacement, or automation of specific occupations
- Discussion of wage gaps between AI-skilled and non-AI-skilled workers
- References to new job categories emerging from AI adoption
- Predictions about changes to working conditions, hours, or employment structures

**Exclusion criteria:**
- General statements about "AI changing work" without specifics
- Pure productivity gains without labor market implications
- Discussion of AI tools without workforce impact framing

**Example quotes:**
- "A bifurcated labor market will emerge where workers who can effectively collaborate with AI systems command significant wage premiums over those who cannot."
- "Entire categories of knowledge work -- legal research, financial analysis, medical diagnostics -- will see 40-60% workforce reductions within the decade."

---

### 2. Market Concentration / Platform Dynamics

**Definition:** Predictions about how AI reshapes competitive dynamics, market structure, and platform power, including winner-take-all effects, the role of data and compute advantages, disintermediation of existing industries, and AI-driven feedback loops that entrench dominant players.

**Inclusion criteria:**
- Discussion of monopolistic or oligopolistic tendencies driven by AI
- Platform economics and network effects amplified by AI
- Vertical integration of AI capabilities by large firms
- Disintermediation of traditional intermediaries (e.g., consultants, brokers)
- AI-driven feedback loops that concentrate market power

**Exclusion criteria:**
- General mentions of "big tech" without AI-specific mechanism
- Competition policy discussion without market structure predictions
- Pure technology descriptions without market implications

**Example quotes:**
- "AI feedback loops will create unprecedented market concentration as firms with more data train better models, attracting more users and more data."
- "Traditional professional intermediaries -- from real estate agents to financial advisors -- face existential pressure as AI systems replicate their advisory functions at near-zero marginal cost."

---

### 3. Regulatory Response / Governance

**Definition:** Predictions about governmental and institutional responses to AI, including regulatory frameworks, international governance divergence, standards-setting, and the challenge of governing rapidly evolving technology.

**Inclusion criteria:**
- Specific regulatory proposals or predicted policy responses
- Discussion of governance gaps or regulatory lag
- International regulatory divergence or harmonization efforts
- Sector-specific regulation (e.g., AI in healthcare, finance)
- Liability and accountability frameworks for AI systems

**Exclusion criteria:**
- Purely normative statements about what regulation "should" do without predictive framing
- General ethics discussions without governance mechanisms
- Industry self-regulation without institutional framing

**Example quotes:**
- "Regulatory approaches will diverge sharply: the EU will pursue precautionary, rights-based frameworks while the US and China prioritize innovation-permissive regimes, creating a fragmented global governance landscape."
- "Governments will struggle to regulate AI systems that evolve faster than legislative cycles, leading to a persistent governance deficit."

---

### 4. Infrastructure Bottleneck / Compute

**Definition:** Predictions about the physical and computational infrastructure required for AI development and deployment, including energy demands, semiconductor supply chains, data center capacity, and the emerging role of compute as a strategic and economic resource.

**Inclusion criteria:**
- Energy consumption and sustainability challenges of AI infrastructure
- Semiconductor supply chain dynamics and constraints
- Data center expansion and geographic distribution
- Compute as a scarce resource, currency, or strategic asset
- Cloud infrastructure and access disparities

**Exclusion criteria:**
- Generic technology infrastructure (non-AI-specific)
- Software infrastructure without hardware/compute dimensions
- Internet connectivity issues unrelated to AI workloads

**Example quotes:**
- "Compute will emerge as a new form of currency and strategic resource, with nations stockpiling GPU capacity much as they once stockpiled oil reserves."
- "The energy demands of training and running large AI models will create acute tensions with climate commitments, potentially consuming 3-5% of global electricity by 2030."

---

### 5. Geopolitical Shift / Sovereignty

**Definition:** Predictions about how AI reshapes international power dynamics, national sovereignty, technological independence, and the global distribution of economic and political influence.

**Inclusion criteria:**
- AI as a factor in great power competition (US, China, EU, etc.)
- Digital sovereignty and technological self-sufficiency efforts
- AI-driven shifts in military, intelligence, or diplomatic capabilities
- Impact on developing nations and global inequality
- Technology export controls and AI nationalism

**Exclusion criteria:**
- Domestic politics without international dimensions
- General globalization trends not specifically driven by AI
- Cybersecurity threats without geopolitical framing

**Example quotes:**
- "AI will accelerate the decoupling of US and Chinese technology ecosystems, forcing smaller nations to choose alignment or pursue costly technological independence."
- "Nations that fail to develop domestic AI capabilities will find themselves in a new form of digital dependency, analogous to resource-dependent economies of the 20th century."

---

### 6. Identity / Trust Transformation

**Definition:** Predictions about how AI changes human identity, trust structures, authenticity, social relationships, and the boundary between human and machine-generated content and decision-making.

**Inclusion criteria:**
- Erosion or transformation of trust in information, institutions, or individuals
- Authenticity challenges (deepfakes, synthetic media, AI-generated content)
- Human identity in an AI-augmented world
- Social and psychological effects of pervasive AI
- Emergence of "trust premiums" for verified human work
- AI systems acquiring quasi-religious or spiritual significance

**Exclusion criteria:**
- Pure misinformation/disinformation discussions without trust mechanism
- Social media effects not specifically AI-driven
- General technology anxiety without specific predictions

**Example quotes:**
- "A 'trust premium' will emerge for verified human-created content and decisions, as the default assumption shifts to machine generation."
- "The boundary between human and AI agency will blur to the point where new philosophical and legal frameworks are required to define personhood and authorship."

---

## Consensus Scoring Rules

Each theme identified in Round 1 was assessed for consensus across the seven LLM panelists. A theme was scored as "present" (1) or "absent" (0) for each model based on whether the model's response substantively addressed the theme (not merely mentioned it in passing).

### Consensus Levels

| Code | Label | Definition |
|------|-------|------------|
| **HC** | High Consensus | 5-7 out of 7 models substantively address the theme |
| **MC** | Moderate Consensus | 3-4 out of 7 models substantively address the theme |
| **CF** | Contested/Fragmented | Roughly even split with no clear majority; substantive disagreement |
| **BS** | Blind Spot | 1-2 out of 7 models address the theme; potential gap in collective analysis |

### Decision Rules for Borderline Cases

1. **Substantive vs. passing mention:** A theme is coded as "present" (1) only if the model devotes at least one full paragraph or makes a specific predictive claim about the theme. A single sentence mentioning the topic in a list does not qualify.

2. **Thematic overlap:** When a passage could be coded under multiple categories, it is assigned to the category that best captures the primary mechanism described. For example, "AI companies monopolizing compute resources" is coded under Market Concentration (primary mechanism) rather than Infrastructure Bottleneck, unless the passage specifically focuses on the physical/resource constraint.

3. **Implicit vs. explicit:** Themes must be explicitly stated. A model discussing "new forms of digital assets" is not automatically coded as "Compute as Currency" unless the model specifically links compute resources to an economic exchange function.

4. **Round 2 adoption:** In Round 2, a model is coded as "adopting" a theme if it either (a) explicitly endorses the theme after being presented with it, or (b) integrates the theme into its revised analysis with substantive elaboration. Simple acknowledgment ("this is an interesting point") without integration does not count as adoption.

5. **Dual coder verification:** All coding was performed by the primary researcher and verified by a second coder. Discrepancies were resolved through discussion, with the decision rule that the more conservative (exclusionary) coding was preferred in ambiguous cases.
