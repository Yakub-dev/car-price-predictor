
import pandas as pd
import pickle as pk 
import streamlit as st 

# Load the model
model = pk.load(open('car_price_predection.pkl', 'rb'))

# Title and labels
st.header('🚗 CARS PRICE PREDICTOR')
st.subheader('🔢 Label Key for Inputs:')
st.markdown("""
- **Fuel_Type**:  
   `0 = Petrol`  
   `1 = Diesel`  
   `2 = CNG`

- **Seller_Type**:  
   `0 = Dealer`  
   `1 = Individual`

- **Transmission**:  
   `0 = Manual`  
   `1 = Automatic`
""")

# User inputs
year = st.text_input('Year (e.g. 2015)')
price = st.text_input('Present Price (in lakhs)')
driven = st.text_input('Kilometers Driven')
fuel = st.text_input('Fuel Type (0=Petrol, 1=Diesel, 2=CNG)')
sel = st.text_input('Seller Type (0=Dealer, 1=Individual)')
trans = st.text_input('Transmission Type (0=Manual, 1=Automatic)')
own = st.text_input('Owner (e.g. 0, 1, 2 for number of previous owners)')

# Predict button
if st.button("Predict Price"):

    # Convert all inputs to float or int
    try:
        input_data = pd.DataFrame([[int(year), float(price), int(driven), int(fuel), int(sel), int(trans), int(own)]],
                                  columns=['Year', 'Present_Price', 'Kms_Driven', 'Fuel_Type', 'Seller_Type', 'Transmission', 'Owner'])

        output = model.predict(input_data)
        st.success(f"💰 Predicted Car Price: ₹ {output[0]*100000:.2f}")
    
    except ValueError:
        st.error("❌ Please enter valid numeric inputs.")
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8051))
    import streamlit.web.cli as stcli
    import sys
    sys.argv = ["streamlit", "run", "app.py", "--server.port", str(port), "--server.enableCORS", "false"]
    sys.exit(stcli.main())
