---
name: curriculum-index-ds
plan: setu
plan_version: "v2.3.0"
generated: "2026-08-21"
verified: "2026-08-30"
days: 240
---

# 📇 Curriculum index — Project Setu, Days 1–240

Generated from `docs/00_MASTER_PLAN_DS_GENAI.md` Part 4 (matrices) ↔ Part 5 (phase map).
Every ID in the matrices appears in ≥1 day. Every day cites ≥1 ID **except** the five days
that build the project rather than teach a curriculum topic: Days 1–3 (the foundry) and Days
239–240 (portfolio and retrospective), which carry `—`.

`./m depth` checks this file against the plan on every full sweep — the phase day-ranges, the
ID coverage and the `plan_version` stamp above. `generated:` is when the rows were written;
`verified:` is when they were last checked against the plan and agreed. v2.0.0–v2.3.0 changed
document architecture and prose rules, not the day map, which is why rows generated under
v1.0.0 still hold under v2.3.0.

**How to read the Kind column:** `lab` = you write and run code · `concept` = reading + a written
artifact, no new code · `project` = a multi-day-scale deliverable in one day · `gate` = the phase's
definition-of-done artifact.

**Run a day:** `./m start N` → work through the day's `LESSON.md` → tick `CHECKLIST.md` → `./m done N`.

---

## Phase 0 · Foundry · Days 1–3

| Day | Title | IDs | Kind |
|---|---|---|---|
| 1 | Foundry I — the repo, the environment, and pins that don't float | — | lab |
| 2 | Foundry II — the quality machine: ruff, pytest, `./m`, CI | — | lab |
| 3 | Foundry III — three free keys, two free databases, one rate budget | — | gate |

## Phase 1 · Python foundations (Module 1) · Days 4–11

| Day | Title | IDs | Kind |
|---|---|---|---|
| 4 | Objects, types, and mutability | PY-01, PY-02 | lab |
| 5 | Operators, precedence, and conditionals | PY-03, PY-04 | lab |
| 6 | Loops, `break`/`continue`, and the capped retry | PY-05 | lab |
| 7 | Strings: methods, split/join, f-string formatting | PY-06 | lab |
| 8 | Lists, tuples, sets, dictionaries, and view objects | PY-07, PY-08 | lab |
| 9 | List and dict comprehensions | PY-09 | lab |
| 10 | Functions, scope, and your first `src/setu/` module | PY-10 | lab |
| 11 | Iterators, generators, lambda and `map` | PY-11, PY-12 | gate |

## Phase 2 · Advanced Python (Module 2) · Days 12–19

| Day | Title | IDs | Kind |
|---|---|---|---|
| 12 | Classes — building the `Paper` object | PY-13 | lab |
| 13 | Inheritance, polymorphism, encapsulation, abstraction | PY-14, PY-15 | lab |
| 14 | Decorators — `@timed` and `@retry` | PY-16 | lab |
| 15 | `classmethod`, `staticmethod`, `property`, and dunder methods | PY-17, PY-18 | lab |
| 16 | Files, `pathlib`, buffering, and context managers | PY-19, PY-20 | lab |
| 17 | Modules, packages, imports, `__init__.py` | PY-21 | lab |
| 18 | Exceptions and custom error types | PY-22 | lab |
| 19 | Typing, dataclasses, Pydantic v2, and concurrency | PY-23, PY-24 | gate |

## Phase 3 · NumPy (Module 3) · Days 20–25

| Day | Title | IDs | Kind |
|---|---|---|---|
| 20 | `ndarray`, dtypes, and array creation (NumPy 2.x names) | NP-01, NP-02 | lab |
| 21 | Indexing, slicing, boolean masks — and the view trap | NP-03 | lab |
| 22 | Broadcasting and array manipulation | NP-04, NP-05 | lab |
| 23 | Universal functions, statistics, and `argsort` top-k | NP-06, NP-07 | lab |
| 24 | Binary/string functions and linear algebra | NP-08, NP-09 | lab |
| 25 | Copy vs view — and a vectorised stats module | NP-10 | gate |

## Phase 4 · Pandas 3.0 (Module 4) · Days 26–35

