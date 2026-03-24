import datetime

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_greeting():
    hour = datetime.datetime.now().hour

    if hour < 12:
        return "Good morning"
    elif hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"