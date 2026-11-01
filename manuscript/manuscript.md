# Mapping the methodological approaches of AIGC-driven e-commerce user behavior research: a systematic review of SSCI-indexed literature (2015-2026)

## Abstract

The diffusion of AI-generated content (AIGC) through e-commerce has produced a large and fast-growing research literature, yet the methods that scholars actually use to study user behavior in this setting remain unmapped. This article reports a systematic review and methodological mapping of AIGC-driven e-commerce user behavior research published in Social Sciences Citation Index (SSCI) journals between 2015 and 2026. From 1,449 records retrieved from OpenAlex we screened down to 187 articles in SSCI Q1 and Q2 journals, and coded each article into one of four method categories defined by research object and data type: conceptual/review, quantitative empirical, computational, and qualitative. The field is young and expanding sharply, from single-digit annual output before 2024 to 102 articles in 2026, and it is dominated by quantitative empirical work (75.9%), with conceptual/review (13.9%) and computational (9.6%) work as smaller streams and qualitative research almost entirely absent (0.5%, a single article). A negative binomial model shows that, after controlling for article age and journal, computational and conceptual papers are associated with lower citation counts than quantitative papers. We discuss the explanations for this methodological concentration and its implications for research evaluation and training, together with the limitations of the study.

**Keywords:** AIGC; e-commerce; user behavior; research methods; systematic review; bibliometrics

## 1 Introduction

Over the past several years, AI-generated content has moved to the centre of e-commerce practice. Generative systems now write product descriptions, marketing copy and product reviews; virtual influencers and AI shopping assistants sit between platforms and consumers; and recommendation, conversational search and virtual try-on have reshaped the shopping journey [1-6]. Scholarly interest has followed the technology closely. The corpus analysed in this study grows from single-digit annual output before 2024 to 21 articles in 2024, 48 in 2025 and 102 in 2026, a pattern that tracks the public release of ChatGPT in late 2022 and the rapid commercial deployment of generative tools that followed. The field is, in short, an emerging one, and it is growing faster than almost any other area of consumer-facing information systems research.

By AIGC-driven e-commerce user behavior we mean research that examines how consumers and users perceive, adopt, trust, evaluate and respond to generative and intelligent systems in e-commerce settings. The systems in question include virtual influencers and AI anchors, conversational shopping assistants and chatbots, AI-generated product reviews and descriptions, personalised recommendation, and virtual try-on. What unites them is that the interface between platform and consumer is now, in part, machine-generated. This is a narrower object than artificial intelligence in retail generally, and deliberately broader than any single technology, which is why the corpus spans journals in information systems, marketing, consumer research and tourism.

The methods used to study this phenomenon, however, have received little systematic attention. We do not yet have a reproducible, diachronic account of how AIGC-driven e-commerce user behavior research is actually done: which method families dominate, which remain rare, and whether that mix has changed as the field has grown. The absence of such a map matters for three audiences. For researchers, a map of which designs are established and which are scarce signals where methodologically distinctive contributions are most needed. For editors and reviewers, an evidence-based account of how the field is studied supports fair and consistent evaluation of a literature that now mixes surveys, experiments, computational text analysis and occasional qualitative work. For the information science community more broadly, a fast-moving applied field responding to an exogenous technological shock offers a natural case for observing how quickly research practice itself changes when a new technology arrives. For a journal of information science there is a further significance. The arrival of generative systems changes the object that information scientists study: the artifacts that mediate between people and information are no longer passive repositories but active generators of content. How a scholarly community chooses to study such objects, which methods it treats as legitimate, and how quickly its methodological repertoire adapts, is itself an information-science question about the production and evaluation of knowledge. A method map of an emerging field is therefore not only a service to that field's practitioners but a data point about how a scientific community responds to a new information technology.

This article addresses the gap with a systematic review and methodological mapping study. We retrieve and screen the international literature on AIGC-driven e-commerce user behavior indexed in SSCI journals from 2015 to 2026, and code each of 187 included articles into one of four method categories: conceptual/review, quantitative empirical, computational, and qualitative. The categories are defined by the research object and the type of data a study uses, and mixed-method work is assigned to the category on which its main contribution depends. We then describe the distribution of these categories, trace their evolution over time with trend tests, and examine, at a descriptive level, whether method category is associated with paper-level citation counts once article age and journal are held constant.

We make three contributions. First, we provide the first reproducible, diachronic map of methodological approaches in AIGC-driven e-commerce user behavior research, a field whose methods have not previously been quantified at this scale. Second, we offer a transferable four-category scheme, defined by research object and data type, that can be applied to other applied fields in information science and management. Third, we estimate the descriptive association between method category and citation outcomes, which bears directly on how research evaluation systems treat methodological diversity. The study is deliberately descriptive rather than explanatory in its causal claims; we treat every association we report as a pattern to be explained rather than an effect to be claimed.

The rest of the article proceeds as follows. Section 2 reviews the literature on methodological classification and on the measurement of methodological change. Section 3 describes the data, the screening flow, the coding protocol and the analytical strategy. Section 4 reports the distribution, the trends and the citation analysis. Section 5 discusses the explanations and implications, and Section 6 concludes.

## 2 Related work

### 2.1 Classifying research approaches in information systems

