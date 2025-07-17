"""
quote_generator.py

A simple command-line random quote generator.
Press ENTER to see a random quote.
Type 'exit' or 'quit' to end the program.
"""

import random

def quote_generator():

    """
    Continuously shows random quotes from a list until the user decides to quit.
    """

    print("📜 Welcome to Quote Generator")

    quotes = [
    "Code never lies, comments sometimes do.",
    "Talk is cheap. Show me the code. – Linus Torvalds",
    "Programs must be written for people to read, and only incidentally for machines to execute. – Harold Abelson",
    "First, solve the problem. Then, write the code. – John Johnson",
    "Simplicity is the soul of efficiency. – Austin Freeman",
    "Any fool can write code that a computer can understand. Good programmers write code that humans can understand. – Martin Fowler",
    "Fix the cause, not the symptom. – Steve Maguire",
    "Experience is the name everyone gives to their mistakes. – Oscar Wilde",
    "In order to be irreplaceable, one must always be different. – Coco Chanel",
    "Code is like humor. When you have to explain it, it’s bad."
    ]

    while True:
        choice = input("Press Enter to generate quote or exit to quit : ")
        if choice.lower().strip() in ["exit" , "quit"]:
            print("Goodbye! 👋. Visit us again..")
            break
        quote = random.choice(quotes)
        print("\nYour quote is:")
        print(f"  \"{quote}\"\n")

if __name__ == "__main__":
    quote_generator()