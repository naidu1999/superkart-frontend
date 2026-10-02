import streamlit as st
import pandas as pd
import requests

BACKEND_URL = "https://naidu1999-superkart-sales-backend.hf.space/predict"

st.title("Superkart Sales Prediction ⚡")

st.markdown("Enter product and store details:")

# Inputs
product_id = st.text_input("Product ID", "FD6114")
product_weight = st.number_input("Product Weight", 0.0, 50.0, 12.66)
product_sugar_content = st.selectbox("Product Sugar Content", ["Low Sugar", "Regular", "No Sugar"])
product_allocated_area = st.number_input("Product Allocated Area", 0.0, 1.0, 0.027)
product_type = st.selectbox("Product Type", [
    "Frozen Foods", "Dairy", "Canned", "Baking Goods",
    "Health and Hygiene", "Snack Foods", "Soft Drinks",
    "Meat", "Fruits and Vegetables", "Household",
    "Breads", "Breakfast", "Hard Drinks",
    "Starchy Foods", "Others", "Seafood"
])
product_mrp = st.number_input("Product MRP", 0.0, 500.0, 117.08)
store_id = st.text_input("Store ID", "OUT004")
store_est_year = st.number_input("Store Establishment Year", 1900, 2025, 2009)
store_size = st.selectbox("Store Size", ["Small", "Medium", "High"])
store_city = st.selectbox("City Type", ["Tier 1", "Tier 2", "Tier 3"])
store_type = st.selectbox("Store Type", [
    "Supermarket Type1",
    "Supermarket Type2",
    "Departmental Store",
    "Food Mart"
])

store_age = 2025 - store_est_year

payload = {
    "Product_Id": product_id,
    "Product_Weight": product_weight,
    "Product_Sugar_Content": product_sugar_content,
    "Product_Allocated_Area": product_allocated_area,
    "Product_Type": product_type,
    "Product_MRP": product_mrp,
    "Store_Id": store_id,
    "Store_Establishment_Year": store_est_year,
    "Store_Size": store_size,
    "Store_Location_City_Type": store_city,
    "Store_Type": store_type,
    "Store_Age": store_age
}

if st.button("Predict Sales"):
    try:
        response = requests.post(BACKEND_URL, json=payload)
        result = response.json()

        if "prediction" in result:
            st.success(f"Predicted Sales: ₹ {result['prediction']:.2f}")
        else:
            st.error(result)

    except Exception as e:
        st.error(f"Backend connection failed: {e}")
