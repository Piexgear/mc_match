# Mc Match

MC Match is a comprehensive data-driven platform designed to simplify motorcycle selection and market analysis. By integrating a custom machine learning pipeline with a streamlined user interface, MC Match provides motorcycle enthusiasts and industry stakeholders with personalized motorcycle suggestions and data-informed market price estimations.

## Live Demo
**Demo link:** [mcmatch.streamlit.app/mc_match](https://mcmatch.streamlit.app/mc_match)

### How it works:
- **Use MC Match**
  1. **Select Preferences:** Enter your desired motorcycle characteristics (e.g., horsepower, torque, budget).
  2. **Get a Match:** The system will predict the best "Usage Type" and suggest the top 5 motorcycles that match your needs.
- **Use the Valuation tool**
  1. **Select Preferences:** Enter your motorcycle's characteristics (e.g., horsepower, torque, budget).
  2. **Price Estimation:** The property details are used to estimate the market price of the motorcycle.

## Data Source
The motorcycle specifications and market data used in this project are sourced from [2023 Bike Model Dataset](https://www.kaggle.com/datasets/peshimaammuzammil/2023-bike-model-dataset-all-data-you-need?select=bikes_data.csv) available on Kaggle.

This dataset provides comprehensive technical specifications for a wide range of motorcycle models, which serves as the foundation for our matching algorithms and market valuation estimates.

## Tech Stack
- **Frontend:** Streamlit
- **Backend/ML Pipeline:** Python, Scikit-Learn, NumPy, SciPy
- **Data Management:** Pandas, SQLite
- **Package Management:** pip, uv

## Installation

### Prerequisites
- Python 3.12+
- `pip` or `uv` package manager

### Getting Started

1. **Clone and Navigate**

   Clone the repository and navigate into the project directory:
   ```sh
   git clone git@github.com:Piexgear/mc_match.git
   cd mc_match
   ```

2. **Environment Setup**

   Create a virtual environment:
   - *Standard:* `python -m venv .venv`
   - *Using uv:* `uv venv`

   Activate the environment:
   - **Windows:** `.venv\Scripts\activate`
   - **macOS/Linux:** `source .venv/bin/activate`

3. **Install Dependencies**

   Choose one of the following methods:

   *Using pip:*
   ```sh
   python -m pip install -r requirements.txt
   ```
   *Using uv:*
   ```sh
   uv sync
   ```

4. **Data Initialization**

   Initialize the database using the internal data import script:
   ```sh
   python -m src.import_data
   ```

5. **Run the Application**

   Launch the Streamlit frontend:
   ```sh
   streamlit run streamlit/app.py
   ```

## Versions
This project was developed using the following versions (or newer):
- **Python:** 3.12.14
- **pip:** 25.1.1
- **uv** 0.11.16
