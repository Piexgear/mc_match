import pandas as pd
import joblib
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "dataset" / "motorcycles_clean.csv"
MODEL_PATH = BASE_DIR / "streamlit" / "models" / "motorcycle_classifier.joblib"


def load_motorcycles():
    return pd.read_csv(DATA_PATH)


def load_model():
    return joblib.load(MODEL_PATH)


def recommend_motorcycles(
    preferred_looks,
    max_price,
    min_cc,
    max_cc,
    min_hp,
    max_hp,
    cylinders,
    seats
):
    df = load_motorcycles()
    model = load_model()

    preferred_cc = (min_cc + max_cc) / 2
    preferred_hp = (min_hp + max_hp) / 2

    classification = pd.DataFrame({
        "Looks": [preferred_looks],
        "Price (SEK)": [max_price],
        "Number of cc": [preferred_cc],
        "Horsepower": [preferred_hp],
        "Number of Cylinders": [cylinders],
        "Number of Seating": [seats]
    })

    probabilities = model.predict_proba(classification)[0]

    best_index = probabilities.argmax()
    best_class = model.classes_[best_index]

    matching_motorcycles = df[
        (df["Usage Type"] == best_class) &
        (df["Price (SEK)"] <= max_price) &
        (df["Number of cc"] >= min_cc) &
        (df["Number of cc"] <= max_cc) &
        (df["Horsepower"] >= min_hp) &
        (df["Horsepower"] <= max_hp) &
        (df["Number of Cylinders"] == cylinders) &
        (df["Number of Seating"] == seats) &
        (df["Looks"] == preferred_looks.strip())
    ].copy()

    return matching_motorcycles, best_class