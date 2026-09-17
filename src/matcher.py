import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

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
        (df["Number of Seating"] == seats) 
    ].copy()


    if matching_motorcycles.empty:
        return matching_motorcycles, best_class

    # CC score
    def range_score(value, minimum, maximum):
        if minimum <= value <= maximum:
            return 1.0

        if value < minimum:
            return max(0, 1 - (minimum - value) / (maximum - minimum))

        return max(0, 1 - (value - maximum) / (maximum - minimum))

    matching_motorcycles["CC Score"] = matching_motorcycles[
        "Number of cc"
    ].apply(
        lambda value: range_score(value, min_cc, max_cc)
    )

    # Horsepower score
    matching_motorcycles["HP Score"] = matching_motorcycles[
        "Horsepower"
    ].apply(
        lambda value: range_score(value, min_hp, max_hp)
    )

    # Looks score
    matching_motorcycles["Looks Score"] = (
        matching_motorcycles["Looks"] == preferred_looks.strip()
    ).astype(float)

    # Cylinder score
    matching_motorcycles["Cylinder Score"] = (
        matching_motorcycles["Number of Cylinders"] == cylinders
    ).astype(float)

    # Final Match Score
    matching_motorcycles["Match Score"] = (
        matching_motorcycles["CC Score"] * 0.30 +
        matching_motorcycles["HP Score"] * 0.30 +
        matching_motorcycles["Looks Score"] * 0.20 +
        matching_motorcycles["Cylinder Score"] * 0.20
    )

    matching_motorcycles = matching_motorcycles.sort_values(
        "Match Score",
        ascending=False
    ).head(5)

    return matching_motorcycles, best_class