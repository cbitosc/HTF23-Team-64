import streamlit as st
from forecast import forecast_tab
from comparison import comparison_tab
from risk_assessment import risk_assessment_tab
from welcome import welcome_page

# Center-align the title using HTML/CSS
st.markdown("""
<style>
    .centered-title {
        text-align: center;
        font-size: 72px;
    }
</style>
""", unsafe_allow_html=True)

# Set app title (centered)
st.markdown("<h1 class='centered-title'>Investopedia</h1>", unsafe_allow_html=True)

# Allow the user to select the tab
selected_tab = st.selectbox("Select a tab:", ["Welcome", "Stock Forecast", "Stock Comparison", "Risk Assessment"])

# Define content for each tab
if selected_tab == "Welcome":
    welcome_page()
elif selected_tab == "Stock Forecast":
    forecast_tab()
elif selected_tab == "Stock Comparison":
    comparison_tab()
elif selected_tab == "Risk Assessment":
    risk_assessment_tab()
