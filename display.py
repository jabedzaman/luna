import time
import os

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")

def print_loading():
    print("Fetching answer ", end="", flush=True)
    for i in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()
