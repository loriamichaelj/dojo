# Machine Learning — Foundational Concepts

> **Claim:** A working quant/ML practitioner needs fluency in a small set of recurring
> ideas — how learning is framed, how models generalize, how they're trained, and how
> they're evaluated. Everything else is a specialization of these. This is a living map,
> not a textbook.

**Pairs with:** [`../math/`](../math/) (linear algebra, calculus, probability,
optimization) and [`../quantitative-analysis/`](../quantitative-analysis/) (validation
discipline, overfitting, multiple-testing).

---

## 1. What "learning" means

- **Definition (Mitchell):** a program learns from experience $E$ w.r.t. task $T$ and
  performance measure $P$ if its performance at $T$, measured by $P$, improves with $E$.
- **The core assumption:** training and deployment data are drawn (roughly) from the same
  distribution. When this breaks — *distribution shift* — models silently degrade. In
  markets this is the norm, not the exception (regime change).
- **Learning ≈ function approximation + generalization.** Fitting the training data is
  trivial; generalizing to unseen data is the whole game.

### Paradigms

| Paradigm | Signal | Typical tasks |
|---|---|---|
| **Supervised** | labeled $(x, y)$ pairs | regression, classification |
| **Unsupervised** | structure in $x$ alone | clustering, dimensionality reduction, density estimation |
| **Self-supervised** | labels derived from data itself | pretraining (LLMs, embeddings) |
| **Reinforcement** | scalar reward from interaction | sequential decision-making, control, execution |
| **Semi-/weakly-supervised** | few labels + much unlabeled | label-scarce domains |

---

## 2. Supervised learning — the spine

### Problem setup

- Inputs $x \in \mathbb{R}^d$ (features), target $y$. Learn $f_\theta: x \mapsto \hat{y}$.
- **Regression:** $y$ continuous. **Classification:** $y$ categorical (output class
  probabilities, not just labels).
- Choose a **hypothesis class** (linear models, trees, neural nets), a **loss**, and an
  **optimizer**. These three choices define almost everything.

### Loss functions

- **MSE** $\frac{1}{n}\sum (y_i - \hat{y}_i)^2$ — regression; penalizes large errors,
  sensitive to outliers.
- **MAE / Huber** — robust regression alternatives.
- **Cross-entropy** $-\sum_i y_i \log \hat{p}_i$ — classification; pairs with softmax.
- **Loss is a modeling choice**, not a detail: it encodes what errors you care about.

### Workhorse models (know the trade-offs, not just the API)

- **Linear / logistic regression** — interpretable, fast, strong baseline, assumes
  linearity. Regularize (L1/L2).
- **Decision trees → random forests → gradient boosting (XGBoost/LightGBM)** — handle
  nonlinearity and interactions, minimal preprocessing, dominate tabular data.
- **SVMs** — margin maximization, kernels for nonlinearity.
- **k-NN** — lazy, distance-based; suffers in high dimensions.
- **Neural networks** — universal approximators; shine on unstructured data (text, images,
  audio), usually overkill for small tabular sets.

---

## 3. The bias–variance trade-off (the central tension)

Expected test error decomposes as

$$\text{Error} = \underbrace{\text{Bias}^2}_{\text{too-simple}} + \underbrace{\text{Variance}}_{\text{too-flexible}} + \underbrace{\sigma^2}_{\text{irreducible}}$$

- **High bias = underfitting:** model too simple, misses signal. Train and test error both
  high.
- **High variance = overfitting:** model memorizes noise. Train error low, test error
  high.
- **Capacity controls** move you along this curve: model complexity, regularization,
  data size, training time.
- **Quant relevance:** with low signal-to-noise (markets), variance is the enemy. Prefer
  simpler models, strong regularization, and brutal validation.

---

## 4. Generalization & regularization

- **Regularization** = anything that constrains capacity to improve test performance:
  - **L2 (ridge):** shrinks weights, handles collinearity.
  - **L1 (lasso):** drives weights to zero → feature selection / sparsity.
  - **Elastic net:** L1 + L2.
  - **Early stopping, dropout, data augmentation, weight decay** (NN-specific).
- **Curse of dimensionality:** as $d$ grows, data sparsity explodes; distances become
  meaningless. More features ≠ better — often worse.
- **Occam's razor, operationalized:** among models that fit comparably, prefer the simpler
  one — it usually generalizes better.

---

## 5. Model evaluation (where most mistakes happen)

### Splitting

- **Train / validation / test.** Train fits parameters, validation tunes
  hyperparameters, test is touched **once**. The test set is not for iterating.
- **Cross-validation (k-fold)** for stable estimates on limited data.
- **Time-series data breaks i.i.d. CV:** use **walk-forward / purged** splits. Random
  shuffling leaks the future into the past. (See
  [`../quantitative-analysis/`](../quantitative-analysis/).)

### Leakage — the silent killer

- **Data leakage:** information from the target or the future sneaks into features
  (e.g. scaling using full-dataset statistics, look-ahead features). Produces beautiful
  backtests that die live. Fit all preprocessing **inside** the training fold only.

