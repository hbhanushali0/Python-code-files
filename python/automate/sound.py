

from gtts import gTTs

import playsound

from playsound import *

audio ="speech.mp3"

language = 'en'

sp = gTTs(text = "enter your text here" , lang = language, slow = False)

sp.save(audio)
playsound(audio)


