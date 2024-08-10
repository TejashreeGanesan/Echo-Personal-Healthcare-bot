import time
import threading
import speech_recognition as sr
import pyttsx3
import json
import re

with open('intents.json', 'r') as file:
    intents = json.load(file)

# It will remove the special characters 
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return ' '.join([word for word in text.split() if word.isalpha()])

# To get response based on symptoms
def get_response(symptoms):
    symptoms = preprocess_text(symptoms)
    max_match_score = 0
    best_response = "Sorry, I don't understand your symptoms. Please try again."
    
    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern = preprocess_text(pattern)
            pattern_words = pattern.split()
            matched_words = set(pattern_words) & set(symptoms.split())
            match_score = len(matched_words) / len(pattern_words)
            
            if match_score > max_match_score:
                max_match_score = match_score
                best_response = intent['responses'][0]
    
    return best_response

# Handles the bot's interaction
def start_bot():
    print("Bot is Running")

    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 175)
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)
    voices = engine.getProperty('voices')

    engine.say("Hello user, I am Echo, your personal Talking Healthcare Chatbot.")
    engine.runAndWait()

    engine.say("IF YOU WANT TO CONTINUE WITH MALE VOICE PLEASE SAY MALE. OTHERWISE SAY FEMALE.")
    engine.runAndWait()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.2)
        audio = recognizer.listen(source)

    audio_text = recognizer.recognize_google(audio)

    if audio_text.lower() == "female":
        engine.setProperty('voice', voices[1].id)
        print("You have chosen to continue with Female Voice")
    else:
        engine.setProperty('voice', voices[0].id)
        print("You have chosen to continue with Male Voice")

    while True:
        with mic as source:
            print("Say Your Symptoms. The Bot is Listening")
            engine.say("You may tell me your symptoms now. I am listening")
            engine.runAndWait()

            try:
                recognizer.adjust_for_ambient_noise(source, duration=0.2)
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio)
                engine.say(f"You said {text}")
                engine.runAndWait()

                engine.say("Scanning our database for your symptom. Please wait.")
                engine.runAndWait()

                time.sleep(1)

                # Gets the response based on symptoms
                response = get_response(text)
                engine.say(response)
                engine.runAndWait()

            except sr.UnknownValueError:
                engine.say("Sorry, Either your symptom is unclear to me or it is not present in our database. Please Try Again.")
                engine.runAndWait()
                print("Sorry, Either your symptom is unclear to me or it is not present in our database. Please Try Again.")
            finally:
                engine.say("If you want to continue please say Continue otherwise say Leave.")
                engine.runAndWait()

        with mic as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.2)
            audio = recognizer.listen(source)
            final = recognizer.recognize_google(audio)

        if final.lower() in ['no', 'leave', 'please exit']:
            engine.say("Thank You. Shutting Down now.")
            engine.runAndWait()
            print("Bot has been stopped by the user")
            exit(0)

bot_thread = threading.Thread(target=start_bot)
bot_thread.start()