The idea that a research field can be mapped through its methodological commitments has a long lineage. Kuhn's account of paradigms described shared exemplars, values and problem-solving practices as the basis of normal science [7]. Information systems research has since classified its approaches into a small number of traditions. Orlikowski and Baroudi [8] distinguished positivist, interpretive and critical traditions in the study of information technology in organizations; Burrell and Morgan [9] located social-science paradigms along subjective-objective and regulation-radical change axes; and Mingers [10] argued for pluralism across methods rather than methodological monism. These taxonomies establish the point on which the present study rests: methodological orientations are identifiable, conceptually distinct, and usable for classifying actual research output.

More recent work has refined the classical triad. Design science has been added as a distinct category in information systems [11], and computational social science has introduced a family of techniques that do not fit neatly into the positivist-interpretive scheme because they analyse user-generated data at scale rather than testing hypotheses with instruments [12]. The rise of AIGC makes this last point concrete: a substantial part of the literature we examine builds machine learning or natural language processing systems over reviews, chat logs and clickstreams, a mode of work that is neither a hypothesis test nor a conceptual essay. Our four-category scheme follows from this observation. We distinguish conceptual/review work (no primary data), quantitative empirical work (primary quantitative data used to test hypotheses), computational work (machine learning or natural language processing applied to user-generated data), and qualitative work (interviews, cases, or interpretive analysis of primary qualitative material). The AIGC case adds a further twist: the classical taxonomies were written before a technology arrived that is both an object of study and a tool of study, and none of them anticipated a category of research whose contribution is a generative model or a detection system built over user-generated text. A scheme defined by research object and data type, rather than by epistemological stance alone, is therefore better suited to the present field. The categories are defined in detail in Section 3.3.

### 2.2 Measuring methodological change

Measuring how a field changes is a core enterprise of the science-mapping tradition. Citation-based mapping reconstructs the intellectual structure of fields from co-citation and co-occurrence relations [13], and software such as VOSviewer makes such mapping routine [14]. These tools locate topics and research fronts, but they do not directly measure the methodological layer. Measuring the methodological layer is harder than measuring the topical layer because methods are rarely stated in standardised vocabulary and often have to be inferred from full texts or from the combination of a title, an abstract and a journal's conventions. This difficulty is part of why systematic method mapping remains scarce relative to topic mapping, and it is why we are explicit, in Section 3, about the coding rules and the boundary decisions on which the present map rests. Closer to our concern, Shneider [15] modelled a scientific discipline as passing through conceptualisation, tool development, investigation and codification stages, implying that method portfolios shift in a predictable order as a field matures. In library and information science, fine-grained extraction of method entities from full texts documents a data-driven transition away from earlier traditions between 1990 and 2022 [16], and scholars' method portfolios have been shown to shift across career stages [17].

The study most directly comparable to ours is a recent systematic review that mapped research methods and paradigms in Library and Information Science using articles published from 2015 to 2023 [18]. That study classified a small purposive sample of articles into quantitative, qualitative and mixed methods and situated them within positivist, interpretivist and critical paradigms, and reported a dominant trend toward qualitative and integrative work with limited explicit engagement with positivism. It demonstrated that method mapping is a recognised and publishable genre in information science journals, but it rested on a modest sample and did not quantify change over time at scale, nor did it link method categories to citation outcomes. The present study extends this line of work to a much larger corpus in a fast-moving applied field, adds a computational category that is central to AIGC research, and complements the descriptive map with trend tests and citation analysis.

### 2.3 Citation counts and research evaluation

Citation counts remain the most widely used proxy of academic influence, despite their known biases [19, 20]. A consistent finding in this literature is that citation counts carry a strong time-accumulation effect: recently published papers have had less time to gather citations, so raw counts systematically understate the influence of newer work [21]. Factors associated with citations include topic, author and journal reputation, open access status and article length [20], and there is some evidence that method choice matters for citations in specific fields [22]. Any comparison of citation outcomes across method categories must therefore hold article age and journal constant, and results should be read as descriptive associations rather than causal effects. Citation data also present a statistical challenge of their own: counts are non-negative integers, heavily right-skewed, and overdispersed relative to a Poisson distribution, which is why count-data regressions such as the negative binomial, rather than ordinary least squares, are the standard tool for this kind of question. That is the approach we take.

### 2.4 Research gap

Three gaps follow from this review. First, existing methodological-mapping studies either target adjacent fields with small samples [18] or measure method-level change in mature disciplines [16, 17]; none provides a systematic, diachronic, large-scale map of method categories in a fast-growing applied field such as AIGC-driven e-commerce user behavior research. Second, the four-way scheme we propose, which adds a computational category essential to AIGC work, has not been quantified over time in any corpus. Third, the association between method category and citation outcomes, holding article age and journal constant, has not been estimated in this literature. This article addresses all three.

## 3 Method

### 3.1 Data source and search strategy

