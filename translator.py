from translate import Translator
#from .engine import Engine
import pyttsx3


lang1=input("Enter language you want to translate:")
lang2=input("Enter language in which you want to translate:")
text=input("Enter Text:")
engine = pyttsx3.init()
translator= Translator(from_lang=lang1,to_lang=lang2)
translation = translator.translate(text)
print(translation)
engine.say(translation)
engine.runAndWait()

