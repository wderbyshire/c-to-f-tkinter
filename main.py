import tkinter as tk
from settings import *


class TemperatureConverture(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry(GEOMETRY)
        self.title(ROOT_TITLE)
        self.iconbitmap(default="app-icon.ico")

        self.temp_input = TemperatureInput()
        self.temp_input.grid(column=0, columnspan=2, row=1, sticky=tk.NSEW, padx=5, pady=5)

        self.rowconfigure([0, 1, 2], weight=1)
        self.columnconfigure([0, 1, 2], weight=1)


class TemperatureInput(tk.Entry):
    def __init__(self):
        super().__init__()

        self.default_input_string = "Type your temperature here"
        self.input_variable = tk.StringVar(value=self.default_input_string)
        self.configure(font=("Segoe UI", 13),
                       textvariable=self.input_variable,
                       foreground=INACTIVE_TEXT_COLOR)




if __name__ == "__main__":
    app = TemperatureConverture()
    app.mainloop()
