from question import ask_question
from display import clear_terminal, print_loading
from filehandling import move_file, rename
from ytdl import ytdl
import argparse
import time

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="enable file management mode", action="store_true")
    parser.add_argument("-ytdl", "--youtubedl", help="download youtube video", action="store_true")
    # parser.add_argument("-h", "--help", help="show this help message and exit", action="store_true")
    args = parser.parse_args()

    clear_terminal()

    if args.file:
        print("luna is here to help you manage your files")
        command = input("Enter a command (e.g. 'move', 'rename'): ")
        if command == "move":
            src_path = input("Enter the path of the file to move: ")
            dest_path = input("Enter the destination path: ")
            move_file(src_path, dest_path)
            exit()
        elif command == "rename":
            src_path = input("Enter the path of the file to rename: ")
            new_name = input("Enter the new name: ")
            rename(src_path, new_name)
            exit()
        else:
            print("Invalid command.")
            exit()
        
    if args.youtubedl:
       print("luna is here to help you download youtube videos")
       ytdl()
       exit()

    # if args.help:
    #     print("luna is your personal tui assistant")
    #     print("usage: main.py [-flag]")
    #     print("optional arguments:")
    #     print("  -h, --help  show this help message and exit")
    #     print("  -f, --file  enable file management mode")
    #     print("  -ytdl, --youtubedl  download youtube video")
    #     exit()


    print("Hello! I'm Luna, your personal desktop assistant.")
    print("What can I help you with today?")

    question = input("> ")
    if question.lower() in ["exit", "quit", "goodbye"]:
        print("Goodbye!")
    else:
        print_loading()
        answer = ask_question(question, "text-davinci-002")
        clear_terminal()
        print(f"Q: {question}")
        for char in answer:
            print(char, end="", flush=True)
            time.sleep(0.05)
        print()

if __name__ == '__main__':
    main()
