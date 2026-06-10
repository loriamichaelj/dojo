# Foundations of Poker

> **Claim:** Poker is a betting game wrapped around an imperfect-information game tree.
> Win by making decisions whose *expected value* is positive given your opponent's
> range — equity tells you how often you win, pot odds tell you what price you're paid,
> and game theory tells you how to be unexploitable when you don't know their hand.

A living reference for the quantitative core of No-Limit Hold'em. Pairs with
[`../game-theory/foundations.md`](../game-theory/foundations.md) — poker is the concrete
testbed for mixed strategies, indifference, and minimax.

House rule for this folder: when analyzing a spot, state the **stakes, positions, stacks,
ranges, and board** up front — the poker analogue of *players, actions, payoffs,
information*.

---

## 1. The game in one paragraph

Each player is dealt private cards (the **hole cards**); community cards are revealed in
stages (**flop**, **turn**, **river**). Between stages players act in turn — *fold, check,
call, bet, or raise*. The imperfect information is the opponents' hole cards; the strategic
object is therefore not a single hand but a **range** — the probability distribution over
all hands a player could hold given their actions so far.

---

## 2. Expected value — the only thing that matters

Every decision reduces to: which action has the highest **expected value (EV)**?

$$
\mathrm{EV}(\text{action}) = \sum_{i} p_i \cdot v_i,
$$

where $p_i$ is the probability of outcome $i$ and $v_i$ its chip (or dollar) result. A
play is correct if it maximizes EV — *regardless of whether this particular hand wins*.
Variance means a +EV decision can lose; the edge only shows up over a large sample.

**Example — calling a river bet.** Pot is \$100, opponent bets \$50, you must call \$50 to
win \$150. If you win the showdown with probability $w$:

$$
\mathrm{EV}(\text{call}) = w \cdot 150 - (1-w)\cdot 50.
$$

This is positive when $w > 0.25$ — which is exactly the pot-odds threshold below.

---

## 3. Pot odds and the break-even threshold

**Pot odds** are the price of a call: the amount to call relative to the total pot you'd
win. Calling $c$ into a final pot of $P$ (pot after the bet) requires win probability

$$
w^\* = \frac{c}{P + c} = \frac{\text{call}}{\text{pot} + \text{call}}.
$$

In the example above, $w^\* = \tfrac{50}{150+50} = 0.25$ — call any time your equity beats
25%. Equivalently, a half-pot bet asks you to be right 25% of the time; a pot-sized bet,
33%; a 2× pot overbet, 40%.

---

## 4. Equity, outs, and the 2-and-4 rule

**Equity** is your share of the pot = probability of winning at showdown (split pots
counted fractionally). When drawing, count your **outs** (cards that make your hand) and
approximate:

$$
P(\text{hit by river, 2 cards to come}) \approx 4 \times \text{outs}, \qquad
P(\text{hit, 1 card to come}) \approx 2 \times \text{outs}.
$$

The exact two-card figure (no replacement, 47 unseen after the flop):

$$
P(\text{hit}) = 1 - \frac{\binom{47-\text{outs}}{2}}{\binom{47}{2}}.
$$

| Draw | Outs | ≈ Turn+River equity |
|---|---|---|
| Gutshot straight | 4 | ~17% |
| Flush draw | 9 | ~35% |
| Open-ended straight | 8 | ~32% |
| Flush + open-ender | 15 | ~54% |

**Decision rule:** call a draw when *equity > pot-odds threshold*, i.e. $w > w^\*$.
**Implied odds** improve this — extra chips you expect to win on later streets when you
hit — while **reverse implied odds** (you make a hand but still lose) work against you.

---

## 5. Fold equity and the bluff break-even

A bet wins two ways: opponent folds now, or you win at showdown. The first is **fold
equity**. A pure bluff betting $b$ into pot $P$ needs the opponent to fold often enough:

$$
\text{break-even fold \%} = \frac{b}{P + b}.
$$

A pot-sized bluff ($b = P$) needs folds 50% of the time to break even; a half-pot bluff,
33%. Note the symmetry with pot odds — the bettor's required fold frequency equals the
caller's required equity. That symmetry is the seed of GTO.

---

## 6. GTO: balance, indifference, and unexploitability

