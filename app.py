import streamlit as st

# Title and description
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Google Like Unit Converter")
st.write("Convert between different units instantly!")

# Dropdowns for conversion types
conversion_types = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Milligram": 1_000_000, "Pound": 2.20462, "Ounce": 35.274},
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# Select conversion category
conversion_category = st.selectbox("Choose a category:", list(conversion_types.keys()))

# Input for value to convert
value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Selecting units
if conversion_category != "Temperature":
    from_unit = st.selectbox("From:", conversion_types[conversion_category].keys())
    to_unit = st.selectbox("To:", conversion_types[conversion_category].keys())
else:
    from_unit = st.selectbox("From:", conversion_types["Temperature"])
    to_unit = st.selectbox("To:", conversion_types["Temperature"])

# Convert function
def convert(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value * (conversion_types[category][to_unit] / conversion_types[category][from_unit])

# Convert button
if st.button("Convert 🔄"):
    if from_unit == to_unit:
        st.warning("Select different units to convert!")
    else:
        result = convert(value, from_unit, to_unit, conversion_category)
        st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.write("Developed by Areesha Kainat using Streamlit")










