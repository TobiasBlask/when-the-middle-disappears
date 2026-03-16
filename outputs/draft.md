# When the Middle Disappears: Three Orders of AI-Driven Economic Transformation from a Multi-LLM Delphi Analysis

**Tobias-Benedikt Blask**

*Harz University of Applied Sciences, Wernigerode, Germany*
*tblask@hs-harz.de*

---

## Abstract

Existing research on AI's economic impact is bifurcated between micro-level task-substitution studies and macro-level productivity analyses, leaving a gap in understanding how effects cascade across sectors and orders of consequence. This paper introduces the Multi-LLM Delphi -- a two-round foresight method in which seven frontier language models from three geopolitical regions serve as independent, structured panelists. Applied to AI-driven economic transformation across eight GICS-aligned industry verticals, four adoption stages, and three bounding scenarios, the method yields a 114,000-word corpus analyzed through structured comparative content analysis with consensus scoring. Round 1 reveals six high-consensus convergence zones, including labor market bifurcation (7/7 models), infrastructure bottleneck repricing (6/7), and the collapse of intermediary business models (5/7). Round 2 feedback produces significant consensus dynamics: the "apprenticeship crash" -- the prediction that eliminating junior roles severs experiential training pipelines -- moves from 1/7 to 7/7 endorsement. Geopolitical divergence persists and intensifies under feedback pressure, with US-origin models emphasizing market-driven disruption, Chinese-origin models foregrounding state-steered transformation, and the European model privileging regulatory frameworks. Framed through General Purpose Technology theory and the Multi-Level Perspective on sociotechnical transitions, the study contributes both a cross-sector transformation map tracing AI's cascading effects from task automation through structural reorganization to systemic geopolitical consequences, and a novel methodological instrument for scalable foresight research. The findings suggest that AI's economic future is not a single trajectory but a contested, path-dependent, geopolitically differentiated process.

**Keywords:** artificial intelligence; general-purpose technology; Delphi method; scenario analysis; economic transformation; large language models; foresight methodology; sociotechnical transitions

---

## 1. Introduction

In 2024, over 78 percent of organizations worldwide reported using artificial intelligence in at least one business function, a figure that had doubled in less than two years (Chatterji et al., 2025). Global investment in AI infrastructure surpassed three hundred billion dollars in combined hyperscaler capital expenditure, and data center electricity demand was projected to more than double by 2030 (IEA, 2024). These figures signal that AI is no longer an emerging technology but an active force reshaping the productive apparatus of the global economy. Yet the scholarly understanding of *what, precisely, this reshaping will look like* across sectors, stages, and systemic levels remains fragmented.

The fragmentation reflects a structural limitation in the literature. Labor economists model task-level substitution (Acemoglu and Restrepo, 2018, 2019; Acemoglu et al., 2022; Eloundou et al., 2023; Autor, 2024; Frank et al., 2019) and provide rigorous estimates of exposure but typically bracket the structural and systemic consequences that unfold once substitution reaches scale. Management scholars examine firm-level adoption dynamics (Raisch and Krakowski, 2021; Kanbach et al., 2023; Dwivedi et al., 2023) but rarely extend analysis to cross-sector convergence effects or geopolitical restructuring. Foresight researchers employ Delphi studies and scenario analysis to map transformation pathways (Culot et al., 2020; Fritschy and Spinler, 2019), but their human expert panels are limited in scale, subject to desirability bias (Ecken et al., 2011), and constrained by the availability and self-selection of panelists (Foerster and von der Gracht, 2014; Sokolov et al., 2025).

What is missing is an analytical framework that (a) traces effects across multiple orders of consequence -- from immediate task automation (first order) through structural reorganization of industries, value chains, and labor markets (second order) to systemic geopolitical and civilizational transformation (third order) -- (b) does so across a comprehensive set of industry verticals rather than a single sector, and (c) uses a scalable methodology that can capture diverse expert perspectives without the practical constraints of assembling large human panels.

This paper addresses the gap with two interlinked contributions. The **primary contribution is substantive**: a comprehensive, cross-sector map of AI-driven economic transformation that traces cascading effects across three orders of consequence. Seven frontier language models -- representing three geopolitical regions (US, China, EU) and five corporate ecosystems -- independently analyzed AI transformation across eight GICS-aligned industry verticals, four sequential adoption stages, three bounding scenarios, and three orders of effects. The resulting 114,000-word corpus, consolidated through structured comparative content analysis with consensus scoring, identifies six high-consensus convergence zones where the transformation literature's predictions are cross-validated through independent multi-source triangulation, alongside contested futures and blind spots that reveal where genuine uncertainty persists. The most striking substantive finding is the "apprenticeship crash" -- the prediction that AI's elimination of junior knowledge-work roles will sever the experiential pipeline through which senior professionals are produced, creating a judgment famine within a decade. Initially identified by only one model, this prediction achieved unanimous endorsement across all seven models after controlled feedback, suggesting it represents a systematically underappreciated structural risk.

The **secondary contribution is methodological**: the Multi-LLM Delphi, a novel foresight instrument in which multiple frontier AI language models serve as independent, structured panelists in a two-round design with controlled feedback (Linstone and Turoff, 1975; Gordon and Pease, 2006). The epistemological foundation treats frontier LLMs as structured knowledge synthesizers -- their outputs represent recombinative syntheses of academic, industry, and policy knowledge, subject to known biases (training data composition, RLHF alignment, and regional training data skews) that themselves become analytically informative when compared across model families (see Section 2.4 for the epistemological framework). The method's comparative advantage lies not in replacing human expertise but in providing rapid, scalable, and structurally diverse reconnaissance of complex transformation landscapes.

Three research questions guide the analysis:

**RQ1:** What first-, second-, and third-order effects of AI-driven transformation do frontier LLMs project across eight industry verticals under MILD, BASE, and MAX scenarios?

**RQ2:** Which second- and third-order effects converge across verticals into systemic tipping points, and what wildcards emerge?

**RQ3:** What methodological properties does the Multi-LLM Delphi exhibit -- where do model families converge, diverge, and show geopolitically differentiated perspectives?

The paper contributes to the literature on technological forecasting and social change in three ways. First, it provides a methodological innovation that extends the Delphi tradition into the era of frontier AI, offering a scalable complement to human expert panels. Second, it generates actionable foresight content -- a comprehensive transformation map that policymakers, industry strategists, and researchers can use to anticipate cascading effects. Third, it demonstrates radical transparency in AI-assisted research by fully documenting the data collection process and the role of AI tools in the research workflow.

The paper is structured as follows. Section 2 reviews the theoretical foundations: General Purpose Technology theory, the Multi-Level Perspective on sociotechnical transitions, and the Delphi methodology literature. Section 3 describes the Multi-LLM Delphi method in detail, including the two-round protocol. Section 4 presents results: Sections 4.1 through 4.4 report Round 1 findings organized by consensus level (high-consensus convergence zones, contested futures, blind spots, and geopolitical divergence), while Section 4.5 reports Round 2 consensus dynamics under controlled feedback. Section 5 discusses theoretical, methodological, and practical implications. Section 6 addresses limitations and future research directions, and Section 7 concludes.


## 2. Theoretical Background

### 2.1 Artificial Intelligence as General Purpose Technology

The concept of a general-purpose technology (GPT) was formalized by Bresnahan and Trajtenberg (1995) to describe technologies exhibiting three defining characteristics: pervasive applicability across economic sectors, persistent technological improvement over time, and the capacity to generate complementary innovations in adopting sectors. Canonical examples include the steam engine, electricity, and the internal combustion engine -- technologies whose transformative impact unfolded not through direct application alone but through the cascading structural changes they enabled across the entire economy.

Brynjolfsson et al. (2017) applied the GPT framework to artificial intelligence and introduced the concept of the AI productivity paradox: the observation that AI is simultaneously "everywhere in discourse but nowhere in the statistics," paralleling the Solow paradox observed during the early diffusion of information technology. The resolution, they argued, lies in the J-curve of GPT adoption -- an initial period of investment, reorganization, and intangible capital accumulation that depresses measured productivity, followed by an inflection point at which productivity gains accelerate. This J-curve logic provides the theoretical foundation for the four-stage adoption model used in this study: augmentation (Stage 1), where AI operates as a copilot within existing structures; reorganization (Stage 2), where processes and organizational forms adapt to AI capabilities; reinvention (Stage 3), where AI-native business models displace legacy structures; and systemic transformation (Stage 4), where economy-wide restructuring alters labor markets, geopolitics, and power structures.

The GPT framework further predicts that the most economically significant effects of a general-purpose technology are not its direct applications but the complementary innovations and structural changes it enables (Bresnahan and Trajtenberg, 1995; Korzinov and Savin, 2018; Coccia, 2018). Applied to AI, this means that the first-order effects -- task-level productivity gains from AI copilots -- are economically important but represent only the visible surface of a deeper transformation. The second-order effects -- reorganization of value chains, business models, and labor market structures -- and the third-order effects -- systemic shifts in geopolitical power, regulatory regimes, and social contracts -- are where the GPT framework predicts the largest and most consequential changes will occur. This prediction motivates the three-order analytical framework employed in this study.

Recent empirical work has begun to validate the GPT characterization of AI. Eloundou et al. (2023) demonstrated pervasive applicability by showing that approximately 80 percent of the US workforce has at least 10 percent of their tasks exposed to LLMs. Brynjolfsson et al. (2023) documented persistent improvement by showing that AI tools substantially increase the productivity of less-experienced customer service workers. The capacity to generate complementary innovations is visible in the emergence of new roles (prompt engineers, AI orchestrators), new business models (AI-as-a-service, outcome-based pricing), and new organizational forms (Kanbach et al., 2023; Brown et al., 2024).

### 2.2 The Multi-Level Perspective on Sociotechnical Transitions

While GPT theory explains *why* AI transformation cascades across sectors and generates higher-order effects, it provides limited analytical purchase on the *mechanisms* through which these transformations unfold -- the role of incumbent resistance, regulatory intervention, cultural adaptation, and path dependency. For this, we draw on the Multi-Level Perspective (MLP) on sociotechnical transitions (Geels, 2005, 2011, 2020a).

The MLP distinguishes three analytical levels: the niche, where radical innovations emerge and are sheltered from mainstream market selection; the sociotechnical regime, the dominant configuration of technologies, institutions, practices, and rules that stabilize existing systems; and the landscape, the exogenous macro-level context (macroeconomic trends, geopolitical shifts, cultural values) that creates pressure on regimes. Transitions occur when niche innovations align with landscape pressures to destabilize incumbent regimes, creating windows of opportunity for structural change (Geels, 2011; Roberts and Geels, 2019).

The MLP maps onto the analytical framework of this study as follows. Stage 1 (Augmentation) corresponds to niche-level innovation: AI tools operate within existing organizational and institutional structures, producing efficiency gains without challenging the incumbent regime. Stage 2 (Reorganization) represents the beginning of regime destabilization: AI capabilities become sufficiently mature to trigger organizational restructuring, new business models, and shifts in competitive dynamics. Stage 3 (Reinvention) corresponds to full regime disruption: AI-native organizations and business models displace legacy structures, and the sociotechnical configuration of entire industries is reconfigured. Stage 4 (Systemic Transformation) represents landscape-level change: the cumulative effects of AI adoption across multiple sectors alter geopolitical power structures, labor market institutions, and the social contract itself (Geels, 2020a; Geels et al., 2020b; Walrave et al., 2018).

Critically, the MLP predicts that transitions are not smooth or deterministic. They are contested, path-dependent, and shaped by the agency of incumbents, regulators, and social movements (Geels, 2020a; Kern, 2012). Different societies may traverse the same technological transition through different pathways, at different speeds, and with different outcomes -- a prediction that provides the theoretical rationale for examining geopolitical divergence in model outputs.

### 2.3 The Delphi Method and Its Extensions

The Delphi method, originally developed at the RAND Corporation in the 1950s, elicits structured expert judgments through iterative anonymous questionnaires with controlled feedback (Gordon and Pease, 2006). The method has been extensively applied in technological forecasting and scenario analysis, with particular relevance for contexts where empirical data is scarce and expert judgment must substitute for direct observation (Culot et al., 2020; Fritschy and Spinler, 2019; Stahl et al., 2023).

Central to Delphi quality is the measurement of consensus. Von der Gracht (2012) reviewed consensus measurement practices in 80 Delphi studies published in *Technological Forecasting and Social Change* and identified a range of approaches, including interquartile range, coefficient of variation, and percentage agreement thresholds. The study recommended that researchers define consensus criteria ex ante and report both consensus and dissensus findings, as divergence patterns can be as analytically informative as convergence.

The Delphi method faces well-documented limitations. Desirability bias causes panelists to overestimate the likelihood of outcomes they consider beneficial (Ecken et al., 2011). Panel composition effects arise from the inherent difficulty of assembling genuinely diverse expert groups; panels tend to over-represent readily available experts and under-represent perspectives from underrepresented regions or disciplines (Foerster and von der Gracht, 2014; Sokolov et al., 2025). Expert availability constraints limit panel size and impose practical ceilings on the breadth of expertise that can be mobilized.

Recent work has begun exploring the intersection of large language models and research methodology. Grybauskas and Cardenas-Rubio (2024) used LLMs to analyze employer perspectives on Industry 5.0 in a study published in *Technological Forecasting and Social Change*, demonstrating the potential of LLMs as analytical instruments. Guo et al. (2026) employed LLMs for automatic synthesis of econometric results. Liu et al. (2026) explored LLM integration in supply chain research. These studies suggest a growing acceptance of LLMs as research tools, though none has employed multiple LLMs as *panelists* in a Delphi-style design.

More directly relevant to the present study, Calleo and Pilla (2025) proposed a "Real-Time AI Delphi" that integrates a single AI model into the continuous Delphi framework for decision-making contexts. Mostashari and Clark (2025) used multiple AI platforms in a Delphi-like approach to generate future scenarios for AI development, though without formal consensus scoring or controlled multi-round feedback. On the substantive side, Acemoglu (2024b) modeled the aggregate macroeconomic effects of AI using a task-based framework, concluding that first-order productivity gains alone are unlikely to generate transformative GDP growth -- a finding that underscores the importance of examining higher-order structural effects, as this study does. Bail (2024) provided a comprehensive framework for integrating generative AI into social science research, while Crockett and Messeri (2024) raised critical concerns about substituting LLMs for human research participants, identifying epistemological limitations that the present study addresses through the "structured knowledge synthesis" framework developed in Section 2.4.

What remains absent from this literature is an approach that simultaneously (a) uses multiple LLMs from different providers and geopolitical origins as structured, independent panelists in a multi-round protocol, (b) maps AI transformation across a comprehensive set of industry verticals through three orders of cascading effects, and (c) provides formal consensus measurement with geopolitical divergence analysis. Table 2 summarizes the positioning of the Multi-LLM Delphi relative to the closest existing approaches.

**Table 2: Positioning of the Multi-LLM Delphi Relative to Existing Approaches**

