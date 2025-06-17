import streamlit as st
import base64
from pathlib import Path


st.set_page_config(page_title="Fuel Price Calculator",page_icon="📃",layout="centered")
st.title("Fuel Price Calculator")

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Get the base64 string of an image
def get_img_with_href(local_img_path):
    img_format = local_img_path.suffix[1:]
    bin_str = get_base64_of_bin_file(local_img_path)
    return f"data:image/{img_format};base64,{bin_str}"

# Path to your image
image_path = Path("assets/fuelPump.jpg").resolve()
background_image = get_img_with_href(image_path)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{background_image}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

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

