#!/usr/bin/python3
import pyttsx3


class TTSEngine(object):
    """
    Text To Speech Engine (STT)
    Google API Speech recognition settings
    SpeechRecognition API : https://pypi.org/project/SpeechRecognition/2.1.3
    """

    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        self.build()
    
    def build(self):
        #getting details of current voice
        voices = self.getProperty('voices')
        #changing index, changes voices. o for male
        #engine.setProperty('voice', voices[0].id)
        #changing index, changes voices. 1 for female
        self.setProperty('voice', voices[1].id)
        self.setProperty('rate', 125) 

    def stop(self):
        if self.engine:
            self.engine.stop()

    def runAndWait(self):
        if self.engine:
            self.engine.runAndWait()

    def speak(self, text):
        self.engine.say(text)
        self.runAndWait()

    def saveToFile(self, text, filename):
        if self.engine:
            #self.engine.save_to_file('Hello World', 'test.mp3')
            self.engine.save_to_file(text, filename)

    def setProperty(self, key, value) -> None:
        if self.engine:
            # self.engine.setProperty('volume',1.0) # setting up volume level  between 0 and 1
            #engine.setProperty('rate', 125)
            self.engine.setProperty(key, value)

    def getProperty(self, key) -> any:
        if self.engine:
            #rate = engine.getProperty('rate')
            return self.engine.getProperty(key)
        return None
