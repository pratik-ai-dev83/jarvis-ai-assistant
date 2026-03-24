import webbrowser
import os
from utils.helpers import get_time

def process_command(command):
    if not command:
        return "I didn't catch that"

    if "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube"

    if "google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google"

    if "time" in command:
        return f"The time is {get_time()}"

    if "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    if "search" in command:
        query = command.replace("search", "").strip()
        if query:
            webbrowser.open(f"https://www.google.com/search?q={query}")
            return f"Searching for {query}"

    return "Sorry, I don't understand"