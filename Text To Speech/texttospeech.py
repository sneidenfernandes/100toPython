import sys
import pyttsx3

engine = pyttsx3.init()
newVoiceRate = 80
engine.setProperty('rate',newVoiceRate )

print('Enter text to speak, or QUIT to quit.')

while True:
    text = input('> ').strip()

    if text.upper() == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    
    engine.say(text)
    engine.runAndWait()

        