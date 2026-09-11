import streamlit as st
import joblib
from pathlib import Path
import pandas as pd

st.title("Mc mathcing")
st.write("Please fill in the fields to see your kind of motorcykle")

Looks = st.selectbox(
    "Looks",
    ["Modern ","Classic", "Sport", "Adventure", "Retro", "Urban", "Off-road", "Cruiser", "Practical"]
)
Price = st.number_input("Price (SEK)", min_value=1000, max_value=1000000, value=5000)
Year = st.number_input("Year", min_value=1960, max_value=2026, value=1960)
AoU = st.selectbox(
    "Area of use",
    ["Off-road", "Touring", "Street", "Race", "Cruise"]
)
hp = st.selectbox(
    "Horse Power",
    ["<50", "<100", "<150", "Much power as possible"]
)
nos = st.selectbox(
    "Number of seats",
    [1, 2]
)

match_mc = pd.DataFrame({
        "Year": [Year],
        "Looks": [Looks],
        "Usage Type": [AoU],
        "horse power": [hp]
        #"numer of seats": []
    })

@st.cache_resource
def load_model():
    # Creating the path for the fetching of the valutation model
    model_path = Path(__file__).parent.parent / "models" / "motorcycle_classifier.joblib"
    # returning the path
    return joblib.load(model_path)

model = load_model()
st.success("Model loaded successfuly!")

if st.button("Predict"):
    prediction = model.predict(match_mc)
    
    st.success("Predikterad MC: ", prediction)

