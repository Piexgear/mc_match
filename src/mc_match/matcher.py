from pathlib import Path
import pandas as pd
import joblib


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "dataset" / "motorcycles_clean.csv"
MODEL_PATH = BASE_DIR / "streamlit" / "models" / "motorcycle_classifier.joblib"

def load_motorcycles():
    df = pd.read_csv(DATA_PATH)
    return df

def load_model():
    model = joblib.load(MODEL_PATH)
    return model


def recommend_motorcycles(
        usage, 
        max_price,
        min_cc,
        max_cc,
        min_hp,
        max_hp,
        seats,
        preferred_looks
):
    df = load_motorcycles()

    recommendations = df[
        (df["Usage Type"] == usage) &
        (df["Price (SEK)"] <= max_price) &
        (df["Number of cc"] >= min_cc) &
        (df["Number of cc"] <= max_cc) &
        (df["Horsepower"] >= min_hp) &
        (df["Horsepower"] <= max_hp) &
        (df["Number of Seating"] == seats)
    ].copy()

    if recommendations.empty:
        return recommendations

    model = load_model()
    model_features = [ 
        "Number of cc", 
        "Horsepower", 
        "Number of Seating", 
        "Looks"
    ] 

    model_input = recommendations[model_features]

    probabilities = model.predict_proba(model_input)
    class_names = model.classes_

    usage_index = list(class_names).index(usage)

    recommendations["AI Score"] = probabilities[:, usage_index]

    preferred_cc = (min_cc + max_cc) / 2
    preferred_hp = (min_hp + max_hp) / 2

    recommendations["CC Score"] = ( 1 - abs(recommendations["Number of cc"] - preferred_cc) / (max_cc - min_cc) ) 

    recommendations["HP Score"] = ( 1 - abs(recommendations["Horsepower"] - preferred_hp) / (max_hp - min_hp) )

    recommendations["Looks Score"] = (
        recommendations["Looks"] == preferred_looks
    ).astype(float)

    recommendations["Match Score"] = ( 
        recommendations["Looks Score"] * 0.40 +
        recommendations["CC Score"] * 0.30 + recommendations["HP Score"] * 0.30 
    )

    recommendations = recommendations.sort_values( "Match Score", ascending=False )

    return recommendations



if __name__ == "__main__":
    result = recommend_motorcycles(
        usage="Street",
        max_price=150000,
        min_cc=600,
        max_cc=1000,
        min_hp=70,
        max_hp=120,
        seats=2,
        preferred_looks="Sport"
    )

    print(result[["Company", "Model", "Price (SEK)", "Usage Type", "Number of cc", "Horsepower", "Number of Seating", "Looks", "Looks Score", "Match Score"]])
