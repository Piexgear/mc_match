import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src import import_data as id
id.migrate_data()

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