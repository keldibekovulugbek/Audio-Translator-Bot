import speech_recognition as sr
from pydub import AudioSegment

def any2mp(ofn):
    mylist = ofn.split(".")
    print(mylist[-1])
    if mylist[-1]=="flac":
        return ofn
    else:
        wfn = ofn.replace(str("."+mylist[-1]),'.flac')
        x = AudioSegment.from_file(ofn)
        x.export(wfn, format='flac')
        return wfn

def stt(filename):

    # initialize the recognizer
    r = sr.Recognizer()

    # open the file
    with sr.AudioFile(filename) as source:
        # listen for the data (load audio to memory)
        audio_data = r.record(source)
        # recognize (convert from speech to text)
        text = r.recognize_google(audio_data)
    return text