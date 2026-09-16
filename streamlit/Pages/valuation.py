import streamlit as st
import joblib
from pathlib import Path
import pandas as pd

st.title("Valuat your MC")
st.write("Please fill in the information needed to see the value on your MC")

brand = st.selectbox(
    "Brand",
    [
        "Benelli",
        "Husqvarna",
        "Mutt Motorcycles",
        "Harley-Davidson",
        "KTM",
        "Triumph",
        "Genuine Scooters",
        "BMW",
        "Beta",
        "Honda",
        "Royal Enfield",
        "GasGas",
        "TVS",
        "Kawasaki",
        "Moto Guzzi",
        "Suzuki",
        "Yamaha",
        "Bajaj",
        "Hero",
        "Jawa",
        "Keeway",
        "Aprilia",
        "Brixton Motorcycles",
        "Buell Motorcycle Company",
        "Cagiva",
        "Ducati",
        "Indian",
        "Mahindra",
        "MV Agusta",
        "Piaggio",
        "SYM",
        "Vespa",
        "Sherco",
        "Victory",
        "Hanway",
        "Zero Motorcycles",
        "Sinnis",
        "SWM",
        "Super Soco",
        "Energica Motor Company",
        "CCM",
        "CFMOTO",
        "Daelim",
        "Kymco",
        "Leonart",
        "Lifan",
        "Norton",
        "Moto Morini",
        "Vmoto Soco",
        "Lexmoto",
        "Mash",
        "Aeon",
        "UM Motorcycles",
        "NIU",
        "Royal Alloy",
        "Zontes",
        "Confederate",
        "Peugeot",
        "FB Mondial",
        "Can-Am",
        "Scomadi",
        "AJS",
        "Lambretta",
        "Triton Electric Bikes",
        "Apollo",
        "Hero Electric",
        "Ampere",
        "Ontrack",
        "Derbi",
        "Italjet",
        "Segway",
        "Arcfox",
        "Hyosung",
        "Fantic",
        "Larry vs Harry",
    ]
)

country = st.text_input(label="Country")

transmission = st.text_input(label="Transmission")

drivetrain = st.text_input(label="Drivetrain")

Looks = st.selectbox(
    "Looks",
    ["Modern ","Classic", "Sport", "Adventure", "Retro", "Urban", "Off-road", "Cruiser", "Practical"]
)

bt = st.selectbox(
    "Body type",
    ["Adventure", "Cafe Racer", "Cruiser", "Enduro", "Naked/Street", "Scooter", "Scrambler", "Sport", "Standard"]
)

Year = st.number_input("Year", min_value=1960, max_value=2026, value=1960)

reference_year = 2020
base_reduction_percent = 45.0
reduction_per_year_older = 1
reduction_per_year_newer = 5.0
min_reduction_percent = 15.0
max_reduction_percent = 75.0
if Year < reference_year:
    years_older = reference_year - Year
    adjustment_percent = min(
        max_reduction_percent,
        base_reduction_percent + years_older * reduction_per_year_older,
    )
else:
    years_newer = Year - reference_year
    adjustment_percent = max(
        min_reduction_percent,
        base_reduction_percent - years_newer * reduction_per_year_newer,
    )

torque = st.number_input("Torque", min_value=3, max_value=301, value=3)

num_of_cc = st.number_input("CC", min_value=7, max_value=2500, value=7)

hp = st.number_input("Horse Power", min_value=10, max_value=600, value=10)

nos = st.selectbox(
    "Number of seats",
    [1, 2]
)

number_of_cylinder = st.selectbox(
    "Number of cylinders",
    [1, 2, 3, 4]
)

Valuation = pd.DataFrame({
        "Company": [brand],
        "Looks": [Looks],
        "Body Type": [bt],
        "Year": [Year],
        "Torque": [torque],
        "Number of cc": [num_of_cc],
        "Horsepower": [hp],
        "Number of Seating": [nos],
        "Number of Cylinders": [number_of_cylinder],
        "Country of Origin": [country], 
        "Transmission Type": [transmission], 
        "Drivetrain": [drivetrain]
    })

# categorical_features = [
#     "Model",
#     "Country of Origin", 
#     "Transmission Type", 
#     "Drivetrain"
# ]



@st.cache_resource
def load_model():
    # Creating the path for the fetching of the valutation model
    model_path = Path(__file__).parent.parent / "models" / "Random_forest_model.joblib"
    # returning the path
    return joblib.load(model_path)

model = load_model()
st.success("Model loaded successfuly!")

if st.button("Predict"):
    prediction = model.predict(Valuation)
    raw_prediction = float(prediction[0])
    adjusted_prediction = max(0, raw_prediction * (1 - adjustment_percent / 100))
    st.success(
        f"Predikterade värde: {adjusted_prediction:,.0f} SEK "
    )



#Naked/Street

# Year

# 2006


# Torque

# 75


# CC

# 750


# Horse Power

# 110


# Number of seats

# 2

# Number of cylinders

# 4

