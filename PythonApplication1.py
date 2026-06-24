# ==========================================================
# EERY TOOL v2.0 (Windows Edition)
# Single-file Python utility hub
# ==========================================================

import os
import sys
import json
import time
import random
import string
import hashlib
import base64
import platform
import getpass
import subprocess

# ----------------------------------------------------------
# Auto-install required packages
# ----------------------------------------------------------

def ensure_package(package):
    try:
        __import__(package)
    except ImportError:
        print(f"[+] Installing {package}...")
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", package]
        )

ensure_package("colorama")
ensure_package("psutil")

from colorama import init, Fore, Style
import psutil

init(autoreset=True)

# ----------------------------------------------------------
# Settings
# ----------------------------------------------------------

SETTINGS_FILE = "eery_settings.json"

DEFAULT_SETTINGS = {
    "theme": "Matrix",
    "custom_banner": ""
}

THEMES = {
    "Matrix": (Fore.GREEN, Fore.CYAN),
    "Cyber": (Fore.CYAN, Fore.MAGENTA),
    "Inferno": (Fore.RED, Fore.YELLOW),
    "Royal": (Fore.MAGENTA, Fore.BLUE),
    "Ice": (Fore.WHITE, Fore.CYAN),
    "Shadow": (Fore.LIGHTBLACK_EX, Fore.WHITE),
    "Kali": (Fore.BLUE, Fore.WHITE),
    "DOS": (Fore.GREEN, Fore.GREEN),
}

# ----------------------------------------------------------
# Main Class
# ----------------------------------------------------------

