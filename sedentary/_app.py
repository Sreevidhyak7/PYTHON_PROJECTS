import json
from os import path
from time import sleep

import winsound
from win10toast import ToastNotifier

toaster = ToastNotifier()

#assets
#SUN_VALLEY_THEME = path.join("")

APP_ICON = path.join("assets", "app.ico")
COFFEE_ICON = path.join("assets", "coffe.ico")
DOLPHIN_WAV = path.join("assets", "dolphin.wav")



JSDATA: dict

def load_json():
    with open("appdata.json") as jsfile:
        return json.load(jsfile)

def update_json(data : dict):
    with open("appdata.json", "w") as jsfile:
        json.dump(data, jsfile, indent = 2)


#notifier
def _notify(msg, icon = COFFEE_ICON, title = None, soundfile = DOLPHIN_WAV):
    toaster.show_toast(
        title = title if title else "Notification",
        msg = msg,
        icon_path = icon,
        threaded=True,

    )

    if soundfile:
        winsound.PlaySound(soundfile, flags=winsound.SND_FILENAME)


def sed_alert():
    dt = load_json()

    if dt['sedentary_alert']:
        interval_secs = dt["interval"] * 6
        sleep(interval_secs)

        _notify(
            msg = "Blink your Eyes and Stretch your Body",
            
        )

        sed_alert()