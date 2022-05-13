#!/usr/bin/python3
import speech_recognition as sr
from ..brain.analyzer import Analyzer

class STTEngine(object):
    """
    Speech To Text Engine (STT)
    Google API Speech recognition settings
    SpeechRecognition API : https://pypi.org/project/SpeechRecognition/2.1.3
    https://github.com/Uberi/speech_recognition/blob/master/reference/library-reference.rst
    """

    _INSTANCE = None
    
    def __init__(self):
        super().__init__()
        self.engine = sr.Recognizer()
        #mic = sr.Microphone(device_index=1) 
        self.microphone = sr.Microphone(sample_rate=28000)
        #print(sr.Microphone.list_microphone_names())
        # energía de audio mínima a considerar para la grabación
        self.engine.energy_threshold = 3800
        # segundos de audio sin hablar antes de que una frase se considere completa
        self.engine.pause_threshold = 0.8
        self.engine.dynamic_energy_threshold = True
        # segundos mínimos de audio hablado antes de que consideremos el audio hablado como una frase; los valores por debajo de esto se ignoran (para filtrar clics y estallidos)
        self.engine.phrase_threshold = 0.8
        # segundos de audio que no habla para mantenerse en ambos lados de la grabación
        self.engine.non_speaking_duration = 0.2
        self.engineLanguage = "es-ES"
        #self.keyword_lang = "es"
        self.keywords = []#[("cristal", 1), ("hey cristal", 1), ("ey cristal", 1), ("christal", 1)]

    @staticmethod
    def getInstance():
        if not STTEngine._INSTANCE:
            STTEngine._INSTANCE = STTEngine()
        return STTEngine._INSTANCE

    def command(self):
        if not isinstance(self.engine, sr.Recognizer):
            raise TypeError("`recognizer` must be `Recognizer` instance")
        if not isinstance(self.microphone, sr.Microphone):
            raise TypeError("`microphone` must be `Microphone` instance")
        #text = self._recognizeSpeechFromMic()
        text = input("Escribe algo:\n")
        text, _ = Analyzer.getInstance().extract(text)
        return text
        
    def stop(self):
        print("Deteniendo...")

    def _recognizeSpeechFromMic(self):
        audio = None
        try:
            with self.microphone as source:
                print("escuchando 1")
                self.engine.adjust_for_ambient_noise(source, duration=0.8)
                audio = self.engine.listen(source, timeout=8)
                #audio = self.engine.record(source=source, duration=50)
        except sr.WaitTimeoutError:
            pass
        try:
            text = None
            if audio:
                text = self.engine.recognize_google(audio, language=self.engineLanguage)
                text = text.lower()
            return text
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError as e:
            print(e)