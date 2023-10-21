import json
import altair as alt
import pandas as pd
from snowflake.snowpark.session import Session
import streamlit as st
import snowflake.snowpark as sp
import warnings
from cachetools import cached
import plotly.graph_objects as go
import tomli



warnings.filterwarnings('ignore')

# Streamlit config
st.set_page_config("Customer Lifetime Value Prediction")
st.write("<style>[data-testid='stMetricLabel'] {min-height: 0.5rem !important}</style>", unsafe_allow_html=True)
st.title("Customer Lifetime Value Prediction")

# Call functions to get Snowflake session and load data
       

# Define the secrets to extract
secrets_to_extract = {
    'account': st.secrets['account'],
    'user': st.secrets['user'],
    'password': st.secrets['password'],
    'warehouse': st.secrets['warehouse']
}

# Write the extracted secrets to a JSON file
with open('creds.json', 'w') as json_file:
    json.dump(secrets_to_extract, json_file, indent=4)

def create_session():
    if "snowpark_session" not in st.session_state:
        session = Session.builder.configs(json.load(open("creds.json"))).create()
        session.use_warehouse("COMPUTE_WH")
        session.use_database("tpcds_xgboost")
        session.use_schema("demo")
        st.session_state['snowpark_session'] = session
    else:
        session = st.session_state['snowpark_session']
    return session

session = create_session()

# Your user input variables
gender = st.selectbox('Gender: ',['Male','Female'])
marital_status = st.selectbox('Marital Status: ',['D','M','S','U','W'])
credit_rating = st.selectbox('Credit Rating: ',['Good','High Risk','Low Risk','Unknown'])
education_status = st.selectbox('Education Status: ',["2YR DEGREE","4YR DEGREE","ADVANCEDDEGREE","COLLEGE","PRIMARY","SECONDARY","UNKNOWN"])
birth_year = st.selectbox('Birth Year: ',range(1990,2000))
department_count = st.selectbox("Count of Dependents For Each Customer: ", range(0,10))

# Initialize all variables as floats
CD_GENDER_F = 0.0
CD_GENDER_M = 0.0
CD_MARITAL_STATUS_D = 0.0
CD_MARITAL_STATUS_M = 0.0
CD_MARITAL_STATUS_S = 0.0
CD_MARITAL_STATUS_U = 0.0
CD_MARITAL_STATUS_W = 0.0
CD_CREDIT_RATING_Good = 0.0
CD_CREDIT_RATING_High_Risk = 0.0
CD_CREDIT_RATING_Low_Risk = 0.0
CD_CREDIT_RATING_Unknown = 0.0
CD_EDUCATION_STATUS_2_yr_Degree = 0.0
CD_EDUCATION_STATUS_4_yr_Degree = 0.0
CD_EDUCATION_STATUS_Advanced_Degree = 0.0
CD_EDUCATION_STATUS_College = 0.0
CD_EDUCATION_STATUS_Primary = 0.0
CD_EDUCATION_STATUS_Secondary = 0.0
CD_EDUCATION_STATUS_Unknown = 0.0
C_BIRTH_YEAR = 0.0
CD_DEP_COUNT = 0.0

# Map user input to float variables
if gender == 'Female':
    CD_GENDER_F = 1.0
elif gender == 'Male':
    CD_GENDER_M = 1.0

if marital_status == 'D':
    CD_MARITAL_STATUS_D = 1.0
elif marital_status == 'M':
    CD_MARITAL_STATUS_M = 1.0
elif marital_status == 'S':
    CD_MARITAL_STATUS_S = 1.0
elif marital_status == 'U':
    CD_MARITAL_STATUS_U = 1.0
elif marital_status == 'W':
    CD_MARITAL_STATUS_W = 1.0

if credit_rating == 'Good':
    CD_CREDIT_RATING_Good = 1.0
elif credit_rating == 'High Risk':
    CD_CREDIT_RATING_High_Risk = 1.0
elif credit_rating == 'Low Risk':
    CD_CREDIT_RATING_Low_Risk = 1.0
elif credit_rating == 'Unknown':
    CD_CREDIT_RATING_Unknown = 1.0

if education_status == '2YR DEGREE':
    CD_EDUCATION_STATUS_2_yr_Degree = 1.0
elif education_status == '4YR DEGREE':
    CD_EDUCATION_STATUS_4_yr_Degree = 1.0
elif education_status == 'ADVANCEDDEGREE':
    CD_EDUCATION_STATUS_Advanced_Degree = 1.0
elif education_status == 'COLLEGE':
    CD_EDUCATION_STATUS_College = 1.0
elif education_status == 'PRIMARY':
    CD_EDUCATION_STATUS_Primary = 1.0
elif education_status == 'SECONDARY':
    CD_EDUCATION_STATUS_Secondary = 1.0
elif education_status == 'UNKNOWN':
    CD_EDUCATION_STATUS_Unknown = 1.0

C_BIRTH_YEAR = float(birth_year)
CD_DEP_COUNT = float(department_count)


df_predicted_roi = session.sql(
    f"SELECT TPCDS_XGBOOST.DEMO.TPCDS_PREDICT_CLV("
    f"{CD_GENDER_F}, {CD_GENDER_M}, {CD_MARITAL_STATUS_D}, {CD_MARITAL_STATUS_M}, "
    f"{CD_MARITAL_STATUS_S}, {CD_MARITAL_STATUS_U}, {CD_MARITAL_STATUS_W}, "
    f"{CD_CREDIT_RATING_Good}, {CD_CREDIT_RATING_High_Risk}, {CD_CREDIT_RATING_Low_Risk}, "
    f"{CD_CREDIT_RATING_Unknown}, {CD_EDUCATION_STATUS_2_yr_Degree}, "
    f"{CD_EDUCATION_STATUS_4_yr_Degree}, {CD_EDUCATION_STATUS_Advanced_Degree}, "
    f"{CD_EDUCATION_STATUS_College}, {CD_EDUCATION_STATUS_Primary}, "
    f"{CD_EDUCATION_STATUS_Secondary}, {CD_EDUCATION_STATUS_Unknown}, "
    f"{C_BIRTH_YEAR}, {CD_DEP_COUNT}) AS PREDICTED_CLV"
).to_pandas()


if st.button("Predict Customer Lifetime Value"):
    st.write(df_predicted_roi)  