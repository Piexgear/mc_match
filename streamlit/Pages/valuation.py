import streamlit as st
import joblib
from pathlib import Path

st.title("Valuat your MC")
st.write("Please fill in the information needed to see the value on your MC")


@st.cache_resource
def load_model():
    # Creating the path for the fetching of the valutation model
    model_path = Path(__file__).parent.parent / "models" / "valutation_model.pkl"
    # returning the path
    return joblib.load(model_path)

model = load_model()
st.success("Model loaded successfuly!")

if st.button("Predict"):
    prediction = model.predict

