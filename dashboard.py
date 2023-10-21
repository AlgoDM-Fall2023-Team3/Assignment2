import streamlit as st

st.set_page_config(
    page_title="Multi Page Application",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

# Create a Streamlit app
st.title("Use Cases with Snowpark and Streamlit")

# Page 1: Customer Lifetime Value Computation
st.header("Customer Lifetime Value Computation")
st.write("This case study focuses on estimating Customer Lifetime Value (CLV) using Snowpark Python.")
st.write("Key steps:")
st.write("- Prepare sales data from various channels and customer information.")
st.write("- Incorporate CLV model findings into a user-friendly Streamlit app.")


# Page 2: Predict Customer Spend
st.header("Predict Customer Spend")
st.write("In this scenario, we're exploring user behavior influence on spending for an e-commerce store.")
st.write("Key steps:")
st.write("- Input customer data and view the predicted spending for individual customers.")
st.write("- This analysis helps identify which user activities have the most impact on customer spending.")

# Page 3: ROI Prediction
st.header("ROI Prediction")
st.write("This example focuses on building a Linear Regression model to predict Return On Investment (ROI) from advertising budgets.")
st.write("Key steps:")
st.write("- Deployed the model within Snowflake for real-time predictions and updates.")
st.write("- Integrated the model with a Streamlit app for user-friendly visualization and interaction.")


