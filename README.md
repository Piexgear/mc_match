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

## Setup
### download the project
clone the repo to your computer by running the this commmand in the terminal in your wished directory: 
```sh
git clone git@github.com:Piexgear/mc_match.git
```

Now open up the projects directory mc_match.

### virtual envirement setup
type this command for setting up your virtual envirement: 

```sh
python -m venv .venv
```

#### or

```sh
uv venv
```

### virtual envirement activate
now activate the venv by typing this command: 
#### Windows: 
```sh
source .venv/Scripts/activate
```

#### Mac/Linux:
```sh
source .venv/bin/activate
```

### installing dependecies 
type one of these commands depending on if you use pip or uv: 

#### pip: 
```sh
python -m pip install -r requirements.txt
```

#### UV:
```sh
uv sync
```

### Initalize the database:
```sh
python -m src.import_data
```

---


### Streamlit
If you want to try the models in the frontend type this command: 
```sh
streamlit run streamlit/app.py 
```

#### or 

```sh
cd streamlit
streamlit run app.py
```
---

## Versions
we run this project on these versions so you need to have at least these versions or a newer version for this project to work.
#### Python
3.12.14

#### pip
25.1.1

#### uv
0.11.16