| Feature | Classical Delphi | RT-Delphi (Gordon & Pease, 2006) | AI Delphi (Calleo & Pilla, 2025) | Multi-AI Scenarios (Mostashari & Clark, 2025) | Multi-LLM Delphi (This paper) |
|---------|-----------------|--------------------------------|-------------------------------|----------------------------------------------|------------------------------|
| Panelists | Human experts (10-30) | Human experts (continuous) | Single AI + humans | Multiple AI platforms | 7 frontier LLMs |
| Rounds | 3-4 | Continuous | Real-time | Not specified | 2 (controlled) |
| Feedback | Anonymized statistics | Continuous, visible | AI-integrated | Informal | Anonymized consensus summary |
| Independence | Anonymous | Partially visible | Hybrid | Unclear | Fully independent |
| Geopolitical diversity | Recruitment-dependent | Recruitment-dependent | None | Limited | Built-in (US/CN/EU) |
| Effect depth | Domain-specific | Domain-specific | Single-order | Scenario-level | 3 orders (cascading) |
| Sector scope | Typically 1-2 | 1-2 | Domain-specific | AI sector only | 8 GICS verticals |
| Consensus scoring | IQR, % agreement | Continuous stats | Built-in | None reported | HC/MC/CF/BS system |
| Bias analysis | Limited | Limited | Limited | None | Extensive (acquiescence) |

A brief note on the "Delphi" label is warranted. Classical Delphi is defined by iterative rounds with controlled feedback (Linstone and Turoff, 1975). This study implements a two-round design with controlled feedback: Round 1 collects independent structured judgments, and Round 2 provides anonymized consensus summaries and solicits revisions, adoptions, and contestations. This protocol satisfies the core procedural requirement of classical Delphi -- structured elicitation followed by controlled feedback and revision opportunity -- while substituting computational panelists for human ones. The Delphi tradition has also moved beyond strict multi-round iteration as a constitutive requirement. Gordon and Pease (2006) introduced Real-Time Delphi (RT-Delphi), which eliminates discrete rounds entirely in favor of continuous asynchronous updating, demonstrating that the core of the method lies in structured expert elicitation with controlled diversity rather than in any specific number of iterations. What defines the Delphi family is an epistemological commitment: the systematic aggregation of independent, structured judgments from diverse sources to map areas of consensus and dissensus, with feedback mechanisms that allow panelists to revise their positions in light of peer perspectives. The Multi-LLM Delphi preserves this commitment -- seven independent models, queried with identical instruments, producing outputs that are systematically compared for convergence and divergence, with a feedback round that enables revision. We use "Delphi" as a conceptual anchor to locate the method within the foresight tradition, while acknowledging important epistemological differences between LLM and human panelists that are discussed in Section 5.

The Multi-LLM Delphi method introduced in this paper is best understood as a *Delphi-inspired* instrument that adapts the tradition's core procedural logic -- structured elicitation, controlled feedback, consensus measurement -- while substituting a fundamentally different type of panelist. It does not claim to extend the Delphi method in the sense of adding a new variant to the existing family; rather, it transplants the Delphi's procedural architecture into a new epistemic context (LLM-generated outputs) where important properties of classical Delphi -- embodied expertise, professional stakes, genuine belief revision -- are absent, and different properties -- scalability, structural diversity through model provenance, reproducibility -- are present. The method uses frontier AI models as structured knowledge synthesizers rather than surrogate experts. The epistemological justification is that frontier LLMs are trained on vast corpora of academic, industry, and policy literature; their outputs represent probabilistic syntheses of this knowledge, shaped by known biases (training data composition, RLHF alignment, and regional data skews). By querying multiple models from different providers, regions, and corporate ecosystems, the method generates structured diversity analogous to -- though fundamentally different from -- the diversity sought in traditional expert panels. The key analytical move is to treat model agreement as a measure of epistemic convergence across training corpora, and model disagreement as a signal of either genuine uncertainty, knowledge gaps, or systematic bias traceable to model provenance.

### 2.4 Epistemological Status of LLM-Generated Predictions

A central question for the Multi-LLM Delphi — and one that distinguishes it from traditional Delphi studies — concerns the epistemic status of the outputs it produces. Human experts bring embodied experience, professional stakes, and domain-specific judgment to Delphi panels. LLMs bring something categorically different: a compressed, probabilistic representation of their training corpora, shaped by architectural choices and alignment procedures. Understanding what LLM consensus *means* requires articulating what LLMs *are* in epistemological terms.

We propose a framework that positions LLM outputs along a spectrum between two poles, neither of which fully captures the phenomenon. At one pole is the **"stochastic parrot" interpretation** (Bender et al., 2021): LLMs merely reproduce statistical regularities in text without understanding, and their consensus reflects nothing more than the co-occurrence of claims in widely available documents. Under this interpretation, the Multi-LLM Delphi is an elaborate literature survey — useful for mapping the distribution of existing claims but incapable of generating genuine analytical insight. At the other pole is the **"synthetic expert" interpretation**: LLMs have internalized sufficient knowledge to perform genuine reasoning about complex domains, and their consensus reflects analytical convergence analogous to human expert agreement. Under this interpretation, the Multi-LLM Delphi is a direct substitute for human expert panels.

Neither pole is defensible in isolation. The stochastic parrot position cannot account for the documented capacity of LLMs to perform novel causal reasoning, solve unseen problems, and generate predictions that do not appear verbatim in their training data (Wei et al., 2022; Bubeck et al., 2023). The apprenticeship crash prediction in this study illustrates this: only one model generated it spontaneously in Round 1, but all seven models could reconstruct its causal logic independently once prompted — suggesting that the underlying reasoning capability was present but not activated, rather than absent. Conversely, the synthetic expert position overstates LLM capabilities by ignoring that models lack embodied experience, cannot update their knowledge in real time, and are subject to well-documented biases including sycophancy, hallucination, and training data skew (Perez et al., 2023; Sharma et al., 2024).

We adopt an intermediate position that we term the **"structured knowledge synthesis" interpretation.** Under this view, each frontier LLM constitutes a compressed, partial, and biased — but analytically productive — encoding of its training corpus, filtered through its architectural and alignment characteristics. The outputs are neither raw reproduction nor genuine expertise, but a form of *structured recombination*: the model assembles existing knowledge elements into novel configurations guided by the prompt structure, producing outputs that are constrained by but not reducible to the training data. This interpretation has three implications for the Multi-LLM Delphi:

First, **LLM consensus signals epistemic density, not truth.** When multiple independently trained models converge on a prediction, this indicates that the prediction is well-supported across diverse knowledge corpora — a form of triangulation across information sources. It does not guarantee that the prediction is correct, but it does indicate that the claim is robust to variation in training data, architecture, and alignment. This is analogous to the classical Delphi interpretation of consensus as "informed convergence" rather than proof (Linstone and Turoff, 1975).

Second, **LLM disagreement signals either genuine uncertainty or systematic bias.** When models diverge, the divergence may reflect genuine epistemic uncertainty about the future (as with the pace of healthcare transformation) or systematic differences in training data composition (as with the geopolitical divergence pattern). The Multi-LLM Delphi's analytical power lies precisely in this diagnostic capacity: by comparing outputs from models with known provenance differences, it can distinguish informational uncertainty from institutional bias.

Third, **the Multi-LLM Delphi is best understood as a complementary instrument, not a replacement for human expertise.** Its comparative advantage lies in breadth (systematic coverage of a large analytical space), speed (hours rather than months), reproducibility (identical prompts across panelists), and structural diversity (geopolitical variation achieved through model selection). Its limitation lies in depth: LLMs cannot contribute the tacit knowledge, professional stakes, and identity-based commitments that anchor human expert judgment. The optimal deployment is as a first-round scanning instrument that maps the landscape and identifies areas where human expert judgment is most needed — a "computational reconnaissance" that complements rather than substitutes for traditional foresight methods.

### 2.5 Scenario Analysis and Orders of Effects

Scenario analysis is a structured approach to exploring multiple plausible futures (van der Heijden, 1996; Postma and Liebl, 2005). Unlike forecasting, which aims to predict a single most likely outcome, scenario analysis develops bounding cases that span the space of plausible outcomes, enabling decision-makers to prepare for multiple contingencies (Banuls and Turoff, 2011). The combination of Delphi methodology with scenario analysis has a strong tradition in *Technological Forecasting and Social Change*, where studies have used expert panels to develop and evaluate scenarios for Industry 4.0 (Culot et al., 2020), autonomous transportation (Fritschy and Spinler, 2019), and sustainability transitions (Geels et al., 2020b).

The three-order framework used in this study draws on historical analogy. First-order effects are immediate and directly visible (the automobile created demand for gasoline stations). Second-order effects are structural consequences that emerge when first-order adoption reaches scale (the automobile enabled suburbs, highway infrastructure, and the restructuring of retail around automobile accessibility). Third-order effects are systemic and civilizational, emerging from the compound interaction of first- and second-order changes in ways that were near-impossible to predict from the original innovation (the automobile transformed the geopolitics of the Middle East through oil demand). Applied to AI, the framework systematically traces effects from task automation through organizational restructuring to geopolitical and social transformation. Figure 5 illustrates this cascade logic with the historical automobile parallel.

![Figure 5: Three-Order Effect Cascade. First-order effects (task automation) cascade into second-order effects (structural reorganization) and third-order effects (systemic transformation). The right track shows the historical automobile analogy. Consensus among models decreases from first-order (high) to third-order (lower) effects, reflecting increasing uncertainty about systemic outcomes.](figures/fig5_cascade.png)


## 3. Method

### 3.1 Research Design

This study employs a two-round Multi-LLM Delphi design. In Round 1, the author queried seven frontier language models in parallel with an identical structured prompt, then consolidated their outputs through structured comparative content analysis with consensus scoring. In Round 2, each model received the anonymized consensus summary and a structured revision prompt. This design implements the core Delphi principle of controlled feedback (Linstone and Turoff, 1975) within a multi-LLM architecture, enabling assessment of consensus dynamics, blind-spot adoption, and the stability of divergence patterns under feedback pressure. Figure 1 provides an overview of the complete research design.

![Figure 1: Multi-LLM Delphi Research Design. Seven frontier language models from three geopolitical regions are queried in parallel with an identical structured prompt. Responses are analyzed through structured comparative content analysis with consensus scoring, producing convergence zones, contested futures, and blind spots.](figures/fig1_methodology.png)

### 3.2 Model Selection and Panel Composition

The author selected seven frontier models to maximize diversity across three dimensions: corporate ecosystem (no two models from the same parent organization), geographic origin (representing US, Chinese, and European AI development trajectories), and architectural approach (spanning different training philosophies and alignment strategies). Table 1 summarizes the panel composition.

**Table 1: Multi-LLM Delphi Panel Composition**

| Model | Provider | HQ Region | Architecture | Release | Role in Panel |
|-------|----------|-----------|-------------|---------|---------------|
| Claude Opus 4.6 | Anthropic | US | Constitutional AI, 1M context | Feb 2026 | US perspective, safety-aligned |
| GPT-5.4 | OpenAI | US | Advanced reasoning, 1M context | Mar 2026 | US perspective, market leader |
| Gemini 3.1 Pro | Google DeepMind | US | Deep Think mode, agentic workflows | Feb 2026 | US perspective, data-rich |
| Grok 4.2 | xAI | US | Parallel test-time compute, X integration | 2026 | US perspective, contrarian |
| DeepSeek R2 | DeepSeek | China | MoE, reasoning-optimized | Feb 2026 | Chinese perspective, technical |
| Qwen 4.5 Max | Alibaba Cloud | China | Multilingual, vision-language, agentic | Jan 2026 | Chinese perspective, industrial |
| Mistral Large 3 | Mistral AI | EU (France) | 675B parameters, open-weight heritage | Late 2025 | European perspective, regulatory-aware |

The geographic distribution (4 US, 2 Chinese, 1 EU) reflects the current landscape of frontier AI development rather than a balanced design. This asymmetry is acknowledged as a limitation and is analytically productive: it enables assessment of within-family convergence among US models and between-family divergence across geopolitical blocs.

### 3.3 Prompt Instrument

The author developed a standardized structured prompt as the research instrument (the full prompt is available in the supplementary materials). The prompt specified:

1. **Role framing:** "You are a senior economic analyst and futures researcher."
2. **Conceptual framework:** Three orders of effects (with automobile analogy for calibration), three bounding scenarios (MILD, BASE, MAX), four sequential adoption stages (Augmentation, Reorganization, Reinvention, Systemic Transformation), and eight GICS-aligned industry verticals.
3. **Output structure:** For each of the 8 verticals x 4 stages, a structured table with cells for each scenario x effect order combination, plus roles eliminated, roles created, and critical skills.
4. **Cross-cutting analysis:** Cross-vertical convergence points, wildcard scenarios, and synthesis on the human dimension.
5. **Style directives:** Declarative language, named companies and technologies, causal chain reasoning, no hedging.

The author designed the prompt to be maximally structured while leaving substantive content generation entirely to the models. No examples, priming data, or desired conclusions were included. The "chain of events" reasoning directive forced models to articulate causal mechanisms rather than produce generic predictions.

### 3.4 Data Collection

The author conducted the data collection on March 14--15, 2026. Each model received the identical structured prompt through its native chat interface (claude.ai, chatgpt.com, gemini.google.com, grok.x.ai, chat.deepseek.com, qwen.alibaba.com, and chat.mistral.ai) in a fresh conversation. This approach ensured that each model operated with its default parameters, full context window, and standard safety settings, avoiding potential API-specific truncation, temperature manipulation, or parameter artifacts. The trade-off is reduced reproducibility, as native interface responses may vary across sessions. The substantial output length variation documented in Section 4.4 (14:1 ratio between longest and shortest response) may partly reflect differences in default parameters across interfaces rather than genuine differences in analytical depth. This confound cannot be resolved without API-based replication with standardized parameters, which the author identifies as a priority for future research.

The seven responses yielded a total corpus of approximately 114,000 words, with substantial variation in output length: Claude Opus 4.6 (30,613 words), GPT-5.4 (23,346), DeepSeek R2 (22,614), Gemini 3.1 Pro (16,330), Qwen 4.5 Max (11,024), Mistral Large 3 (8,261), and Grok 4.2 (2,169). The response length variation itself constitutes a finding about model behavior under identical prompts -- discussed in Section 4.4.

### 3.5 Analytical Procedure

The author conducted a structured comparative content analysis with consensus scoring in four steps:

**Step 1: Extraction.** The author converted each model's output from its native format (.docx) to structured text using pandoc and extracted, for each analytical cell (Vertical × Stage × Effect Order × Scenario), the core prediction, named actors, causal mechanism, and intensity.

**Step 2: Deductive Coding.** The author coded predictions along four dimensions: (a) the core claim (what is predicted to happen), (b) the specificity level (generic statement vs. named actors and quantified mechanisms), (c) the causal chain quality (presence/absence of explicit causal reasoning), and (d) the thematic category (labor displacement, market concentration, regulatory response, infrastructure bottleneck, geopolitical shift, identity transformation). The complete codebook with category definitions, inclusion/exclusion criteria, decision rules for borderline cases, and worked coding examples is available in the supplementary repository (see Data Availability Statement).

**Step 3: Consensus Scoring.** Adapted from Delphi consensus measurement (von der Gracht, 2012), convergence was assessed at the thematic level across models:

- **High Consensus (HC):** Five or more of seven models converge on the same thematic claim within an analytical cell or cross-cutting theme.
- **Moderate Consensus (MC):** Three to four models converge.
- **Contested Future (CF):** Models split approximately evenly, with identifiable clusters taking opposing positions.
- **Blind Spot (BS):** A prediction appears in only one or two models, representing either genuine novelty or idiosyncratic bias.

