# -*- coding: utf-8 -*-
"""Rewrite the References section into SAGE Vancouver style (JIS requirement).

SAGE Vancouver (per the official SAGE Vancouver reference style PDF):
  - reference numbers carry a full point in the list (1. 2. ...);
  - journal article: Author AA, Author BB and Author CC. Title. Journal Name
    Year; Volume(Issue): Pages.  (journal name ITALIC, sentence-case title);
  - list at most three authors, then "et al.";
  - book: Author AA. Title. Edition. Place: Publisher, Year.  (title ITALIC)
  - online-first: ... Journal Name. Epub ahead of print Year. DOI: ...
  - non-English articles: translate the title into English and mark the
    language at the end, e.g. [in Chinese]; the journal name is given in its
    English form.
Page ranges use an en dash. Italic is marked with *asterisks* for the docx
builder.
"""
from pathlib import Path

PATH = Path("manuscript_JIS_draft.md")
txt = PATH.read_text(encoding="utf-8")

REFS = """## References

1. Dwivedi YK, Kshetri N, Hughes L, et al. 'So what if ChatGPT wrote it?' Multidisciplinary perspectives on opportunities, challenges and implications of generative conversational AI for research, practice and policy. *International Journal of Information Management* 2023; 71: 102642.

2. Huang MH and Rust RT. A strategic framework for artificial intelligence in marketing. *Journal of the Academy of Marketing Science* 2021; 49(1): 30–50.

3. Cheng X, Bao Y, Zarifis A, et al. Exploring consumers' response to text-based chatbots in e-commerce: the moderating role of task complexity and chatbot disclosure. *Internet Research* 2021; 32(2): 496–517.

4. Chen H, Shao B, Yang X, et al. Avatars in live streaming commerce: the influence of anthropomorphism on consumers' willingness to accept virtual live streamers. *Computers in Human Behavior* 2024; 156: 108216.

5. Sidlauskiene J, Joye Y and Auruškevičienė V. AI-based chatbots in conversational commerce and their effects on product and price perceptions. *Electronic Markets* 2023; 33(1): 24.

6. Guan Y, Wei Q and Chen G. Deep learning based personalized recommendation with multi-view information integration. *Decision Support Systems* 2019; 118: 58–69.

7. Kuhn TS. *The Structure of Scientific Revolutions*. Chicago: University of Chicago Press, 1962.

8. Orlikowski WJ and Baroudi JJ. Studying information technology in organizations: research approaches and assumptions. *Information Systems Research* 1991; 2(1): 1–28.

9. Burrell G and Morgan G. *Sociological Paradigms and Organisational Analysis*. London: Heinemann, 1979.

10. Mingers J. Combining IS research methods: towards a pluralist methodology. *Information Systems Research* 2001; 12(3): 240–259.

11. Hevner AR, March ST, Park J, et al. Design science in information systems research. *MIS Quarterly* 2004; 28(1): 75–105.

12. Lazer D, Pentland A, Adamic L, et al. Computational social science. *Science* 2009; 323(5915): 721–723.

13. Small H. Co-citation in the scientific literature: a new measure of the relationship between two documents. *Journal of the American Society for Information Science* 1973; 24(4): 265–269.

14. van Eck NJ and Waltman L. Software survey: VOSviewer, a computer program for bibliometric mapping. *Scientometrics* 2010; 84(2): 523–538.

15. Shneider AM. Four stages of a scientific discipline; four types of scientist. *Trends in Biochemical Sciences* 2009; 34(5): 217–223.

16. Zhang C, Mao Y and Peng S. Data-driven evolution of library and information science research methods (1990-2022): a perspective based on fine-grained method entities. *Scientometrics* 2024; 129(12): 7889–7912.

17. Hao J and Zhang C. Evolution of research method usage across the academic careers of library and information science scholars. *Scientometrics*. Epub ahead of print 2026. DOI: 10.1007/s11192-026-05652-8.

18. Mirza KB, Khan A and Ahmad P. Mapping emerging research methodologies in Library and Information Science (2015-2023): a systematic review. *Journal of Information Science*. Epub ahead of print 2026. DOI: 10.1177/01655515251388623.

19. Bornmann L and Daniel HD. What do citation counts measure? A review of studies on citing behavior. *Journal of Documentation* 2008; 64(1): 45–80.

20. Tahamtan I, Safipour Afshar A and Ahamdzadeh K. Factors affecting number of citations: a comprehensive review of the literature. *Scientometrics* 2016; 107(3): 1195–1225.

21. Wang J. Citation time window choice for research impact evaluation. *Scientometrics* 2013; 94(3): 851–872.

22. Ullah A, Hayat S and Ameen K. Impact of research characteristics and methodologies used in LIS articles on citation count. *Journal of Librarianship and Information Science* 2025; 57(4): 1192–1204.

23. Donthu N, Kumar S, Mukherjee D, et al. How to conduct a bibliometric analysis: an overview and guidelines. *Journal of Business Research* 2021; 133: 285–296.

24. Priem J, Piwowar H and Orr R. OpenAlex: a fully-open index of scholarly works, authors, venues, institutions, and concepts. arXiv:2205.01833, 2022.

25. Page MJ, McKenzie JE, Bossuyt PM, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ* 2021; 372: n71.

26. Moher D, Liberati A, Tetzlaff J, et al. Preferred reporting items for systematic reviews and meta-analyses: the PRISMA statement. *PLoS Medicine* 2009; 6(7): e1000097.

27. Landis JR and Koch GG. The measurement of observer agreement for categorical data. *Biometrics* 1977; 33(1): 159–174.

28. Cohen J. A coefficient of agreement for nominal scales. *Educational and Psychological Measurement* 1960; 20(1): 37–46.

29. Krippendorff K. *Content Analysis: An Introduction to Its Methodology*. 2nd ed. Thousand Oaks, CA: SAGE, 2004.

30. Braun V and Clarke V. Using thematic analysis in psychology. *Qualitative Research in Psychology* 2006; 3(2): 77–101.

31. Mann HB. Nonparametric tests against trend. *Econometrica* 1945; 13(3): 245–259.

32. Kendall MG. *Rank Correlation Methods*. 4th ed. London: Charles Griffin, 1975.

33. Cameron AC and Trivedi PK. *Regression Analysis of Count Data*. 2nd ed. Cambridge: Cambridge University Press, 2013.

34. Hilbe JM. *Negative Binomial Regression*. 2nd ed. Cambridge: Cambridge University Press, 2011.

35. Davis FD. Perceived usefulness, perceived ease of use, and user acceptance of information technology. *MIS Quarterly* 1989; 13(3): 319–340.

36. Venkatesh V, Morris MG, Davis GB, et al. User acceptance of information technology: toward a unified view. *MIS Quarterly* 2003; 27(3): 425–478.

37. Mehrabian A and Russell JA. *An Approach to Environmental Psychology*. Cambridge, MA: MIT Press, 1974.

38. Xylogiannopoulos KF, Xanthopoulos P, Karampelas P, et al. ChatGPT paraphrased product reviews can confuse consumers and undermine their trust in genuine reviews. *Information Processing & Management* 2024; 61(6): 103842.

39. Özyirmidokuz EK, Molu Elmas B and Stoica EA. AI-based sentiment analysis of e-commerce customer feedback: a bilingual parallel study on the fast food industry. *Journal of Theoretical and Applied Electronic Commerce Research* 2025; 20(4): 294.

40. Xie Y and Desouza KC. Feeling grounded when watching live streaming shows of highly anthropomorphic interactive virtual influencers: an exploratory study on customer opinions. *Journal of Business Research* 2025; 199: 115507.

41. Chattaraman V, Kwon WS, Gilbert JE, et al. Should AI-based, conversational digital assistants employ social- or task-oriented interaction style? A task-competency and reciprocity perspective for older adults. *Computers in Human Behavior* 2018; 90: 315–330.

42. Ameen N, Tarhini A, Reppel A, et al. Customer experiences in the age of artificial intelligence. *Computers in Human Behavior* 2021; 114: 106548.

43. Castelo N, Bos MW and Lehmann DR. Task-dependent algorithm aversion. *Journal of Marketing Research* 2019; 56(5): 809–825.

44. Zupic I and Cater T. Bibliometric methods in management and organization. *Organizational Research Methods* 2015; 18(3): 429–472.

45. Snyder H. Literature review as a research methodology: an overview and guidelines. *Journal of Business Research* 2019; 104: 333–339.

46. Puntoni S, Reczek RW, Giesler M, et al. Consumers and artificial intelligence: an experiential perspective. *Journal of Marketing* 2021; 85(1): 131–151.

47. Li R, Ma B, Zhang P, et al. The mechanism by which AI anchor characteristics influence consumers' purchase intention in e-commerce: a dual perspective of technology perception and social interaction [in Chinese]. *Journal of Beijing Institute of Technology (Social Sciences Edition)* 2025; 27(1): 127–144.

48. Wang C, Xu J, Qin H, et al. The influence of anchor type on consumers' purchase behavior in e-commerce: AI anchors versus human anchors [in Chinese]. *Journal of Management Science* 2023; 36(4): 30–43.

49. Li S and Yang Z. Detecting AI-generated fake reviews in e-commerce based on BERT-BiLSTM-GAT [in Chinese]. *Chinese Journal of Management* 2025; 22(3): 557–567.
"""

idx = txt.index("## References")
head = txt[:idx].rstrip() + "\n\n"
PATH.write_text(head + REFS, encoding="utf-8")
print("References rewritten to SAGE Vancouver style with italics (49 entries)")
