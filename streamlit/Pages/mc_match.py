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

cylinders = st.slider(
    "Cylinders",
    min_value=1,
    max_value=5,
    value=1
)

seats = st.selectbox(
    "Number of seats",
    [1, 2],
    index=1
)

preferred_cc = (min_cc + max_cc) / 2
preferred_hp = (min_hp + max_hp) / 2

classification = pd.DataFrame({
        "Looks": [preferred_looks],
        "Number of cc": [preferred_cc],
        "Horsepower": [preferred_hp],
        "Number of Seating": [seats],
        "Number of Cylinders":[cylinders],
        "Price (SEK)": [max_price]
    })

#missing: {'Transmission Type', 'Number of Cylinders', 'Drivetrain', 'Country of Origin', 'Year', 'Engine Type', 'Torque'}
# categorical_features_2 = [
#     "Looks",
#     "Country of Origin",
#     "Engine Type",
#     "Drivetrain",
#     "Transmission Type"
# ]
# X_3 = df[numeric_features + categorical_features_2]
# y_3 = df["Usage Type"]

@st.cache_resource
def load_model():
    # Creating the path for the fetching of the valutation model
    model_path = Path(__file__).parent.parent / "models" / "motorcycle_classifier_test.joblib"
    # returning the path
    return joblib.load(model_path)

model = load_model()
st.success("Model loaded successfuly!")


if st.button("Predict"): 
    df = pd.read_csv("dataset/motorcycles_clean.csv")

    # Gör Price (SEK) till numeriska värden
    df["Price (SEK)"] = pd.to_numeric(
        df["Price (SEK)"],
        errors="coerce"
    )

    probabilities = model.predict_proba(classification)[0]

    best_index = probabilities.argmax()
    best_class = model.classes_[best_index]

    best_probability = probabilities[best_index]

    # Filtrera på klass + maxpris
    matching_motorcycles = df[
        (df["Usage Type"] == best_class) &
        (df["Price (SEK)"] <= max_price)
    ]

    st.success(
        f"Bästa klass: {best_class} "
        f"({best_probability:.1%})"
    )

    st.subheader(
        f"Motorcyklar inom {best_class} "
        f"och under {max_price:,} SEK"
    )

    st.dataframe(matching_motorcycles[["Company","Model", "Body Type","Price (SEK)"]], hide_index=True)