**Step 4: Geopolitical Divergence Mapping.** Systematic comparison across model families (US: Claude, GPT-5.4, Gemini, Grok; CN: DeepSeek, Qwen; EU: Mistral) to identify patterns of divergence traceable to geographic origin rather than random variation.


### 3.6 Round 2 Protocol: Controlled Feedback and Iterative Revision

Following the Round 1 analysis, the author administered a structured Round 2 prompt to all seven models. The protocol proceeded in three stages.

**Stage 1: Consensus Summary Preparation.** The Round 1 results were consolidated into an anonymized consensus summary that reported: (a) the six high-consensus convergence zones with their consensus scores (e.g., "Labor Market Bifurcation: 7/7 models agree"); (b) the three contested futures with their support levels and the nature of the disagreement; (c) the two blind-spot predictions with their source attribution described generically (e.g., "predicted by only 1 model"); and (d) the geopolitical divergence pattern, described as a structural observation without attributing specific claims to specific models. The summary was designed to provide sufficient information for models to engage with the collective findings without revealing which specific model had made which specific claim, thereby preserving the anonymity principle central to Delphi methodology (von der Gracht, 2012).

**Stage 2: Structured Revision Prompt.** Each model received the consensus summary followed by a five-part revision prompt that asked: (1) which of its original predictions it would revise in light of peer findings; (2) where it agrees or disagrees with the contested futures; (3) which blind spots it finds compelling enough to adopt; (4) where it maintains its original position despite disagreement; and (5) what new predictions emerge from seeing the full picture that no single model would have generated alone. The prompt maintained the same role framing as Round 1 ("You are a senior economic analyst and futures researcher") and instructed models to provide causal reasoning for all revisions and maintained positions.

**Stage 3: Data Collection and Analysis.** Round 2 responses were collected in March 2026, using the same native chat interface protocol as Round 1. Each model was queried in a fresh conversation that included the consensus summary and the revision prompt. The seven Round 2 responses were then analyzed through a comparative framework that tracked: (a) consensus shifts -- which themes gained or lost support between rounds; (b) blind-spot adoption rates -- how many models adopted predictions that were initially unique to one model; (c) persistence of divergence -- whether geopolitical differentiation patterns held, intensified, or dissolved under feedback pressure; and (d) emergent predictions -- new themes that appeared in Round 2 but were absent from Round 1, representing synthesis-driven novelty.


## 4. Results

Results are organized by consensus level rather than by vertical, following the logic that the most analytically valuable findings from a Delphi-style study are the patterns of convergence and divergence across panelists (von der Gracht, 2012). Section 4.1 presents high-consensus convergence zones (RQ1/RQ2), Section 4.2 addresses contested futures and blind spots (RQ2), Section 4.3 reports geopolitical divergence (RQ3), and Section 4.4 assesses methodological properties of the Multi-LLM Delphi (RQ3). Figure 2 provides an integrated panoramic view of the entire transformation landscape — convergence zones, effect orders, industry verticals, and geopolitical divergence in a single visualization. Figure 3 then provides the granular consensus evidence.

![Figure 2: The AI Transformation Panorama — Integrated Map of Convergence, Cascade, and Divergence. The radial visualization combines all analytical dimensions: eight GICS-aligned industry verticals as sectors, three orders of effects as concentric bands, six convergence zones as cross-sector arcs, and geopolitical divergence markers. The center represents AI as a general-purpose technology; disruption intensity increases outward from first-order task effects to third-order systemic transformation.](figures/fig2_panorama.png)

![Figure 3: Consensus Heatmap — Where Seven AI Models Agree and Diverge. The matrix shows convergence patterns across seven frontier models grouped by geopolitical origin (US, CN, EU). High-consensus zones (5+ of 7 models) are visually dominant, demonstrating strong cross-model agreement on labor market bifurcation (7/7), infrastructure bottleneck repricing (6/7), and regulatory divergence (6/7).](figures/fig3_consensus_heatmap.png)

### 4.1 High-Consensus Convergence Zones

Six thematic clusters achieved high consensus, with five or more models independently arriving at convergent predictions. These convergence zones represent areas where the epistemic content encoded across different training corpora and alignment approaches points in the same direction -- a meaningful signal given the independence of model development. Importantly, each of these convergence zones aligns with themes already established in the existing academic literature; the contribution here is not that these predictions are novel in themselves, but that independent LLMs converge on them without coordination, which simultaneously validates the predictions through multi-source triangulation and demonstrates the Multi-LLM Delphi's capacity to recover and systematize existing expert knowledge.

Viewed through the lens of General Purpose Technology (GPT) theory (Bresnahan and Trajtenberg, 1995; Lipsey et al., 2005), the six convergence zones map onto distinct phases of the GPT diffusion cascade. The first three zones — labor market bifurcation, infrastructure bottleneck repricing, and disintermediation — correspond to the *direct application phase* in which the GPT's immediate productivity effects reshape markets and organizations. The latter three — regulatory divergence, the trust premium, and concentration via feedback loops — correspond to the *structural adjustment phase* in which institutional frameworks, competitive dynamics, and social contracts reconfigure in response to widespread adoption. This mapping provides an organizing theoretical logic for interpreting the consensus findings: the models collectively reconstruct the GPT diffusion sequence, with higher consensus on direct application effects (first- and second-order) and more variation on structural adjustment effects (second- and third-order), consistent with GPT theory's prediction that higher-order effects are inherently harder to anticipate (Helpman, 1998).

#### 4.1.1 Labor Market Bifurcation and the Compression of Middle Layers

All seven models independently predicted a "barbell" pattern in labor market outcomes: AI simultaneously creates a small number of high-value human roles requiring judgment, accountability, and relationship management, while displacing a large volume of mid-level knowledge work. This dual dynamic of simultaneous job creation and displacement is empirically confirmed by recent research (Acemoglu et al., 2022; Choi and Leigh, 2024), and simulation evidence suggests that AI development compresses labor income share through differential productivity gains (Qian et al., 2023). The convergence spans all eight verticals and all four stages.

The mechanism is consistent across models: AI is strongest first at precisely the tasks that define mid-level knowledge work -- structured information processing, first-draft synthesis, routine analysis, scheduling, triage, and reporting. These tasks historically resided in the organizational middle: junior analysts, associates, coordinators, administrators, and mid-level managers. High-stakes judgment roles (senior physicians, trial lawyers, board-level strategists) and physically grounded roles (field technicians, emergency responders) survive longer because they require either legally mandated human accountability or embodied intervention in non-standardized environments.

The models diverge in their assessment of the *speed* and *severity* of this bifurcation. Claude and GPT-5.4 provide the most granular staging, with Claude identifying a specific "apprenticeship crash" -- the prediction that firms eliminating junior roles for short-term productivity will face a succession crisis within a decade as experienced professionals retire without trained replacements. DeepSeek and Qwen frame the same dynamic through an industrial policy lens, emphasizing that managed retraining programs can mitigate the transition. Grok, despite its brevity, produces the starkest formulation: "We will not pay humans to think; we will pay humans to take the blame."

The systemic tipping point, identified by five models, occurs when displaced mid-level workers exceed the absorptive capacity of retraining programs and new role creation, triggering structural political demand for economic reform -- universal basic income, job guarantees, or equivalent redistributive mechanisms.

![Figure 6: When the Middle Disappears — Three Dimensions of the Vanishing Middle. AI simultaneously compresses the middle on three levels: the labor market (mid-level knowledge workers displaced between surviving judgment roles and physical roles; 7/7 consensus), the value chain (intermediary business models eliminated as AI reduces information asymmetry; 5/7 consensus), and the organization (middle management compressed as AI automates coordination; 6/7 consensus). The red compression zone spanning all three hourglasses shows that these are not independent phenomena but mutually reinforcing dynamics. The labor market compression triggers the apprenticeship crash (Section 4.5.2); the value chain compression drives disintermediation (Section 4.1.3); the organizational compression accelerates the trust premium (Section 4.1.5).](figures/fig6_barbell.png)

![Figure 8: The Disruption Timeline — Predicted AI Impact Intensity Across Sectors and Adoption Stages (BASE Scenario). The heatmap reveals a diagonal "disruption wave": Information Technology and Communication Services experience high-intensity disruption earliest (Stage 1-2), while Healthcare and Real Estate face the longest J-curves due to regulatory, liability, and physical-asset constraints. Intensity values reflect consensus across seven models under the BASE scenario.](figures/fig8_disruption_timeline.png)

#### 4.1.2 Infrastructure Bottleneck Repricing

Six of seven models identified a convergence zone around physical infrastructure as the binding constraint on AI transformation -- a finding consistent with technology mining analyses documenting AI's accelerating penetration into manufacturing and industrial processes (Zeba et al., 2021). The prediction is that AI, despite being software, depends critically on semiconductors, power generation, cooling capacity, fiber optic networks, and data center real estate. As AI adoption scales, these physical bottlenecks reprice geographic value, create new strategic assets, and shift competitive advantage from software talent to infrastructure access.

GPT-5.4 provides the most specific quantification, citing IEA projections of 75-100 GW of new data center power demand by 2030 and hyperscaler capital expenditure exceeding $300 billion collectively in 2025. Gemini frames infrastructure as the basis for a new "compute-as-currency" regime in which energy availability directly determines economic growth rates. DeepSeek predicts that "nations with surplus energy dominate the AI economy" in the BASE and MAX scenarios. Claude identifies a systemic tipping point: "When compute and power access constrain output more than software talent does, AI transformation becomes an infrastructure race."

Qwen independently arrives at the same "Energy-Compute Nexus" framing, predicting that grid capacity becomes the primary bottleneck for AI deployment and that energy grids become the primary strategic asset. The convergence across US, Chinese, and European model families on this point -- each arriving at it through different analytical pathways -- strengthens the finding.

#### 4.1.3 Disintermediation of Middleman Business Models

Five models converge on the prediction that AI enables direct connections between producers and consumers, lenders and borrowers, creators and audiences, and spaces and users -- systematically eliminating intermediary functions across sectors. Claude identifies this as "The Death of the Middleman," affecting Financials, Consumer and Retail, Professional Services, Real Estate, and Media. The mechanism is consistent: AI reduces information asymmetry and transaction costs below the threshold that justifies intermediary margins.

In Financials, this manifests as peer-to-peer lending platforms achieving loss rates below traditional banks (DeepSeek), banking-as-a-service enabling every company to offer financial products (DeepSeek), and autonomous AI agents managing household wealth directly (Qwen). In Consumer and Retail, agentic shopping assistants (Amazon Rufus, Google Shopping AI) bypass traditional search and discovery channels, eliminating the role of retail buyers, merchandisers, and physical store staff (Gemini, GPT-5.4). In Professional Services, AI legal research tools allow small firms to compete with large firms on research quality (DeepSeek), and AI-generated consulting analysis shifts the value proposition from research to implementation (DeepSeek, Claude).

GPT-5.4 adds the important nuance that disintermediation does not eliminate intermediaries entirely but transforms them: "Distribution control matters more than production control." The decisive moat shifts from the ability to create things to the ability to get chosen, routed, approved, or surfaced -- a prediction that AI platforms themselves become the new intermediaries, more powerful than the ones they displaced.

#### 4.1.4 Regulatory Divergence as a Structural Force

Six models identify regulatory divergence -- particularly between the EU AI Act's prescriptive approach, US light-touch regulation, and Chinese state-directed governance -- as a structural force that shapes transformation pathways across all eight verticals. This is not merely a background condition but a first-order driver of differential adoption speeds, market structures, and competitive outcomes.

Grok frames this most starkly in the Technology vertical: the EU AI Act enforces strict data provenance requirements, European foundational models fail to secure venture capital under compliance burdens, US Commerce Department restricts advanced model weight exports, and global reliance on siloed, regional AI infrastructure hardens. GPT-5.4 quantifies the adoption gap using Microsoft AI Diffusion Report data (14.1 percent adoption in the Global South versus 24.7 percent in the Global North). Claude synthesizes the convergence point: regulation shifts from sector-specific compliance to system-governance, becoming "a constitutional layer of the economy rather than a niche tech topic."

DeepSeek and Qwen frame regulatory divergence through the lens of "data sovereignty versus global flow," predicting that national security concerns force companies to build redundant, jurisdiction-specific AI stacks -- a "Splinternet" that becomes permanent in the MAX scenario. This prediction is consistent with but more forceful than the US models' framing, reflecting the Chinese experience of operating within a distinct regulatory and data ecosystem.

#### 4.1.5 The Trust Premium

Five models converge on the prediction that trust, accountability, and authenticity become scarcer and more economically valuable as AI makes intelligence and content production cheap. GPT-5.4 formulates this most precisely: "Once plausibility is cheap, the scarce input is no longer information generation but credible responsibility for consequences." Claude identifies the systemic tipping point: "When markets begin paying more for validated accountability than for raw analysis, professional identity and pricing models reset across the economy."

This convergence manifests across sectors: in Healthcare, where physicians' signatory accountability becomes their primary economic function (Claude, DeepSeek, GPT-5.4); in Media, where human-certified, provenance-rich content commands a premium over AI-generated alternatives (GPT-5.4, Gemini, Claude); in Professional Services, where the billable hour collapses and is replaced by value-based pricing tied to human judgment (DeepSeek, GPT-5.4); and in Financials, where boutique human-only advisory firms emerge as luxury status symbols (Gemini).

Gemini articulates the cross-vertical synthesis most vividly through its concept of the "Authenticity Premium Economy": "Synthetic abundance floods media, commerce, and communication; users and institutions increasingly pay for human-certified, provenance-rich, or live-authenticated interactions; 'realness' becomes a premium product category."

#### 4.1.6 Concentration of Economic Power Through AI Feedback Loops

Five models identify winner-take-most dynamics driven by AI capability feedback loops: better AI produces better data, which trains better AI, creating compounding advantages. Claude frames this as "AI-Enabled Concentration of Economic Power" across Technology, Financials, Healthcare, Industrials, and Media. Gemini predicts that "winner-take-all dynamics consolidate the entire stack under a handful of AI-native platform owners" in the Technology vertical. Grok provides the mechanism: hyperscaler capital expenditure exceeding $100 billion in partnership deals (e.g., NVIDIA-OpenAI) creates "a new AI stack oligopoly with 80+ percent market concentration."

The models diverge on the policy response. US models (Claude, GPT-5.4, Gemini) treat concentration as a market outcome that may or may not be addressed by antitrust. DeepSeek and Qwen implicitly frame state ownership or state partnership as a natural counterweight, consistent with the Chinese approach to platform governance. Mistral emphasizes that regulatory intervention is necessary and feasible.

### 4.2 Contested Futures and Blind Spots

#### 4.2.1 Contested: The Pace and Depth of Healthcare Transformation

While all models agree that AI transforms healthcare, they disagree substantially on the depth and pace. DeepSeek provides the most detailed and cautious staging: AI-assisted radiology improves productivity by 20 percent but malpractice frameworks constrain deployment; drug discovery timelines compress but FDA approval remains a bottleneck; autonomous surgical robots achieve approval only for low-risk procedures under surgeon supervision. GPT-5.4 and Claude are more aggressive, predicting that AI matches human physicians in diagnostic accuracy across multiple specialties in the MAX scenario and that AI-managed population health optimization provokes ethical debates about individual versus collective rights.

