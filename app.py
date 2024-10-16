import streamlit as st

# Functions to convert temperatures
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

# Streamlit UI
st.title("Temperature Converter")

# Input temperature
temp_input = st.number_input("Enter the temperature you want to convert:", value=0.0)

# Choose input and output scale
input_scale = st.selectbox("Choose the input scale:", ("Celsius", "Fahrenheit", "Kelvin"))
output_scale = st.selectbox("Choose the output scale:", ("Celsius", "Fahrenheit", "Kelvin"))

# Conversion logic
if st.button("Convert"):
    if input_scale == "Celsius":
        if output_scale == "Fahrenheit":
            converted_temp = celsius_to_fahrenheit(temp_input)
        elif output_scale == "Kelvin":
            converted_temp = celsius_to_kelvin(temp_input)
        else:
            converted_temp = temp_input  # If both scales are same
    elif input_scale == "Fahrenheit":
        if output_scale == "Celsius":
            converted_temp = fahrenheit_to_celsius(temp_input)
        elif output_scale == "Kelvin":
            converted_temp = fahrenheit_to_kelvin(temp_input)
        else:
            converted_temp = temp_input
    elif input_scale == "Kelvin":
        if output_scale == "Celsius":
            converted_temp = kelvin_to_celsius(temp_input)
        elif output_scale == "Fahrenheit":
            converted_temp = kelvin_to_fahrenheit(temp_input)
        else:
            converted_temp = temp_input
    
    # Display result
    st.success(f"The converted temperature is: {converted_temp:.2f} {output_scale}")

