# Mc match
This is our school project for machine learning and we decided to make two models. 
One model is a classification model and the second one is a prediction model that validates price. 
# ================================================================================================
## Setup
### download the project
clone the repo to your computer by running the this commmand in the terminal in your wished directory: 
git clone git@github.com:Piexgear/mc_match.git

Now open up the project direcotry mc_match.

### virtual envirement setup
type this command for setting up your virtual envirement: 
python -m venv .venv 

### virtual envirement activate
now activate the venv by typing this command: 
#### Windows: 
source .venv/Scripts/activate

#### Mac/Linux:
source .venv/bin/activate

### installing dependecies 
type one of these commands depending on if you use pip or uv: 

#### pip: 
pip install requirements.txt

#### UV:
uv sync
# ================================================================================================
### Streamlit
If you want to try the models in the frontend type this command: 
streamlit run streamlit/app.py 
# ================================================================================================
## Versions
we run this project on these versions so you need to have at least these versions or a newer version for this project to work.
#### Python
3.12.14

#### pip
25.1.1

#### uv
0.11.16