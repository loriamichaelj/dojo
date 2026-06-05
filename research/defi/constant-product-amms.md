# Constant-Product AMMs: Pricing, Slippage, and Impermanent Loss

> **Claim:** A constant-product market maker prices trades entirely off one invariant,
> $x \cdot y = k$. Everything a quant cares about — execution price, slippage, the
> arbitrage that keeps the pool honest, and the loss liquidity providers eat for
> providing it — falls out of that single equation.

**Context:** Uniswap v2 mechanics (Ethereum mainnet). Constant-product is the v2 model;
v3 generalizes it with *concentrated liquidity*, noted at the end. Fee figures use the
canonical v2 swap fee of 30 bps. No block/time-specific data — this is the static model.

---

## 1. The invariant

A pool holds reserves of two tokens, $x$ (token $X$) and $y$ (token $Y$). The pool
commits to keeping their product constant across any swap:

$$x \cdot y = k.$$

A swap moves the reserves *along the hyperbola* $xy = k$. Adding $X$ pushes $x$ up, so
$y$ must fall — the trader receives the $Y$ the curve gives up. The pool never needs an
external price feed: the curve *is* the price.

### Spot (marginal) price

The marginal price of $X$ in units of $Y$ is the slope of the curve. From $y = k/x$:

$$P_X = -\frac{dy}{dx} = \frac{k}{x^2} = \frac{y}{x}.$$

So the spot price is just the reserve ratio, $P = y/x$. A pool deep in $X$ (large $x$)
prices $X$ cheaply, exactly as supply/demand intuition demands.

---

## 2. Swap math with fees

Let the trader send $\Delta x$ of token $X$ and receive $\Delta y$ of token $Y$. Let
$\gamma = 1 - f$ be the fee retention factor, with $f = 0.003$ (30 bps) on v2. Only the
post-fee amount $\gamma\,\Delta x$ enters the curve; the fee stays in the pool and accrues
to LPs.

The invariant must hold *after* the swap on the post-fee reserves:

$$(x + \gamma\,\Delta x)\,(y - \Delta y) = x y.$$

Solving for the output:

$$\boxed{\;\Delta y = \frac{y\,\gamma\,\Delta x}{x + \gamma\,\Delta x}\;}$$

This is exact — it's the actual formula the contract evaluates, not an approximation.

### Execution price and slippage

The **average execution price** the trader pays is

$$P_{\text{exec}} = \frac{\Delta x}{\Delta y} = \frac{x + \gamma\,\Delta x}{y\,\gamma}.$$

Compare it to the pre-trade spot price $P = x/y$ (price of $Y$ in $X$, matching the units
above). As $\Delta x \to 0$,

$$P_{\text{exec}} \to \frac{x}{y\,\gamma} = \frac{P}{\gamma},$$

i.e. even an infinitesimal trade pays the fee. Beyond that, the $\gamma\,\Delta x$ in the
numerator is the **slippage**: price impact grows with trade size relative to reserves.
The fractional price impact (ignoring fees) is

$$\frac{P_{\text{exec}}}{P} - 1 \approx \frac{\Delta x}{x} \quad (\text{small trades}),$$

so trading 1% of the reserve moves your execution price by roughly 1%. **Depth is
everything**: slippage scales with $\Delta x / x$, which is why large orders fragment
across pools or wait for deeper liquidity.

---

## 3. Arbitrage keeps the pool at the market price

Nothing in the contract knows the "true" price. The pool tracks the external market only
because arbitrageurs trade against any divergence. If the external price of $X$ rises
above the pool's $y/x$, buying $X$ from the pool is profitable until the pool's marginal
price rises to meet it. At equilibrium the pool satisfies two conditions simultaneously:

$$x \cdot y = k, \qquad \frac{y}{x} = P_{\text{ext}}.$$

Solving:

$$x = \sqrt{\frac{k}{P_{\text{ext}}}}, \qquad y = \sqrt{k\,P_{\text{ext}}}.$$

This rebalancing is the mechanism behind impermanent loss (next section) and a primary
source of MEV — the arbitrage profit is paid by LPs. See
[`../game-theory/`](../game-theory/) for the order-flow-as-a-game framing and
[`../strategy-development/`](../strategy-development/) for capturing the arb edge.

---

## 4. Impermanent loss (divergence loss)

**Question:** If I provide liquidity and the price moves, how much worse off am I than if
I had simply held the two tokens?

