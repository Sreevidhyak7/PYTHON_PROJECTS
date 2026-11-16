from tkinter import Tk, ttk, StringVar, IntVar
from _app import *


# root window
App = Tk()
App.title("Sedentary Alert")
App.iconbitmap(APP_ICO)
App.resizable(False, False)

#user interface
frame = ttk.Frame(App, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

sedentary_alert = IntVar()



sed_check = ttk.Checkbutton(
    frame, variable=sedentary_alert,
    text="Sedentary Alert"
)

sed_check.grid(row=0, column=0, pady=10)


App.mainloop()