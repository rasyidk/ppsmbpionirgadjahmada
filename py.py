import speech_recognition as sr
import pyttsx3

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Katakan sesuatu:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("dapat audio")
    try:
        print("Mengenali...")
        text = recognizer.recognize_google(audio)
        print(f"Anda mengatakan: {text}")
        return text
    except sr.UnknownValueError:
        print("Maaf, tidak dapat memahami audio.")
        return None
    except sr.RequestError as e:
        print(f"Tidak dapat meminta hasil dari layanan Google Speech Recognition; {e}")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        user_input = recognize_speech()

        if user_input:
            if "keluar" in user_input.lower():
                print("Keluar dari program.")
                break
            else:
                response = "Anda mengatakan: " + user_input
                print(response)
                speak(response)
