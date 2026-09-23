# Mc match
This is our school project for machine learning and we decided to make two models. 
One model is a classification model and the second one is a prediction model that validates price. 

---

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