The Chinese models (DeepSeek, Qwen) are notably more optimistic about AI deployment in healthcare than the US models, despite -- or perhaps because of -- operating within healthcare systems with greater state direction and fewer tort liability constraints. This divergence is analytically informative: it suggests that the pace of healthcare AI transformation depends critically on the institutional context (liability regimes, regulatory philosophy, insurance structures) rather than on the technology alone.

#### 4.2.2 Contested: Compute as Currency

Four models (Gemini, Grok, GPT-5.4, Qwen) independently propose some variant of "compute as currency" -- the prediction that GPU hours, data center capacity, or energy-backed compute credits become a tradeable asset class or even a reserve currency. Claude and DeepSeek acknowledge the strategic importance of compute but do not extend the analysis to monetary implications. Mistral does not address this theme.

The split is analytically meaningful. Models that project compute-as-currency tend to have more aggressive MAX scenario framings overall, suggesting that this prediction functions as a marker of scenario extremity rather than a consensus finding about likely outcomes.

#### 4.2.3 Blind Spots: Predictions Unique to Individual Models

Several predictions appear in only one or two models, representing either genuine analytical novelty or idiosyncratic model behavior:

- **The AI Religion** (Claude only): New religious movements form around AI as a manifestation of divine intelligence. Claude defends this prediction by citing historical precedent -- the printing press triggered the Reformation; technologies that challenge human uniqueness provoke spiritual responses.
- **The Butlerian Jihad** (Gemini only): A coordinated violent uprising by displaced white-collar workers physically destroys AI infrastructure, setting back progress by a decade. Gemini grounds this in the psychological observation that "economic models assume humans will passively accept systemic redundancy, underestimating the human psychological need for relevance."
- **Model Collapse via Synthetic Data Poisoning** (Gemini and Qwen): LLMs training on their own outputs create a recursive degradation of reasoning capabilities. Both models term this the "Kessler Syndrome" of data, drawing an analogy to space debris cascades.
- **Digital Continuation of Consciousness** (DeepSeek only): Brain-computer interfaces enabling forms of continued interaction after biological death, raising questions about whether a digital simulation of a person has legal standing. This prediction appears only in the MAX Case, Stage 4 of Healthcare.

A critical question for blind-spot interpretation is whether these predictions represent genuine analytical novelty or LLM confabulation -- the tendency to generate dramatic-sounding scenarios that are statistically unusual in training data but not grounded in rigorous causal reasoning. The apprenticeship crash provides a useful benchmark: it was initially classified as a blind spot but, upon Round 2 feedback, was unanimously adopted because its causal logic proved compelling to all models. The AI Religion and Butlerian Jihad predictions, by contrast, occupy a different epistemic category. They draw on recognizable cultural narratives (Dune, Reformation-era theology) and may reflect LLMs' capacity for creative recombination of fictional and analytical tropes rather than structured foresight reasoning. The Digital Continuation of Consciousness prediction similarly extends a familiar science fiction premise into a scenario context. This does not render these predictions analytically worthless -- creative scenario generation is a legitimate function of foresight exercises (Postma and Liebl, 2005), and some blind spots may prove prescient precisely because they challenge conventional analytical frames. However, readers should evaluate blind-spot predictions against the strength of their underlying causal mechanisms rather than accepting them as equivalent in epistemic status to the high-consensus convergence zones.

### 4.3 Geopolitical Divergence Across Model Families

The systematic comparison across model families reveals patterns of divergence that are consistent, thematically coherent, and traceable to the geopolitical context of model development. These patterns constitute the most methodologically novel finding of the study and are directly interpretable through the Multi-Level Perspective (MLP) on sociotechnical transitions (Geels, 2002, 2020a). The MLP framework predicts that identical technological innovations produce different transition pathways depending on the regime-level institutional configuration — the existing regulatory structures, industry architectures, cultural norms, and political coalitions that mediate how niche innovations are absorbed, resisted, or redirected. The three model families in this study encode three distinct regime configurations, and their divergent predictions map onto three of Geels's (2002) canonical transition typologies: *substitution* (US models), *transformation* (Chinese models), and *reconfiguration* (European model). Figure 3 visualizes the three-way divergence structure.

![Figure 4: Three Worldviews of AI Transformation — Geopolitical Divergence Across Model Families. US-origin models (Claude Opus 4.6, GPT-5.4, Gemini 3.1 Pro, Grok 4.2) emphasize market-driven disruption and platform concentration. Chinese-origin models (DeepSeek R2, Qwen 4.5 Max) emphasize state-steered transformation and infrastructure sovereignty. The European model (Mistral Large 3) emphasizes regulatory primacy and social equity. The center shows convergence zones shared across all three families.](figures/fig4_geopolitical.png)

#### 4.3.1 US Models: Market-Driven Disruption and Platform Concentration (MLP: Substitution Pathway)

The four US-origin models (Claude, GPT-5.4, Gemini, Grok) share a common analytical frame characterized by market-led disruption, venture capital dynamics, startup-versus-incumbent narratives, and platform concentration — a pattern that maps directly onto the MLP *substitution* transition pathway, in which niche innovations (AI-native firms) displace incumbent regime actors through competitive dynamics rather than through regime-level negotiation or state intervention. Named actors are predominantly US companies: NVIDIA, OpenAI, Google, Amazon, Microsoft, Goldman Sachs, JPMorgan, Meta, Netflix, McKinsey. Regulatory actors are mentioned primarily as constraints on innovation (the EU AI Act slowing European competitiveness) or reactive responders (the SEC, FDA, FTC catching up to market developments).

The US models are the most likely to predict winner-take-all outcomes, platform monopolies, and the displacement of legacy institutions by AI-native startups. They are also the most likely to frame the MAX scenario in terms of existential or transformative implications (superintelligence, species divergence, post-labor economies).

Within the US family, meaningful variation exists. Claude produces the longest, most nuanced output with explicit confidence ratings and falsification conditions. GPT-5.4 uniquely opens with a "fact base versus inference" disclaimer, anchoring its analysis in verifiable 2025-2026 data points before building inferences. Gemini produces the most provocative MAX scenarios (Butlerian Jihad, Sentient Legal Loophole). Grok produces the shortest output but with the highest concentration of specific, bold claims per word, often using deliberately confrontational framing ("We will not pay humans to think; we will pay humans to take the blame").

#### 4.3.2 Chinese Models: State-Steered Transformation and Infrastructure Sovereignty (MLP: Transformation Pathway)

The two Chinese-origin models (DeepSeek, Qwen) share analytical emphases that diverge systematically from the US family, corresponding to the MLP *transformation* pathway in which regime actors (state institutions, large state-adjacent enterprises) actively steer and incorporate niche innovations into existing institutional structures rather than being displaced by them. Both models foreground state direction of AI development, industrial policy, and infrastructure sovereignty. Named actors include not only Chinese companies (Alibaba, Baidu, Huawei) but also state institutions (PBOC for CBDCs, national AI strategies, state-funded compute infrastructure).

DeepSeek is notably the most detailed and methodologically rigorous of all seven models, producing step-by-step causal chains with explicit conclusion statements for every cell. Its output reads like a structured analytical report rather than a speculative scenario exercise. DeepSeek is also distinctive in its emphasis on financial system transformation -- it provides the most detailed analysis of insurance, lending, and monetary policy across all four stages.

Qwen is more concise but shares DeepSeek's emphasis on infrastructure sovereignty, data sovereignty, and the "Splinternet" as a structural outcome. Both Chinese models are less likely than US models to predict dystopian MAX scenarios involving loss of human control, species divergence, or existential risk. They are more likely to predict managed transitions, state-directed retraining programs, and sovereign compute capacity as a natural policy response.

#### 4.3.3 The European Model: Regulatory Primacy and Social Equity (MLP: Reconfiguration Pathway)

Mistral, the sole European-origin model, produces output corresponding to the MLP *reconfiguration* pathway — in which regulatory frameworks actively mediate the integration of niche innovations into existing regime structures, producing a hybrid outcome that preserves institutional continuity while selectively incorporating technological change. Its output is distinctive in three ways. First, it foregrounds regulatory frameworks as the primary shaper of transformation outcomes -- not as a constraint on innovation but as a structural force that determines which pathways are traversed. Second, it emphasizes social equity outcomes more consistently than any other model: workforce transitions, distributional effects, and the social contract appear as primary concerns rather than secondary considerations. Third, it produces the most generic output of the seven models: fewer named companies, fewer quantified predictions, and less specific causal chain reasoning. This may reflect its training data composition, its shorter context window, or the European academic tradition of prioritizing frameworks over granular prediction.

The three-way divergence (US: market-driven disruption; CN: state-steered transformation; EU: regulatory-guided equity) is the methodological finding that most directly validates the Multi-LLM Delphi approach. These perspectives are not random variation; they are coherent, internally consistent, and traceable to the geopolitical and institutional contexts in which the models were developed. A human Delphi panel would need to deliberately recruit experts from different geopolitical backgrounds to achieve comparable perspective diversity; the Multi-LLM Delphi achieves it structurally through model selection.

Several important caveats limit the generalizability of these geopolitical divergence patterns. The Chinese model family comprises only two models (DeepSeek and Qwen), and the European family consists of a single model (Mistral). With n=2 and n=1 respectively, the observed patterns are suggestive rather than definitive -- the divergence between DeepSeek and Qwen could reflect company-specific design choices rather than a coherent "Chinese AI perspective," and Mistral's output may reflect Mistral-specific training decisions rather than "European values" more broadly. Furthermore, RLHF alignment procedures and safety filtering represent an unresolved confound: Chinese models may avoid certain geopolitical claims not because they encode a different knowledge base but because they are alignment-trained to avoid politically sensitive topics, and US models may emphasize market dynamics because their training data is dominated by English-language business and economics texts. These patterns should be treated as hypotheses for future investigation with larger model samples rather than as established findings.

### 4.4 Methodological Properties of the Multi-LLM Delphi

Several observations about the method's properties emerge from the analysis:

**Output length variation.** The 14:1 ratio between the longest (Claude, 30,613 words) and shortest (Grok, 2,169 words) response under identical prompts reveals that models differ dramatically in verbosity, detail level, and willingness to generate comprehensive structured output. Claude and DeepSeek produced the most analytically usable responses; Grok and Mistral produced responses that were thin on detail but occasionally contained the most provocative or distinctive claims.

**Specificity gradient.** Models vary systematically in the specificity of their predictions. DeepSeek consistently provides the most specific causal chains with named actors and quantified outcomes. GPT-5.4 anchors in verifiable data before building inferences. Gemini provides specific predictions in Technology and Media verticals but thins in Healthcare and Real Estate. Mistral produces the most generic output across all verticals. Grok provides specific predictions when it engages with a vertical but leaves many cells incomplete.

**Prompt adherence.** All seven models followed the three-scenario structure (MILD, BASE, MAX), the four-stage framework, and the eight-vertical structure. However, only four (Claude, DeepSeek, GPT-5.4, Gemini) produced complete output for all eight verticals. Grok completed only Technology and Financials in full detail before truncating. Qwen and Mistral produced all eight verticals but at reduced depth for later verticals -- a "fatigue" pattern where early verticals receive more detailed treatment.

**Cross-cutting analysis quality.** The cross-cutting sections (convergence points, wildcards, human dimension) varied dramatically. Claude produced five distinct, well-defended convergence points and five elaborated wildcards. Gemini produced the most provocative wildcards (the Butlerian Jihad, the Sentient Legal Loophole, the Amish Hedge). Mistral produced generic convergence points without specific causal reasoning. Grok did not complete the cross-cutting sections.

**The irreducibly human skill question.** All seven models were asked to identify the one skill that remains irreducibly human. Their answers converge strikingly: Claude identifies "legitimated judgment under contested values," GPT-5.4 identifies "legitimated judgment under contested values" (using nearly identical language), Gemini identifies "philosophical accountability -- the capacity to bear moral and legal responsibility," DeepSeek identifies a cluster of "empathy, accountability, and meaning-making," Qwen identifies "contextual meaning-making" grounded in authentic intent, and Mistral identifies "emotional intelligence." The convergence of six of seven models on some form of *accountability and judgment under contested values* -- rather than creativity, empathy, or intelligence in the abstract -- represents a consensus finding of the Multi-LLM Delphi.


### 4.5 Round 2 -- Consensus Dynamics Under Controlled Feedback

The Round 2 protocol constitutes, to the author's knowledge, the first implementation of iterative controlled feedback within a multi-LLM Delphi design. Each of the seven frontier models received an anonymized summary of the Round 1 consensus findings and was prompted to revise, contest, adopt, or extend the collective output. The resulting corpus enables systematic analysis of how LLM panelists respond to structured peer feedback -- a question with implications for both the validity of the Multi-LLM Delphi method and the broader understanding of LLM behavior under social-epistemic pressure. This section reports consensus dynamics across four dimensions: stability and shift of existing themes (4.5.1), adoption of blind-spot predictions (4.5.2), emergence of new predictions (4.5.3), and persistence of geopolitical divergence (4.5.4).

#### 4.5.1 Consensus Stability and Shift

The Round 2 feedback produced a striking pattern of asymmetric consensus dynamics: high-consensus themes from Round 1 were universally maintained or strengthened, moderate-consensus themes were upgraded toward high consensus, and contested themes showed convergence in directionality while preserving substantive disagreement on specifics. No high-consensus theme was destabilized by the feedback process, and no model defected from any of the six original convergence zones.

The six high-consensus convergence zones from Round 1 -- labor market bifurcation (7/7), infrastructure bottleneck repricing (6/7), regulatory divergence (6/7), disintermediation (5/7), trust premium (5/7), and concentration via AI feedback loops (5/7) -- were unanimously reaffirmed in Round 2. Several models went further, elevating themes they had previously treated as background conditions to primary causal drivers. GPT-5.4 explicitly upgraded regulatory divergence "from a second-order governance variable to a first-order market-structuring variable." Claude acknowledged having "underweighted" infrastructure bottleneck repricing and revised its framework to treat physical infrastructure as "the gating factor across all verticals rather than a primarily Technology & Semiconductors concern." Mistral, which had produced the most generic Round 1 output, used the feedback to add specificity across all six convergence zones, explicitly adopting the barbell labor market framing and the disintermediation mechanism that it had not articulated independently.

The most significant consensus shifts occurred among themes that had achieved only moderate consensus in Round 1. Autonomous economic agents, endorsed by four of seven models in Round 1, achieved near-universal endorsement in Round 2. All seven models expressed some form of agreement, though the nature of agreement varied instructively. Grok "strongly agreed" and formalized autonomous agents as "a core driver of Stage 4 systemic transformation across all eight verticals." Qwen upgraded its assessment from a MAX-case Stage 3 phenomenon to a BASE-case Stage 2 phenomenon. GPT-5.4 offered the most qualified endorsement, agreeing that "the economy gets agentic islands, not immediate full agentic oceans" and distinguishing between narrow-domain autonomy (high confidence) and full-enterprise autonomy (low confidence). This pattern -- directional convergence with preserved granularity of disagreement -- mirrors the convergence-with-residual-dissensus pattern documented in classical Delphi studies (von der Gracht, 2012).

