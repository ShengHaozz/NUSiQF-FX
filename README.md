# NUSiQF-FX

0. API calls


1. Alpha function


Mean Reversion 1: -(close(today) - close(X_days_ago)) / close(X_days_ago)

Aroon Indicator: 

𝐴𝑈 = [1 − (P_high / 𝐴𝐿) ] × 100

𝐴𝐷 = [1 − (𝑃_low / 𝐴𝐿) ] × 100

AL = Lookback period of the Aroon Indicator

P_high = Periods since last High within the lookback period AL

P_low = Periods since last Low within the lookback period AL


2. Alpha to asset allocation

WQ  Allocator:

a. Get alpha scores for each day
b. Neutralise alphas (set average() = 0)
c. Normalise alphas (set sum(abs()) = 1)

QuantyMacro Allocator:

a. Get average alpha in each basket A, B
b. If alpha_A > alpha_B, long A short B, else long B short A
c. Neutralise weights (set average() = 0)
d. Normalise weights (set sum(abs()) = 1)


3. Backtesting