| Day | Title | IDs | Kind |
|---|---|---|---|
| 26 | pandas 3.0 — Copy-on-Write, `str` dtype, and the chained-assignment trap | PD-01 | lab |
| 27 | Reading and writing: CSV, JSON, Parquet, SQL — typed at read time | PD-02 | lab |
| 28 | `loc`, `iloc`, boolean masks, reindexing and alignment | PD-03, PD-04 | lab |
| 29 | Iteration vs vectorisation; sorting and ranking | PD-05, PD-06 | lab |
| 30 | Missing data — and why the imputer lives in the pipeline | PD-07 | lab |
| 31 | `groupby`: split–apply–combine, `agg` and `transform` | PD-08 | lab |
| 32 | Merge, join, concat, pivot, melt | PD-09, PD-10 | lab |
| 33 | The `.str` and `.dt` accessors; resampling | PD-11, PD-12 | lab |
| 34 | Categorical dtype and `describe()` as a data-quality report | PD-13, PD-14 | lab |
| 35 | Where pandas stops — Polars and DuckDB, benchmarked | PD-15 | gate |

## Phase 5 · Visualisation (Module 5) · Days 36–41

| Day | Title | IDs | Kind |
|---|---|---|---|
| 36 | Matplotlib — figure, axes, and the object API | VIZ-01 | lab |
| 37 | Customising charts; choosing the right chart type | VIZ-02, VIZ-03 | lab |
| 38 | Seaborn — statistical plots and faceting | VIZ-04 | lab |
| 39 | Distributions and relationships; the correlation heatmap | VIZ-05, VIZ-06 | lab |
| 40 | Styling, palettes, and colour-blind-safe defaults | VIZ-07 | lab |
| 41 | Plotly — when interactivity earns its weight | VIZ-08 | gate |

## Phase 6 · SQL & NoSQL (Module 6) · Days 42–51

| Day | Title | IDs | Kind |
|---|---|---|---|
| 42 | Relational thinking; Supabase Postgres from Python | DB-01, DB-02 | lab |
| 43 | `SELECT`, `WHERE`, `ORDER BY`, `GROUP BY`, `HAVING` | DB-03 | lab |
| 44 | Primary keys, foreign keys, constraints | DB-04 | lab |
| 45 | Joins and unions — the same question in SQL and pandas | DB-05 | lab |
| 46 | Subqueries, CTEs, and window functions | DB-06 | lab |
| 47 | Parameterised queries and SQLAlchemy Core | DB-07 | lab |
| 48 | MongoDB Atlas — documents, collections, and when they beat rows | DB-08 | lab |
| 49 | CRUD: insert, find, query operators, sort, projection | DB-09 | lab |
| 50 | Updates, deletes, indexes, and the aggregation pipeline | DB-10, DB-11 | lab |
| 51 | SQL vs NoSQL — **ADR-004** | DB-12 | gate |

## Phase 7 · Streamlit (Module 7) · Days 52–57

| Day | Title | IDs | Kind |
|---|---|---|---|
| 52 | Streamlit's execution model — why your counter resets | APP-01 | lab |
| 53 | Widgets, forms, and layout | APP-02, APP-03 | lab |
| 54 | `st.session_state` and multi-step flows | APP-04 | lab |
| 55 | Caching, charts, and dataframes | APP-05, APP-06 | lab |
| 56 | Async, generators, and `st.write_stream` | APP-07 | lab |
| 57 | Deploy to Streamlit Community Cloud; secrets handling | APP-08 | gate |

## Phase 8 · Statistics foundations (Module 8) · Days 58–68

| Day | Title | IDs | Kind |
|---|---|---|---|
| 58 | Descriptive vs inferential; levels of measurement | ST-01, ST-02 | lab |
| 59 | Central tendency — mean, median, mode | ST-03 | lab |
| 60 | Dispersion — range, variance, std, IQR, and `ddof` | ST-04 | lab |
| 61 | Skewness and kurtosis | ST-05 | lab |
| 62 | Covariance and correlation — Anscombe's quartet | ST-06 | lab |
| 63 | Sets, random variables, probability, conditional probability | ST-07, ST-08 | lab |
| 64 | PMF, PDF, CDF | ST-09 | lab |
| 65 | Bernoulli, binomial, Poisson, uniform | ST-10, ST-11 | lab |
| 66 | The normal distribution, z-scores, standardisation | ST-12, ST-13 | lab |
| 67 | The Central Limit Theorem — simulated, not asserted | ST-14 | lab |
| 68 | Estimation, standard error, and a bootstrap CI from scratch | ST-15 | gate |

