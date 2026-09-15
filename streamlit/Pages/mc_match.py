import streamlit as st
import joblib
from pathlib import Path
import pandas as pd
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

from src.mc_match.matcher import recommend_motorcycles

st.title("Motorcycle Match")

st.write("Find the motorcycle that best matches your preferences.")

#User preferences

usage = st.selectbox(
    "What till you mainly use the motorcycle for?",
    ["Street", "Cruise", "Race", "Off-road", "Touring"]
)

preferred_looks = st.selectbox(
    "What style do you prefer?",
    ["Modern ","Classic", "Sport", "Adventure", "Retro", "Urban", "Off-road", "Cruiser", "Practical"]
)

max_price = st.number_input(
    "Maximum budget (SEK)",
    min_value=10000,
    max_value=1000000,
    value=80000,
    step=5000
)

min_cc, max_cc = st.slider(
    "Engine size (cc)",
    min_value=100,
    max_value=2500,
    value=(600, 1000),
    step=50
)

min_hp, max_hp = st.slider(
    "Horsepower",
    min_value=10,
    max_value=500,
    value=(70, 120),
    step=5
)

seats = st.selectbox(
    "Number of seats",
    [1, 2],
    index=1
)

if st.button("Find my motorcycle"):
    result = recommend_motorcycles( 
        usage=usage, 
        max_price=max_price, 
        min_cc=min_cc, 
        max_cc=max_cc, 
        min_hp=min_hp, 
        max_hp=max_hp, 
        seats=seats, 
        preferred_looks=preferred_looks 
    )

    if result.empty:
        st.warning(
            "No motorcycles match all of your requirements."
            "Try adjusting your filters."
        )

    else:
        st.subheader("Your top matches")
        for _, motorcycle in result.iterrows():
            st.write(
                f"### {motorcycle['Company']} {motorcycle['Model']}"
            )
            st.write(
                f"**Price:** {motorcycle['Price (SEK)']:,.0f} SEK"
            )
            st.write(
                f"**Engine:** {motorcycle['Number of cc']:.0f} cc | " f"**Horsepower:** {motorcycle['Horsepower']:.0f} hp"
            ) 
            st.write( 
                f"**Style:** {motorcycle['Looks']} | " f"**Usage:** {motorcycle['Usage Type']}" 
            ) 
            st.write( 
                f"**Match Score:** {motorcycle['Match Score']:.0%}" 
            ) 
            st.divider()


# Year = st.number_input("Year", min_value=1960, max_value=2026, value=1960)



# @st.cache_resource
# def load_model():
#     # Creating the path for the fetching of the valutation model
#     model_path = Path(__file__).parent.parent / "models" / "motorcycle_classifier.joblib"
#     # returning the path
#     return joblib.load(model_path)

# model = load_model()
# st.success("Model loaded successfuly!")


