import streamlit as st

# Set page config
st.set_page_config(page_title="Weather App", page_icon="☀️")

# Sidebar
st.sidebar.title("☀️ Weather Forecast App")
st.sidebar.write("Enter the name of a city to view a simulated weather report.")

# Input from user
city = st.sidebar.text_input("City Name", "Bahawalnagar")

# Mock weather data
def get_mock_weather(city_name):
    sample_data = {
        "Bahawalnagar": {
            "country": "PK",
            "description": "clear sky",
            "temp": 34,
            "humidity": 30,
            "wind": 3.5
        },
        "Lahore": {
            "country": "PK",
            "description": "light rain",
            "temp": 29,
            "humidity": 60,
            "wind": 5.2
        },
        "Karachi": {
            "country": "PK",
            "description": "haze",
            "temp": 31,
            "humidity": 50,
            "wind": 4.8
        }
    }
    return sample_data.get(city_name.title())

# Display results
if city:
    data = get_mock_weather(city)
    if data:
        st.title(f"🌇 Weather in {city.title()}, {data['country']}")
        st.write(f"**Condition:** {data['description'].title()}")
        st.write(f"**Temperature:** {data['temp']} ℃")
        st.write(f"**Humidity:** {data['humidity']}%")
        st.write(f"**Wind Speed:** {data['wind']} m/s")
    else:
        st.warning("City not found in sample data. Try Bahawalnagar, Lahore, or Karachi.")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit |M Abdullah")