## Phase 9 · Inferential statistics (Module 9) · Days 69–75

| Day | Title | IDs | Kind |
|---|---|---|---|
| 69 | Hypothesis testing — the mechanism, step by step | ST-16 | lab |
| 70 | p-values, significance, Type I/II error, power | ST-17 | lab |
| 71 | t-tests and ANOVA | ST-18 | lab |
| 72 | Bayes' theorem and Bayesian updating | ST-19 | lab |
| 73 | Chi-square: distribution, goodness-of-fit, independence | ST-20 | lab |
| 74 | Multiple comparisons and p-hacking, demonstrated | ST-21 | lab |
| 75 | A statistical report you would defend — **ADR-005** | ST-22 | gate |

## Phase 10 · Feature engineering (Module 10) · Days 76–83

| Day | Title | IDs | Kind |
|---|---|---|---|
| 76 | Missing data mechanisms and imputation strategies | FE-01 | lab |
| 77 | Outlier detection — IQR, z-score, isolation forest | FE-02 | lab |
| 78 | Imbalanced data — resampling, SMOTE, class weights, thresholds | FE-03 | lab |
| 79 | **The split, first** — train/val/test, stratified, grouped | FE-04 | lab |
| 80 | Scaling — standard, min-max, robust | FE-05 | lab |
| 81 | Encoding — one-hot, ordinal, target encoding and its leak | FE-06 | lab |
| 82 | Feature construction — interactions, binning, dates, transforms | FE-07 | lab |
| 83 | Feature selection and the `ColumnTransformer` pipeline | FE-08, FE-09 | gate |

## Phase 11 · EDA (Module 11) · Days 84–90

| Day | Title | IDs | Kind |
|---|---|---|---|
| 84 | The EDA loop and an automated `audit(df)` | EDA-01, EDA-02 | lab |
| 85 | Univariate and bivariate exploration | EDA-03 | lab |
| 86 | Multivariate structure; PCA for looking, not modelling | EDA-04 | lab |
| 87 | Case study — sentiment of movie reviews | EDA-05 | project |
| 88 | Case study — wine quality and type | EDA-06 | project |
| 89 | Case study — stock and commodity prices (and the forecasting trap) | EDA-07 | project |
| 90 | An EDA report that changes a decision — **ADR-006** | EDA-08 | gate |

## Phase 12 · Machine learning fundamentals (Module 12) · Days 91–106

| Day | Title | IDs | Kind |
|---|---|---|---|
| 91 | AI vs ML vs DL vs Data Science; the four learning types | ML-01, ML-02 | concept |
| 92 | Simple linear regression **from scratch** | ML-03 | lab |
| 93 | Multiple linear regression, assumptions, multicollinearity | ML-04 | lab |
| 94 | Regression metrics — MSE, MAE, RMSE, R², adjusted R² | ML-05 | lab |
| 95 | Gradient descent **from scratch** — batch, stochastic, mini-batch | ML-06 | lab |
| 96 | Bias–variance, over/underfitting, learning curves | ML-07 | lab |
| 97 | Cross-validation — k-fold, stratified, grouped, time-series | ML-08 | lab |
| 98 | Regularisation — Ridge, Lasso, ElasticNet | ML-09 | lab |
| 99 | Logistic regression **from scratch** | ML-10 | lab |
| 100 | Confusion matrix; picking the metric from the cost of the error | ML-11 | lab |
| 101 | ROC-AUC, PR-AUC, calibration, threshold tuning | ML-12 | lab |
| 102 | Naive Bayes — Bayes' theorem, made concrete | ML-13 | lab |
| 103 | KNN and the curse of dimensionality | ML-14 | lab |
| 104 | Support Vector Machines and the kernel trick | ML-15 | lab |
| 105 | Decision trees — entropy, Gini, pruning | ML-16 | lab |
| 106 | Hyperparameter search — grid, random, Optuna — **ADR-007** | ML-17 | gate |

