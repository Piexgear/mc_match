import pandas as pd
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "dataset" / "motorcycles_clean.csv"
MODEL_PATH = BASE_DIR / "streamlit" / "models" / "motorcycle_classifier.joblib"

def load_motorcycles() -> pd.DataFrame:
    try:
        return pd.read_csv(DATA_PATH)
    except FileNotFoundError:
        print(f"Error: Data file not found at {DATA_PATH}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error loading motorcycles: {e}")
        return pd.DataFrame()

def load_model() -> any:
    try:
        return joblib.load(MODEL_PATH)
    except FileNotFoundError:
        print(f"Error: Model file not found at {MODEL_PATH}")
        raise
    except Exception as e:
        print(f"Error loading model: {e}")
        raise

def recommend_motorcycles(
    preferred_looks: str,
    max_price: float,
    min_cc: float,
    max_cc: float,
    min_hp: float,
    max_hp: float,
    cylinders: int,
    seats: int
) -> tuple[pd.DataFrame, str]:
    df = load_motorcycles()
    if df.empty:
        return df, "No data loaded"
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

    # Higher scores awarded to bikes closest to the target within a range
    def range_score(value: float, minimum: float, maximum: float) -> float: 
        # value is in range
        if minimum <= value <= maximum:
            return 1.0
        
        diff = maximum - minimum
        # prevent division by zero
        if diff == 0.0:
            diff = 1.0
        # value is below minimum
        if value < minimum:
            return max(0.0, 1.0 - (minimum - value) / diff)
        # value is above maximum
        else:
            return max(0.0, 1.0 - (value - maximum) / diff)

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