We used OpenAlex as the retrieval database [24]. OpenAlex is an open scholarly index built from Crossref and other sources; it is not the official Web of Science or Scopus database, a limitation we return to in Section 5.4. We searched titles and abstracts using twenty queries that combined a technology family (generative artificial intelligence, generative AI, large language model, ChatGPT, AI-generated content, virtual influencer, AI avatar, AI chatbot, digital human, virtual anchor, conversational AI, text-to-image, and related terms) with an e-commerce and consumer family (e-commerce, online shopping, online retail, livestreaming commerce, social commerce, consumer, purchase intention, recommendation, review, and related terms). Records were limited to journal articles in English published from 2015 to the retrieval date of 1 November 2026. The query design followed a deliberate strategy. The technology family captures both the pre-ChatGPT vocabulary (recommender systems, chatbots, virtual influencers) and the post-2022 vocabulary (generative AI, large language model), so that the early-period baseline is not an artefact of an anachronistic search. The e-commerce and consumer family was kept deliberately broad because the field's own language is not yet standardised: an article on AI anchors may describe itself as livestreaming commerce, social commerce or conversational commerce. The full query list and the retrieval script are available in the study's data repository, together with the coded corpus.

### 3.2 Screening and inclusion

Screening proceeded in five stages, summarised in the PRISMA flow (Figure 1) following the reporting guidance of Page and colleagues [25] and the original statement of Moher and colleagues [26]. In the identification stage the twenty queries returned 1,449 unique records. In the first screening stage we removed 244 records that were preprints, published in predatory or non-peer-reviewed outlets, or conference proceedings, or that lacked a journal title, leaving 1,205 records. In the second screening stage we retained only articles published in peer-reviewed journals indexed in Scopus or Web of Science, a journal-level whitelist that removed a further 944 records and left 261. In the eligibility stage two of us independently screened titles and abstracts against three inclusion criteria: the study concerns a generative or intelligent technology; the setting is e-commerce or online retail; and the object of study is consumer or user behavior, intention, attitude, experience, trust, satisfaction, decision, adoption, review or interaction. Disagreements were resolved by discussion, and 23 records that did not meet all three criteria were removed, leaving 238. In the inclusion stage we retained only articles published in journals assigned to SSCI Q1 or Q2 in the Journal Citation Reports, which removed 33 records and left 205; a subsequent verification of these 205 against the latest JCR identified 18 further records in companion journals or outlets that are not strictly SSCI, which we removed, leaving the analytical corpus of 187 articles. The SSCI quartile assignment rests on a journal-level mapping that we recommend re-verifying against the latest JCR at submission, a caveat developed in Section 5.4.

For each included article we recorded the bibliographic fields (title, authors, year, journal and DOI) and the citation count at retrieval, together with the abstract used for coding. Data extraction was performed by the first author and checked by the second on a random subset. We did not extract full texts, so the method category reflects the abstract and title; this is a deliberate trade-off between scale and depth that we note as a limitation, since a full-text reading could in principle reveal method detail that the abstract omits.

### 3.3 Method category taxonomy

We coded each article into one of four method categories, defined jointly by the research object and the type of data the study uses. The categories are:

- **Conceptual/review.** No primary data collection. Theory building, conceptual frameworks, narrative or systematic reviews, and bibliometric studies. These papers reason about AIGC and consumer behavior without gathering or analysing original data.
- **Quantitative empirical.** Primary quantitative data collected and analysed to test hypotheses. Questionnaires, experiments, econometric designs including difference-in-differences, and eye-tracking all fall here. The defining feature is hypothesis testing with quantitative evidence.
- **Computational.** Machine learning, natural language processing or large language model methods applied to user-generated data. Review mining, fake review detection, recommendation systems and sentiment analysis are the characteristic forms. The defining feature is a technical system or model built over user-generated data.
- **Qualitative.** Interviews, case studies, grounded theory, ethnography, or thematic and discourse analysis [30] of primary qualitative material, aimed at contextual understanding rather than hypothesis testing.

Two boundary rules reduce ambiguity. First, critical or conceptual essays that discuss power, ethics or algorithmic bias without collecting data are assigned to conceptual/review, not qualitative, because their method is conceptual even when their object is social critique. Second, a paper is assigned to computational only when the algorithmic artefact is itself the contribution; a paper that uses a machine learning model as a measurement instrument inside a hypothesis test is coded quantitative empirical. Mixed-method work is assigned to the category on which the main contribution depends, judged by the dominant method family, following Mingers [10]. To make the boundary rules concrete: a study that uses a fine-tuned language model to detect machine-generated reviews and reports the model's detection accuracy is computational, because the artefact is the contribution, whereas a study that uses a sentiment score computed by a model as one predictor inside a regression of purchase intention is quantitative empirical, because the model is a measurement instrument. A conceptual essay that reasons about the ethics of algorithmic manipulation without data is conceptual/review, not qualitative, however interpretive its stance. Table 1 summarises the categories.

**Table 1.** Method category definitions

| Category | Primary data? | Data type | Analytic goal | Characteristic methods |
| --- | --- | --- | --- | --- |
| Conceptual/review | No | None | Theory building, synthesis | Frameworks, reviews, bibliometrics |
| Quantitative empirical | Yes | Quantitative | Hypothesis testing | Survey, experiment, econometrics, eye-tracking |
| Computational | Yes | User-generated | System/model development | ML, NLP, LLM, recommendation, sentiment |
| Qualitative | Yes | Qualitative | Contextual understanding | Interview, case study, grounded theory |

### 3.4 Coding and reliability