## Phase 13 · Ensembles & clustering (Module 13) · Days 107–116

| Day | Title | IDs | Kind |
|---|---|---|---|
| 107 | Why averaging works — the bias/variance view of ensembles | ML-18 | lab |
| 108 | Bagging and Random Forest | ML-19 | lab |
| 109 | Out-of-bag evaluation and honest feature importance | ML-20 | lab |
| 110 | Boosting intuition — AdaBoost to gradient boosting, by hand | ML-21 | lab |
| 111 | Gradient Boosting classifier and regressor | ML-22 | lab |
| 112 | XGBoost — early stopping and the hyperparameters that matter | ML-23 | lab |
| 113 | LightGBM and CatBoost — the honest comparison | ML-24 | lab |
| 114 | SHAP — what the model actually keys on — **ADR-008** | ML-25 | lab |
| 115 | Clustering, distance metrics, and K-Means from scratch | ML-26, ML-27, ML-28 | lab |
| 116 | MLflow + **Project: Network Intrusion Detection System** | ML-29, ML-30 | gate |

## Phase 14 · Classical NLP (Module 14) · Days 117–124

| Day | Title | IDs | Kind |
|---|---|---|---|
| 117 | What NLP is; normalisation and tokenisation | NLP-01, NLP-02 | lab |
| 118 | Stemming, lemmatisation, and when stopwords carry meaning | NLP-03, NLP-04 | lab |
| 119 | Parts-of-speech tagging with NLTK and spaCy | NLP-05 | lab |
| 120 | Named Entity Recognition | NLP-06 | lab |
| 121 | One-hot, Bag of Words, and n-grams | NLP-07, NLP-08 | lab |
| 122 | TF-IDF **from scratch**, then `TfidfVectorizer` | NLP-09 | lab |
| 123 | Word vectors, cosine similarity, and Word2Vec | NLP-10, NLP-11 | lab |
| 124 | **Project: TF-IDF text classifier** — the baseline to beat | NLP-12 | gate |

## Phase 15 · Deep learning foundations (Module 15) · Days 125–137

| Day | Title | IDs | Kind |
|---|---|---|---|
| 125 | Why deep learning now; the perceptron by hand | DL-01, DL-02 | lab |
| 126 | Forward propagation **is** matrix multiplication | DL-03 | lab |
| 127 | The chain rule and backpropagation, derived on paper | DL-04 | lab |
| 128 | A full training loop in pure NumPy | DL-05 | lab |
| 129 | Activation functions and the vanishing gradient, reproduced | DL-06, DL-07 | lab |
| 130 | Loss functions — MSE, MAE, BCE, categorical cross-entropy | DL-08 | lab |
| 131 | Optimisers — SGD → Momentum → RMSProp → Adam → AdamW | DL-09 | lab |
| 132 | Weight initialisation — Xavier and He | DL-10 | lab |
| 133 | Dropout, batch normalisation, layer normalisation | DL-11, DL-12 | lab |
| 134 | Keras 3 — Sequential, functional API, callbacks | DL-13 | lab |
| 135 | PyTorch — tensors, autograd, `nn.Module`, the explicit loop | DL-14 | lab |
| 136 | `Dataset`, `DataLoader`, batching, and your hardware reality | DL-15 | lab |
| 137 | TensorBoard and reading a training curve honestly | DL-16 | gate |

## Phase 16 · Sequence models & transformers (Module 16) · Days 138–149

