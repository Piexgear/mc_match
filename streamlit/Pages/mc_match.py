import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[2]))

import streamlit as st
from src.matcher import recommend_motorcycles


st.title("🏍️ Motorcycle Match")

st.write("Find the motorcycle that best matches your preferences.")


preferred_looks = st.selectbox(
    "What style do you prefer?",
    [
        "Modern",
        "Classic",
        "Sport",
        "Adventure",
        "Retro",
        "Urban",
        "Off-road",
        "Cruiser",
        "Practical"
    ]
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
    value=2
)


seats = st.selectbox(
    "Number of seats",
    [1, 2],
    index=1
)


if st.button("Find my motorcycle"):

    matching_motorcycles, best_class = recommend_motorcycles(
        preferred_looks=preferred_looks,
        max_price=max_price,
        min_cc=min_cc,
        max_cc=max_cc,
        min_hp=min_hp,
        max_hp=max_hp,
        cylinders=cylinders,
        seats=seats
    )

    st.success(
        f"According to your preferences, we recommend: **{best_class}**"
    )

    if matching_motorcycles.empty:

        st.warning(
            "No motorcycles match all of your requirements. "
            "Try adjusting your preferences."
        )

    else:

        st.subheader("Your matches")

        for _, motorcycle in matching_motorcycles.iterrows():

            st.write(
                f"### {motorcycle['Company']} "
                f"{motorcycle['Model']}"
            )

            st.write(
                f"**Price:** "
                f"{motorcycle['Price (SEK)']:,.0f} SEK"
            )

            st.write(
                f"**Engine:** "
                f"{motorcycle['Number of cc']:.0f} cc | "
                f"**Horsepower:** "
                f"{motorcycle['Horsepower']:.0f} hp"
            )

            st.write(
                f"**Cylinders:** "
                f"{motorcycle['Number of Cylinders']:.0f} | "
                f"**Seats:** "
                f"{motorcycle['Number of Seating']}"
            )

            st.write(
                f"**Style:** {motorcycle['Looks']} | "
                f"**Usage:** {motorcycle['Usage Type']}"
            )

            st.divider()