Let the price move by a factor $r$, from $P_0$ to $P = r P_0$ (price of $X$ in $Y$).
Use $Y$ as the numéraire. Reserves rebalance per §3 to $x = \sqrt{k/P}$, $y = \sqrt{kP}$.

**Value of the LP position** (in units of $Y$):

$$V_{\text{pool}} = y + x \cdot P = \sqrt{kP} + \sqrt{\tfrac{k}{P}}\cdot P = 2\sqrt{kP}.$$

**Value of just holding** the initial bag $(x_0, y_0)$ with $x_0 = \sqrt{k/P_0}$,
$y_0 = \sqrt{kP_0}$, marked at the new price $P$:

$$V_{\text{hodl}} = y_0 + x_0 \cdot P = \sqrt{kP_0} + \frac{P\sqrt{k}}{\sqrt{P_0}}
= \sqrt{k}\,\frac{P_0 + P}{\sqrt{P_0}}.$$

The relative shortfall is

$$\text{IL} = \frac{V_{\text{pool}}}{V_{\text{hodl}}} - 1
= \frac{2\sqrt{kP}}{\sqrt{k}\,(P_0+P)/\sqrt{P_0}} - 1
= \frac{2\sqrt{P P_0}}{P_0 + P} - 1.$$

Substituting $P = r P_0$ collapses it to a clean function of the price multiple alone:

$$\boxed{\;\text{IL}(r) = \frac{2\sqrt{r}}{1 + r} - 1\;}$$

### Properties

- $\text{IL}(1) = 0$: no price move, no loss.
- $\text{IL}(r) \le 0$ for all $r > 0$, with equality only at $r = 1$ — by AM–GM,
  $\sqrt{r} \le (1+r)/2$. **It is always a loss** relative to holding; "impermanent" only
  because it reverses if the price returns to $P_0$.
- **Symmetric in $r \leftrightarrow 1/r$**: a $2\times$ move up and a halving cost the
  same. Halving the price ($r=0.5$) and doubling it ($r=2$) both cost ≈ 5.7%.
- Convex losses in the tails: $4\times$ → −20%, $10\times$ → −42.5%.

| Price multiple $r$ | 0.5 | 0.8 | 1.0 | 1.25 | 2 | 4 | 10 |
|---|---|---|---|---|---|---|---|
| IL | −5.7% | −0.6% | 0% | −0.6% | −5.7% | −20.0% | −42.5% |

*(Closed form verified against a direct rebalancing simulation — exact match to 1e-9.)*

---

## 5. LP economics: the fee–IL trade-off

IL is only half the ledger. LPs also earn the 30 bps fee on every swap. The position is
profitable when accumulated fees outrun divergence loss:

$$\underbrace{\text{fees}(\text{volume}, f)}_{\text{grows with turnover}}
\;\;>\;\;
\underbrace{|\text{IL}(r)|}_{\text{grows with price divergence}}.$$

This reframes LPing as a bet: **you are short volatility / realized variance and long
trading volume.** High-volume, low-volatility pairs (e.g. correlated stablecoins) are
where constant-product LPing tends to pay; volatile, trending pairs are where IL
dominates. The economic rationale and stress-testing discipline belong in
[`../strategy-development/`](../strategy-development/), and the variance interpretation
ties to [`../quantitative-analysis/`](../quantitative-analysis/).

---

## 6. Beyond constant product (v3 and others)

- **Concentrated liquidity (Uniswap v3):** LPs supply liquidity only within a price range
  $[P_a, P_b]$. Capital efficiency rises sharply, but IL is amplified inside the range and
  the position becomes one-sided (and stops earning fees) once price exits it — closer to
  a short options payoff.
- **StableSwap (Curve):** blends constant-product with constant-sum to flatten slippage
  near the peg, ideal for assets expected to trade ~1:1.
- **Weighted pools (Balancer):** generalize to $\prod_i x_i^{w_i} = k$ with arbitrary
  weights, decoupling the 50/50 value split.

---

## Open questions / next notes

- Quantify the fee-vs-IL break-even explicitly: given a price path, what realized
  volatility and volume make an LP position break even? (Connect IL to realized variance.)
- v3 concentrated liquidity as a derivatives position — can the range payoff be replicated
  or hedged with options?
- Just-in-time (JIT) liquidity and the MEV it extracts from passive LPs — a game-theory
  note. See [`../game-theory/`](../game-theory/).