**Game-theory-optimal** play is a Nash equilibrium strategy — one that cannot be exploited
no matter how the opponent adjusts. Its engine is the **indifference principle** from
[`../game-theory/foundations.md`](../game-theory/foundations.md): you mix your bets so the
opponent is *indifferent* between folding and calling, denying them any profitable
deviation.

**Optimal bluffing frequency.** To make a calling station indifferent, your betting range
should contain value hands and bluffs in a ratio set by the pot odds you're laying.
Betting $b$ into $P$, the bluff fraction of your betting range is

$$
\frac{\text{bluffs}}{\text{value} + \text{bluffs}} = \frac{b}{P + 2b}.
$$

A pot-sized bet → ~33% bluffs (1 bluff per 2 value bets). This makes the opponent's call
exactly break-even, so they can't exploit you by always calling or always folding.

**Minimum defense frequency (MDF).** Symmetrically, to stop the opponent from auto-profiting
by bluffing, the *defender* must continue (call or raise) with at least

$$
\mathrm{MDF} = 1 - \frac{b}{P + b} = \frac{P}{P + b}.
$$

Facing a pot-sized bet, defend ≥ 50%; facing a half-pot bet, ≥ 67%. Fold more than MDF
allows and bluffs print money against you.

---

## 7. GTO vs. exploitative play

| | **GTO** | **Exploitative** |
|---|---|---|
| Goal | Be unexploitable | Maximize EV vs. *this* opponent |
| Assumes | Opponent plays perfectly | Opponent has identifiable leaks |
| Risk | Leaves EV on the table vs. weak players | Becomes exploitable yourself |
| Use when | Tough/unknown opponents, high stakes | Reads available, weak fields |

GTO is the *baseline*; the money comes from deviating toward exploitation once you spot a
leak (a player who folds too much → bluff more than 33%; a station who never folds → bluff
0% and value-bet thin). The cost of exploiting is that you, too, become exploitable — fine
if the opponent can't or won't adjust.

---

## 8. Position and ranges

**Position** (acting later) is worth real EV: you see opponents act before you decide, so
your information set is strictly larger. Standard positions at a 6-max table, tightest to
widest opening range:

$$
\text{UTG} \subset \text{MP} \subset \text{CO} \subset \text{BTN}, \qquad
\text{Blinds: SB, BB (out of position post-flop)}.
$$

The button opens the widest range precisely because it always acts last post-flop.
**Range** thinking replaces "what does he have?" with "what is his *distribution* of
hands, and how does my range interact with this board?" — range vs. range, not hand vs.
hand.

---

## 9. Variance, bankroll, and risk of ruin

Even a winning strategy loses over short samples. Model results as a random walk with
per-hand edge $\mu$ (in big blinds/100) and standard deviation $\sigma$ (typically
~80–100 bb/100 for NLHE). For a simplified gambler's-ruin bound, the probability of busting
a bankroll of $B$ big blinds with per-unit win probability $p$ ($q=1-p$) is

$$
P(\text{ruin}) \approx \left(\frac{q}{p}\right)^{B}.
$$

The practical takeaway: bankroll requirements scale with **variance**, not just edge. Rule
of thumb — keep 20–40 buy-ins for cash, more for higher-variance tournaments. Sample size
to be confident an edge is real grows with $(\sigma/\mu)^2$.

---

## 10. Where this connects

- **Game theory** — bluffing as indifference, MDF as best-response, minimax in heads-up →
  [`../game-theory/`](../game-theory/).
- **Quantitative analysis** — variance, risk of ruin, sample size, significance of a
  win-rate → [`../quantitative-analysis/`](../quantitative-analysis/).
- **AI** — Counterfactual Regret Minimization (CFR) and self-play solved heads-up limit
  and power modern solvers → [`../ai/`](../ai/).

### To expand later
- [ ] Counterfactual Regret Minimization (CFR) — how solvers actually compute GTO
- [ ] Combinatorics: counting combos, blockers, and removal effects
- [ ] Bet sizing theory and polarized vs. merged ranges
- [ ] ICM (Independent Chip Model) and tournament/payout-aware adjustments
- [ ] Multiway pots — why heads-up GTO intuitions break with 3+ players

---

### References
- Sklansky, *The Theory of Poker*
- Janda, *Applications of No-Limit Hold'em*
- Ankenman & Chen, *The Mathematics of Poker*
- Brown & Sandholm, *Superhuman AI for heads-up no-limit poker* (Libratus), 2017