| Day | Title | IDs | Kind |
|---|---|---|---|
| 138 | Sequence data; why MLPs fail on it; RNNs and BPTT | DL-17, DL-18 | lab |
| 139 | LSTM — the three gates and the cell state | DL-19 | lab |
| 140 | GRU; bidirectional and stacked recurrent layers | DL-20, DL-21 | lab |
| 141 | Seq2seq encoder–decoder and the bottleneck problem | DL-22 | lab |
| 142 | Attention — intuition, then the maths, then the plot | DL-23 | lab |
| 143 | **Self-attention and multi-head attention, from scratch** | DL-24 | lab |
| 144 | Positional encoding | DL-25 | lab |
| 145 | The transformer block; encoder-only vs decoder-only vs enc-dec | DL-26 | lab |
| 146 | BERT — masked LM, `[CLS]`, fine-tuning | DL-27 | lab |
| 147 | GPT-family — causal LM, sampling parameters | DL-28 | lab |
| 148 | Tokenisation for LLMs — BPE, WordPiece, `tiktoken` | DL-29 | lab |
| 149 | **Projects: summarisation · translation · question answering** | DL-30 | gate |

## Phase 17 · Generative AI foundations (Module 17) · Days 150–154

| Day | Title | IDs | Kind |
|---|---|---|---|
| 150 | What generative AI is; generative vs discriminative | GEN-01, GEN-02 | lab |
| 151 | Next-token prediction, end to end, from your own model | GEN-03 | lab |
| 152 | The landscape — LLMs, diffusion, multimodal — and the limits | GEN-04 | concept |
| 153 | Prompting as interface design; hallucination and grounding | GEN-05, GEN-06 | lab |
| 154 | The end-to-end GenAI project lifecycle — **ADR-009** | GEN-07 | gate |

## Phase 18 · Vector databases (Module 18) · Days 155–161

| Day | Title | IDs | Kind |
|---|---|---|---|
| 155 | Local embeddings and similarity search **from scratch** | VDB-01, VDB-02 | lab |
| 156 | Why a vector DB; HNSW and IVF; the recall/latency trade | VDB-03, VDB-04 | lab |
| 157 | Storage and index types — in-memory, on-disk, cloud | VDB-05 | lab |
| 158 | Chroma — collections, metadata, filtering | VDB-06 | lab |
| 159 | FAISS — flat vs IVF vs HNSW, benchmarked | VDB-07 | lab |
| 160 | Qdrant and LanceDB; Pinecone literacy | VDB-08, VDB-09 | lab |
| 161 | Atlas Vector Search; choosing a store — **ADR-010** | VDB-10, VDB-11 | gate |

## Phase 19 · RAG (Module 19) · Days 162–171

| Day | Title | IDs | Kind |
|---|---|---|---|
| 162 | The RAG pipeline drawn, then built **naked** in 60 lines | RAG-01, RAG-02 | lab |
| 163 | Loading and parsing real documents — PDF, HTML, tables | RAG-03 | lab |
| 164 | Chunking strategies, measured against retrieval hit-rate | RAG-04 | lab |
| 165 | Embedding choice and the chunk-size ↔ context interaction | RAG-05 | lab |
| 166 | Retrieval — top-k, MMR, metadata filters, self-query | RAG-06 | lab |
| 167 | Hybrid search (BM25 + dense) and cross-encoder reranking | RAG-07, RAG-08 | lab |
| 168 | Prompt assembly, citation, and refusing to answer | RAG-09 | lab |
| 169 | RAG evaluation with Ragas | RAG-10 | lab |
| 170 | Conversational memory and multimodal RAG | RAG-11, RAG-12 | lab |
| 171 | **Project: RAG Q&A system with a CI eval gate** | RAG-13 | gate |

## Phase 20 · LangChain (Module 20) · Days 172–181

| Day | Title | IDs | Kind |
|---|---|---|---|
| 172 | LangChain 1.x mental model + the free-provider fallback router | LC-01, LC-02 | lab |
| 173 | Messages, standard content blocks, prompt templates, few-shot | LC-03, LC-04 | lab |
| 174 | LCEL and `Runnable` — invoke, batch, stream, compose | LC-05 | lab |
| 175 | Structured output with `with_structured_output` | LC-06 | lab |
| 176 | Tools, schemas, runtime injection, toolkits | LC-07, LC-08 | lab |
| 177 | Loaders, splitters, and vector-store integrations | LC-09 | lab |
| 178 | Memory and message-history management | LC-10 | lab |
| 179 | `create_agent` and middleware | LC-11, LC-12 | lab |
| 180 | Synthetic data generation for eval sets | LC-13 | lab |
| 181 | LangSmith tracing and datasets; LangServe literacy | LC-14, LC-15 | gate |

