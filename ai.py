from pathlib import Path
import openai
import speech_recognition as sr
client=openai.OpenAI()
import pygame
import time


def play_mp3(file_path):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

        # Allow time for the audio to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(1)

    except pygame.error as e:
        print(f"Error: {e}")

    pygame.quit()
def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio, language="en-US")
        print(f"Transcribed text: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Error making request to Google Speech Recognition API: {e}")
        return None
def tts(ans):
    speech_file_path = Path(__file__).parent / "tts.mp3"
    response = openai.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=ans
    )
    response.stream_to_file(speech_file_path)

def loof():
    conversation_history = []
    while True:
        question=input()
        if question.lower() in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        conversation_history.append({"role": "user", "content": question})
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
        )
        answer=completion.choices[0].message.content
        tts(completion.choices[0].message.content)
        play_mp3("tts.mp3")
        print(answer)
        conversation_history.append({"role": "assistant", "content": answer})


transcribed_text=input()
if transcribed_text in ["hi", "hello", "hey", "chat", "hey jarvis", "jarvis"]:
    play_mp3("speech.mp3")
    loof() 
    




