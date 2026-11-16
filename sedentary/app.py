from tkinter import Tk, ttk, StringVar, IntVar
from _app import *

# load app data
JSDATA = load_json()

# root window
App = Tk()
App.title("Sedentary Alert")
App.iconbitmap(APP_ICO)
App.resizable(False, False)

#user interface
frame = ttk.Frame(App, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

sedentary_alert = IntVar()
sedentary_alert.set(
    1 if JSDATA["sedentary_alert"]
                   else 0
)

def toggle_sed_alert():
    print(sedentary_alert.get())

sed_check = ttk.Checkbutton(
    frame, variable=sedentary_alert,
    text="Sedentary Alert", command=toggle_sed_alert
)

sed_check.grid(row=0, column=0, pady=5, columnspan=2)

sed_lbl = ttk.Label(frame, text="Interval")
sed_lbl.grid(row=1, column=0, pady=5, )


def interval_change(interval):
    print(interval)

interval_opt = ["20 min", "15 min", "30 min", "45 min"]
interval_period = StringVar()
interval_period.set(f'{JSDATA["interval"]} min')

interval_dropdown = ttk.OptionMenu(
    frame, interval_period, "Select",
    *interval_opt,  command=interval_change
)
interval_dropdown.grid(row=1, column=1, pady=5)



App.mainloop()