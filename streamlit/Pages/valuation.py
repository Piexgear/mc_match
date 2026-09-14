import streamlit as st
import joblib
from pathlib import Path
import pandas as pd

st.title("Valuat your MC")
st.write("Please fill in the information needed to see the value on your MC")

Looks = st.selectbox(
    "Looks",
    ["Modern ","Classic", "Sport", "Adventure", "Retro", "Urban", "Off-road", "Cruiser", "Practical"]
)

bt = st.selectbox(
    "Body type",
    ["Adventure", "Cafe Racer", "Cruiser", "Enduro", "Naked/Street", "Scooter", "Scrambler", "Sport", "Standard"]
)

Year = st.number_input("Year", min_value=1960, max_value=2026, value=1960)

hp = st.selectbox(
    "Horse Power",
    ["<50", "<100", "<150", "Much power as possible"]
)
nos = st.selectbox(
    "Number of seats",
    [1, 2]
)

Valuation = pd.DataFrame({
        "Year": [Year],
        "Looks": [Looks],
        "Body Type": [bt],
        "Horsepower": [hp],
        "Number of Seating": [nos]
    })

@st.cache_resource
def load_model():
    # Creating the path for the fetching of the valutation model
    model_path = Path(__file__).parent.parent / "models" / "Valuation_model.joblib"
    # returning the path
    return joblib.load(model_path)

model = load_model()
st.success("Model loaded successfuly!")

if st.button("Predict"):
    prediction = model.predict(Valuation)
    st.success("Predikterad värde för : ", Valuation)


# ValueError: columns are missing: {'Price (SEK)', 'Horsepower', 'Number of Seating', 'Number of Cylinders', 'Company', 'Torque', 'Number of cc'}
