import pyttsx3
import speech_recognition as sr
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#text to speech engine 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice

def speak(text):
    print(f"bot: {text}")
    engine.say(text)
    engine.runAndWait()

#speech recognition
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("listining...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"you: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't catch that...")
        return ""
    
#load Knowledge base
df = pd.read_csv("knowledge_sentences.csv")
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["sentence"])

#response generator
def generate_response(query):
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, X)
    index = similarity.argmax()
    score = similarity[0, index]
    if score > 0.3:
        return df.iloc[index]["sentence"]
    else:
        return "Sorry, I couldn't find a good match. Can you try asking differently?"
    

#main loop
def main():
    speak("Hello! I am your solar nano-grid bot. Ask me anything about the project!")
    while True:
        query = listen()
        if any (x in query for x in ["exit", "finish", "end", "thank you"]):
            speak("Thank you! Good bye, have a nice day!")
            break
        response = generate_response(query)
        speak(response)

if __name__ == "__main__":
    main()