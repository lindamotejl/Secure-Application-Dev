# FoodleBot
## Setting up and activating a virtual environment
It is highly recommended (but not required) to create a virtual enrironment with conda. You can check whether the conda is install by running `conda -V` in your terminal.
```
conda create --name envname python=3.7 
conda activate envname
```
## Installing additional Python packages to a virtual environment
Make sure that you activated your virtual environment!
```
conda install ujson
conda install tensorflow
pip install rasa
```
Installing tensorflow with conda rather then pip will save you a lot of time.
## Setting environment variables
The value you assign to a temporary environment variable only lasts until you close the terminal session.
Assign a temporary environment variable with the export command:
```
export BOT_API_KEY=[your_api_key]
```
where `[your_api_key] ` is your Yelp Fusion API key.
## Starting an action server, loading a trained model and talking to chatbot on the command line.
Run these command to start an action server:
```
cd Secure-Application-Dev/rasachatbot
rasa run actions
```
Now when the action endpoint is up and running open a new command line window, cd into rasachatbot directory, activate the virtual environment and use `rasa shell` to talk with the chatbot.

