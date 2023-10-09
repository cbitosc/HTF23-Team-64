import streamlit as st
import yfinance as yf
import pandas as pd
from plotly import graph_objs as go
from datetime import date, timedelta


def comparison_tab():
    st.title('Stock Comparison')

    stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
    selected_stocks_compare = st.multiselect('Select stocks for comparison:', stocks)

    if len(selected_stocks_compare) < 2:
        st.write("Please select at least two stocks for comparison.")
        return

    START = "2017-01-01"
    TODAY = date.today()
    data_compare = yf.download(selected_stocks_compare, START, TODAY.strftime("%Y-%m-%d"))

    # Manually add the 'Date' column to the DataFrame
    data_compare['Date'] = data_compare.index

    # Create an empty figure
    fig_compare = go.Figure()

    # Add traces for each selected stock
    for stock in selected_stocks_compare:
        trace = go.Scatter(x=data_compare['Date'], y=data_compare['Close'][stock], mode='lines', name=stock)
        fig_compare.add_trace(trace)

    # Update layout
    fig_compare.update_layout(title='Stock Comparison', xaxis_title='Date', yaxis_title='Price')

    # Show the chart
    st.plotly_chart(fig_compare)