## Phase 21 · Agentic AI concepts (Module 21) · Days 182–184

| Day | Title | IDs | Kind |
|---|---|---|---|
| 182 | What an AI agent is — the think → act → observe loop | AGT-01, AGT-02 | concept |
| 183 | Agentic vs generative AI; multi-agent collaboration topologies | AGT-03, AGT-04 | concept |
| 184 | The framework landscape; Setu's permission table — **ADR-011** | AGT-05, AGT-06 | gate |

## Phase 22 · LangGraph fundamentals (Module 22) · Days 185–191

| Day | Title | IDs | Kind |
|---|---|---|---|
| 185 | Graph thinking — state, nodes, edges, drawn before coded | LG-01 | lab |
| 186 | Your first `StateGraph`; LangGraph Studio | LG-02 | lab |
| 187 | Chains as graphs — sequential composition | LG-03 | lab |
| 188 | Routers and conditional edges | LG-04 | lab |
| 189 | Agents in LangGraph — the ReAct loop as a graph | LG-05 | lab |
| 190 | Agents with memory | LG-06 | lab |
| 191 | `langgraph dev` and execution basics | LG-07 | gate |

## Phase 23 · State & memory (Module 23) · Days 192–196

| Day | Title | IDs | Kind |
|---|---|---|---|
| 192 | State schemas — `TypedDict`, Pydantic state, annotations | LG-08 | lab |
| 193 | Reducers — how state updates merge | LG-09 | lab |
| 194 | Multiple schemas — input, output, and private state | LG-10 | lab |
| 195 | Checkpointers and threads — persistence as a runtime property | LG-11 | lab |
| 196 | Trimming and filtering messages; context budgeting | LG-12 | gate |

## Phase 24 · HITL & UX (Module 24) · Days 197–201

| Day | Title | IDs | Kind |
|---|---|---|---|
| 197 | Streaming modes — values, updates, messages | LG-13 | lab |
| 198 | Breakpoints — static and dynamic | LG-14 | lab |
| 199 | `interrupt()` — human-in-the-loop as a **durable** pause | LG-15 | lab |
| 200 | Editing state with human input — approve, edit, reject | LG-16 | lab |
| 201 | Time travel, forking, subgraphs, and the review UI | LG-17, LG-18 | gate |

## Phase 25 · Agentic RAG (Module 25) · Days 202–208

| Day | Title | IDs | Kind |
|---|---|---|---|
| 202 | Adaptive RAG — routing by query type | RAG-14 | lab |
| 203 | Adaptive RAG, running fully locally | RAG-15 | lab |
| 204 | Agentic RAG — retrieval as a tool the agent may decline | RAG-16 | lab |
| 205 | C-RAG — grade retrieved documents, re-query on failure | RAG-17 | lab |
| 206 | Self-RAG — reflection and self-critique loops | RAG-18 | lab |
| 207 | Self-RAG over a vector DB, deployed locally | RAG-19 | lab |
| 208 | Four-architecture bake-off on one eval set — **ADR-013** | RAG-20 | gate |

## Phase 26 · Model Context Protocol (Module 26) · Days 209–215

| Day | Title | IDs | Kind |
|---|---|---|---|
| 209 | Why MCP — the N×M problem; core components and architecture | MCP-01, MCP-02 | lab |
| 210 | Tools, resources, prompts; the request lifecycle | MCP-03, MCP-04 | lab |
| 211 | **Build Setu's `paper-db` MCP server** | MCP-05 | lab |
| 212 | Integrating with Claude Desktop and Cursor IDE | MCP-06 | lab |
| 213 | Consuming MCP servers from LangChain and LangGraph | MCP-07 | lab |
| 214 | Open MCP registries, the Docker catalog, and a security review | MCP-08, MCP-09 | lab |
| 215 | Auth; agent-as-MCP-server; the freshness drill — **ADR-012** | MCP-10, MCP-11, MCP-12 | gate |

## Phase 27 · Multi-agent systems (Module 27) · Days 216–224

