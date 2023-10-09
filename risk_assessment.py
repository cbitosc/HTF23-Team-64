import streamlit as st
import yfinance as yf
import numpy as np
from datetime import date
import matplotlib.pyplot as plt


def risk_assessment_tab():
    st.title('Risk Assessment')

    START = "2017-01-01"
    TODAY = date.today()
    stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
    selected_risk_stock = st.selectbox('Select a stock for risk assessment:', stocks)

    if selected_risk_stock:
        data_risk = yf.download(selected_risk_stock, START, TODAY.strftime("%Y-%m-%d"))
        data_risk['Daily Return'] = data_risk['Close'].pct_change()

        # Historical Volatility
        volatility = data_risk['Daily Return'].std()
        st.subheader('Historical Volatility')
        st.write(f'Historical Volatility measures the "excitement level" of {selected_risk_stock}. '
                 f'It shows how much the stock price "jumps around" each day. '
                 f'A high volatility means it has more "rollercoaster" moments. '
                 f'{selected_risk_stock} has a historical volatility of {volatility:.2%}. '
                 f'That means it can make your heart race!')

        # Value at Risk (VaR) Calculation using Monte Carlo Simulation
        st.subheader('Value at Risk (VaR) Calculation')
        st.write('Let\'s calculate Value at Risk (VaR) using a little bit of magic!')

        # Specify parameters for VaR calculation
        initial_investment = st.number_input('Enter Initial Investment:', value=10000)
        days = st.number_input('Enter Number of Days for VaR Calculation:', value=30)
        simulations = st.number_input('Enter Number of Monte Carlo Simulations:', value=1000)
        confidence_level = st.slider('Select Confidence Level:', min_value=0.01, max_value=0.99, value=0.05)

        # Calculate daily returns
        daily_returns = data_risk['Daily Return'].dropna().values

        # Perform Monte Carlo simulations
        final_prices = []
        for _ in range(simulations):
            daily_returns_sample = np.random.choice(daily_returns, size=days)
            price_path = [initial_investment]
            for ret in daily_returns_sample:
                price_path.append(price_path[-1] * (1 + ret))
            final_prices.append(price_path[-1])

        # Calculate VaR at the specified confidence level
        var_index = int(confidence_level * simulations)
        final_prices_sorted = sorted(final_prices)
        var_value = final_prices_sorted[var_index]

        st.write(f'Value at Risk (VaR) at {confidence_level * 100}% confidence for {days} days: '
                 f'${initial_investment - var_value:.2f}')

        # Plot Monte Carlo Simulation Results
        st.subheader('Monte Carlo Simulation Results')
        st.write('Let\'s visualize how the stock price might behave in the future.')

        plt.figure(figsize=(10, 6))
        plt.title(f'Monte Carlo Simulation for {selected_risk_stock}')
        for i in range(5):  # Plot 5 sample simulations
            sample_path = np.random.choice(final_prices, size=days)
            plt.plot(sample_path, label=f'Simulation {i + 1}')
        plt.xlabel('Days')
        plt.ylabel('Stock Price')

        # Add a line indicating the VaR value
        plt.axhline(var_value, color='red', linestyle='--', label=f'VaR ({confidence_level * 100}%)')

        plt.legend()
        st.pyplot(plt)

        st.write('Remember, this is just a playful prediction. '
                 'Stock markets can be as unpredictable as the weather. '
                 'Invest wisely, and may your investments be as stable as a sleeping cat on a sunny day!')

# To use this updated function, call risk_assessment_tab() in your main app.py script.
