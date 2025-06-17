import streamlit as st
st.set_page_config(page_title="Fuel Price Calculator",page_icon="📃",layout="centered")
st.title("Fuel Price Calculator")
st.markdown("Enter The Details to Get Your Fuel Cost")

with st.form("Fuel Calculator"):
    st.subheader("Trip Details")
    
    distance = st.number_input(
        "Distance (Kilometers)", 
        min_value=0.0, 
        value=0.0, 
        step=1.0,
        help="Enter the total distance of your trip"

    )
    fuel_eff = st.number_input(
        "Fuel Efficency (Km/L)", 
        min_value=0.0, 
        value=0.0, 
        step=1.0,
        help="Enter Your Vehicles Fuel efficency"

    )
    fuel_price = st.number_input(
        "Fuel Price Per liter", 
        min_value=0.0, 
        value=0.0, 
        step=1.0,
        help="Enter the current fuel price in liter"

    )
    
    submitted = st.form_submit_button("Calculate Fuel Cost")

if submitted:
    if distance > 0 and fuel_eff > 0 and fuel_price > 0:

        fuel_needed = distance / fuel_eff
        fuel_cost = fuel_needed * fuel_price

        st.success("✅ Calculation Complete!")

        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Fuel Needed", f"{fuel_needed:.2f} L")
        
        with col2:
            st.metric("Total Cost", f"₹{fuel_cost:.2f}")
    else:
        st.error("⚠️ Please enter valid positive values for all fields!")

st.markdown("---")
st.markdown("💡 **Tip:** Keep track of your fuel efficiency to plan better trips!")       

