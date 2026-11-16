import json
from os import path

# assets
ASSETS = "assets"

APP_ICO = path.join(ASSETS, "app.ico")
COFFE_ICO = path.join(ASSETS, "coffe.ico")
DOLPHIN_WAV = path.join(ASSETS, "dolphin.wav")

# data
JSDATA: dict

def load_json():
    with open('schedule.json') as jsfile:
        return json.load(jsfile)

def update_json(data: dict):
    with open('schedule.json', "w") as jsfile:
        json.dump(
            data, jsfile, indent=2
        )
