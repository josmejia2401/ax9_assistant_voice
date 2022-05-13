#!/usr/bin/python3
import gtts
from playsound import playsound
import os


class TTSEngine(object):
    """
    Text To Speech Engine (STT)
    # all available languages along with their IETF tag
    print(gtts.lang.tts_langs()
    """
    _INSTANCE = None

    def __init__(self):
        super().__init__()
        # 'es-es': 'Spanish (Spain)', 'es-us': 'Spanish (United States)', 'es': 'Spanish'
        self.language = 'es-us'
        self.filename = 'speak.mp3'

    @staticmethod
    def getInstance():
        if not TTSEngine._INSTANCE:
            TTSEngine._INSTANCE = TTSEngine()
        return TTSEngine._INSTANCE

    def stop(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass

    def runAndWait(self):
        playsound(self.filename)

    def speak(self, text):
        if not text:
            return
        self.stop()
        tts = gtts.gTTS(text, lang=self.language)
        tts.save(self.filename)
        self.runAndWait()
        self.stop()
