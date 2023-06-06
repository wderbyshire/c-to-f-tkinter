import tkinter as tk
from settings import *
import utils
from PIL import Image, ImageTk


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

        self.c_to_f = True

        self.temp_input = TemperatureInput()
        self.temp_input.grid(column=0, columnspan=2, row=1, sticky=tk.NSEW, padx=5)

        self.input_label_sv = tk.StringVar(value="Temperature (C)")
        self.input_label = tk.Label(
            font=(PRIMARY_FAMILY, LABEL_SIZE),
            textvariable=self.input_label_sv,
            anchor="sw",
        )
        self.input_label.grid(column=0, columnspan=2, row=0, sticky=tk.NSEW, padx=5, pady=5)

        self.convert_button = tk.Button(
            self,
            text="Convert",
            font=(PRIMARY_FAMILY, LABEL_SIZE),
            command=self.convert_temp
        )

        self.convert_button.grid(row=2, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.output_label_sv = tk.StringVar(value="Result (F)")
        self.output_label = tk.Label(
            font=(PRIMARY_FAMILY, LABEL_SIZE),
            textvariable=self.output_label_sv,
            anchor="sw",
        )

        self.output_label.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)

        raw_image = Image.open("refresh.png")
        resized_image = raw_image.resize((10, 10), Image.LANCZOS)
        self.button_image = ImageTk.PhotoImage(resized_image)
        self.swap_conversion = tk.Button(
            self,
            image=self.button_image,
            command=self.swap_conversion
        )
        self.swap_conversion.grid(row=2, column=1, sticky=tk.NSEW, padx=5, pady=5)

        self.output_variable = tk.StringVar()
        self.output = tk.Label(
            font=(PRIMARY_FAMILY, 13, "bold"),
            textvariable=self.output_variable,
        )

        self.output.grid(row=1, column=2, sticky=tk.NSEW, padx=5, pady=5)

        self.rowconfigure([0, 1, 2], weight=1)
        self.columnconfigure([0, 1, 2], weight=1)

    def convert_temp(self):
        if self.temp_input.get() == "":
            self.output_variable.set("0°")
        else:
            if self.c_to_f:
                answer = round((float(self.temp_input.get()) * (9/5)) + 32, 1)
            else:
                answer = round((float(self.temp_input.get()) - 32) * (5/9), 1)

            self.output_variable.set(str(answer) + "°")

    def swap_conversion(self):
        if self.c_to_f:
            self.input_label_sv.set("Temperature (F)")
            self.output_label_sv.set("Result (C)")
            self.c_to_f = False
        else:
            self.input_label_sv.set("Temperature (C)")
            self.output_label_sv.set("Result (F)")
            self.c_to_f = True


class TemperatureInput(tk.Entry):
    def __init__(self):
        super().__init__()

        self.input_variable = tk.StringVar()
        self.configure(font=(PRIMARY_FAMILY, PRIMARY_SIZE),
                       textvariable=self.input_variable,
                       foreground=INACTIVE_TEXT_COLOR,
                       validate="key",
                       validatecommand=(self.register(utils.check_float), "%P"))


if __name__ == "__main__":
    app = TemperatureConverture()
    app.mainloop()
