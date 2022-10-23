import os
import random
from tkinter import Frame
from jsonpickle import encode, decode

join = os.path.join


class PyBehaviour:
    Paths = {
        'data': r"data",
        'SerializedObjects': r"data\SerializedObjects",
        'progress': r"progress"
    }

    @staticmethod
    def VerifyFolders():
        for path in PyBehaviour.Paths:
            path = PyBehaviour.Paths.get(path)
            currentFolder = os.path.dirname(
                os.path.realpath(__file__).replace("Systems", ""))
            print(f"checking for {path}")
            if not os.path.exists(currentFolder + "\\" + path):
                os.mkdir(path=currentFolder + "\\" + path)
                print(f"Created {path} folder")

    def Save(self, filename: str = ""):
        PyBehaviour.VerifyFolders()
        if filename == "":
            print("no filename found, generating one...")
            for i in range(7):
                filename += str(random.randint(0, 9))
        filename += f".{self.__class__.__name__}"
        print(f"Generating file {filename}")
        with open(join(PyBehaviour.Paths.get('data'), filename), 'w') as file:
            file.write(str(encode(self)))
        print(f"File {filename} created")

    @staticmethod
    def Load(filename: str):
        PyBehaviour.VerifyFolders()
        with open(join(PyBehaviour.Paths.get('data'), filename), 'r') as file:
            fileExt = filename.split(".")[1]
            fileContent = file.read()
            obj = decode(fileContent)

            print(
                f"Loaded {filename} of type {obj.__class__.__name__}")

            return obj

    def Show(self):
        Black = "#1B2631"
        White = "#F8F9F9"

        import tkinter as tk
        variables = self.__dict__
        title = self.__class__.__name__.upper()

        window = tk.Tk()

        TitleLabel = tk.Label(master=window, text=title,
                              fg=White, bg=Black, height=2, width=80)
        TitleLabel.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        frame = tk.Frame(master=window, bg=Black,
                         borderwidth=1)
        i = 0
        for parm in variables:
            frame.rowconfigure(i, weight=1)
            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=2)

            labelFrame = Frame(master=frame, relief=tk.RAISED, borderwidth=.2)
            tk.Label(
                master=labelFrame, text=f"{parm}", fg=White, bg=Black).pack()

            contentFrame = Frame(master=frame, relief=tk.RAISED, borderwidth=.2)
            tk.Label(
                master=contentFrame, text=f"{variables.get(parm)}", fg=White, bg=Black).pack()
            labelFrame.grid(row=i, column=0, )
            contentFrame.grid(row=i, column=1)
            i += 1

        frame.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        window.mainloop()


# PyBehaviour.VerifyFolders()
