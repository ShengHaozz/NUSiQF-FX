import pandas as pd
import numpy as np
from scipy.stats import pearsonr
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from typing import Tuple

def calculate_pnl(
    weights_df: pd.DataFrame,
    prices_df: pd.DataFrame,
    initial_capital: float = 1000000
) -> Tuple[pd.DataFrame, pd.Series]:

    returns_df = prices_df.pct_change()
    
    # We use today's weights with tomorrow's returns
    shifted_weights = weights_df.shift(1)
    
    # Calculate position-level returns by multiplying previous day's weights with today's returns
    position_returns = shifted_weights * returns_df
    
    # Calculate portfolio daily returns (sum across all positions)
    portfolio_returns = position_returns.sum(axis=1)
    
    # Calculate cumulative portfolio value
    portfolio_value = initial_capital * (1 + portfolio_returns).cumprod()
    
    # Calculate position-level PnL
    position_pnl = position_returns * initial_capital
    
    return position_pnl, portfolio_value


def plot_pnl_analysis(risk_free: float, portfolio_pnl: pd.Series, position_pnl: pd.DataFrame = None):
    plt.figure(figsize=(15, 10))
    
    plt.subplot(2, 1, 1)
    portfolio_pnl.plot(label='Portfolio Value')
    plt.title('Portfolio Value Over Time')
    plt.grid(True)
    plt.legend()
    
    plt.subplot(2, 1, 2)
    drawdown = portfolio_pnl / portfolio_pnl.cummax() - 1
    drawdown.plot(label='Drawdown')
    plt.title('Portfolio Drawdown')
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    returns = portfolio_pnl.pct_change().dropna()
    daily_sharpe = (returns.mean() - risk_free) / returns.std()
    annual_sharpe = daily_sharpe * np.sqrt(252)
    annual_return = ((1 + returns).prod()) ** (252/len(returns)) - 1
    annual_vol = returns.std() * np.sqrt(252)
    max_drawdown = drawdown.min()
    
    print("\nPerformance Metrics:")
    print(f"Annual Return: {annual_return:.2%}")
    print(f"Annual Volatility: {annual_vol:.2%}")
    print(f"Annual Sharpe: {annual_sharpe:.2f}")
    print(f"Maximum Drawdown: {max_drawdown:.2%}")

def run_strategy_analysis(
    input_df: pd.DataFrame,
    weights_df: pd.DataFrame,
    start_date: str,
    end_date: str,
    risk_free: float,
    initial_capital: float = 1000000
):
    """
    Run strategy analysis using price data and weights
    
    Parameters:
    input_df (pd.DataFrame): Price data for assets
    start_date (str): Start date for analysis
    end_date (str): End date for analysis
    initial_capital (float): Initial portfolio value
    weights_df (pd.DataFrame): DataFrame containing portfolio weights
    """
    # Filter date range
    input_df = input_df.loc[start_date:end_date]
    weights_df = weights_df.loc[start_date:end_date]
    
    # Calculate returns from prices
    returns = input_df.pct_change()
    
    # Shift weights by one day to avoid look-ahead bias
    shifted_weights = weights_df.shift(1)
    
    # Calculate strategy returns
    strategy_returns = (shifted_weights * returns).sum(axis=1)
    
    # Calculate cumulative returns and PnL
    portfolio_pnl = initial_capital * (1 + strategy_returns).cumprod()
    
    # Calculate individual position PnL
    position_pnl = shifted_weights * returns * initial_capital
    
    # Plot results with risk-free rate for Sharpe calculation
    plot_pnl_analysis(
        portfolio_pnl=portfolio_pnl,
        position_pnl=position_pnl,
        risk_free=risk_free
    )
    
    return position_pnl, portfolio_pnl