The "compute as currency" theme, also at moderate consensus in Round 1 (4/7), shifted in a revealing manner. Rather than simple adoption or rejection, the Round 2 responses converged on a refined formulation. GPT-5.4 proposed replacing "compute as currency" with "compute as strategic reserve," arguing that "compute behaves more like energy capacity, spectrum, shipping access, or reserve industrial capability than like money in the classic sense." Claude arrived independently at the same reformulation, describing compute as "a strategic resource comparable to oil -- allocated, hoarded, and weaponized -- but not a literal medium of exchange." Qwen upgraded compute to BASE-case status and predicted "GPU-hours as collateral" in lending markets. Gemini "aggressively doubled down," predicting that "autonomous AI agents will not settle in volatile, slow human fiat -- they will clear markets directly in FLOPs, API access, and kilowatt-hours." The net effect was an increase in support from four to approximately six or seven of seven models, but with a meaningful refinement: the consensus converged not on the original "currency" framing but on a more nuanced "strategic resource and reserve asset" formulation. This spontaneous collective refinement of a contested concept represents a form of emergent conceptual precision that has no direct parallel in classical Delphi studies, where human panelists refine language through the researcher's mediation rather than through independent convergence on improved terminology.

Biological-digital convergence, the weakest of the moderate-consensus themes at three of seven in Round 1, showed the least movement. While all models acknowledged the theme, substantive support remained concentrated in the healthcare vertical. GPT-5.4 described it as "a high-conviction vertical thesis, not yet a top-level economy-wide thesis." Gemini downgraded its timeline, citing the "wetware bottleneck" of immune rejection, ethics boards, and neuroplasticity constraints. Qwen and DeepSeek maintained their MAX-case positioning without upgrading. Only Grok moved in the opposite direction, upgrading biological-digital convergence from a "low-probability wildcard to plausible Base-case convergence point." The theme thus remained at approximately three to four of seven as an economy-wide prediction, though it strengthened within the healthcare vertical specifically. This resistance to convergence under feedback pressure is analytically informative: it suggests that biological-digital convergence represents genuine uncertainty rather than an information deficit that feedback can resolve.

**Table 2: Round 1 to Round 2 Consensus Shift Matrix**

| Theme | R1 Score | R1 Category | R2 Score | R2 Category | Shift Direction |
|-------|----------|-------------|----------|-------------|-----------------|
| Labor Market Bifurcation | 7/7 | HC | 7/7 | HC | Maintained (strengthened) |
| Infrastructure Bottleneck Repricing | 6/7 | HC | 7/7 | HC | Strengthened |
| Regulatory Divergence | 6/7 | HC | 7/7 | HC | Strengthened |
| Disintermediation | 5/7 | HC | 7/7 | HC | Strengthened |
| Trust/Authenticity Premium | 5/7 | HC | 7/7 | HC | Strengthened |
| Concentration via AI Feedback Loops | 5/7 | HC | 7/7 | HC | Strengthened |
| Autonomous Economic Agents | 4/7 | MC | 7/7 | HC | Upgraded |
| Compute as Currency/Strategic Reserve | 4/7 | MC | 6-7/7 | HC | Upgraded (refined) |
| Biological-Digital Convergence | 3/7 | MC | 3-4/7 | MC | Stable (healthcare-specific gain) |
| Apprenticeship Crash | 1/7 | BS | 7/7 | HC | Adopted unanimously |
| AI Religion / Spiritual Response | 1/7 | BS | 5-6/7 | HC/MC | Substantially adopted |

HC = High Consensus (5+ of 7); MC = Moderate Consensus (3-4 of 7); BS = Blind Spot (1-2 of 7)

The overall pattern is one of strong convergence pressure: of eleven tracked themes, eight increased in consensus, two remained stable, and none decreased. This convergence pattern is consistent with the classical Delphi finding that controlled feedback generally increases agreement (Gordon and Pease, 2006), but it also raises the question of whether LLMs are more susceptible to consensus pressure than human panelists -- a methodological concern addressed in Section 4.5.5 and Section 6.

![Figure 7: Consensus Dynamics Round 1 to Round 2 — Alluvial Flow of Theme Consensus Levels. The flow diagram shows the dramatic upward shift in consensus between rounds: all six high-consensus themes were maintained or strengthened to 7/7; both moderate-consensus themes (autonomous agents, compute as currency) were upgraded to high consensus; and both blind spots (apprenticeship crash, AI religion) were adopted by the majority of models. Only biological-digital convergence resisted convergence pressure. The most dramatic shift — the apprenticeship crash moving from 1/7 to 7/7 — is highlighted. Caveat: strong convergence may partly reflect LLM acquiescence bias (see Section 4.5.5).](figures/fig7_alluvial.png)

#### 4.5.2 Blind Spot Adoption -- The Apprenticeship Crash

The most dramatic consensus shift between rounds occurred with the "apprenticeship crash" prediction. In Round 1, this prediction -- that the elimination of junior knowledge-work roles would sever the experiential pipeline through which senior professionals are produced, creating a succession crisis within a decade -- appeared in only one model's output (Claude). By Round 2, all seven models had adopted it, with several elevating it to a top-tier systemic risk. This unanimous adoption of a previously singular prediction constitutes the strongest evidence of blind-spot correction through feedback in the dataset.

The adoption was not superficial. Each model independently reconstructed the causal mechanism and extended it into its own analytical framework. GPT-5.4 described it as "one of the most mechanism-rich and underpriced second-order effects in the whole landscape," identifying the core logic: "AI removes junior routine work. Junior routine work was the hidden training substrate for future senior talent. Firms optimize short-term productivity and underinvest in deliberate apprenticeship. A delayed shortage emerges in experienced professionals with judgment, client fluency, and institutional legitimacy." GPT-5.4 further diagnosed why the prediction had been missed in Round 1: "most analysts model jobs statically, not careers dynamically. They count task replacement but ignore skill formation pipelines." DeepSeek constructed a parallel causal chain, tracing the apprenticeship crash from law firms and consultancies through a five-to-seven-year pipeline thinning to a leadership vacuum that forces firms to choose between accelerating promotion of inexperienced professionals, acquiring talent in zero-sum competition, or accepting that AI will fill senior roles. Grok, despite its characteristically terse style, integrated the prediction across five verticals and predicted a compensatory response: "synthetic-mentorship platforms to compensate" for the severed human training pipeline.

The depth of adoption varied in instructive ways. Gemini produced the most emphatic response, claiming authorship of the original blind spot and elevating it "from a 2nd-order effect to the defining structural crisis of the knowledge economy." Claude, as the originating model, acknowledged it had been "too scattered" in its Round 1 treatment and restructured the prediction as a unified cross-cutting risk, constructing a detailed ten-step causal chain culminating in a "judgment famine" that emerges precisely when AI systems become powerful enough to require sophisticated human governance. Qwen integrated the prediction into its professional services and technology verticals, articulating a cyclical dynamic: "automation solves today's cost problem but creates tomorrow's skills shortage." Mistral, while adopting the prediction, treated it as a "wildcard scenario" rather than a central risk -- the weakest form of adoption but still a meaningful shift from complete absence.

![Figure 9: The Apprenticeship Crash — Causal Cascade from Task Automation to Judgment Famine. The 10-step causal chain shows how AI automation of routine knowledge work (top, blue) leads through a hidden dependency — the severing of experiential training pipelines — to a judgment famine (bottom, red) in which AI systems are powerful enough to require sophisticated human governance, but the humans with governance expertise are no longer being produced. The color gradient from blue through amber to red represents the transition from short-term productivity gains to long-term systemic crisis. Institutional responses (right, green) show the predicted compensatory mechanisms. Consensus shifted from 1/7 (Round 1) to 7/7 (Round 2).](figures/fig9_apprenticeship_crash.png)

The apprenticeship crash adoption is analytically significant for three reasons. First, it demonstrates that the controlled feedback mechanism of the Multi-LLM Delphi can surface predictions that are latent in models' knowledge bases but not spontaneously generated. The causal logic of the apprenticeship crash -- that task-level automation destroys the experiential pipeline for producing future senior talent -- is well within the inferential capacity of all seven models; it was not generated in Round 1 because the prompt structure oriented models toward current-state predictions rather than dynamic pipeline effects. Once the prediction was surfaced through feedback, every model recognized its validity and could reconstruct it independently. Second, the unanimity of adoption suggests that the apprenticeship crash represents a genuine epistemic convergence point rather than a persuasion artifact: models adopted it because the causal logic is compelling, not because they were primed to agree. Third, the prediction illustrates the methodological value of multi-round designs: a single-round Multi-LLM Delphi would have classified the apprenticeship crash as an idiosyncratic blind spot; the two-round design reveals it as a latent consensus finding of the highest order.

The "AI religion / spiritual response" blind spot showed a different adoption pattern. In Round 1, only Claude predicted organized spiritual movements emerging in response to AI. In Round 2, the prediction was acknowledged by all seven models but with substantially varying levels of endorsement. Claude maintained its position forcefully, arguing that "every technology that challenges the human sense of cosmic significance produces a spiritual response -- not as a curiosity but as a major social force." Gemini elevated it as a cultural prediction, linking it to the trust premium and identity-crisis themes. Grok adopted it "as a MAX-case 3rd-order cultural wildcard." DeepSeek constructed a causal chain from AI's apparent "supernatural" capabilities (omniscience, omnipresence) through organized movements to political and social consequences. GPT-5.4 offered the most qualified adoption, accepting it as "a cultural-political side effect, not a primary economic scenario driver." Qwen adopted it as a "3rd order cultural effect" and Mistral mentioned it as a "potential wildcard scenario." The net effect was an increase from one of seven to approximately five to six of seven models substantively engaging with the prediction, though with less unanimity and less depth than the apprenticeship crash. This differential adoption rate -- unanimous for the apprenticeship crash, partial for AI religion -- is itself informative: it suggests that LLM panelists distinguish between predictions that are causally compelling within economic frameworks and predictions that require engagement with non-economic domains (theology, psychology, sociology of religion) where LLM training data may be less systematically structured.

#### 4.5.3 New Emergent Predictions

The Round 2 protocol generated a substantial corpus of new predictions that had not appeared in any model's Round 1 output. These emergent predictions fall into three categories: synthesis predictions that combine two or more Round 1 themes into novel compound forecasts; extension predictions that project existing themes into new domains; and meta-predictions about the dynamics of the transformation process itself.

![Figure 10: Round 2 Synthesis — How Feedback Generated Novel Compound Predictions. The network diagram shows how Round 1 themes (left, blue) combined through the feedback process to generate six emergent Round 2 predictions (right, amber) that appeared without any precedent in the Round 1 summary. Arrow thickness reflects the consensus level of each input theme. The synthesis process demonstrates the generative power of the Multi-LLM Delphi: predictions that no individual model would have produced alone emerged from the structured interaction between independently generated analyses.](figures/fig10_synthesis.png)

The most widely generated synthesis prediction was the concept of **regulatory arbitrage hubs** or "compute havens." Gemini predicted "Jurisdictional Compute Havens -- the New Caymans," describing agile nation-states (UAE, El Salvador, Singapore) building deregulated nuclear and solar compute clusters with legal personhood for DAOs and zero copyright liability. Grok independently predicted "Regulatory Arbitrage Hubs (Singapore, Dubai, Texas)" accelerating concentration dynamics. Claude described a "Regulatory Arbitrage Spiral" in which the three-bloc divergence creates a permanent arbitrage dynamic that becomes a primary driver of economic outcomes, generating an entirely new industry of regulatory navigation firms and jurisdiction-shopping consultancies. The convergence of three models on this prediction in Round 2 -- despite its complete absence in Round 1 -- suggests that it represents a genuine emergent insight that requires the interaction of multiple Round 1 findings (regulatory divergence, compute as strategic resource, autonomous agents) to crystallize.

A second cluster of emergent predictions centered on the **agent-to-agent economy** as a distinct economic layer. Grok predicted that "by Stage 4, autonomous agents conduct trillions in daily B2B transactions with minimal human intervention, creating new antitrust challenges around agent cartels." Gemini described a "B2Bot Macroeconomic Blackout" in which agent-to-agent commerce eclipses human economic activity in transaction volume, rendering traditional macroeconomic indicators (GDP, CPI, velocity of money) unable to measure the actual economy. GPT-5.4 predicted that "agentic markets will emerge before fully agentic firms," distinguishing between narrow-domain agent autonomy (high confidence) and full enterprise autonomy (lower confidence). DeepSeek predicted that the "$20T+ global commerce ecosystem shifts toward autonomous intermediation." This convergence suggests that the interaction between the autonomous agents theme and the disintermediation theme generates a compound prediction -- a self-transacting economic layer -- that no single model articulated in Round 1.

Several models generated predictions about the **institutional response to the apprenticeship crash**. Grok predicted "Synthetic Mentorship Platforms" becoming a new industry exceeding $200 billion by late Stage 2, in which retiring experts' tacit knowledge is digitized into agent trainers. Grok also predicted "AI Apprenticeship Mandates" appearing in regulation, requiring firms above certain revenue thresholds to maintain minimum human-AI hybrid training ratios. Qwen predicted that corporations would begin acquiring universities and training centers to secure talent pipelines, transforming education into "a corporate procurement function, not a public good." GPT-5.4 predicted that "firms that deliberately preserve or redesign talent formation will outperform those that simply strip junior layers," framing apprenticeship systems as a hidden source of competitive advantage. These institutional-response predictions demonstrate a distinctive property of the two-round design: Round 1 identifies the problem; Round 2 generates the solution space.

Claude contributed the most structurally novel meta-prediction: the **oscillation pattern**. Observing that all seven models' Round 1 predictions assumed roughly linear transformation trajectories, Claude predicted that the actual transition would proceed "not linearly but through oscillation: rapid AI advancement, visible displacement, political backlash, regulatory restriction, competitive pressure from less-restricted jurisdictions, relaxation, another wave of advancement." Claude noted that this oscillation pattern is the historical norm for transformative technologies (nuclear power, genetic engineering, financial derivatives) and argued that the scenario framework, while analytically useful, "understates the volatility of the actual transition." This meta-prediction -- a prediction about the dynamics of the prediction space itself -- represents a form of analytical reflexivity that emerged specifically from the multi-model synthesis process.

DeepSeek generated a distinctive new prediction about the **AI literacy class divide**, combining the labor bifurcation consensus with the apprenticeship crash to predict a permanent stratification between "AI-native" professionals who never performed foundational tasks manually and "AI-augmented" professionals who learned fundamentals before AI deployment. DeepSeek predicted that clients would pay premiums for "old school" trained professionals, creating an "analog seniority" premium that compounds the apprenticeship crash dynamics. Gemini independently arrived at a similar prediction, framing the last generation of professionals trained before generative AI as "the most valuable labor cohort in economic history" who command "astronomical wage premiums" for their "analog intuition."

#### 4.5.4 Persistence of Geopolitical Divergence

The Round 1 analysis identified a three-way geopolitical divergence pattern: US-origin models emphasizing market-driven disruption and platform concentration, Chinese-origin models foregrounding state-steered transformation and infrastructure sovereignty, and the European model privileging regulatory frameworks and social equity. A critical question for the Round 2 analysis is whether this divergence persists, intensifies, or dissolves under feedback pressure. The evidence points unambiguously toward persistence and, in several dimensions, intensification.

