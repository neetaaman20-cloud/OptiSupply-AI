import streamlit as st
import joblib
import pandas as pd

st.set_page_config(page_title="OptiSupply AI", page_icon="📦")

st.title("OptiSupply AI 📦")
st.subheader("Predictive Inventory Demand")

# Load the saved model
try:
    model = joblib.load('demand_model.pkl')
except:
    st.error("Model file not found! Please run 'python3 model_trainer.py' first.")

# User Inputs
day = st.slider("Select Day of the Year", 1, 365, 50)
dow = st.selectbox("Select Day of the Week", 
                   options=[0, 1, 2, 3, 4, 5, 6], 
                   format_func=lambda x: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"][x])

if st.button("Predict Stock Demand"):
    # FIX: Create a DataFrame for the prediction to avoid warnings/errors
    input_data = pd.DataFrame([[day, dow]], columns=['day_of_year', 'day_of_week'])
    prediction = model.predict(input_data)
    
    st.metric(label="Estimated Units Needed", value=f"{int(prediction[0])} units")
    st.info("Tip: Higher demand is usually predicted for weekends!")