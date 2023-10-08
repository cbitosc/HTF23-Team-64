import streamlit as st


def welcome_page():

    st.title('Welcome to Investopedia!')

    st.write("Are you ready to embark on a financial adventure?")
    st.write(
        "Whether you're a financial wizard or just starting your investment journey, we're here to help you make sense of the stock market.")
    # Disclaimer Section
    st.write("## Disclaimer 🚩")
    st.write(
        "Please note that investing in stocks carries risks, and past performance is not indicative of future results. The tools provided by Investopedia are for educational and informational purposes only.")
    st.write(
        "Investopedia does not provide investment advice, and any decisions you make based on the information and predictions from this website are your responsibility. Always consider seeking advice from a qualified financial professional before making investment decisions.")

    st.write("## Unlocking the Power of Investopedia")

    st.write(
        "Investopedia offers you three incredible tools to navigate the world of stocks: Stock Forecast, Stock Comparison, and Risk Assessment. These tools are like a wizard's wand in your hands!")

    st.write("### Stock Forecast 🌟")
    st.write(
        "Our Stock Forecast tool uses historical stock price data and the magical Prophet library to predict future prices. It's like peering into a crystal ball, but with data!")

    st.write("Here's how to use it:")
    st.write("1. **Select a Stock:** Choose a stock from the dropdown menu. Feel free to pick your favorite company!")
    st.write(
        "2. **Select Time Period:** Choose the time period you want to forecast for (Months, Days, Weeks, or Years). Time-travel at your fingertips!")
    st.write(
        "3. **Adjust the Slider:** Use the slider to specify how far into the future you want to predict. Be the master of time!")
    st.write(
        "4. **View the Forecast:** Explore the forecasted data and plots to get insights into potential price trends. Your crystal ball awaits.")

    st.write(
        "But remember, stock market predictions are like predicting the weather. Sometimes we get it right, sometimes it rains when the sun was supposed to shine. So, invest wisely!")

    st.write("### Stock Comparison 📊")
    st.write(
        "Our Stock Comparison tool allows you to compare the performance of multiple stocks. It's like hosting a race for your stocks to see which one wins!")

    st.write("How to use it:")
    st.write(
        "1. **Select Stocks:** Use the multiselect option to choose the stocks you want to compare. It's like choosing your champion racehorses!")
    st.write(
        "2. **Visualize Comparison:** The tool will create a line chart to visualize how the selected stocks perform over time. May the best stock win!")

    st.write(
        "This feature helps you see how your investments stack up against each other. It's like a friendly competition among your stock portfolio!")

    st.write("### Risk Assessment ⚠️")
    st.write(
        "Our Risk Assessment tools help you understand the potential risks associated with your investment choices. It's like having a guardian angel on your investment journey!")

    st.write("Here's what you can do:")
    st.write("1. **Select a Stock:** Choose a stock from the dropdown menu. Choose your stock wisely, young padawan!")

    st.write("2. **We offer two types of risk assessment:**")
    st.write(
        "i. **Historical Volatility:** This measures how much a stock's price has historically 'jumped around' each day. It's like checking if your rollercoaster has loops!")
    st.write(
        "ii. **Value at Risk (VaR) Calculation:** This calculates the potential loss at a specified confidence level using Monte Carlo simulations. Think of it as a 'what-if' machine!")

    st.write(
        "Both tools provide valuable insights into risk. But remember, investing is like a rollercoaster ride—sometimes unpredictable! So, buckle up!")

    st.write(
        "Now, dear adventurer, go forth and explore the power of Investopedia. May your investments be as prosperous as a leprechaun's pot of gold!")
