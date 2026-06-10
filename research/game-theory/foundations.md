# Foundations of Game Theory

> **Claim:** Most of game theory is bookkeeping — specify *players, actions, payoffs,
> and information* precisely, and the "hard" solution concepts fall out as
> consistency conditions on rational behavior.

This is a living reference for the core vocabulary and equilibrium concepts. Later
notes (microstructure-as-a-game, auctions/MEV, repeated games) will build on it.

---

## 1. What is a game?

A **game** is a model of strategic interaction: each player's outcome depends not only
on their own choice but on the choices of others. To specify one, always pin down the
four primitives (the house rule for this folder):

| Primitive | Symbol | Meaning |
|---|---|---|
| **Players** | $N = \{1, 2, \dots, n\}$ | the decision-makers |
| **Actions** | $A_i$ | what player $i$ can do; a *profile* is $a = (a_1, \dots, a_n)$ |
| **Payoffs** | $u_i : A \to \mathbb{R}$ | $i$'s utility over outcomes |
| **Information** | — | who knows what, and when |

Notation convention: $a_{-i}$ denotes the actions of *everyone except* $i$, so a profile
splits as $a = (a_i, a_{-i})$. The same subscript trick applies to strategies $s_{-i}$.

---

## 2. Normal-form (strategic) games

A **normal-form game** presents all players as choosing simultaneously, with no
information about others' choices:

$$
G = \langle N, (A_i)_{i \in N}, (u_i)_{i \in N} \rangle .
$$

For two players this is a payoff matrix. The canonical example, the **Prisoner's
Dilemma** (entries are *(row, column)* payoffs):

|  | **Cooperate** | **Defect** |
|---|---|---|
| **Cooperate** | $(-1, -1)$ | $(-3, 0)$ |
| **Defect** | $(0, -3)$ | $(-2, -2)$ |

Even though $(C, C)$ Pareto-dominates $(D, D)$, both players defect — the engine behind
free-riding, price wars, and many DeFi mechanism failures.

### Strategies: pure vs. mixed

- A **pure strategy** picks a single action $a_i \in A_i$.
- A **mixed strategy** $\sigma_i \in \Delta(A_i)$ is a probability distribution over
  actions, where $\Delta(A_i)$ is the simplex over $A_i$.

Expected payoff under a mixed profile $\sigma = (\sigma_i, \sigma_{-i})$:

$$
u_i(\sigma) = \sum_{a \in A} \left( \prod_{j \in N} \sigma_j(a_j) \right) u_i(a) .
$$

---

## 3. Dominance and rationalizability

Action $a_i$ **strictly dominates** $a_i'$ if it is better *no matter what others do*:

