import os
import random
from jsonpickle import encode, decode
from tkinter import BOTH, BOTTOM, E, LEFT, N, TOP, W, Button, Entry, Frame, Tk, Label, StringVar

join = os.path.join


class PyBehaviour:
    name: StringVar = None
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
            if self.name != None and self.name.get() != "":
                filename = self.name.get()
            else:
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

        variables = self.__dict__
        title = self.__class__.__name__.upper()

        window = Tk()
        window.title(title)
        self.name = StringVar()

        TitleLabel = Label(master=window, text=title,
                           fg=White, bg=Black, height=2, padx=10, pady=10)
        TitleLabel.pack(fill=BOTH, side=TOP, expand=True)

        frame = Frame(master=window, bg=Black,
                      borderwidth=1)
        i = 0
        for parm in variables:
            frame.rowconfigure(i, weight=1)
            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=2)

            labelFrame = Frame(master=frame, borderwidth=.2)
            Label(
                master=labelFrame, text=f"{parm}", fg=White, bg=Black, justify=LEFT, anchor="w", padx=5, pady=5).pack(fill=BOTH)

            contentFrame = Frame(
                master=frame, borderwidth=.2)
            Label(
                master=contentFrame, text=f"{variables.get(parm)}", fg=White, bg=Black, justify=LEFT, anchor="w", padx=5, pady=5).pack(fill=BOTH)
            labelFrame.grid(row=i, column=0, sticky=(E,N))
            contentFrame.grid(row=i, column=1, sticky=W)
            i += 1

        frame.pack(fill=BOTH, side=TOP, expand=True)

        btns = Frame(master=window, bg=Black, pady=15, padx=10)
        label = Label(master=btns, text=f"Filename", fg=White, bg=Black, justify=LEFT,
                      anchor="w", padx=5, pady=5).pack(fill=BOTH, expand=True)
        entry = Entry(master=btns, bg=Black,
                      fg=White, textvariable=self.name)
        entry.pack(fill=BOTH)
        Button(
            master=btns, text=f"Save", fg=White, bg=Black, padx=5, pady=3, command=self.Save).pack()
        btns.pack(fill=BOTH, side=BOTTOM, expand=True)
        window.mainloop()
