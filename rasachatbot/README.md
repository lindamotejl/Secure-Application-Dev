# foodlechatbot

## rasa installation
run these commands to install rasa:
```
conda create --name envname python=3.7 
conda activate envname
conda install ujson
conda install tensorflow
pip install rasa
export BOT_API_KEY=<enter API key>
```
then run the chatbot:
```
cd rasachatbot
rasa train
rasa run actions
rasa shell
```