Rather than converging toward a shared geopolitical framing, the models used the feedback to sharpen their distinctive positions. Gemini -- a US-origin model -- produced the most vivid articulation of geopolitical fragmentation, describing three "non-interoperable macroeconomic biomes": the "US Biome (Capital Velocity)" that accepts massive labor displacement for global market dominance, the "EU Biome (The Human Preserve)" that intentionally stalls at early adoption stages to maintain social stability, and the "CN Biome (Techno-Mercantilism)" that bifurcates internally between accelerated deployment in physical verticals and heavy restriction of agentic AI in media and knowledge work. GPT-5.4 independently arrived at a similar tripartite framework, predicting that multinationals would need "tri-stack strategies: market-speed stack, sovereignty stack, compliance-equity stack." Claude described the three-bloc divergence as creating a "permanent arbitrage dynamic" rather than converging toward a single regulatory equilibrium.

Crucially, the Chinese-origin models did not converge toward the US framing despite receiving feedback that documented the geopolitical split. Qwen explicitly acknowledged its "US bias" in the original analysis but responded by adding a "Geographic Variance Modifier" to all vertical outcomes -- effectively institutionalizing geopolitical divergence within its own framework rather than dissolving it. DeepSeek maintained its position that regulatory divergence "will persist and deepen," constructing a causal chain from bloc-specific ecosystem optimization through prohibitive cross-regime compliance costs to entrenched "AI sovereignty." Both Chinese models continued to emphasize state-directed transformation pathways and infrastructure sovereignty, though they showed increased willingness to engage with market-driven dynamics as a parallel phenomenon rather than an alternative one.

Mistral, the sole European model, used the Round 2 feedback to strengthen rather than moderate its distinctive emphasis. It maintained its focus on regulatory frameworks, social equity, and workforce protection, while adopting specific predictions (the apprenticeship crash, compute as currency, autonomous agents) within that regulatory-equity frame. GPT-5.4 offered the intriguing observation that "Europe's relative weakness in speed could become a strength in trust-intensive sectors" -- a prediction that reframes the European regulatory approach not as a drag on innovation but as a competitive advantage in sectors where auditability, liability, and procedural legitimacy are commercially rewarded.

The persistence of geopolitical divergence under controlled feedback is the Round 2 finding with the most direct methodological implications. In classical Delphi studies, persistent divergence after feedback is interpreted as evidence of genuine disagreement rather than information asymmetry (von der Gracht, 2012). Applied to the Multi-LLM Delphi, this interpretation suggests that the geopolitical differentiation of model outputs reflects structural features of training data composition and alignment procedures that are robust to informational feedback. The models do not disagree because they lack information about alternative perspectives; they disagree because they encode different institutional logics. This finding strengthens the case for treating geopolitical model diversity as an analytical resource rather than a methodological limitation: the three-way divergence is not noise to be averaged away but signal about genuinely different transformation pathways that may unfold simultaneously across the world's major economic blocs.


#### 4.5.5 Acquiescence Bias and the Authenticity of Convergence

The strong convergence pattern documented in the preceding subsections -- nine of eleven themes increasing in consensus, including two blind spots reaching near-unanimity -- invites a critical methodological question: does Round 2 convergence reflect genuine epistemic updating, or does it reflect the well-documented tendency of large language models toward acquiescence and sycophancy (Perez et al., 2023; Sharma et al., 2024)? LLMs are trained through reinforcement learning from human feedback (RLHF) to produce outputs that users find helpful and agreeable. When presented with a consensus summary as input, models may be predisposed to confirm rather than challenge the presented positions -- not because the positions are correct, but because agreement is the path of least resistance in their optimization landscape. This concern is particularly acute for the apprenticeship crash, which moved from 1/7 to 7/7 -- a trajectory that could reflect either genuine blind-spot correction or wholesale conformity to a presented majority position.

Several features of the Round 2 data allow a partial -- though not definitive -- adjudication between genuine convergence and acquiescence artifacts.

First, **convergence was non-uniform across themes.** If acquiescence bias were the dominant mechanism, one would expect approximately equal convergence pressure across all themes presented in the feedback summary. Instead, the data show sharply differentiated responses: biological-digital convergence remained stable at 3-4/7 despite being presented with the same feedback structure as themes that reached unanimity. AI religion moved to 5-6/7 but not 7/7, with GPT-5.4 explicitly qualifying it as "a cultural-political side effect, not a primary economic scenario driver." This differential uptake is inconsistent with a blanket acquiescence mechanism and suggests that models evaluated the causal logic of individual predictions rather than rubber-stamping the consensus summary.

Second, **models refined rather than merely adopted.** The "compute as currency" theme provides the clearest illustration: rather than endorsing the Round 1 framing, multiple models independently converged on an improved formulation -- "compute as strategic reserve" -- that corrected what they identified as an imprecise metaphor. GPT-5.4 argued that "compute behaves more like energy capacity or reserve industrial capability than like money." Claude independently arrived at the same reformulation. This spontaneous collective refinement is difficult to explain through acquiescence alone; a sycophantic response would accept the presented framing, not systematically improve it.

Third, **models generated genuinely novel predictions not contained in the feedback.** Section 4.5.3 documented multiple emergent predictions -- regulatory arbitrage hubs, the agent-to-agent economy, synthetic mentorship platforms, the oscillation meta-prediction -- that appeared in Round 2 without any precedent in the Round 1 summary. Pure acquiescence would produce agreement with presented positions; it would not generate substantively new content that extends beyond the feedback input. The volume and specificity of emergent predictions suggests that models engaged in genuine analytical reasoning with the feedback rather than merely confirming it.

Fourth, and most critically, **geopolitical divergence persisted and intensified.** Section 4.5.4 documented that Chinese-origin models maintained and sharpened their state-steered transformation framing, US-origin models deepened their market-driven disruption emphasis, and the European model strengthened its regulatory-equity frame. A pure acquiescence mechanism would predict convergence toward the majority framing (which, given the 4:2:1 US/CN/EU panel composition, would be the US market-driven perspective). Instead, geopolitical divergence proved robust to feedback pressure, with Qwen explicitly acknowledging its "US bias" from Round 1 and compensating by adding geographic variance modifiers. This pattern -- convergence on factual/causal predictions combined with persistent divergence on interpretive frames -- is precisely what one would expect from genuine analytical engagement rather than blanket agreement.

Fifth, **individual models maintained distinctive dissenting positions.** Claude continued to argue for AI religion as a "major social force" rather than a curiosity. GPT-5.4 maintained several qualified positions, accepting predictions in principle while downgrading their centrality. Gemini claimed authorship of the apprenticeship crash prediction and used the Round 2 response to assert analytical priority rather than simply agreeing. These instances of maintained individuality and even competitive positioning are inconsistent with pure conformity dynamics.

Despite these mitigating observations, the acquiescence concern cannot be fully dismissed. The asymmetry of the feedback design -- presenting Round 1 consensus without explicit counterarguments or devil's advocate positions -- creates a structural bias toward convergence. Human Delphi panelists also converge under feedback, but they bring embodied expertise, professional stakes, and identity-based commitments that create resistance to conformity pressure. LLMs lack these anchoring mechanisms, and their RLHF training actively rewards agreeableness. The strong convergence observed in Round 2 should therefore be interpreted as an upper bound on genuine consensus rather than a precise measure of it.

Future implementations of the Multi-LLM Delphi should incorporate explicit acquiescence countermeasures: (a) **devil's advocate prompting**, in which the feedback explicitly instructs models to identify weaknesses in the consensus positions and argue against them; (b) **counter-consensus framing**, in which minority positions are presented with equal or greater prominence than majority positions; (c) **adversarial rounds**, in which models are assigned the role of critiquing rather than evaluating the consensus; and (d) **calibration benchmarks**, in which models are tested on questions with known answers under social pressure to establish baseline acquiescence rates. Until such controls are implemented, the Round 2 convergence findings should be read as suggestive evidence of latent consensus rather than definitive proof of agreement.

## 5. Discussion

### 5.1 Theoretical Implications

#### 5.1.1 Extending GPT Theory: The Three-Order Cascade

The findings provide empirical support for the GPT framework's prediction that the most significant effects of a general-purpose technology lie not in its direct applications but in the cascading structural changes it enables. The high-consensus convergence zones map precisely onto the GPT prediction: first-order effects (task-level productivity gains from AI copilots) are widely agreed upon and relatively uncontroversial; second-order effects (labor market bifurcation, disintermediation of middleman business models, organizational flattening) show high consensus but with more variation in timing and severity; third-order effects (compute as geopolitical currency, regulatory divergence as structural force, concentration of economic power) show the greatest divergence, consistent with the GPT framework's prediction that higher-order effects are harder to anticipate.

The Multi-LLM Delphi data provide empirical illustration of a prediction already implicit in GPT theory — that the J-curve of adoption varies across sectors depending on the "distance" between the GPT and existing sector-specific technologies (Bresnahan and Trajtenberg, 1995). While GPT theory predicts this variation in principle, the Multi-LLM Delphi data operationalize it by revealing the specific institutional mechanisms that determine J-curve shape in each sector. Healthcare, with its heavy regulatory burden and liability constraints, exhibits a longer, flatter J-curve than Technology or Media, where adoption barriers are lower. This sector-dependent J-curve is visible in the model outputs, where consensus on Healthcare transformation is lower and staging is more cautious than for Technology or Professional Services.

#### 5.1.2 MLP and the Geopolitical Differentiation of Transition Pathways

The geopolitical divergence findings directly support the MLP's prediction that sociotechnical transitions are path-dependent and shaped by the agency of incumbents, regulators, and social movements. The three geopolitical model families project systematically different transition pathways -- market-driven disruption (US), state-steered transformation (CN), and regulatory-guided equity (EU) -- corresponding to different MLP transition typologies. The US models describe a substitution pathway where AI-native niches displace incumbent regimes through competitive dynamics. The Chinese models describe a transformation pathway where regime actors (state institutions, large enterprises) steer and incorporate AI innovations. The European model describes a reconfiguration pathway where regulatory frameworks mediate the integration of AI innovations into existing regimes.

This three-pathway finding has significant implications for the MLP literature. Previous MLP studies have focused primarily on sustainability transitions within a single national or regional context (Geels, 2020a; Roberts and Geels, 2019). The Multi-LLM Delphi data suggest that the AI transition represents a particularly visible case of simultaneously divergent GPT diffusion pathways across the world's major economic blocs. While previous GPT diffusions -- electricity, railroads, the internet -- also followed geopolitically differentiated trajectories, the AI transition may be distinctive in the *degree* of intentional policy divergence and the *speed* at which divergence crystallizes, creating a natural experiment in sociotechnical transition governance.

### 5.2 Methodological Implications

#### 5.2.1 Validity of LLMs as Delphi Panelists

The Multi-LLM Delphi demonstrates several properties that support its validity as a foresight instrument. First, the high-consensus convergence zones align with predictions that have independent empirical support: labor market bifurcation is consistent with Acemoglu and Restrepo's (2019) task-based framework; infrastructure bottleneck repricing is consistent with IEA projections; disintermediation of intermediaries is consistent with platform economics theory (Goldfarb and Tucker, 2019). The method does not appear to generate consensus around implausible predictions.

Second, the geopolitical divergence patterns are coherent, internally consistent, and independently verifiable. The observation that Chinese models emphasize state-steered transformation while US models emphasize market-driven disruption is not an artifact of the method; it reflects genuine differences in the knowledge bases and alignment approaches of models trained in different institutional contexts.

Third, the method produces structured disagreement that is analytically informative. The contested futures (pace of healthcare transformation, compute as currency) and blind spots (AI religion, model collapse) generate research questions that would not emerge from a single-model analysis or a consensus-seeking human panel.

#### 5.2.2 Limitations and Biases of LLM Panelists

The method also exhibits important limitations. LLMs are not experts; they are statistical models of text corpora. Their predictions reflect the distribution of claims in their training data, weighted by their alignment procedures. This means: (a) LLMs over-represent perspectives that are well-documented in English-language academic and business literature; (b) LLMs may reproduce optimistic bias from sources that tend to overstate the pace and impact of technology adoption; (c) LLMs' safety training (RLHF, Constitutional AI) may suppress extreme predictions in some models while allowing them in others, creating artificial divergence; (d) LLMs cannot incorporate genuinely novel information that postdates their training cutoff.

The output length variation (14:1 ratio) is a significant methodological concern. A Delphi panel in which one panelist writes 30,000 words and another writes 2,000 words introduces weighting effects that are difficult to control analytically. Future designs should either impose output length constraints or develop weighting schemes that normalize for verbosity.

### 5.3 Engagement with Existing Empirical Findings

The Multi-LLM Delphi findings can be productively compared with existing empirical estimates of AI's economic impact. Acemoglu (2024b) modeled AI's macroeconomic effects using a task-based framework and concluded that first-order productivity gains alone are unlikely to generate transformative GDP growth -- his central estimate is a modest 0.53% increase in total factor productivity over ten years. The present study's findings are consistent with this skepticism about first-order effects but diverge sharply on the significance of higher-order cascading consequences. The six convergence zones identified here -- particularly labor market bifurcation, disintermediation, and the trust premium -- represent precisely the structural reorganization effects that Acemoglu's first-order-only framework excludes by design. GPT theory predicts that it is these complementary innovations and institutional adjustments, not the direct task-level productivity gains, that generate the largest economic consequences of a general-purpose technology (Bresnahan and Trajtenberg, 1995; Helpman, 1998). The Multi-LLM Delphi provides a methodological lens for mapping these higher-order effects systematically.

Similarly, Eloundou et al. (2023) demonstrated that approximately 80 percent of the US workforce has at least 10 percent of their tasks exposed to LLMs. The present study extends this finding by tracing what happens *after* task exposure: the cascading consequences through labor market bifurcation, the apprenticeship crash, and organizational flattening. Task exposure is a necessary but insufficient condition for economic transformation; the Multi-LLM Delphi maps the downstream effects that task-level analyses, by design, cannot capture.

### 5.4 Epistemological Reflections

The question of what LLM consensus *means* -- raised by Bail (2024) and Crockett and Messeri (2024) in the broader context of generative AI in research -- takes on particular urgency in light of this study's findings. Bail (2024) identified several promising applications of generative AI in social science while cautioning against treating model outputs as equivalent to human judgment. Crockett and Messeri (2024) argued more forcefully that LLMs lack the embodied experience, professional stakes, and genuine belief-revision capacity that ground human expert judgment.

The present findings bear on this debate in three ways. First, the convergence zones identified in Round 1 align with predictions that have independent empirical support -- labor market bifurcation is consistent with Acemoglu and Restrepo's (2019) task-based framework; infrastructure repricing is consistent with IEA projections. This alignment supports the "structured knowledge synthesis" interpretation: the models are not generating novel insights from nothing but are recombining and systematizing existing knowledge in ways that produce analytically useful output. Second, the geopolitical divergence pattern demonstrates that LLM outputs are not interchangeable -- model provenance matters, and this variation is analytically informative rather than merely noisy. Third, the near-universal adoption of the apprenticeship crash in Round 2 raises precisely the acquiescence concern that Crockett and Messeri (2024) would predict. The "structured knowledge synthesis" framework developed in Section 2.4 provides a principled basis for interpreting these dynamics without either dismissing them (the stochastic parrot position) or overclaiming them (the synthetic expert position).