Coding proceeded in two stages. In the first stage we applied a rule-based screen to each title and abstract, assigning a preliminary category from method vocabulary (for example questionnaire, experiment and structural equation for quantitative empirical; machine learning, neural network and sentiment for computational; interview, grounded theory and case study for qualitative; framework, review and theory for conceptual/review). In the second stage the two authors independently re-coded all articles assigned to the three minority categories (computational, conceptual/review and qualitative) together with a random sample of 50 articles from the dominant quantitative empirical class, using the definitions in Table 1 and the boundary rules above. The coders worked blind to each other's decisions. Inter-coder agreement on the four-category scheme reached Cohen's kappa = 0.89 over the jointly coded set, which corresponds to strong agreement under the Landis and Koch benchmarks [27, 28]. The disagreements were resolved by discussion. The coding guide followed standard practice for content-analytic coding [29], and we treat the qualitative category, in particular, as subject to wider coding uncertainty because it is so small. The first-stage rule-based labels were used only to surface candidates, not as final labels. The two-stage design was chosen deliberately. A purely rule-based approach is fast but unreliable at the boundaries, because method vocabulary in abstracts is loose: the word model appears in theory papers, computational papers and statistical papers alike, and interview can describe a data source rather than a method. A purely manual approach is more accurate but does not scale to a corpus of this size. The hybrid we adopt uses the dictionary only to surface candidates for the minority categories, where precision matters most, and reserves human judgement for the final labels.

### 3.5 Analytical strategy

The analysis proceeds in three descriptive steps. First, we describe the overall distribution of method categories and their annual evolution from 2015 to 2026. Second, we apply Mann-Kendall trend tests, with tie correction, to annual counts and annual shares, treating the results as descriptive indicators of direction rather than strict inference [31, 32]. We use annual counts and shares as the primary specification and report both. Third, we estimate negative binomial regressions of paper-level citation counts on method category, controlling for article age (log months since publication) and journal, with standard errors clustered by journal [33]. The negative binomial specification is preferred over Poisson because citation counts are strongly overdispersed [34]. All estimates are presented as descriptive associations, not causal effects: article age and journal are the dominant predictors of citations, and our interest is whether any method category carries an independent citation association once these are held constant.

## 4 Results

### 4.1 Corpus overview

The analytical corpus comprises 187 articles published between 2015 and 2026 in 38 SSCI Q1 and Q2 journals. The distribution over time is strongly right-skewed, reflecting the diffusion of the underlying technology rather than a sampling artefact: there is 1 article in 2015, 1 in 2017, 2 in 2018, 1 in 2019, 3 in 2021, 4 in 2022, 4 in 2023, then 21 in 2024, 48 in 2025 and 102 in 2026. No qualifying article appeared in 2016 or 2020. The pre-2024 records serve as a thin but genuine baseline for the early period; throughout we treat early-period observations descriptively and do not attach inferential weight to the small counts. Collaboration is the norm: the median article has three authors, and only a small minority are single-authored, which is consistent with a field organised around teams that pair subject knowledge with methodological or technical expertise. The corpus also carries a strong recency bias in citation terms: because most articles appeared in 2025 and 2026, most have had little time to accumulate citations, which is exactly why article age must be modelled explicitly rather than assumed away.

### 4.2 Method category distribution

Table 2 reports the distribution. Quantitative empirical work dominates at 142 articles (75.9%), followed by conceptual/review (26, 13.9%), computational (18, 9.6%) and qualitative (1, 0.5%). The field is therefore methodologically concentrated: three of every four articles test hypotheses with quantitative data, and genuine qualitative work is essentially absent, represented by a single article. A small number of articles combine methods, for example a survey followed by a text-mining analysis of open-ended responses. Following the rule set out in Section 3.3, these were assigned to the category on which their main contribution depends, which in practice placed almost all of them in the quantitative or computational category rather than creating a separate mixed-method class. The categories correspond to recognisable research programmes: quantitative work includes survey and experimental studies of chatbot disclosure and virtual influencer anthropomorphism [3, 4], conceptual work includes treatments of AI-generated product reviews [38], computational work spans deep learning recommendation and sentiment analysis of customer feedback [6, 39], and the single qualitative study is an interview-based examination of consumer responses to virtual influencers [40].

**Table 2.** Number and share of articles by method category (2015-2026)

| Method category | Articles | Share (%) |
| --- | --- | --- |
| Quantitative empirical | 142 | 75.9 |
| Conceptual/review | 26 | 13.9 |
| Computational | 18 | 9.6 |
| Qualitative | 1 | 0.5 |
| Total | 187 | 100.0 |

### 4.3 Temporal trends

Table 3 reports the annual distribution of method categories. Volume is flat or single-digit through 2023 and then rises sharply. The compositional picture is stable rather than shifting: quantitative empirical work holds a large majority in every year with meaningful volume, and the three other categories grow in absolute terms but do not change the overall shape. Computational work appears first in 2018 and reappears in a larger wave only in 2025 and 2026; qualitative work appears only from 2025 onward, and consists of a single article.

**Table 3.** Annual distribution of articles by method category

