# Fuel Price Calculator

A simple Streamlit web app to calculate the total fuel cost for a trip based on distance, vehicle fuel efficiency, and current fuel price. The app features a custom background image for a more engaging user experience.

## Live Demo
Try the live application here: [Fuel Price Calculator](https://surjith-ap-fuel-price-calculator-main-qhtz2c.streamlit.app/)

## Features
- Calculate fuel required and total cost for a trip
- User-friendly form interface
- Instant results and helpful tips

## How to Run
1. Make sure you have Python installed.
2. Install Streamlit if you haven't already:
   ```bash
   pip install streamlit
   ```
   streamlit run main.py
   ```

## Calculation Formula
- **Fuel Required** = Distance ÷ Fuel Efficiency
- **Total Fuel Cost** = (Distance ÷ Fuel Efficiency) × Fuel Price per Liter

## Example
- Distance: 300 km
- Vehicle efficiency: 15 km/L
- Petrol price: ₹100/L

**Fuel required** = 300 ÷ 15 = 20 liters  
**Total cost** = 20 × ₹100 = ₹2,000

---
Made with Streamlit 🚗⛽