### Metrics (match the metric to the cost)

- **Regression:** RMSE, MAE, $R^2$.
- **Classification:** accuracy is misleading under class imbalance. Use
  **precision / recall / F1**, the **confusion matrix**, **ROC-AUC** and **PR-AUC**.
- **Calibration:** are predicted probabilities trustworthy? Often more important than
  ranking.
- **Ranking / trading:** information coefficient, Sharpe of the resulting strategy — the
  ML metric is a proxy, the P&L is the truth.

---

## 6. Optimization — how models actually train

- **Gradient descent:** step against the gradient of the loss,
  $\theta \leftarrow \theta - \eta \nabla_\theta L$.
- **Variants:** **SGD** (minibatch, noisy but cheap), **momentum**, **RMSProp**,
  **Adam** (adaptive, default for deep nets).
- **Learning rate** is the single most important hyperparameter — too high diverges, too
  low crawls. Use schedules / warmup.
- **Backpropagation** = the chain rule applied efficiently to compute gradients through a
  computational graph. Understand it conceptually even if frameworks autodiff for you.
- **Convex vs non-convex:** linear/logistic losses are convex (one optimum); neural nets
  are non-convex (many local minima, but SGD finds good ones in practice).

---

## 7. Features & data

- **"Garbage in, garbage out" dominates model choice.** Feature engineering usually beats
  model tweaking, especially on tabular/financial data.
- **Standardization / normalization:** scale-sensitive models (SVM, k-NN, NN,
  regularized linear) need it; tree ensembles don't.
- **Categorical encoding:** one-hot, target/mean encoding (watch leakage), embeddings.
- **Missing data:** imputation vs. explicit "missing" indicators — missingness is often
  itself a signal.
- **Class imbalance:** resampling, class weights, threshold tuning — not just accuracy.

---

## 8. Deep learning — when and why

- **When:** large datasets, unstructured inputs (images, text, audio, sequences), where
  hand-crafted features fail. Less compelling for small, noisy tabular problems.
- **Building blocks:** layers (linear + nonlinearity), activations (ReLU, GELU, sigmoid,
  tanh), depth = composition of representations.
- **Architectures to recognize:**
  - **MLP** — generic tabular/dense.
  - **CNN** — spatial/local structure (images, some time-series).
  - **RNN / LSTM** — sequences (largely superseded by attention).
  - **Transformers / attention** — the dominant architecture; powers LLMs, increasingly
    everything else.
- **Why they generalize despite huge capacity** is still an active research question
  (implicit regularization of SGD, overparameterization) — hold this knowledge loosely.

---

## 9. Unsupervised & representation learning

- **Clustering:** k-means, hierarchical, DBSCAN — group without labels (regime detection,
  segmentation).
- **Dimensionality reduction:** **PCA** (linear, variance-maximizing), **t-SNE / UMAP**
  (nonlinear, for visualization only — don't feed coordinates downstream naively).
- **Embeddings:** dense vector representations that put "similar" items close together;
  the bridge from raw data to ML-ready features.

---

## 10. Reinforcement learning (the decision-making frame)

- **Setup:** agent ↔ environment, states $s$, actions $a$, reward $r$, policy $\pi$.
  Maximize expected cumulative (discounted) reward.
- **Concepts:** value functions, $Q$-learning, policy gradients,
  **exploration vs. exploitation**, credit assignment.
- **Quant relevance:** execution, market-making, dynamic hedging, portfolio
  rebalancing — but RL is data-hungry and unstable; treat with skepticism on noisy
  financial rewards.

---

## 11. Practical workflow & pitfalls

1. **Start with a baseline** (mean predictor, linear model). If you can't beat it, stop.
2. **Establish the validation scheme before modeling** — especially the time-series split.
3. **Iterate on the validation set; lock the test set away.**
4. **Diagnose with learning curves** (train vs. val error) to tell bias from variance.
5. **Reproducibility:** fix seeds, version data + code, log experiments.

**Recurring failure modes:**
- Overfitting to the validation set via too many trials (**multiple-testing** — correct
  for it).
- Leakage from preprocessing, look-ahead features, or improper CV.
- Optimizing a metric that isn't the real objective.
- Chasing complex models when the data is small and noisy.
- Ignoring distribution shift between backtest and live.

---

## 12. The honest meta-lesson

> ML is a force multiplier for signal, and an equally efficient amplifier of noise and
> bias. In high-SNR domains it wins decisively; in markets it mostly **fails gracefully if
> you are disciplined and fails expensively if you are not.** The skill that matters is
> not fitting models — frameworks do that — but knowing *whether the result is real.*

**See:** the cross-cutting question in [`../README.md`](../README.md) — *when does ML beat
a well-specified statistical model, and when does it just overfit?*

---

### Next threads to spin out

- `bias-variance-experiments.py` — empirical decomposition on synthetic data.
- `validation-leakage-demo.py` — how naive CV inflates a financial backtest.
- `gradient-descent-from-scratch.py` — implement SGD/Adam to internalize the optimizer.
- `tree-ensembles-vs-linear.md` — when boosting actually beats a regularized baseline.