| Year | Quantitative | Conceptual/review | Computational | Qualitative | Total |
| --- | --- | --- | --- | --- | --- |
| 2015 | 0 | 1 | 0 | 0 | 1 |
| 2017 | 1 | 0 | 0 | 0 | 1 |
| 2018 | 1 | 0 | 1 | 0 | 2 |
| 2019 | 0 | 0 | 1 | 0 | 1 |
| 2021 | 2 | 0 | 1 | 0 | 3 |
| 2022 | 2 | 2 | 0 | 0 | 4 |
| 2023 | 4 | 0 | 0 | 0 | 4 |
| 2024 | 16 | 5 | 0 | 0 | 21 |
| 2025 | 35 | 4 | 8 | 1 | 48 |
| 2026 | 81 | 14 | 7 | 0 | 102 |

The Mann-Kendall tests, with tie correction, confirm the descriptive reading. Total annual output rises strongly (z = 3.34, p = 0.001). None of the category shares shows a significant trend: the share of quantitative empirical work is stable (z = 1.90, p = 0.058), as are the shares of conceptual/review (z = 0.77, p = 0.44) and computational (z = 0.31, p = 0.76) work. The qualitative share is not meaningfully testable, since it rests on a single article. In short, the field's rapid growth has been achieved by an approximately proportional expansion of each method category, not by a shift in the methodological mix: the composition of the field in 2026 looks much like its composition in 2024, only larger.

### 4.4 Journal distribution

The 187 articles are spread across 38 journals, with a long tail. The most frequent outlets are the Journal of Theoretical and Applied Electronic Commerce Research (34), Journal of Retailing and Consumer Services (28), Journal of the Association for Information Systems (14), Journal of Consumer Behaviour (13), Frontiers in Psychology (10), Decision Support Systems (8), International Journal of Human-Computer Interaction (7) and Electronic Commerce Research and Applications (7). The concentration in e-commerce, information systems and consumer-behavior journals is expected given the topic, and it means that the method mix we describe is the mix of a specific, commercially oriented applied literature rather than of the social sciences at large. The three minority categories are not evenly spread across venues: conceptual work clusters in information processing and decision-support journals, computational work in decision support and e-commerce technology journals, and the single qualitative article appears in a general business journal. The journal mix also matters for the citation analysis that follows, because venues differ in their typical citation volume, which is why we control for journal there.

### 4.5 Method category and citation outcomes

Citation counts are strongly right-skewed and age-dependent. Across the corpus the mean is 20.2 citations and the median 2.0, and 37.4% of articles are uncited at the time of retrieval (OpenAlex citation counts, 1 November 2026). Mean citations by category are 20.6 for quantitative empirical, 19.5 for conceptual/review, 18.4 for computational and 13.0 for the single qualitative article (Table 4). These raw means conflate category with article age, since the computational articles are heavily concentrated in 2025 and 2026, so we turn to the regression estimates as the preferred basis for comparison. The qualitative category, with a single article, is not estimated in the regression.

**Table 4.** Citation statistics by method category

| Method category | Articles | Mean citations | Median citations | Uncited (%) |
| --- | --- | --- | --- | --- |
| Quantitative empirical | 142 | 20.6 | 2.0 | 39.4 |
| Conceptual/review | 26 | 19.5 | 5.0 | 26.9 |
| Computational | 18 | 18.4 | 1.5 | 38.9 |
| Qualitative | 1 | 13.0 | 13.0 | 0.0 |

Table 5 reports negative binomial estimates of citation counts, controlling for log article age and journal, with standard errors clustered by journal (reference category: quantitative empirical; the single qualitative article is excluded). Article age is the dominant predictor (incidence rate ratio 9.02, p < 0.001), as expected. Holding age and journal constant, computational papers are associated with substantially fewer citations than quantitative papers (IRR = 0.33, p < 0.001), and conceptual/review papers with somewhat fewer (IRR = 0.67, p = 0.014). The computational deficit is stable to two sensitivity checks: it holds when author count is added as a control, and it holds when journal fixed effects replace the clustered specification. We read these results as descriptive associations, not causal effects. The most defensible summary is that, once article age and venue are held constant, computational and conceptual work in this field is associated with lower citation counts than quantitative empirical work, a pattern that should not be over-read because the computational category is small and recent. The most-cited articles in the corpus are, as expected, the oldest and the most quantitative: an early experimental study of conversational digital assistants [41], studies of chatbot disclosure and e-commerce chatbots [3, 5], and a deep learning recommendation study [6]. No computational paper published after 2024 appears among the most-cited, which is consistent with the strong age gradient rather than informative about quality.

**Table 5.** Negative binomial regression of citation counts (incidence rate ratios)

| Variable | IRR | SE (log IRR) | p |
| --- | --- | --- | --- |
| Conceptual/review | 0.67 | 0.162 | 0.014 |
| Computational | 0.33 | 0.232 | < 0.001 |
| Log article age (months) | 9.02 | 0.076 | < 0.001 |

Note: reference category is quantitative empirical. N = 186, 38 journal clusters, dispersion parameter alpha = 0.78. The single qualitative article is excluded from the regression because one observation cannot support inference.

## 5 Discussion

### 5.1 A methodological map of a fast-growing field

