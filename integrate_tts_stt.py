import pyttsx3
import speech_recognition as sr
import os

# Text-to-Speech Module
class TextToSpeech:
    def __init__(self, rate: int = 175, volume: float = 1.0):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', rate)  # Words per minute
        self.engine.setProperty('volume', volume)  # Volume (0.0 to 1.0)

    def speak(self, text: str):
        self.engine.say(text)
        self.engine.runAndWait()

# Speech-to-Text Module
class SpeechToText:
    def __init__(self, timeout: int = 5, phrase_time_limit: int = 10):
        self.recognizer = sr.Recognizer()
        self.timeout = timeout
        self.phrase_time_limit = phrase_time_limit

    def listen(self) -> str:
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=self.timeout, phrase_time_limit=self.phrase_time_limit)
                text = self.recognizer.recognize_google(audio)
                print(f"Boss: {text}")
                return text
            except sr.WaitTimeoutError:
                print("Listening timed out.")
                return ""
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
                return ""
            except sr.RequestError as e:
                print(f"API request error: {e}")
                return ""

# Integration Example
def main():
    tts = TextToSpeech()
    stt = SpeechToText()

    while True:
        print("\nWaiting for your command...")
        command = stt.listen()
        if not command:
            continue

        if "exit" in command.lower():
            tts.speak("Goodbye Sir ! Have a nice day")
            break
        elif "hello" in command.lower():
            tts.speak("Hello! How can I assist you today?")
        elif "what is your name" in command.lower():
            tts.speak("I am pandu. A virtual assistant designed for Himanshu Boss")
        else:
            tts.speak(f"{command}")

if __name__ == "__main__":
    main()
