import os
import json
import time
import random
import string
import hashlib
import base64
import platform
import getpass

try:
    import psutil
    PSUTIL = True
except:
    PSUTIL = False

try:
    from colorama import init, Fore
    init(autoreset=True)
except:
    class F:
        RED = GREEN = CYAN = YELLOW = ""
    Fore = F()

SETTINGS_FILE = "eery.json"

THEMES = {
    "Matrix": Fore.GREEN,
    "Cyber": Fore.CYAN,
    "Inferno": Fore.RED,
    "Ghost": Fore.YELLOW
}


class EERY:

    def __init__(self):
        self.settings = self.load()

    def load(self):
        if os.path.exists(SETTINGS_FILE):
            try:
                return json.load(open(SETTINGS_FILE))
            except:
                pass
        return {"theme": "Matrix"}

    def save(self):
        json.dump(self.settings, open(SETTINGS_FILE, "w"), indent=4)

    def clear(self):
        os.system("cls")

    def color(self):
        return THEMES.get(self.settings["theme"], Fore.GREEN)

    # =========================
    # ASCII BANNER (UPDATED)
    # =========================

    def banner(self):
        self.clear()
        c = self.color()

        print(c + r"""
███████╗███████╗██████╗ ██╗   ██╗
██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝
█████╗  █████╗  ██████╔╝ ╚████╔╝
██╔══╝  ██╔══╝  ██╔══██╗  ╚██╔╝
███████╗███████╗██║  ██║   ██║
╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝

██████████╗ ██████╗  ██████╗ ██╗     ████████╗ ██████╗  ██████╗ ██╗
╚══██╔════╝██╔═══██╗██╔═══██╗██║     ╚══██╔══╝██╔═══██╗██╔═══██╗██║
   ██║     ██║   ██║██║   ██║██║        ██║   ██║   ██║██║   ██║██║
   ██║     ██║   ██║██║   ██║██║        ██║   ██║   ██║██║   ██║██║
   ██║     ╚██████╔╝╚██████╔╝███████╗   ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝      ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

                 E E R Y   T O O L
""")

    def pause(self):
        input("\nENTER")

    # =========================
    # MENU
    # =========================

    def menu(self):
        while True:
            self.banner()
            print("[1] System Info")
            print("[2] File Tools")
            print("[3] Dev Tools")
            print("[4] Utilities")
            print("[5] Themes")
            print("[0] Exit")

            c = input("> ")

            if c == "1":
                self.sys()
            elif c == "2":
                self.files()
            elif c == "3":
                self.dev()
            elif c == "4":
                self.util()
            elif c == "5":
                self.theme()
            elif c == "0":
                break

    # =========================
    # SYSTEM
    # =========================

    def sys(self):
        self.banner()
        print("OS:", platform.system())
        print("User:", getpass.getuser())

        if PSUTIL:
            print("RAM:", psutil.virtual_memory().percent, "%")

        self.pause()

    # =========================
    # FILES
    # =========================

    def files(self):
        self.banner()
        print("[1] Create file")
        print("[2] Delete file")
        print("[3] List files")

        c = input("> ")

        if c == "1":
            open(input("name: "), "w").close()

        elif c == "2":
            try:
                os.remove(input("file: "))
            except:
                pass

        elif c == "3":
            print(os.listdir())

        self.pause()

    # =========================
    # DEV
    # =========================

    def dev(self):
        self.banner()
        print("[1] Base64 Encode")
        print("[2] Base64 Decode")
        print("[3] Hash")

        c = input("> ")

        if c == "1":
            print(base64.b64encode(input("text: ").encode()).decode())

        elif c == "2":
            try:
                print(base64.b64decode(input("text: ")).decode())
            except:
                print("error")

        elif c == "3":
            t = input("text: ")
            print(hashlib.md5(t.encode()).hexdigest())

        self.pause()

    # =========================
    # UTILITIES
    # =========================

    def util(self):
        self.banner()
        print("[1] Password Gen")

        c = input("> ")

        if c == "1":
            chars = string.ascii_letters + string.digits
            print("".join(random.choice(chars) for _ in range(12)))

        self.pause()

    # =========================
    # THEMES
    # =========================

    def theme(self):
        self.banner()
        print("Matrix / Cyber / Inferno / Ghost")

        t = input("theme: ")

        self.settings["theme"] = t
        self.save()


if __name__ == "__main__":
    EERY().menu()