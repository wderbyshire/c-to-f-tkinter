import tkinter as tk
from settings import *


class TemperatureConverture(tk.Tk):
    """
    The root application which contains all the widgets and logic for the running of the app
    """
    def __init__(self):
        super().__init__()

        # Set the size of the app window to the prepared values in settings file
        self.geometry(GEOMETRY)

        # Set the title of the window to the prepared value in settings file
        self.title(ROOT_TITLE)

        # Sets the icon for the app window
        self.iconbitmap(default="app-icon.ico")


if __name__ == "__main__":
    app = TemperatureConverture()
    app.mainloop()
