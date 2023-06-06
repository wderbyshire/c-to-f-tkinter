import tkinter as tk
from settings import *


class TemperatureConverture(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry(GEOMETRY)


if __name__ == "__main__":
    app = TemperatureConverture()
    app.mainloop()