$$
u_i(a_i, a_{-i}) > u_i(a_i', a_{-i}) \quad \text{for all } a_{-i} \in A_{-i}.
$$

(Weak dominance replaces $>$ with $\ge$ and requires strictness somewhere.) A rational
player never plays a strictly dominated action, so we can **iteratively eliminate** them
(IESDS). What survives is the set of *rationalizable* strategies. In the Prisoner's
Dilemma, Defect strictly dominates Cooperate for both — one round of elimination solves
the game.

---

## 4. Nash equilibrium

A profile $\sigma^* = (\sigma_1^*, \dots, \sigma_n^*)$ is a **Nash equilibrium** if no
player can improve by unilaterally deviating:

$$
u_i(\sigma_i^*, \sigma_{-i}^*) \ge u_i(\sigma_i, \sigma_{-i}^*)
\quad \text{for all } \sigma_i \in \Delta(A_i), \ \text{for all } i \in N.
$$

Equivalently, every player's strategy is a **best response** to the others:

$$
\sigma_i^* \in \arg\max_{\sigma_i \in \Delta(A_i)} u_i(\sigma_i, \sigma_{-i}^*) .
$$

A Nash equilibrium is a *fixed point* of the best-response correspondence
$B(\sigma) = \big(B_1(\sigma_{-1}), \dots, B_n(\sigma_{-n})\big)$.

**Existence (Nash, 1951).** Every finite game (finite players, finite actions) has at
least one Nash equilibrium in mixed strategies. The proof applies Kakutani's fixed-point
theorem to $B$, which is non-empty, convex-valued, and upper hemicontinuous on the
compact convex set $\prod_i \Delta(A_i)$.

### The indifference principle (computing mixed equilibria)

If a player mixes over several actions in equilibrium, every action in the *support* must
yield the **same** expected payoff — otherwise they'd shift weight to the best one. So you
solve for the *opponent's* mix that makes you indifferent.

*Matching Pennies* — players pick H/T; the matcher wants to match, the mismatcher wants to
differ. Payoff to row (matcher):

|  | **H** | **T** |
|---|---|---|
| **H** | $(+1, -1)$ | $(-1, +1)$ |
| **T** | $(-1, +1)$ | $(+1, -1)$ |

There is no pure equilibrium. Let column play H with probability $q$. Row is indifferent
when

$$
\underbrace{q(1) + (1-q)(-1)}_{\text{row plays H}} = \underbrace{q(-1) + (1-q)(1)}_{\text{row plays T}}
\;\Longrightarrow\; q = \tfrac{1}{2}.
$$

By symmetry $p = \tfrac{1}{2}$. The unique equilibrium is both mixing 50/50 — the logical
core of randomized execution and any zero-sum hide-and-seek (order placement, spoofing
detection).

---

## 5. Beyond Nash: correlated and Bayesian equilibria

### Correlated equilibrium (Aumann, 1974)

A trusted device draws an action profile from a joint distribution $\pi$ and privately
*recommends* $a_i$ to each player. It is a **correlated equilibrium** if obeying is
optimal given the conditional beliefs the recommendation induces:

$$
\sum_{a_{-i}} \pi(a_i, a_{-i})\, u_i(a_i, a_{-i}) \;\ge\;
\sum_{a_{-i}} \pi(a_i, a_{-i})\, u_i(a_i', a_{-i})
\quad \text{for all } a_i, a_i' \in A_i.
$$

The set of correlated equilibria is a *convex polytope* that **contains** all Nash
equilibria (any product distribution $\prod_i \sigma_i$ is a special case). It can achieve
better payoffs — a traffic light is the everyday example — and, unlike Nash, it is
computable by linear programming.

### Bayesian games (incomplete information)

When players have private information, each $i$ has a **type** $\theta_i \in \Theta_i$
drawn from a common prior $p(\theta)$. Strategies map types to actions,
$s_i : \Theta_i \to A_i$. A **Bayes–Nash equilibrium** maximizes *interim* expected
payoff, conditioning on one's own type:

$$
s_i^*(\theta_i) \in \arg\max_{a_i \in A_i}
\sum_{\theta_{-i}} p(\theta_{-i} \mid \theta_i)\,
u_i\big(a_i, s_{-i}^*(\theta_{-i}); \theta_i, \theta_{-i}\big).
$$

This is the workhorse for **auctions** and any setting with asymmetric information
(adverse selection in markets, informed-vs-uninformed traders).

---

## 6. Extensive-form games and sequential rationality

When moves happen *in sequence*, represent the game as a tree: nodes are decision points,
edges are actions, and **information sets** group nodes a player cannot distinguish.
Perfect information ⇔ every information set is a singleton.

### Subgame perfection

A Nash equilibrium can rely on **non-credible threats** off the equilibrium path. A
**subgame-perfect equilibrium (SPE)** rules these out by requiring Nash behavior in *every*
subgame. For finite games of perfect information, find it by **backward induction**: solve
the last movers first, fold their optimal choices back, repeat.

> *Entry game.* An incumbent threatens a price war if a rival enters. The threat is Nash
> but not subgame-perfect — once entry happens, fighting hurts the incumbent too, so
> backward induction predicts accommodation. Credibility, not preference, decides the
> outcome.

For imperfect information, the refinement is **Perfect Bayesian Equilibrium**: a profile of
strategies *plus* beliefs at every information set, where strategies are sequentially
rational given beliefs and beliefs are updated by Bayes' rule on the path of play.

---

## 7. Repeated games and cooperation

Repetition can sustain cooperation that one-shot play destroys. In an infinitely repeated
game, payoffs are discounted by $\delta \in (0,1)$:

$$
U_i = (1 - \delta) \sum_{t=0}^{\infty} \delta^{t}\, u_i(a^t).
$$

Under a **grim-trigger** strategy (cooperate until any defection, then defect forever),
cooperation in the Prisoner's Dilemma is sustainable iff the discount factor is high
enough — players are patient enough that the one-shot gain from defecting is outweighed by
lost future cooperation:

$$
\delta \ge \frac{\text{tempt} - \text{coop}}{\text{tempt} - \text{punish}}.
$$

The **Folk Theorem** generalizes this: for $\delta$ close enough to $1$, *any* feasible
payoff profile that gives every player more than their minmax value can be supported as a
subgame-perfect equilibrium. Repetition vastly enlarges the set of equilibria — explaining
both stable collusion and fragile cooperation.

---

## 8. Zero-sum games and the minimax theorem

A two-player game is **zero-sum** if $u_1(a) + u_2(a) = 0$ for all $a$. Von Neumann's
**minimax theorem** says the value is well-defined: order of commitment doesn't matter at
the optimum,

$$
\max_{\sigma_1} \min_{\sigma_2} u_1(\sigma_1, \sigma_2)
= \min_{\sigma_2} \max_{\sigma_1} u_1(\sigma_1, \sigma_2) = v.
$$

The optimal mixed strategies solve a **linear program** (LP duality *is* the minimax
theorem). This is the right frame for adversarial settings: robust execution against a
worst-case counterparty, and the formal basis for much of adversarial ML.

---

## 9. Solution-concept hierarchy

From weakest (most permissive) to strongest (most restrictive). Each refinement is a
strict subset of the one above:

$$
\text{Rationalizable} \;\supseteq\; \text{Nash} \;\supseteq\;
\text{Subgame-perfect} \;\supseteq\; \text{Perfect Bayesian / Sequential}.
$$

And cutting across these, **correlated equilibrium** $\supseteq$ Nash. Which concept you
reach for depends on the *information and timing* of the game — the same reason the four
primitives come first.

---

## 10. Where this connects

- **Market microstructure** — limit-order placement as a Bayesian game; informed vs.
  uninformed traders → see `../quantitative-analysis/`.
- **DeFi / MEV** — auctions and mechanism design explain priority-gas auctions and
  mechanism failures → see `../defi/`.
- **Multi-agent AI** — minimax, self-play, and correlated signals → see `../ai/`.

### To expand later

- [ ] Mechanism design & the revelation principle
- [ ] Auction formats: first/second-price, revenue equivalence, VCG
- [ ] Evolutionary game theory & ESS
- [ ] Computing equilibria: support enumeration, Lemke–Howson, LP for zero-sum/correlated

---

### References

- Osborne & Rubinstein, *A Course in Game Theory*
- Fudenberg & Tirole, *Game Theory*
- Maschler, Solan & Zamir, *Game Theory*
