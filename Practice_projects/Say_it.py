import pyttsx3 # Import the pyttsx3 module

# Get user input
name = input("Enter your message: ")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set the voice to use for the text-to-speech engine
engine.setProperty('voice', 'english+f10') 

# Set the rate at which the text should be spoken
engine.setProperty('rate', 130) 

# Convert the text to audio and play it
engine.say(name)
engine.runAndWait()


