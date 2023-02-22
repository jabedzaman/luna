from question import ask_question
from display import clear_terminal, print_loading
import argparse
import time

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--voice", help="enable text-to-speech", action="store_true")
    args = parser.parse_args()

    clear_terminal()
    print("Hello! I'm Luna, your personal desktop assistant.")
    print("What can I help you with today?")

    if args.voice:
      print("Voice not yet implemented.")
      exit()

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
