import tkinter as tk
from settings import *
import utils


class TemperatureConverture(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry(GEOMETRY)
        self.title(ROOT_TITLE)
        self.iconbitmap(default="app-icon.ico")

        self.temp_input = TemperatureInput()
        self.temp_input.grid(column=0, columnspan=2, row=1, sticky=tk.NSEW, padx=5)

        self.input_label = tk.Label(
            font=(PRIMARY_FAMILY, LABEL_SIZE),
            text="Temperature (C)",
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

        self.output_label = tk.Label(
            font=(PRIMARY_FAMILY, LABEL_SIZE),
            text="Result (F)",
            anchor="sw",
        )

        self.output_label.grid(row=0, column=2, sticky=tk.NSEW, padx=5, pady=5)

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
            answer = round((float(self.temp_input.get()) * (9/5)) + 32, 1)
            self.output_variable.set(str(answer) + "°")


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
