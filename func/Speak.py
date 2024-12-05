import speech_recognition as sr 

recognizer = sr.Recognizer()

def Listen():
    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio_data = recognizer.listen(source)

        try:
            print("Recognizing....")

            text = recognizer.recognize_google(audio_data)
            print(f"Speech recognized: {text}")
            return text
        
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        
        except sr.Recognizer as e:
            print(f"Error: {e}")
            return None
        
recognized_text = Listen()