class EERYTool:

    def __init__(self):
        self.settings = self.load_settings()

    # ---------------------------
    # Utility methods
    # ---------------------------

    def clear(self):
        os.system("cls")

    def pause(self):
        input("\nPress Enter to continue...")

    def load_settings(self):
        if os.path.exists(SETTINGS_FILE):
            try:
                with open(SETTINGS_FILE, "r") as f:
                    return json.load(f)
            except:
                pass

        return DEFAULT_SETTINGS.copy()

    def save_settings(self):
        with open(SETTINGS_FILE, "w") as f:
            json.dump(self.settings, f, indent=4)

    def theme_colors(self):
        return THEMES.get(
            self.settings["theme"],
            THEMES["Matrix"]
        )

    # ---------------------------
    # Login
    # ---------------------------

    def login(self):

        self.clear()

        print(Fore.GREEN + "EERY TOOL LOGIN\n")

        for _ in range(3):

            pw = input("Password: ")

            if pw == "EERY":
                return True

            print(Fore.RED + "Incorrect password.")

        return False

    # ---------------------------
    # Banner
    # ---------------------------

    def banner(self):

        self.clear()

        p, s = self.theme_colors()

        if self.settings["custom_banner"]:
            print(p + self.settings["custom_banner"])
        else:
            print(p + r"""
███████╗███████╗██████╗ ██╗   ██╗
██╔════╝██╔════╝██╔══██╗╚██╗ ██╔╝
█████╗  █████╗  ██████╔╝ ╚████╔╝
██╔══╝  ██╔══╝  ██╔══██╗  ╚██╔╝
███████╗███████╗██║  ██║   ██║
╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝

████████╗ ██████╗  ██████╗ ██╗
╚══██╔══╝██╔═══██╗██╔═══██╗██║
   ██║   ██║   ██║██║   ██║██║
   ██║   ██║   ██║██║   ██║██║
   ██║   ╚██████╔╝╚██████╔╝███████╗
   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

                EERY TOOL v2.0
""")

        print(s + "=" * 70)
        print(s + f"Theme: {self.settings['theme']}")
        print(s + "=" * 70)

    # ---------------------------
    # Loading animation
    # ---------------------------

    def loading(self):

        self.banner()

        tasks = [
            "Loading modules",
            "Checking dependencies",
            "Initializing interface",
            "Preparing utilities",
            "Launching EERY Tool"
        ]

        for task in tasks:
            print(Fore.GREEN + f"[+] {task}...")
            time.sleep(0.6)

        time.sleep(1)

    # ---------------------------
    # Main Menu
    # ---------------------------

    def main_menu(self):

        while True:

            self.banner()

            print("[1] System Information")
            print("[2] File Tools")
            print("[3] Developer Tools")
            print("[4] Utilities")
            print("[5] Customization")
            print("[6] About")
            print("[0] Exit")

            choice = input("\nSelect Option: ")

            if choice == "1":
                self.system_info()

            elif choice == "2":
                self.file_tools()

            elif choice == "3":
                self.dev_tools()

            elif choice == "4":
                self.utilities()

            elif choice == "5":
                self.customization()

            elif choice == "6":
                self.about()

            elif choice == "0":
                sys.exit()

            else:
                print("Invalid choice.")
                self.pause()

    # ---------------------------
    # System Info
    # ---------------------------

    def system_info(self):

        self.banner()

        print("Operating System :", platform.system())
        print("Release          :", platform.release())
        print("Version          :", platform.version())
        print("Machine          :", platform.machine())
        print("Processor        :", platform.processor())
        print("RAM Usage        :", str(
            psutil.virtual_memory().percent) + "%")
        print("Current User     :", getpass.getuser())

        self.pause()

    # ---------------------------
    # File Tools
    # ---------------------------

    def file_tools(self):

        while True:

            self.banner()

            print("[1] Create File")
            print("[2] Delete File")
            print("[3] List Directory")
            print("[0] Back")

            c = input("\nChoice: ")

            if c == "1":

                name = input("Filename: ")

                try:
                    open(name, "w").close()
                    print("File created.")
                except Exception as e:
                    print(e)

                self.pause()

            elif c == "2":

                name = input("File to delete: ")

                try:
                    os.remove(name)
                    print("Deleted.")
                except Exception as e:
                    print(e)

                self.pause()

            elif c == "3":

                path = input("Directory path: ")

                try:
                    for item in os.listdir(path):
                        print(item)
                except Exception as e:
                    print(e)

                self.pause()

            elif c == "0":
                return

    # ---------------------------
    # Developer Tools
    # ---------------------------

    def dev_tools(self):

        while True:

            self.banner()

            print("[1] Python Runner")
            print("[2] Base64 Encode")
            print("[3] Base64 Decode")
            print("[4] Hash Generator")
            print("[0] Back")

            c = input("\nChoice: ")

            if c == "1":

                print("Enter a single line of Python code:")
                code = input(">>> ")

                try:
                    exec(code)
                except Exception as e:
                    print(e)

                self.pause()

            elif c == "2":

                text = input("Text: ")
                print(base64.b64encode(text.encode()).decode())
                self.pause()

            elif c == "3":

                text = input("Encoded text: ")

                try:
                    print(base64.b64decode(text).decode())
                except:
                    print("Invalid Base64.")

                self.pause()

            elif c == "4":

                text = input("Text: ")

                print("MD5    :", hashlib.md5(
                    text.encode()).hexdigest())

                print("SHA1   :", hashlib.sha1(
                    text.encode()).hexdigest())

                print("SHA256 :", hashlib.sha256(
                    text.encode()).hexdigest())

                self.pause()

            elif c == "0":
                return

    # ---------------------------
    # Utilities
    # ---------------------------

    def utilities(self):

        while True:

            self.banner()

            print("[1] Password Generator")
            print("[2] Calculator")
            print("[0] Back")

            c = input("\nChoice: ")

            if c == "1":

                try:
                    length = int(input("Length: "))

                    chars = (
                        string.ascii_letters +
                        string.digits +
                        "!@#$%^&*"
                    )

                    password = "".join(
                        random.choice(chars)
                        for _ in range(length)
                    )

                    print("\nGenerated Password:")
                    print(password)

                except:
                    print("Invalid length.")

                self.pause()

            elif c == "2":

                expr = input("Expression (example: 5+5): ")

                try:
                    print("Result:", eval(expr))
                except:
                    print("Invalid expression.")

                self.pause()

            elif c == "0":
                return

    # ---------------------------
    # Customization
    # ---------------------------

    def customization(self):

        while True:

            self.banner()

            print("[1] Change Theme")
            print("[2] Set Custom Banner")
            print("[0] Back")

            c = input("\nChoice: ")

            if c == "1":

                themes = list(THEMES.keys())

                for i, theme in enumerate(themes, 1):
                    print(f"[{i}] {theme}")

                try:
                    n = int(input("\nSelect Theme: "))
                    self.settings["theme"] = themes[n - 1]
                    self.save_settings()
                except:
                    print("Invalid choice.")

                self.pause()

            elif c == "2":

                print("\nPaste banner.")
                print("Type END on a new line to finish.\n")

                lines = []

                while True:

                    line = input()

                    if line.upper() == "END":
                        break

                    lines.append(line)

                self.settings["custom_banner"] = "\n".join(lines)
                self.save_settings()

                print("Banner saved.")
                self.pause()

            elif c == "0":
                return

    # ---------------------------
    # About
    # ---------------------------

    def about(self):

        self.banner()

        print("EERY TOOL v2.0")
        print("Windows Utility Hub")
        print("\nFeatures:")
        print("- Multiple themes")
        print("- File tools")
        print("- Developer tools")
        print("- Utilities")
        print("- Custom banners")
        print("- Settings saved to JSON")
        print("- Password protected (Password: EERY)")

        self.pause()


# ----------------------------------------------------------
# Start Program
# ----------------------------------------------------------

if __name__ == "__main__":

    app = EERYTool()

    if app.login():
        app.loading()
        app.main_menu()
    else:
        print("\nToo many incorrect attempts.")