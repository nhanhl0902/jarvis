import pyttsx3

def get_available_voices():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    return voices

if __name__ == "__main__":
    voices = get_available_voices()

    print("Available Voices:")
    for i, voice in enumerate(voices):
        print(f"Voice {i + 1}:")
        print(f" - ID: {voice.id}")
        print(f" - Name: {voice.name}")
        print(f" - Languages: {voice.languages}")
        print(f" - Gender: {voice.gender}")
        print(f" - Age: {voice.age}")
        print("\n")