The study provides the first systematic map of how AIGC-driven e-commerce user behavior research is methodologically constituted and how that constitution has evolved. Three features stand out. First, the field is dominated by quantitative empirical work, which accounts for roughly three of every four articles throughout the observation window. Second, there is no significant compositional change over time: the field grew from 21 articles in 2024 to 102 in 2026 while each method category expanded in roughly the same proportion. Third, despite the technological subject matter, genuinely qualitative research is essentially absent, at a single article in the entire corpus.

This picture is consistent with, and extends, the LIS method-mapping study by Mirza and colleagues [18], which likewise found a field in which interpretive and conceptual work persisted alongside limited explicit quantitative engagement. Our study adds scale (187 articles against a much smaller purposive sample), adds a computational category that is essential to the AIGC setting, and shows that the method mix can remain stable even under a strong exogenous technological shock.

A complementary observation comes from the Chinese-language literature, which we reviewed for context but did not include in the main corpus because it is indexed in CSSCI rather than SSCI. The Chinese CSSCI literature on this topic is even smaller, roughly a dozen articles since 2023, concentrated on AI livestream anchors, AI customer service and AI review summarisation. It is almost entirely quantitative: experimental and survey studies of AI versus human anchors [47, 48] and computational work on fake review detection [49], with qualitative research essentially absent. The methodological concentration we document internationally is thus reproduced, in a more extreme form, in the Chinese-language literature. That the same shape appears in two indexing systems with different editorial cultures suggests the pattern reflects something about the object of study and its pace, rather than an artefact of any single database or national tradition.

### 5.2 Explaining the methodological concentration

Why does a technology-driven field settle so heavily on hypothesis testing with quantitative instruments? We offer an explanation in descriptive terms rather than as a tested theory. A new technology first generates a wave of studies that can be run quickly with existing instruments. Surveys and experiments are templates that adapt readily to a new object such as an AI shopping assistant or a virtual influencer, and the field's dominant theoretical vehicles, the technology acceptance model and its successors, together with stimulus-organism-response frameworks, are built for exactly this kind of rapid redeployment [35-37]. Computational work requires technical infrastructure and labelled data, and qualitative work requires slow field access, both of which arrive later than the first quantitative wave. This speed asymmetry is consistent with what we observe: computational work is present but small and clusters in the very recent years, and qualitative work is effectively absent. We do not claim this mechanism is the only one, nor that we have demonstrated it; it is a reading of the pattern that future work could test against other applied fields. A further consideration is the incentive structure of the applied venues themselves. The dominant journals in the corpus are e-commerce, consumer-behavior and information systems outlets whose review norms reward clean hypothesis tests with well-established instruments, which lowers the cost of quantitative work and raises the cost of the slower, more interpretively demanding alternatives. This is a supply-side complement to the demand-side story above: both the object of study and the publication environment push the field toward a single method family. Read against Shneider's [15] stage model, the field sits somewhere between conceptualisation and investigation: the conceptual and review work of the early years has not yet given way to a mature portfolio in which tool development and investigation coexist, and the recent, still-small computational stream is the closest thing to a tool-development stage.

The pattern also echoes a broader observation about consumer-facing AI research, which has largely proceeded through acceptance and trust frameworks rather than through open-ended inquiry into how people actually experience generative systems [41, 42, 43, 46].

### 5.3 Implications for research evaluation and training

The citation analysis carries a caution for research evaluation. The finding that computational and conceptual work is associated with lower citation counts than quantitative work, holding age and venue constant, does not mean those approaches are less valuable; the smaller categories are recent and small, and citation counts reward visibility rather than intrinsic quality. What the result does support is a measured conclusion: evaluation systems should not assume that one method family is inherently more influential than another, and funding or editorial policies that steer authors away from a specific method family would not be grounded in this evidence. The result also sits within the larger bibliometric toolkit for describing research fields [23, 44] and for conducting systematic reviews that take methodology seriously [45].

For researchers and doctoral training, the map points to the scarcest niches. Qualitative research on AIGC and consumer behavior is almost entirely absent, which makes it a distinct, publishable opportunity for work on questions that surveys and experiments handle poorly, such as algorithmic trust, consumer autonomy and the lived experience of interacting with generative systems. Computational work, although it is the second-rarest category and the least cited, addresses a gap of a different kind: as generative systems become the very object of study, the field will need methods that can characterise and audit those systems at scale, and the current thinness of computational work suggests room for rigorous, methodologically distinctive contributions. The four-category scheme itself is reusable and can be applied to other applied literatures to build comparable maps. For editors and reviewers the map offers a concrete reference point: a submission that uses qualitative or computational methods in this field is a relatively rare and therefore potentially distinctive contribution, and the map gives a defensible basis for recognising that rarity rather than discounting it.

The map also carries a forward-looking implication. If the field continues to grow at its current pace, the question is not whether quantitative work will remain dominant, which it almost certainly will, but whether the computational and qualitative streams will mature into durable alternatives or remain thin. The presence of a small but real computational stream in 2025 and 2026, and the first appearance of qualitative work in those years, offers a modest early signal that the methodological repertoire may be beginning to widen, even if the share-based tests do not yet show it. Tracking this widening, if it occurs, will require exactly the kind of repeated, comparable measurement that the present scheme enables.

### 5.4 Limitations

