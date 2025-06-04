import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import pyautogui
import time
import pywhatkit
import pyjokes

# Initialize the speech engine
engine = pyttsx3.init()

# Function to speak a message
def speak(message):
    engine.say(message)
    engine.runAndWait()

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
        except sr.RequestError:
            speak("Sorry, there was an error with the speech recognition service.")
        return ""

# Function to handle commands
def handle_command(command):
    command = command.lower()

    if 'search in google' in command:
        query = command.replace('search in google', '').strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Searching for {query} on Google.")

    elif 'search in youtube' in command:
        query = command.replace('search in youtube', '').strip()
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        speak(f"Searching {query} on YouTube.")

    elif 'tell me joke' in command:
        speak(pyjokes.get_joke())

    elif "play on youtube" in command:
        song = command.replace('play', "").strip()
        speak(f"Playing {song} on YouTube")
        pywhatkit.playonyt(song)

    elif 'who is' in command:
        person = command.replace('who is', '').strip()
        try:
            summary = wikipedia.summary(person, sentences=1)
            speak(summary)
        except wikipedia.exceptions.DisambiguationError as e:
            speak("There are multiple results. Could you be more specific?")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any information on that topic.")

    elif 'good bye' in command:
        speak("Goodbye Tejas! Have a great day!")
        return False

    else:
        speak("I am not sure how to help with that.")

    return True

def main():
    speak("Hello Tejas! I am your virtual assistant. How can I assist you today?")

    while True:
        command = recognize_speech()
        if command:
            if not handle_command(command):
                break

if __name__ == "__main__":
    main()




# Commands for virtual assistant


# 1) search for "flipkart"

# 2) play on may way

# 3) who is "mukesh ambani"


