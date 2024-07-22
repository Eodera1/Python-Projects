import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    # You can adjust the rate (speed) and volume
    engine.setProperty('rate', 150)    # Speed percentage (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Convert text to speech
    engine.say("Hey Erick, I am a Python module. Welcome to the world of Python programming.")
    engine.runAndWait()

# Example usage
poem = """
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are!
"""

text_to_speech(poem)
