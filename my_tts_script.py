import pyttsx3

def list_and_test_voices():
    """List all available voices and play a sample sentence for each."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')  # Fetch available voices
    
    print(f"Found {len(voices)} voices on your system.\n")
    
    for idx, voice in enumerate(voices):               
        print(f"Voice {idx + 1}:")
        print(f" - Name: {voice.name}")
        print(f" - ID: {voice.id}")
        print(f" - Language: {voice.languages if hasattr(voice, 'languages') else 'Unknown'}")
        print(f" - Gender: {voice.gender if hasattr(voice, 'gender') else 'Unknown'}\n")
        
        # Set the current voice
        engine.setProperty('voice', voice.id)
        
        # Test sentence spoken with the current voice
        engine.say(f"This is voice number {idx + 1}. Hello, how are you?")
        engine.runAndWait()

if __name__ == "__main__":
    print("Testing all available voices on your system...\n")
    list_and_test_voices()
    print("Finished testing voices!")
