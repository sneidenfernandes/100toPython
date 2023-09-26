import sounddevice as sd
import wavio as wv 
from progressbar import timeProgressBar

duration = int(input('Please enter the length of the recording \n>'))

freq = 44100


recording = sd.rec(int(duration*freq), samplerate=freq, channels=2)

timeProgressBar(duration)

recordingName = input('What would you like to call your recording \n>') + '.wav'

wv.write(recordingName, recording, freq, sampwidth=2)