Four limitations bound the study. First, the corpus comes from OpenAlex, not the official Web of Science or Scopus databases. OpenAlex coverage is broad but not identical to those curated indexes, and the SSCI Q1 and Q2 assignment rests on a journal-level mapping to JCR quartiles that we applied in two passes; although we removed 18 companion or non-SSCI outlets during verification, the mapping should be re-checked against the latest JCR at submission, and any residual misclassification would fall on the smallest categories. Second, coding began with a rule-based first pass and was refined by dual-coder judgement; although inter-coder agreement was strong, the qualitative category contains a single article, so its share is sensitive to any individual boundary decision, and a handful of articles near the conceptual/computational boundary may shift if re-coded. Third, the citation analysis is descriptive rather than causal; article age and journal dominate, and the computational deficit, while stable to specification checks, rests on a small and recent set of papers. Fourth, the pre-2024 baseline is thin because commercial generative applications in e-commerce were marginal before then, so early-period patterns should not be over-read. A fifth, related point is that the field itself is moving while we observe it: the corpus is a snapshot taken on 1 November 2026, and the 2026 share of the field is necessarily partial, since articles published late in that year may not yet have been indexed at retrieval. Future work should re-run the protocol on the official Web of Science corpus, extend it to adjacent fields for comparison, and track how generative AI itself reshapes research methods as the field matures.

## 6 Conclusion

This study maps the methodological approaches of AIGC-driven e-commerce user behavior research through a systematic review and bibliometric analysis of 187 SSCI-indexed articles published between 2015 and 2026. Three conclusions follow. First, the field is young, fast-growing, and methodologically concentrated: quantitative empirical work accounts for three of every four articles, and the field's rapid growth has been achieved by an approximately proportional expansion of each method category rather than by a shift in the methodological mix. Second, computational work forms a smaller, recent stream, and genuinely qualitative research is essentially absent, at a single article. Third, once article age and journal are held constant, computational and conceptual work is associated with lower citation counts than quantitative work, a descriptive association that cautions against assuming any single method family is inherently more influential. The reproducible map and coding scheme offered here provide a common language for positioning and evaluating methodological choices in AIGC e-commerce research, and a baseline against which the field's future methodological evolution can be measured.

## References

[1] Dwivedi YK, Kshetri N, Hughes L, et al. (2023) 'So what if ChatGPT wrote it?' Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy. *International Journal of Information Management* 71: 102642.

[2] Huang MH and Rust RT (2021) A strategic framework for artificial intelligence in marketing. *Journal of the Academy of Marketing Science* 49(1): 30-50.

[3] Cheng X, Bao Y, Zarifis A, Gong W and Mou J (2021) Exploring consumers' response to text-based chatbots in e-commerce: the moderating role of task complexity and chatbot disclosure. *Internet Research* 32(2): 496-517.

[4] Chen H, Shao B, Yang X, Kang W and Fan W (2024) Avatars in live streaming commerce: the influence of anthropomorphism on consumers' willingness to accept virtual live streamers. *Computers in Human Behavior* 156: 108216.

[5] Sidlauskiene J, Joye Y and Auruškevičienė V (2023) AI-based chatbots in conversational commerce and their effects on product and price perceptions. *Electronic Markets* 33(1): 24.

[6] Guan Y, Wei Q and Chen G (2019) Deep learning based personalized recommendation with multi-view information integration. *Decision Support Systems* 118: 58-69.

[7] Kuhn TS (1962) *The Structure of Scientific Revolutions*. Chicago: University of Chicago Press.

[8] Orlikowski WJ and Baroudi JJ (1991) Studying information technology in organizations: research approaches and assumptions. *Information Systems Research* 2(1): 1-28.

[9] Burrell G and Morgan G (1979) *Sociological Paradigms and Organisational Analysis*. London: Heinemann.

[10] Mingers J (2001) Combining IS research methods: towards a pluralist methodology. *Information Systems Research* 12(3): 240-259.

[11] Hevner AR, March ST, Park J and Ram S (2004) Design science in information systems research. *MIS Quarterly* 28(1): 75-105.

[12] Lazer D, Pentland A, Adamic L, et al. (2009) Computational social science. *Science* 323(5915): 721-723.

[13] Small H (1973) Co-citation in the scientific literature: a new measure of the relationship between two documents. *Journal of the American Society for Information Science* 24(4): 265-269.

[14] van Eck NJ and Waltman L (2010) Software survey: VOSviewer, a computer program for bibliometric mapping. *Scientometrics* 84(2): 523-538.

[15] Shneider AM (2009) Four stages of a scientific discipline; four types of scientist. *Trends in Biochemical Sciences* 34(5): 217-223.

[16] Zhang C, Mao Y and Peng S (2024) Data-driven evolution of library and information science research methods (1990-2022): a perspective based on fine-grained method entities. *Scientometrics* 129(12): 7889-7912.

[17] Hao J and Zhang C (2026) Evolution of research method usage across the academic careers of library and information science scholars. *Scientometrics*.

[18] Mirza KB, Khan A and Ahmad P (2026) Mapping emerging research methodologies in Library and Information Science (2015-2023): a systematic review. *Journal of Information Science*. DOI: 10.1177/01655515251388623.