| Day | Title | IDs | Kind |
|---|---|---|---|
| 216 | Designing five non-overlapping agents and their contracts | MAS-01, MAS-02 | lab |
| 217 | Shared state and typed inter-agent messages | MAS-03 | lab |
| 218 | Memory across agents — thread, long-term, entity | MAS-04 | lab |
| 219 | Multi-turn collaboration prompting; human feedback checkpoints | MAS-05, MAS-06 | lab |
| 220 | Tooling — arXiv API, web search, PDF parsers (politely) | MAS-07 | lab |
| 221 | Wiring the LangGraph-structured multi-agent workflow | MAS-08 | lab |
| 222 | Adding RAG as the shared knowledge layer | MAS-09 | lab |
| 223 | Failure modes — loops, deadlock, contradiction, runaway cost | MAS-10 | lab |
| 224 | FastAPI backend and the Streamlit logs/graph/report UI | MAS-11, MAS-12 | gate |

## Phase 28 · 🏁 Capstone — Project Setu · Days 225–238

Full specification: `docs/CAPSTONE_SETU.md`

| Day | Title | IDs | Kind |
|---|---|---|---|
| 225 | Architecture on one page — **ADR-014** | CAP-01 | lab |
| 226 | The data layer — Postgres schema, Mongo collections, Chroma index | CAP-02 | lab |
| 227 | Ingestion — the review-scraper project, generalised | CAP-03 | project |
| 228 | The hardened `paper-db` MCP server | CAP-04 | lab |
| 229 | Search and Reader agents | CAP-05 | lab |
| 230 | Analyst agent — real statistics and a real trained model | CAP-06 | lab |
| 231 | Generator agent and citation discipline | CAP-07 | lab |
| 232 | Coordinator graph — durable checkpoints and interrupts | CAP-08 | lab |
| 233 | The eval suite — unit, retrieval, trajectory, outcome | CAP-09 | lab |
| 234 | FastAPI service and the Streamlit review UI | CAP-10 | lab |
| 235 | CI/CD with GitHub Actions and the eval gate | CAP-11 | lab |
| 236 | Docker Compose; AWS EC2 deployment (optional) | CAP-12 | lab |
| 237 | Graduated autonomy review; observability and cost dashboard | CAP-13 | lab |
| 238 | End-to-end demo on 20 unseen questions | CAP-14 | gate |

## Phase 29 · Portfolio & handoff · Days 239–240

| Day | Title | IDs | Kind |
|---|---|---|---|
| 239 | README-as-portfolio, architecture diagram, demo video, interview Q&A | — | lab |
| 240 | Retrospective; schedule the standing freshness check; write the addendum | — | gate |

---

## Decision records produced by this plan

| ADR | Day | Question it answers |
|---|---|---|
| ADR-001 | 25 | Where does a NumPy view bite, and what is our house rule? |
| ADR-002 | 35 | pandas, Polars or DuckDB for Setu's data layer? |
| ADR-003 | 57 | What belongs in a Streamlit app and what belongs behind an API? |
| ADR-004 | 51 | Postgres, MongoDB, or both — and why both is not a cop-out |
| ADR-005 | 75 | A statistical claim, its assumptions, and its error bar |
| ADR-006 | 90 | What the EDA found, and which modelling decision it changed |
| ADR-007 | 106 | Which model ships, and the honest estimate of how it performs |
| ADR-008 | 114 | What SHAP says the model keys on, and whether we believe it |
| ADR-009 | 154 | The GenAI project lifecycle for Setu — and where guardrails sit |
| ADR-010 | 161 | Which vector store, and what would make us switch |
| ADR-011 | 184 | The permission table: what each agent may read, call, and write |
| ADR-012 | 215 | Why every Setu data source sits behind MCP |
| ADR-013 | 208 | Which RAG architecture wins on our eval set, and by how much |
| ADR-014 | 225 | The capstone architecture, defended end to end |

## Standing weekly items

| Cadence | Item |
|---|---|
| Every Friday | Freshness check — release notes for every pin + the MCP spec page (Principle 13) |
| Every phase gate | Regenerate `TRACEABILITY_DS.md`; confirm every ID in the phase has a committed demo |
| Every model-touching day | Print the request count; log it against `RATE_BUDGET_DS.md` |
