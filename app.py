import streamlit as st
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd
import os
import plotly.express  as px
import datetime as dt

PARENT_DATABASE_NAME = "AD_FORECAST_DEMO"  
NESTED_DATABASE = "DEMO"
user="MITESH20"
password="9987323889Ritesh."
account_identifier="ykoplix-imb81144"


def fetch_query1():
    engine = create_engine(
        'snowflake://{user}:{password}@{account_identifier}/'.format(
            user=user,
            password=password,
            account_identifier=account_identifier,
        )
    )
    connection = engine.connect()
    try:
        query = f"""
        select * from {PARENT_DATABASE_NAME}.{NESTED_DATABASE}.daily_impressions;
        """
        results = pd.read_sql(query,connection)
        return results
    finally:
        connection.close()
        engine.dispose()

def fetch_query2(period):
    engine = create_engine(URL(
            user=user,
            password=password,
            account=account_identifier,
            database=PARENT_DATABASE_NAME,
            schema=NESTED_DATABASE
    ))
    connection = engine.connect()
    try:
        # connection.execute("Use Database AD_FORECAST_DEMO.DEMO")
        query1 = f"""
        CALL impressions_forecast!FORECAST(FORECASTING_PERIODS => {period});             
        """
        st.success("Model Running Successfully")
        results_1 = pd.read_sql(query1,connection)
        query2 = """
        SELECT day AS ts, impression_count AS actual, NULL AS forecast, NULL AS lower_bound, NULL AS upper_bound
        FROM daily_impressions
        """
        results_2 =pd.read_sql(query2,connection)
        results = pd.concat([results_2,results_1],ignore_index=True)
        return results
    finally:
        connection.close()
        engine.dispose()

def plot_data(data):
    fig = px.area(data,x='day',y='impression_count',
                 title="Impression Count Visualisation")
    fig.update_layout(width=1200,height=700,xaxis_title='Day',yaxis_title='Impression Count')
    st.plotly_chart(fig)

def plot_forecast_data(data):
    fig = px.line(data,x='ts',y=['actual','forecast'], title='Forecast and Actual Trend')
    fig.update_layout(width=1200,height=700,xaxis_title='Timestamp',yaxis_title='Forecast and Actual Trend')
    st.plotly_chart(fig)

st.set_page_config(layout='wide')
st.title("Dashboard")

c1, c2 = st.tabs(['Forecast','Anomaly'])

with c1:
    results= fetch_query1()
    if st.button("View Impression Data"):
        st.write(results)
    if st.button("Visualise Impression Data"):
        plot_data(results)
    period = st.number_input("Select the days who want to forecast data")
    if st.button("Run Forecast Model"):
        data = fetch_query2(period)
        st.write("Actual and Forecasted Daily Impressions Data: ")
        st.write(data)
        plot_forecast_data(data)


