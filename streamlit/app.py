import streamlit as st



home = st.Page(
    "Pages/home.py",
    title="Home",
    default=True
)

match = st.Page(
    "Pages/mc_match.py",
    title="Mc match",
)

valuation = st.Page(
    "Pages/valuation.py",
    title="Valuation",
)

pg = st.navigation([
    home,
    match,
    valuation
])

pg.run()