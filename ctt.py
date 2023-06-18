import tkinter as tk
from tkinter import ttk
import random
import colorama
import time
from enum import Enum

colorama.init()

class Error(Enum):
    INFO = 1
    SUCCESS = 2
    FAIL = 3

def consoleLog(msg="Message could not be loaded", enum=Error.INFO):
    if enum == Error.INFO:
        msg = f"{colorama.Fore.CYAN}[INFO]:{colorama.Fore.RESET} {msg}"
    
    if enum == Error.SUCCESS:
        msg = f"{colorama.Fore.GREEN}[INFO]:{colorama.Fore.RESET} {msg}"

    if enum == Error.FAIL:
        msg = f"{colorama.Fore.RED}[INFO]:{colorama.Fore.RESET} {msg}"

    print(msg)

class ClickerGame:
    def __init__(self):
        consoleLog("Initializing...")
        self.count = 0
        self.finished = False
        self.root = tk.Tk()
        self.root.geometry("300x250")
        self.root.title("Click To Ten")
        self.root.configure(background="#2E3440")
        consoleLog("Successfully set window by 300x250 and title, creating themes...", Error.SUCCESS)
        self.style = ttk.Style()
        self.style.theme_create("Nord", parent="alt", settings={
            "TLabel": {
                "configure": {"font": ("Montserrat", 10)},
                "map": {
                    "background": [("!disabled", "#2E3440")],
                    "foreground": [("!disabled", "#D8DEE9")]
                }
            },
            "TCombobox": {
                "configure": {"font": ("Montserrat", 10)},
                "map": {
                    "background": [("readonly", "#3B4252")],
                    "fieldbackground": [("readonly", "#3B4252")],
                    "foreground": [("readonly", "#D8DEE9")],
                    "selectbackground": [("readonly", "#88C0D0")],
                    "selectforeground": [("readonly", "#2E3440")]
                }
            }
        })
        consoleLog("Nord theme has been created...", Error.SUCCESS)
        self.style.theme_create("Turquoise", parent="alt", settings={
            "TLabel": {
                "configure": {"font": ("Montserrat", 10)},
                "map": {
                    "background": [("!disabled", "#1ABC9C")],
                    "foreground": [("!disabled", "#FFFFFF")]
                }
            },
            "TCombobox": {
                "configure": {"font": ("Montserrat", 10)},
                "map": {
                    "background": [("readonly", "#16A085")],
                    "fieldbackground": [("readonly", "#16A085")],
                    "foreground": [("readonly", "#FFFFFF")],
                    "selectbackground": [("readonly", "#E0F8F7")],
                    "selectforeground": [("readonly", "#1ABC9C")]
                }
            }
        })
        consoleLog("Turquoise theme has been created...", Error.SUCCESS)
        self.style.theme_use("Nord")
        consoleLog("Set theme as nord!", Error.SUCCESS)

        self.label = ttk.Label(self.root, text="Click to Ten: " + str(self.count))
        self.label.place(relx=0.5, rely=0.4, anchor="center")
        self.infolabel = ttk.Label(self.root, text="Clicks in Total: " + str(self.count))
        self.infolabel.place(relx=0.5, rely=0.25, anchor="center")

        self.theme_label = ttk.Label(self.root, text="Select Theme:", anchor="center")
        self.theme_label.place(relx=0.5, rely=0.8, anchor="center")

        self.theme_var = tk.StringVar()
        self.theme_dropdown = ttk.Combobox(self.root, textvariable=self.theme_var, values=["Nord", "Turquoise"])
        self.theme_dropdown.current(0)
        self.theme_dropdown.bind("<<ComboboxSelected>>", self.apply_theme)
        self.theme_dropdown.place(relx=0.5, rely=0.85, anchor="center")

        self.root.bind("<Button-1>", self.increment)
        consoleLog("Created UI elements!", Error.SUCCESS)
        self.root.resizable(False, False)

    def apply_theme(self, event):
        selected_theme = self.theme_var.get()
        consoleLog(f"Theme has changed to: {selected_theme}", Error.SUCCESS)
        self.style.theme_use(selected_theme)
        if selected_theme == "Turquoise":
            self.root.configure(background="#1ABC9C")
        else:
            self.root.configure(background="#2E3440")
    
    def increment(self, event):
        self.count += 1
        self.infolabel.config(text="Clicks in Total: " + str(self.count))
        consoleLog(f"The window was clicked {self.count} times")
        if self.finished:
            if self.count % 5 == 0:
                messages = [
                    "Really? The game is finished....",
                    "Why are you doing this?",
                    "Um, hello?",
                    "No point doing this",
                    "Stop",
                    "Um",
                    "...",
                    "Stop, you already won",
                    ":/",
                    ":(",
                    ">:/",
                    "._.",
                    ".-.",
                    "-_-",
                    "(ˉ﹃ˉ)",
                    "OK, I ran out of emojis",
                    "STOP",
                    "I give up",
                    "...",
                    "Why are you doing this?",
                    "What's the point?",
                    "Just useless"
                ]
                if self.count == (len(messages) * 5) or self.count > (len(messages) * 5):
                    random_message = random.choice(messages)
                    consoleLog(f"Randomly selected message: {random_message}")
                    self.label.config(text=random_message)
                else:
                    index = int(((self.count - 10) / 5))
                    message = messages[index]
                    consoleLog(f"Message displayed: {message}")
                    self.label.config(text=message)
            return

        self.label.config(text="Click to Ten: " + str(self.count))
        if self.count == 10:
            self.finished = True
            consoleLog(self.finished, Error.SUCCESS)
            # self.root.unbind("<Button-1>")  # Unbind the left mouse button click event
            self.label.config(text="You did it! You clicked to ten!")
        
    def run(self):
        self.root.mainloop()


clicker_game = ClickerGame()
clicker_game.run()
