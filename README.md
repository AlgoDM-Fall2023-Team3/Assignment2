# Assignment2
The Snowflake tutorial for predicting ad impressions with ML-powered analysis was successfully completed, and part 1 of the assignment was extended with the creation of a Streamlit app that allows interactive data exploration and forecasting, including anomaly detection. 
Furthermore in part 2, the three applications discussed in class, which are Customer Lifetime Value computation, Predict Customer Spend, and ROI prediction, were tested and integrated. A Streamlit app was developed as a multipage platform that combines all three functions, providing a comprehensive analytics tool for businesses seeking to harness the power of Snowflake, Snowpark, and ML for informed decision-making. The versatility and capabilities of Snowflake's data analytics ecosystem for practical business applications are demonstrated by this Assignment.

# Prerequisites:
Snowpark for Python library v.06

* Snowflake account
* Snowpark for Python
* The examples also use the following Python libraries:
   ```
   scikit-learn
   pandas
   numpy
   matplotlib
   seaborn
   streamlit
   ```
* Jupyter or JupyterLab
If any of the packages used in the example are not part of your python environment, you can install them using
<br>`import sys`<br>
`!conda install --yes --prefix {sys.prefix} <package_name>`
* Latest streamlit package, which you can get by
 `!pip install streamlit`

# Setting up snowflake environment
here are the key steps to set up the environment for your Snowflake project
Step 1: Create Warehouse, Database, and Schema
  - Use the USE ROLE ACCOUNTADMIN; command to ensure you have the necessary permissions.
  - Create a Snowflake warehouse, database (e.g., DASH_DB) within the warehouse and establish a schema within the database.
Step 2: Set up Stages for all the case studies (data loading, Revenue Data, Budget Allocations and ROI)
  - Select or create a suitable file format for your data.
  - Create a stage for the data and specify the file format and the URL where your data is hosted.
  - Create a table to hold the data with specific column data types.
  - Copy data from the defined stage into the newly created table
Step 5: Set up Internal Stages for Snowflake Objects
  - Create internal stages to store stored procedures, UDFs, and ML model files within Snowflake.

# Usage/Steps
To run locally,

1. Open terminal and clone this repo or use GitHub Desktop, since it is part of the snowflakecorp organisation you need to set up the authentification before cloning

2. Change to the Assignment2 directory and launch  JupyterLab

3. Paste the URL in a browser window and once JupyterLab comes up, switch to the work directory and make `creds.json` and give the details of your snoflake account, Warehouse, Database, and Schema details to reflect your snowflake environment.

4. To run streamlit (files), on your terminal run  `streamlit run files.py`