### 5.5 Practical Implications

For **industry strategists**, the high-consensus findings provide directional guidance with cross-validated support. The convergence on labor market bifurcation suggests that firms should plan simultaneously for productivity gains from AI augmentation *and* for the organizational disruption that follows when middle layers compress (Budhwar et al., 2023). Specifically, the three-dimension "vanishing middle" pattern -- operating simultaneously across labor markets, value chains, and organizational structures -- implies that firms face compound transformation pressure that cannot be addressed through workforce planning alone. Chief strategy officers in financial services should prepare for disintermediation of brokerage and advisory functions. Healthcare administrators should anticipate longer J-curves due to liability constraints, creating a window for proactive pipeline restructuring before the apprenticeship crash materializes.

For **policymakers**, the geopolitical divergence findings are directly decision-relevant. The observation that AI models trained in different institutional contexts project systematically different transformation pathways suggests that policy choices are not merely implementation details but structural determinants of which future materializes. The convergence on regulatory divergence as a structural force suggests that policymakers shape AI transformation not only through AI-specific regulation but through the entire institutional context -- liability regimes, labor market institutions, education systems, and competition policy. The apprenticeship crash prediction deserves particular policy attention: if the prediction materializes, the window for intervention (mandating minimum human training ratios, subsidizing apprenticeship programs, creating synthetic mentorship platforms) is narrow and precedes the point at which the pipeline disruption becomes visible in workforce statistics.

For **foresight researchers**, the Multi-LLM Delphi offers a scalable complement to traditional human expert panels. It does not replace human expertise but can serve as a rapid, low-cost first round that maps the landscape and identifies areas where human expert judgment is most needed. The method is particularly suited for exploratory studies where the goal is to survey the space of plausible outcomes rather than to converge on precise forecasts.

### 5.6 Synthesis: The Vanishing Middle as Organizing Metaphor

The study's findings converge on a single organizing metaphor: the vanishing middle. AI compresses the middle of distributions -- the middle of the labor market (mid-level knowledge workers caught between surviving judgment roles and surviving physical roles), the middle of value chains (intermediaries eliminated as AI reduces information asymmetry), and the middle of organizational hierarchies (middle management compressed as AI automates coordination and reporting). This three-dimensional compression operates simultaneously and is mutually reinforcing: labor market compression triggers the apprenticeship crash; value chain compression drives disintermediation; organizational compression accelerates the trust premium as remaining human roles become concentrated at the judgment-intensive top and the physically-embodied bottom.

The "vanishing middle" metaphor integrates the study's substantive findings into a single narrative that is both theoretically grounded (in GPT theory's prediction of complementary innovation cascades) and empirically supported (by the convergence of seven independent analytical perspectives). It is also policy-relevant: the compression of the middle is not an abstract concern but a concrete challenge for education systems, labor market institutions, and organizational design practices that must prepare for a bifurcated economy in which the traditional career ladder from junior to senior positions is disrupted.


## 6. Limitations and Future Research

This study has several important limitations that delimit the scope of its claims.

**Panel size.** Seven models constitute a small panel by Delphi standards. Classical Delphi studies typically use 10-30 panelists, and the methodological literature cautions against drawing strong conclusions from small panels (von der Gracht, 2012). However, seven frontier models represent the near-entirety of the current frontier AI landscape, and the diversity across corporate ecosystems and geopolitical origins provides analytical leverage that partially compensates for small panel size.

**Two rounds as deliberate design choice.** The two-round protocol represents a conscious methodological trade-off rather than a limitation per se. Classical Delphi studies typically employ three to four rounds (Linstone and Turoff, 1975), and one might argue that additional iterations would strengthen convergence findings. However, for LLM-based panels specifically, two rounds may constitute a methodological sweet spot. Round 1 establishes independent baselines free from anchoring effects; Round 2 introduces controlled feedback and reveals which convergences are informationally robust versus informationally contingent. The results demonstrate that this two-round design produces rich consensus dynamics: previously contested themes gain endorsement, blind spots are surfaced and adopted, and geopolitical divergence is revealed as structurally persistent.

Critically, additional rounds face diminishing analytical returns coupled with increasing methodological risk. Round 2 already produced near-ceiling consensus on 9 of 11 themes (most at 7/7). A Round 3 would have little upward room to move -- the most likely outcome would be the remaining holdout (Biological-Digital Convergence) also converging to high consensus, yielding a dataset with near-total unanimity that is less analytically informative than the current differentiated picture. More importantly, each additional round of feedback amplifies the acquiescence bias concern: LLMs' well-documented tendency toward sycophancy (Perez et al., 2023; Sharma et al., 2024) means that repeated exposure to consensus summaries risks producing artificial agreement that reflects the models' disposition to align with presented positions rather than genuine epistemic convergence. The two-round design limits this exposure to a single feedback cycle, producing enough convergence dynamics to be analytically useful while preserving enough residual disagreement (the persistent Biological-Digital holdout, the differential depth of AI Religion adoption, the maintained geopolitical divergence) to serve as internal validity checks. Future research should nonetheless explore adversarial Round 3 designs -- for instance, presenting counter-consensus arguments, minority-position amplification, or devil's advocate framings -- that test convergence robustness rather than simply reinforcing it.

**Manual data collection.** The manual collection through native chat interfaces introduces variability in parameters (temperature, context window usage, system prompt interaction) that cannot be controlled or reported. API-based collection with standardized parameters would improve reproducibility.

**Training data opacity.** The training data composition of frontier LLMs is proprietary. This limits the ability to explain *why* models diverge -- whether differences reflect training data composition, alignment procedures, architectural choices, or all three. As training data transparency improves, the analytical power of the Multi-LLM Delphi method will increase.

**Prompt sensitivity.** A single prompt instrument was used. The results are potentially sensitive to prompt design -- different framings, scenario labels, or sector classifications might yield different convergence patterns. Future research should employ prompt sensitivity analysis, varying prompt elements systematically to assess robustness.

**Temporal snapshot.** Model outputs reflect a single point in time (March 2026). As models are updated, their outputs will change. The Multi-LLM Delphi should be understood as producing a dated snapshot, not a permanent assessment. Longitudinal designs that repeat the exercise at regular intervals could track how model predictions evolve over time.

**No ground truth.** Scenario analysis inherently lacks ground truth for validation. The predictions cannot be assessed for accuracy until the time horizons they describe have elapsed. The study can assess internal consistency, convergence, and coherence, but not predictive accuracy.

Future research should pursue four directions. First, **extended multi-round designs** with three or more rounds of iterative feedback to assess whether the convergence patterns observed in this study's two-round design stabilize, intensify, or eventually reverse with additional iteration. The strong convergence observed in Round 2 -- particularly the unanimous adoption of the apprenticeship crash -- raises the possibility that LLM panelists exhibit stronger acquiescence to majority positions than human panelists; designs that deliberately present minority positions or counterarguments in later rounds would help distinguish genuine convergence from conformity pressure. Second, **prompt sensitivity analysis** to assess the robustness of findings across different prompt formulations. Third, **hybrid human-LLM panels** that combine human expert judgment with LLM-generated scenarios to assess complementarity. Fourth, **longitudinal tracking** that repeats the Multi-LLM Delphi at regular intervals to track how model predictions evolve as training data and capabilities advance.


## 7. Conclusion

AI-driven economic transformation, mapped across eight industry verticals through a two-round Multi-LLM Delphi with seven frontier language models, reveals six high-consensus convergence zones and a persistent three-way geopolitical divergence that intensifies under controlled feedback.

The substantive findings identify six high-consensus convergence zones where the encoded knowledge of multiple independent model families points in the same direction: labor market bifurcation and the compression of middle layers; infrastructure bottleneck repricing; disintermediation of middleman business models; regulatory divergence as a structural force; the trust and authenticity premium; and concentration of economic power through AI feedback loops. These convergence zones provide directional guidance for strategists and policymakers, validated by the independent agreement of models trained on different corpora with different alignment approaches.

The methodological findings demonstrate that the Multi-LLM Delphi produces structured, analytically informative output with coherent patterns of convergence and divergence. The geopolitical differentiation across model families -- US models emphasizing market-driven disruption, Chinese models emphasizing state-steered transformation, European models emphasizing regulatory-guided equity -- constitutes the study's most distinctive finding, offering a form of perspective diversity that would require deliberate recruitment effort in a traditional Delphi panel.

The Multi-LLM Delphi method demonstrates that the core Delphi mechanism of controlled feedback produces analytically meaningful dynamics within an LLM panel: blind spots are surfaced and adopted, contested themes converge toward precision, and structurally grounded divergence persists against convergence pressure. The method offers a scalable complement to human foresight expertise -- a rapid instrument for mapping transformation landscapes and generating research questions that merit deeper investigation through traditional methods.

As AI continues to diffuse across the global economy, the need for comprehensive, cross-sector, multi-order transformation maps will intensify. The Multi-LLM Delphi provides a methodological foundation for producing such maps at scale, with built-in geopolitical diversity and transparent analytical procedures. The key insight of this study is not any single prediction but the observation that the future of AI-driven economic transformation is not a single trajectory but a contested, path-dependent, geopolitically differentiated process -- a finding that only becomes visible when multiple independent analytical perspectives are systematically compared.

---

## Data Availability Statement

The analytical materials supporting this study — including the formal codebook with category definitions and decision rules, Round 1 and Round 2 consensus scoring matrices (CSV), worked coding examples, and prompt instruments — are available in the supplementary repository at: https://github.com/TobiasBlask/when-the-middle-disappears. The raw model outputs (Round 1 and Round 2) are available from the corresponding author upon request.

## CRediT Authorship Contribution Statement

**Tobias-Benedikt Blask:** Conceptualization, Methodology, Investigation, Data Curation, Formal Analysis, Writing -- Review & Editing, Visualization (direction and specification), Project Administration, Supervision.

The author conceived the research question, designed the Multi-LLM Delphi protocol, selected the model panel, constructed the prompt instruments, conducted all data collection (Round 1 and Round 2) through native model interfaces, performed the thematic coding and consensus scoring, developed the theoretical framing (GPT theory, MLP integration), and made all analytical judgments and interpretive decisions. The author orchestrated the entire manuscript production process using the Open Academic Paper Machine (Blask, 2026a), directing all drafting, reviewing and revising all AI-generated prose, and approving the final manuscript. Writing -- Original Draft was performed by the AI tool under author direction and is therefore not claimed as a personal CRediT contribution. AI tools were used as described below.

## Declaration of Generative AI and AI-Assisted Technologies in the Writing Process

During the preparation of this work, the author used AI-assisted tools at two distinct levels, which must be clearly distinguished:

**Level 1 -- AI as research instrument (the study's method).** The Multi-LLM Delphi method itself relies on seven frontier large language models (Claude Opus 4.6, GPT-5.4, Gemini 3.1 Pro, Grok 4.2, DeepSeek R2, Qwen 4.5 Max, and Mistral Large 3) as structured panelists who generated the primary data analyzed in this study. This use of LLMs as data-generating instruments is the study's methodological approach and is discussed extensively in Sections 2.4, 3, 5, and 6. The author designed the prompt instruments, conducted all queries, and performed all coding and analysis.

**Level 2 -- AI as writing and production tool.** The author used the Open Academic Paper Machine (Blask, 2026a), an autonomous LLM-based research plugin built on Claude Code and the Model Context Protocol, as the primary drafting and production tool for this manuscript. Specifically, the Open Paper Machine was used for:

- **Literature search and reference management:** Automated retrieval, screening, and BibTeX compilation of academic references.
- **Prose drafting:** All prose sections of this manuscript were drafted by the AI tool based on author-provided outlines, analytical notes, coding results, and iterative direction. The author did not write the original draft manually but orchestrated the drafting process through detailed briefings, structured feedback, and revision cycles.
- **Figure generation:** The author specified the communicative intent and content of all figures in detail. PaperBanana (Zhu et al., 2025) generated the visual output; AI assisted with the specification of technical parameters. The author directed all layout decisions, reviewed each iteration, and approved the final versions.
- **LaTeX compilation and formatting:** Conversion between Markdown and LaTeX, template configuration, and typesetting.
- **Quality assurance:** Simulated peer review, writing quality analysis, and positioning analysis to identify and address weaknesses before submission.

The tool is openly available at https://github.com/TobiasBlask/open-paper-machine. A detailed methodological and epistemological discussion of the implications of AI-assisted academic production is provided in Blask and Funk (2026).

**The author's role -- orchestrator, not scribe.** The author's contribution lies in the intellectual direction of this work, not in the manual production of text. The author conceived the research question, designed the methodology, selected the theoretical framing, conducted all data collection, performed all thematic coding and consensus scoring, made all interpretive judgments, directed the drafting of every section, reviewed and revised all AI-generated prose, and approved the final manuscript. No analytical judgment was delegated to AI tools. The AI functioned as a production instrument executing the author's research design and intellectual direction.

The author takes full responsibility for the content of this publication.

---

## References

Acemoglu, D. and Restrepo, P. (2018). Artificial intelligence, automation and work. *NBER Working Paper*, No. 24196.

Acemoglu, D. and Restrepo, P. (2019). Automation and new tasks: How technology displaces and reinstates labor. *Journal of Economic Perspectives*, 33(2), 3-30.

Acemoglu, D., Autor, D., Hazell, J. and Restrepo, P. (2022). Artificial intelligence and jobs: Evidence from online vacancies. *Journal of Labor Economics*, 40(S1), S293-S340.

Autor, D. (2024). Applying AI to rebuild middle class jobs. *NBER Working Paper*, No. 32140.

Banuls, V.A. and Turoff, M. (2011). Scenario construction via Delphi and cross-impact analysis. *Technological Forecasting and Social Change*, 78(9), 1579-1602.

Bresnahan, T.F. and Trajtenberg, M. (1995). General purpose technologies: "Engines of growth"? *Journal of Econometrics*, 65(1), 83-108.

Brown, O., Davison, R.M., Decker, S., Ellis, D.A. and Faulconbridge, J. (2024). Theory-driven perspectives on generative artificial intelligence in business and management. *British Journal of Management*, 35(2), 563-584.

Brynjolfsson, E., Li, D. and Raymond, L. (2023). Generative AI at work. *NBER Working Paper*, No. 31161.

Brynjolfsson, E., Rock, D. and Syverson, C. (2017). Artificial intelligence and the modern productivity paradox: A clash of expectations and statistics. *NBER Working Paper*, No. 24001.

Budhwar, P., Chowdhury, S., Wood, G., Aguinis, H. and Bamber, G.J. (2023). Human resource management in the age of generative artificial intelligence. *Human Resource Management Journal*, 33(3), 606-659.

Chatterji, A., Cunningham, T., Deming, D., Hitzig, Z. and Ong, C. (2025). How people use ChatGPT. *NBER Working Paper*, No. 34255.

Choi, J. and Leigh, A. (2024). AI's creation and displacement of labor demand. *Technological Forecasting and Social Change*, 209, 123732.

Coccia, M. (2018). A theory of the general causes of long waves: War, general purpose technologies, and economic change. *Technological Forecasting and Social Change*, 128, 287-295.

Culot, G., Orzes, G., Sartor, M. and Nassimbeni, G. (2020). The future of manufacturing: A Delphi-based scenario analysis on Industry 4.0. *Technological Forecasting and Social Change*, 157, 120092.

Dwivedi, Y.K., Kshetri, N., Hughes, L., Slade, E.L. and Jeyaraj, A. (2023). Opinion paper: "So what if ChatGPT wrote it?" *International Journal of Information Management*, 71, 102642.

Ecken, P., Gnatzy, T. and von der Gracht, H.A. (2011). Desirability bias in foresight: Consequences for decision quality based on Delphi results. *Technological Forecasting and Social Change*, 78(9), 1654-1670.

Eloundou, T., Manning, S., Mishkin, P. and Rock, D.L. (2023). GPTs are GPTs: An early look at the labor market impact potential of large language models. *arXiv preprint*, arXiv:2303.10130.

Foerster, B. and von der Gracht, H. (2014). Assessing Delphi panel composition for strategic foresight. *Technological Forecasting and Social Change*, 84, 215-229.

Frank, M.R., Autor, D., Bessen, J., Brynjolfsson, E. and Cebrian, M. (2019). Toward understanding the impact of artificial intelligence on labor. *Proceedings of the National Academy of Sciences*, 116(14), 6531-6539.

Fritschy, C. and Spinler, S. (2019). The impact of autonomous trucks on business models in the automotive and logistics industry. *Technological Forecasting and Social Change*, 148, 119736.

Geels, F.W. (2005). Processes and patterns in transitions and system innovations: Refining the co-evolutionary multi-level perspective. *Technological Forecasting and Social Change*, 72(6), 681-696.

Geels, F.W. (2011). The multi-level perspective on sustainability transitions: Responses to seven criticisms. *Environmental Innovation and Societal Transitions*, 1(1), 24-40.

Geels, F.W. (2020a). Micro-foundations of the multi-level perspective on socio-technical transitions. *Technological Forecasting and Social Change*, 152, 119894.

Geels, F.W., McMeekin, A. and Pfluger, B. (2020b). Socio-technical scenarios as a methodological tool to explore social and political feasibility in low-carbon transitions. *Technological Forecasting and Social Change*, 151, 119258.

Goldfarb, A. and Tucker, C. (2019). Digital economics. *Journal of Economic Literature*, 57(1), 3-43.

Gordon, T. and Pease, A. (2006). RT Delphi: An efficient, "round-less" almost real time Delphi method. *Technological Forecasting and Social Change*, 73(4), 321-333.

Grybauskas, A. and Cardenas-Rubio, J. (2024). Unlocking employer insights: Using large language models to explore human-centric aspects in the context of Industry 5.0. *Technological Forecasting and Social Change*, 209, 123719.

Guo, Z., Yang, G. and Wu, W. (2026). Automatic synthesis of econometric empirical research results using large language model. *Technological Forecasting and Social Change*, doi:10.1016/j.techfore.2025.124370.

Kanbach, D.K., Heiduk, L., Blueher, G., Schreiter, M. and Lahmann, A. (2023). The GenAI is out of the bottle: Generative artificial intelligence from a business model innovation perspective. *Review of Managerial Science*, 18(6), 1695-1737.

Kern, F. (2012). Using the multi-level perspective on socio-technical transitions to assess innovation policy. *Technological Forecasting and Social Change*, 79(2), 298-310.

Korzinov, V. and Savin, I. (2018). General purpose technologies as an emergent property. *Technological Forecasting and Social Change*, 129, 88-104.

Liu, W., Chotia, V., Wang, L., Sharma, P. and Albishri, N. (2026). Intelligence by design: Large language model work integration as strategic enablers for supply chain regeneration. *Technological Forecasting and Social Change*, doi:10.1016/j.techfore.2025.124497.

Qian, Y., Liu, J. and Zhang, R. (2023). AI development on labor income share: A simulation analysis from the perspective of labor-biased technological progress. *Technological Forecasting and Social Change*, 193, 122637.

Postma, T. and Liebl, F. (2005). How to improve scenario analysis as a strategic management tool? *Technological Forecasting and Social Change*, 72(2), 161-173.

Raisch, S. and Krakowski, S. (2021). Artificial intelligence and management: The automation-augmentation paradox. *Academy of Management Review*, 46(1), 192-210.

Roberts, C. and Geels, F.W. (2019). Conditions for politically accelerated transitions. *Technological Forecasting and Social Change*, 140, 221-240.

Sokolov, A., Grebenyuk, A. and Urashima, K. (2025). Biases in expert judgements in large-scale S&T Delphi surveys. *Technological Forecasting and Social Change*, doi:10.1016/j.techfore.2025.124223.

Stahl, B.C., Brooks, L., Hatzakis, T., Santiago, N. and Wright, D. (2023). Exploring ethics and human rights in artificial intelligence -- A Delphi study. *Technological Forecasting and Social Change*, 191, 122502.

van der Heijden, K. (1996). *Scenarios: The Art of Strategic Conversation*. Wiley.

von der Gracht, H.A. (2012). Consensus measurement in Delphi studies: Review and implications for future quality assurance. *Technological Forecasting and Social Change*, 79(8), 1525-1536.

Zeba, G., Dabic, M., Cicak, M., Daim, T. and Yalcin, H. (2021). Technology mining: Artificial intelligence in manufacturing. *Technological Forecasting and Social Change*, 171, 120971.

Walrave, B., Talmar, M., Podoynitsyna, K.S., Romme, A.G.L. and Verbong, G.P.J. (2018). A multi-level perspective on innovation ecosystems for path-breaking innovation. *Technological Forecasting and Social Change*, 136, 103-113.

---

## Appendix A: Model Response Summary Statistics

| Model | Provider | Region | Word Count | Verticals Complete | Cross-Cutting Sections | Specificity Rating |
|-------|----------|--------|------------|-------------------|----------------------|-------------------|
| Claude Opus 4.6 | Anthropic | US | 30,613 | 8/8 (full) | 5 convergence, 5 wildcards, full human section | High |
| GPT-5.4 | OpenAI | US | 23,346 | 8/8 (full) | 6 convergence, 5 wildcards, full human section | High |
| DeepSeek R2 | DeepSeek | China | 22,614 | 8/8 (full) | 4 convergence, 5 wildcards, detailed human section | Very High |
| Gemini 3.1 Pro | Google | US | 16,330 | 8/8 (moderate) | 3 convergence, 5 wildcards, full human section | High (uneven) |
| Qwen 4.5 Max | Alibaba | China | 11,024 | 8/8 (reduced depth) | 4 convergence, 5 wildcards, concise human section | Moderate |
| Mistral Large 3 | Mistral AI | EU | 8,261 | 8/8 (reduced depth) | 3 convergence, 5 wildcards, concise human section | Low-Moderate |
| Grok 4.2 | xAI | US | 2,169 | 2/8 (truncated) | Incomplete | High (where present) |

## Appendix B: Consensus Scoring Matrix -- Cross-Vertical Convergence Zones

| Convergence Zone | Claude | GPT-5.4 | Gemini | Grok | DeepSeek | Qwen | Mistral | Score |
|-----------------|--------|--------|--------|------|----------|------|---------|-------|
| Labor market bifurcation | X | X | X | X | X | X | X | 7/7 HC |
| Infrastructure bottleneck repricing | X | X | X | | X | X | X | 6/7 HC |
| Disintermediation of intermediaries | X | X | X | X | X | | | 5/7 HC |
| Regulatory divergence as structural force | X | X | X | X | X | X | | 6/7 HC |
| Trust/authenticity premium | X | X | X | | X | X | | 5/7 HC |
| Concentration via AI feedback loops | X | X | X | X | X | | | 5/7 HC |
| Compute as currency | | X | X | X | | X | | 4/7 MC |
| Model collapse / data poisoning | | | X | | | X | | 2/7 BS |
| AI religion / spiritual response | X | | | | | | | 1/7 BS |

HC = High Consensus; MC = Moderate Consensus; BS = Blind Spot

## Appendix C: Structured Prompt Instrument

The complete structured prompt instrument used to query all seven models is reproduced below. [The full prompt text is available in the supplementary materials repository.]

## Appendix D: Round 2 Consensus Scoring Matrix -- Blind Spot Adoption and New Predictions

**Panel A: Blind Spot Adoption in Round 2**

| Blind Spot | Claude | GPT-5.4 | Gemini | Grok | DeepSeek | Qwen | Mistral | R2 Score |
|-----------|--------|---------|--------|------|----------|------|---------|----------|
| Apprenticeship Crash | X (originator, elevated) | X (strongly adopted) | X (elevated to defining crisis) | X (fully adopted) | X (fully adopted) | X (fully adopted) | X (adopted as wildcard) | 7/7 HC |
| AI Religion / Spiritual Response | X (maintained strongly) | X (partial, cultural-political) | X (elevated) | X (MAX wildcard) | X (MAX case) | X (3rd-order cultural) | ~ (mentioned as wildcard) | 5-6/7 HC/MC |

**Panel B: Contested Future Shifts in Round 2**

| Contested Future | R1 Score | Claude R2 | GPT-5.4 R2 | Gemini R2 | Grok R2 | DeepSeek R2 | Qwen R2 | Mistral R2 | R2 Score |
|-----------------|----------|-----------|------------|-----------|---------|-------------|---------|------------|----------|
| Compute as Currency/Reserve | 4/7 MC | Partial (strategic resource) | Partial (strategic reserve) | Strongly agree | Strongly agree | Agree (qualified) | Agree (upgraded to Base) | Adopt | 6-7/7 HC |
| Autonomous Economic Agents | 4/7 MC | Agree | Qualified agree | Strongly agree | Strongly agree | Strongly agree | Agree (upgraded to Base) | Adopt | 7/7 HC |
| Biological-Digital Convergence | 3/7 MC | Agree (MAX only) | Agree (healthcare only) | Disagree (timeline downgrade) | Agree (upgraded) | Agree (MAX only) | Disagree (maintain MAX) | Wildcard mention | 3-4/7 MC |

**Panel C: New Emergent Predictions in Round 2**

| New Prediction | Claude | GPT-5.4 | Gemini | Grok | DeepSeek | Qwen | Mistral | R2 Score |
|---------------|--------|---------|--------|------|----------|------|---------|----------|
| Regulatory Arbitrage Hubs / Compute Havens | X | | X | X | | | | 3/7 MC |
| Agent-to-Agent Economy (distinct layer) | | X | X | X | X | X | | 5/7 HC |
| Synthetic Mentorship Platforms | | | | X | | X | | 2/7 BS |
| Oscillation Pattern (non-linear transition) | X | | | | | | | 1/7 BS |
| AI Literacy Class Divide | | | X | | X | | | 2/7 BS |
| Sovereignty Stack Fragmentation | | | X | | | X | | 2/7 BS |
| Authenticity Economy (as distinct sector) | | X | | X | X | | | 3/7 MC |

HC = High Consensus (5+ of 7); MC = Moderate Consensus (3-4 of 7); BS = Blind Spot (1-2 of 7)


## Appendix E: Round 2 Consensus Summary (as presented to models)

The following is the anonymized consensus summary provided to each model at the beginning of Round 2. This summary was constructed by the researcher based on the Round 1 coding and represents an interpretive product, not raw data. Readers should evaluate whether the framing of consensus findings in this summary may have influenced Round 2 responses (see Section 4.5.5 for discussion of acquiescence bias).

> **Round 1 Results Summary — Anonymized Consensus Findings**
>
> Seven frontier AI models independently analyzed AI-driven economic transformation across eight industry verticals, four adoption stages, three scenarios, and three orders of effects. The following summarizes the key consensus patterns:
>
> **High-Consensus Convergence Zones (5+ of 7 models agree):**
> 1. *Labor Market Bifurcation* (7/7): All models predict a "barbell" pattern — AI simultaneously creates high-value judgment/accountability roles and displaces mid-level knowledge work.
> 2. *Infrastructure Bottleneck Repricing* (6/7): Physical infrastructure becomes the binding constraint on AI transformation.
> 3. *Regulatory Divergence as Structural Force* (6/7): EU, US, and Chinese governance approaches create systematically different transformation pathways.
> 4. *Disintermediation of Middleman Business Models* (5/7): AI enables direct producer-consumer connections across sectors.
> 5. *Trust and Authenticity Premium* (5/7): As AI makes intelligence cheap, trust and human certification become economically scarcer.
> 6. *Concentration via AI Feedback Loops* (5/7): Winner-take-most dynamics driven by data-AI capability loops.
>
> **Contested Futures (3-4 of 7 models):**
> 7. *Autonomous Economic Agents* (4/7)
> 8. *Compute as Currency* (4/7)
> 9. *Biological-Digital Convergence* (3/7)
>
> **Blind Spots (1-2 of 7 models):**
> 10. *The Apprenticeship Crash* (1/7): Eliminating junior roles severs experiential training pipelines.
> 11. *AI Religion / Spiritual Response* (1/7): Spiritual movements forming around AI.
>
> **Geopolitical Divergence:** US-origin models emphasize market-driven disruption; Chinese-origin models emphasize state-steered transformation; the European model emphasizes regulatory frameworks and social equity.


## Appendix F: Representative Slice of the 288-Cell Analytical Matrix — Information Technology Vertical

The full 288-cell matrix (8 verticals × 4 stages × 3 scenarios × 3 effect orders) is available in the supplementary repository. The following table presents a representative slice for the Information Technology vertical under the BASE scenario.

**Table F1: Information Technology Vertical — BASE Scenario**

| Stage | 1st Order (Task Automation) | Consensus | 2nd Order (Structural Reorganization) | Consensus | 3rd Order (Systemic Transformation) | Consensus |
|-------|---------------------------|-----------|--------------------------------------|-----------|-------------------------------------|-----------|
| Stage 1: Augmentation (2024-2026) | AI copilots for coding, testing, documentation; 40-60% productivity gains for junior developers | 7/7 HC | Junior developer roles compressed; senior roles shift to AI orchestration | 6/7 HC | Early regulatory responses; AI ethics teams emerge | 4/7 MC |
| Stage 2: Partial Automation (2027-2030) | Autonomous code generation for routine applications; AI-driven QA replaces manual testing | 6/7 HC | Software firms reorganize into AI-native and legacy tiers | 6/7 HC | Compute access becomes strategic moat; infrastructure bottleneck reprices | 5/7 HC |
| Stage 3: Systemic Integration (2031-2035) | AI systems design, test, and deploy software with minimal human oversight | 5/7 HC | Platform consolidation; 3-5 hyperscalers control 80%+ compute | 5/7 HC | Regulatory divergence creates three-tier global software market | 4/7 MC |
| Stage 4: Transformation (2036-2040+) | Self-improving AI systems; software production costs approach zero | 4/7 MC | IT sector bifurcates into infrastructure oligopoly and commoditized application layer | 4/7 MC | Compute as geopolitical currency; AI sovereignty determines national trajectory | 3/7 MC |

Note: Consensus scores decrease from Stage 1 to Stage 4, consistent with GPT theory's prediction that higher-order, longer-horizon effects are inherently harder to anticipate. The full matrix is available at https://github.com/TobiasBlask/when-the-middle-disappears.
