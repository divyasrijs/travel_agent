import streamlit as st
import cohere

# Initialize Cohere client
co = cohere.Client('aBu7GGmHlDVV0rfxBXBlTlIwFvPoIE2PD8uLkHtO')

# Function to generate itinerary
def get_itinerary(destination, days, interests):
    prompt = f"Plan a {days}-day itinerary for a trip to {destination} focusing on {interests}."
    response = co.generate(
        model='command-r-plus',
        prompt=prompt,
        max_tokens=600
    )
    return response.generations[0].text.strip()

# Streamlit app
st.title("🌍 AI Travel Itinerary Planner")

destination = st.text_input("Where are you traveling to?")
days = st.number_input("Number of days", min_value=1, step=1)
interests = st.text_input("What are your interests? (e.g., adventure, relaxation, culture)")

if destination and days and interests:
    itinerary = get_itinerary(destination, days, interests)
    st.subheader("🧳 Your Travel Itinerary")
    st.write(itinerary)
else:
    st.info("Please fill in all fields to generate your itinerary.")