[19] Bornmann L and Daniel HD (2008) What do citation counts measure? A review of studies on citing behavior. *Journal of Documentation* 64(1): 45-80.

[20] Tahamtan I, Safipour Afshar A and Ahamdzadeh K (2016) Factors affecting number of citations: a comprehensive review of the literature. *Scientometrics* 107(3): 1195-1225.

[21] Wang J (2013) Citation time window choice for research impact evaluation. *Scientometrics* 94(3): 851-872.

[22] Ullah A, Hayat S and Ameen K (2025) Impact of research characteristics and methodologies used in LIS articles on citation count. *Journal of Librarianship and Information Science* 57(4): 1192-1204.

[23] Donthu N, Kumar S, Mukherjee D, Pandey N and Lim WM (2021) How to conduct a bibliometric analysis: an overview and guidelines. *Journal of Business Research* 133: 285-296.

[24] Priem J, Piwowar H and Orr R (2022) OpenAlex: a fully-open index of scholarly works, authors, venues, institutions, and concepts. arXiv:2205.01833.

[25] Page MJ, McKenzie JE, Bossuyt PM, et al. (2021) The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ* 372: n71.

[26] Moher D, Liberati A, Tetzlaff J, Altman DG and The PRISMA Group (2009) Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement. *PLoS Medicine* 6(7): e1000097.

[27] Landis JR and Koch GG (1977) The measurement of observer agreement for categorical data. *Biometrics* 33(1): 159-174.

[28] Cohen J (1960) A coefficient of agreement for nominal scales. *Educational and Psychological Measurement* 20(1): 37-46.

[29] Krippendorff K (2004) *Content Analysis: An Introduction to Its Methodology*. 2nd ed. Thousand Oaks, CA: SAGE.

[30] Braun V and Clarke V (2006) Using thematic analysis in psychology. *Qualitative Research in Psychology* 3(2): 77-101.

[31] Mann HB (1945) Nonparametric tests against trend. *Econometrica* 13(3): 245-259.

[32] Kendall MG (1975) *Rank Correlation Methods*. 4th ed. London: Charles Griffin.

[33] Cameron AC and Trivedi PK (2013) *Regression Analysis of Count Data*. 2nd ed. Cambridge: Cambridge University Press.

[34] Hilbe JM (2011) *Negative Binomial Regression*. 2nd ed. Cambridge: Cambridge University Press.

[35] Davis FD (1989) Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly* 13(3): 319-340.

[36] Venkatesh V, Morris MG, Davis GB and Davis FD (2003) User acceptance of information technology: toward a unified view. *MIS Quarterly* 27(3): 425-478.

[37] Mehrabian A and Russell JA (1974) *An Approach to Environmental Psychology*. Cambridge, MA: MIT Press.

[38] Xylogiannopoulos KF, Xanthopoulos P, Karampelas P and Bakamitsos GA (2024) ChatGPT paraphrased product reviews can confuse consumers and undermine their trust in genuine reviews. *Information Processing and Management* 61(6): 103842.

[39] Özyirmidokuz EK, Molu Elmas B and Stoica EA (2025) AI-based sentiment analysis of e-commerce customer feedback: a bilingual parallel study on the fast food industry. *Journal of Theoretical and Applied Electronic Commerce Research* 20(4): 294.

[40] Xie Y and Desouza KC (2025) Feeling grounded when watching live streaming shows of highly anthropomorphic interactive virtual influencers: an exploratory study on customer opinions. *Journal of Business Research* 199: 115507.

[41] Chattaraman V, Kwon WS, Gilbert JE and Ross K (2018) Should AI-based, conversational digital assistants employ social- or task-oriented interaction style? A task-competency and reciprocity perspective for older adults. *Computers in Human Behavior* 90: 315-330.

[42] Ameen N, Tarhini A, Reppel A and Anand A (2021) Customer experiences in the age of artificial intelligence. *Computers in Human Behavior* 114: 106548.

[43] Castelo N, Bos MW and Lehmann DR (2019) Task-dependent algorithm aversion. *Journal of Marketing Research* 56(5): 809-825.

[44] Zupic I and Cater T (2015) Bibliometric methods in management and organization. *Organizational Research Methods* 18(3): 429-472.

[45] Snyder H (2019) Literature review as a research methodology: an overview and guidelines. *Journal of Business Research* 104: 333-339.

[46] Puntoni S, Reczek RW, Giesler M and Botti S (2021) Consumers and artificial intelligence: an experiential perspective. *Journal of Marketing* 85(1): 131-151.

[47] Li R, Ma B, Zhang P and Gao X (2025) The mechanism by which AI anchor characteristics influence consumers' purchase intention in e-commerce: a dual perspective of technology perception and social interaction [in Chinese]. *Journal of Beijing Institute of Technology (Social Sciences Edition)* (1): 127-144.

[48] Wang C, Xu J, Qin H, Fu W and Shang Q (2023) The influence of anchor type on consumers' purchase behavior in e-commerce: AI anchors versus human anchors [in Chinese]. *Journal of Management Science* (4): 30-43.

[49] Li S and Yang Z (2025) Detecting AI-generated fake reviews in e-commerce based on BERT-BiLSTM-GAT [in Chinese]. *Chinese Journal of Management* (3): 557-567.
