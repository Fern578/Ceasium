import os
import json
import time
import random
import string
import hashlib
import base64
import platform
import getpass

# optional safe imports
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
        GREEN = CYAN = RED = YELLOW = MAGENTA = WHITE = ""
    Fore = F()

# =========================
# SETTINGS
# =========================

SETTINGS_FILE = "eery_core.json"

THEMES = {
    "Matrix": Fore.GREEN,
    "Cyber": Fore.CYAN,
    "Inferno": Fore.RED,
    "Royal": Fore.MAGENTA,
    "Ghost": Fore.WHITE
}

# =========================
# CORE ENGINE
# =========================

class EERY:

    def __init__(self):
        self.data = self.load()
        self.glitch_chars = "#$@%&*!?/\\|<>[]{}"

    # -------------------------
    # SETTINGS
    # -------------------------

    def load(self):
        if os.path.exists(SETTINGS_FILE):
            try:
                return json.load(open(SETTINGS_FILE))
            except:
                pass
        return {"theme": "Matrix"}

    def save(self):
        json.dump(self.data, open(SETTINGS_FILE, "w"), indent=4)

    # -------------------------
    # UI SYSTEM
    # -------------------------

    def clear(self):
        os.system("cls")

    def color(self):
        return THEMES.get(self.data["theme"], Fore.GREEN)

    def glitch_line(self):
        return "".join(random.choice(self.glitch_chars) for _ in range(70))

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

        print(self.glitch_line())
        print("SYSTEM STATUS: ONLINE | CORE: STABLE | MODE: INSANE")
        print(self.glitch_line())

    # -------------------------
    # LOADING ANIMATION
    # -------------------------

    def boot(self):
        self.banner()
        steps = [
            "Injecting modules",
            "Bypassing sanity checks",
            "Loading EERY core",
            "Syncing UI layers",
            "Launching terminal"
        ]

        for s in steps:
            print("[+] " + s)
            time.sleep(0.4)

        time.sleep(0.5)

    # -------------------------
    # MENU
    # -------------------------

    def menu(self):
        while True:
            self.banner()

            print("[1] SYSTEM SCAN")
            print("[2] FILE MANAGER")
            print("[3] DEV ENGINE")
            print("[4] UTILITY HUB")
            print("[5] PASSWORD GENERATOR")
            print("[6] THEME CONTROL")
            print("[7] GLITCH MODE TEST")
            print("[0] EXIT")

            c = input("\n> ")

            if c == "1":
                self.system()
            elif c == "2":
                self.files()
            elif c == "3":
                self.dev()
            elif c == "4":
                self.utils()
            elif c == "5":
                self.passgen()
            elif c == "6":
                self.theme()
            elif c == "7":
                self.glitch_mode()
            elif c == "0":
                break

    # -------------------------
    # SYSTEM SCAN (INSANE STYLE)
    # -------------------------

    def system(self):
        self.banner()
        print("SCANNING SYSTEM...\n")

        for i in range(5):
            print(f"Checking kernel layer {i}... OK")
            time.sleep(0.3)

        print("\nOS:", platform.system())
        print("User:", getpass.getuser())

        if PSUTIL:
            print("RAM:", psutil.virtual_memory().percent, "%")
            print("CPU:", psutil.cpu_percent(), "% load")

        self.fake_matrix_effect()
        input("\nENTER")

    # -------------------------
    # FILE SYSTEM
    # -------------------------

    def files(self):
        while True:
            self.banner()
            print("[1] Create file")
            print("[2] Write file")
            print("[3] Delete file")
            print("[4] List files")
            print("[0] Back")

            c = input("> ")

            if c == "1":
                open(input("name: "), "w").close()

            elif c == "2":
                f = input("file: ")
                open(f, "a").write(input("text: ") + "\n")

            elif c == "3":
                try:
                    os.remove(input("file: "))
                except:
                    pass

            elif c == "4":
                print(os.listdir())

            elif c == "0":
                break

            self.fake_matrix_effect()

    # -------------------------
    # DEV ENGINE
    # -------------------------

    def dev(self):
        self.banner()
        print("[1] Base64 Encode")
        print("[2] Base64 Decode")
        print("[3] Hash Burst Mode")

        c = input("> ")

        if c == "1":
            print(base64.b64encode(input("text: ").encode()).decode())

        elif c == "2":
            try:
                print(base64.b64decode(input("text: ")).decode())
            except:
                print("FAIL")

        elif c == "3":
            t = input("text: ")
            print("MD5:", hashlib.md5(t.encode()).hexdigest())
            print("SHA1:", hashlib.sha1(t.encode()).hexdigest())
            print("SHA256:", hashlib.sha256(t.encode()).hexdigest())

        input()

    # -------------------------
    # UTILS
    # -------------------------

    def utils(self):
        self.banner()
        print("[1] Calculator")
        print("[2] Random Number")
        print("[3] Fake CPU Burn Test")

        c = input("> ")

        if c == "1":
            try:
                print(eval(input("calc: ")))
            except:
                print("error")

        elif c == "2":
            print(random.randint(1, 999999999))

        elif c == "3":
            for i in range(10):
                print("CPU LOAD:", random.randint(10, 100), "%")
                time.sleep(0.2)

        input()

    # -------------------------
    # PASSWORD GEN
    # -------------------------

    def passgen(self):
        self.banner()
        chars = string.ascii_letters + string.digits + "!@#$%^&*"
        print("".join(random.choice(chars) for _ in range(20)))
        input()

    # -------------------------
    # THEMES
    # -------------------------

    def theme(self):
        self.banner()
        print("Matrix / Cyber / Inferno / Royal / Ghost")
        t = input("theme: ")
        self.data["theme"] = t
        self.save()

    # -------------------------
    # GLITCH EFFECT
    # -------------------------

    def glitch_mode(self):
        self.banner()
        for i in range(20):
            print(self.glitch_line())
            time.sleep(0.05)

    def fake_matrix_effect(self):
        for _ in range(3):
            print("".join(random.choice("01") for _ in range(60)))


# =========================
# RUN
# =========================

if __name__ == "__main__":
    app = EERY()
    app.boot()
    app.menu()