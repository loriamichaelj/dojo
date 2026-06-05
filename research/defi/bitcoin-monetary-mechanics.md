# Bitcoin: Monetary Mechanics and the Security Game

> **Claim:** Bitcoin's three load-bearing properties — a hard supply cap, a self-tuning
> block interval, and resistance to rewriting history — are not promises but
> *consequences* of code: a geometric reward schedule, a feedback control loop on
> difficulty, and an economic game that makes attacking more expensive than honest mining.

**Context:** Bitcoin protocol as deployed on mainnet (consensus rules stable since the
early eras; figures use the canonical constants — 10-min target block time, 210,000-block
halving interval, 2016-block difficulty retarget). This is the static economic model, not
a price view. Bitcoin is not "DeFi" in the smart-contract sense, but it is the foundational
decentralized-finance system the rest of this folder assumes — a useful baseline for the
[`../game-theory/`](../game-theory/) and tokenomics threads.

---

## 1. The supply schedule is a truncated geometric series

Miners receive a block subsidy that **halves every 210,000 blocks** (≈ 4 years at
10-min blocks). The subsidy starts at 50 BTC:

$$\text{subsidy}_{\,\text{era } n} = \frac{50}{2^{\,n}} \text{ BTC}, \qquad n = 0, 1, 2, \dots$$

Total issuance is the sum over all eras of (blocks per era) × (subsidy):

$$S_{\text{ideal}} = 210{,}000 \sum_{n=0}^{\infty} \frac{50}{2^{\,n}}
= 210{,}000 \cdot 50 \cdot \frac{1}{1 - \tfrac12}
= 210{,}000 \cdot 100 = 21{,}000{,}000 \text{ BTC}.$$

The famous 21M cap is just the closed form of a geometric series with ratio $\tfrac12$.

### The cap is actually *below* 21M

The protocol counts in **satoshis** (1 BTC = $10^8$ sat) and halves by integer
right-shift (`reward >>= 1`), which *truncates* the remainder. Once the subsidy drops
below 1 satoshi it becomes 0, ending issuance after a finite number of eras. Summing the
real integer schedule:

$$S_{\text{actual}} = 20{,}999{,}999.97690000 \text{ BTC},$$

reached after **33 halving eras** — about 0.0231 BTC short of the idealized cap. The
"21 million" is a rounding of a slightly smaller, exactly-defined integer.

*(Both figures computed directly from the integer reward schedule; see the derivation
script logic in the note's companion — terminal subsidy hits 0 sat at era 33.)*

### Disinflation, not deflation, until ~2140

Issuance is positive but shrinking — Bitcoin is *disinflationary*. The annualized issuance
rate falls by ~50% every four years and asymptotes to zero around block 6,930,000
(≈ year 2140), after which **transaction fees alone** fund security.

---

## 2. Difficulty adjustment is a control loop

Block production is a Poisson process: with global hashrate $H$ and a difficulty target
admitting probability $p$ per hash, blocks arrive at rate $\lambda = pH$. The protocol
wants $\mathbb{E}[\text{interval}] = 1/\lambda = 600$ s regardless of how $H$ moves.

It can't observe $H$, so it infers it from realized block times. Every **2016 blocks**
(≈ 14 days at target) it retargets:

$$D_{\text{new}} = D_{\text{old}} \cdot \frac{T_{\text{expected}}}{T_{\text{actual}}},
\qquad T_{\text{expected}} = 2016 \times 600 \text{ s},$$

clamped to a factor of $[\tfrac14, 4]$ per adjustment to damp shocks. This is a
proportional feedback controller: blocks too fast ($T_{\text{actual}} < T_{\text{expected}}$,
i.e. hashrate rose) ⇒ difficulty up; too slow ⇒ difficulty down. The 10-minute interval
is the controller's setpoint, held stable across a hashrate range spanning many orders of
magnitude over Bitcoin's history.

> The retarget uses the *previous* 2016-block window, so it lags real hashrate by up to a
> period — the source of the well-known "difficulty bomb / death spiral" discussions when
> hashrate drops sharply between retargets.

---

## 3. Mining as an economic game

### The security budget

Honest miners spend real resources (energy, hardware) to win the right to append a block.
The **security budget** — what the network pays per unit time for its integrity — is

$$\text{budget} = \text{subsidy} + \text{fees}.$$

In competitive equilibrium, rational miners expand until marginal cost ≈ marginal revenue,
so aggregate mining expenditure tracks the budget. Two consequences a quant should hold
onto:

1. **Security is bought, not free.** As the subsidy halves, security must increasingly be
   funded by the **fee market**. Whether fees can sustain the historical security budget
   is *the* open question for Bitcoin's long-run security
   ([`../game-theory/`](../game-theory/), tokenomics).
2. **Price ↔ security feedback.** Budget is denominated in BTC but priced in fiat, so the
   USD security budget scales with price — security and valuation are coupled.

### The 51% attack and why honesty is the equilibrium

To rewrite confirmed history an attacker must out-produce the honest chain, requiring a
majority of hashrate. The instantaneous *flow* cost is roughly

$$\text{cost} \;\gtrsim\; (\text{honest hashrate}) \times (\text{cost per hash}) \times
(\text{attack duration}),$$

plus the capex to acquire that hashrate. The game-theoretic point is sharper than the
sticker price: a credible attacker who *owns* enough hardware to attack also has the most
to lose — their rig's value and BTC holdings collapse if they break the chain they mine.
Honest mining is (under standard assumptions) the **subgame-perfect equilibrium**:
deviating destroys the asset securing the deviation's payoff. This incentive alignment, not
cryptography alone, is what secures the ledger. Known cracks in the simple story —
**selfish mining** (Eyal–Sirer), fee-sniping, and time-bandit reorgs once fees dominate —
are exactly the multi-agent failure modes worth a dedicated note.

---

## 4. Quant lenses and a caution

- **Issuance as a known schedule.** Unlike fiat or most tokens, Bitcoin's supply at any
  future block is *deterministic*. The flow (new supply/time) is a pure function of block
  height — useful when modeling miner sell pressure or "supply overhang."
- **Stock-to-flow — handle with care.** The S2F model maps scarcity (stock/flow) to price
  via a fitted power law. It is **popular and badly flawed**: it regresses a level on a
  near-deterministic trending regressor (spurious regression), has no error model, and has
  failed out-of-sample. Cite it only as an example of overfitting a narrative to a trend —
  see [`../quantitative-analysis/`](../quantitative-analysis/) on multiple-testing and
  look-ahead discipline.
- **Volatility & regimes.** BTC return behavior (fat tails, volatility clustering,
  halving-cycle narratives) is fertile ground for the time-series tools in
  [`../quantitative-analysis/`](../quantitative-analysis/) — but beware fitting four-year
  "cycles" to four observed halvings ($n \approx 4$ is not a sample).

---

## Open questions / next notes

- **Fee-market sustainability:** model the post-subsidy equilibrium — what fee level and
  block-space demand keep the security budget at parity with today's?
  ([`../game-theory/`](../game-theory/))
- **Selfish mining** formalized: the threshold hashrate share at which withholding beats
  honest mining, and what network propagation assumptions it needs.
- **Difficulty as a controller:** simulate the retarget loop under hashrate shocks —
  quantify the lag, overshoot, and the conditions for a death spiral.
- Relate BTC's deterministic issuance to token emission schedules elsewhere in this folder
  (vesting, staking inflation) — a tokenomics comparison.
