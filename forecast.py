# Import necessary libraries
import streamlit as st
import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go
from datetime import date, timedelta
import plotly.graph_objects as go


# Function to calculate moving averages
def calculate_moving_averages(df):
    df['MA_50'] = df['y'].rolling(window=50).mean()
    df['MA_200'] = df['y'].rolling(window=200).mean()
    return df


# Main forecast_tab function
def forecast_tab():
    TODAY = date.today()
    max_allowed_start_date = TODAY - timedelta(days=180)

    st.title('Stock Forecast and Prediction')

    START = st.date_input("Select a start date:", date(2018, 1, 1), max_value=max_allowed_start_date)

    stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
    selected_stock = st.selectbox('Select dataset for prediction', stocks)

    time_periods = ('Months', 'Days', 'Weeks', 'Years')
    selected_time_period = st.selectbox('Select time period:', time_periods, index=3)

    time_period_info = {
        'Months': {'unit': 'months', 'slider_range': (1, 12)},
        'Days': {'unit': 'days', 'slider_range': (1, 7)},
        'Weeks': {'unit': 'weeks', 'slider_range': (1, 4)},
        'Years': {'unit': 'years', 'slider_range': (1, 4)}
    }

    n_time_units = st.slider(f'Number of {selected_time_period} for prediction:',
                             min_value=time_period_info[selected_time_period]['slider_range'][0],
                             max_value=time_period_info[selected_time_period]['slider_range'][1],
                             value=1)

    end_date = TODAY

    if selected_time_period == 'Months':
        end_date = TODAY + timedelta(days=30.44 * n_time_units)
    elif selected_time_period == 'Days':
        end_date = TODAY + timedelta(days=n_time_units)
    elif selected_time_period == 'Weeks':
        end_date = TODAY + timedelta(weeks=n_time_units)
    elif selected_time_period == 'Years':
        end_date = TODAY + timedelta(days=365.25 * n_time_units)

    df_train = yf.download(selected_stock, START, TODAY.strftime("%Y-%m-%d"))
    df_train.reset_index(inplace=True)
    df_train = df_train[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    # Calculate moving averages (50-day and 200-day)
    df_train = calculate_moving_averages(df_train)

    m = Prophet()
    m.fit(df_train)

    future = m.make_future_dataframe(periods=(end_date - TODAY).days)
    forecast = m.predict(future)

    forecast = forecast.iloc[::-1].reset_index(drop=True)

    st.write(f'Forecasted Price for {n_time_units} {selected_time_period.lower()}')
    fig3 = go.Figure()

    # Plot 50-day moving average
    fig3.add_trace(go.Scatter(x=df_train['ds'], y=df_train['MA_50'], mode='lines', name='50-Day MA'))

    # Plot 200-day moving average
    fig3.add_trace(go.Scatter(x=df_train['ds'], y=df_train['MA_200'], mode='lines', name='200-Day MA'))

    # Plot forecasted price
    fig3.add_trace(go.Scatter(x=forecast['ds'], y=forecast['yhat'], mode='lines', name='Forecasted Price'))

    fig3.layout.update(
        title_text=f'Forecasted Price with Moving Averages for {n_time_units} {selected_time_period.lower()}',
        xaxis_title='Date', yaxis_title='Price')
    st.plotly_chart(fig3)

    st.subheader('Forecast data')
    st.write(forecast)
    
    fig1 = plot_plotly(m, forecast)

    fig1.layout.update(
        title_text=f'Forecasted Price for {n_time_units} {selected_time_period.lower()}',
        xaxis_title='Date', yaxis_title='Price')

    for trace in fig1.data:
        trace.marker.color = 'red'  # Change marker color to red
        trace.line.color = 'green'  # Change line color to red (if it's a line trace)

    # Display the updated figure
    st.plotly_chart(fig1)


# Run the Streamlit app
if __name__ == "__main__":
    forecast_tab()
