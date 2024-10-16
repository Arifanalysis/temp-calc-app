import streamlit as st
import matplotlib.pyplot as plt

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

# Function to generate background color based on temperature
def get_temperature_color(temp, scale):
    if scale == "Celsius":
        temp_range = [-50, 50]  # Assuming Celsius temperature range for color scaling
    elif scale == "Fahrenheit":
        temp_range = [-58, 122]  # Fahrenheit equivalent
    else:
        temp_range = [223.15, 323.15]  # Kelvin range

    # Normalize the temperature for color scaling
    norm_temp = (temp - temp_range[0]) / (temp_range[1] - temp_range[0])
    norm_temp = max(0, min(1, norm_temp))  # Keep it within [0, 1]

    # Use a color scale from blue (cold) to red (hot)
    return plt.cm.coolwarm(norm_temp)[:3]  # Extract RGB values

# Streamlit UI
st.title("🌡️ Temperature Converter with Color Scale 🌡️")

# Input temperature
temp_input = st.number_input("Enter the temperature you want to convert:", value=0.0)

# Choose input and output scale
input_scale = st.selectbox("Choose the input scale:", ("Celsius", "Fahrenheit", "Kelvin"))
output_scale = st.selectbox("Choose the output scale:", ("Celsius", "Fahrenheit", "Kelvin"))

# Convert and display background color
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
    
    # Get color for the input temperature
    temp_color = get_temperature_color(temp_input, input_scale)
    
    # Convert RGB tuple to hex color code
    temp_color_hex = '#%02x%02x%02x' % (int(temp_color[0] * 255), int(temp_color[1] * 255), int(temp_color[2] * 255))

    # Display the result with background color
    st.markdown(f"<div style='padding:10px; border-radius:5px; background-color:{temp_color_hex}; color:white; text-align:center; font-size:24px;'>The converted temperature is: {converted_temp:.2f} {output_scale}</div>", unsafe_allow_html=True)

# Adding footer with color scale reference
st.markdown("""
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: grey;
        background-color: #f5f5f5;
        padding: 10px;
        border-top: 1px solid #eaeaea;
    }
    </style>
    <div class="footer">
        <p><strong>Color Scale:</strong> Blue = Cold, Red = Hot</p>
    </div>
    """, unsafe_allow_html=True)
