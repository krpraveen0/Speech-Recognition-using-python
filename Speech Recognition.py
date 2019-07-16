# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 07:59:01 2019

@author: praveen
"""

import speech_recognition as sr
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Hey there !! say something  !!!")
    audio = r.listen(source)

try:
    print("Google thinks your said:\n" + r.recognize_google(audio))
except:
    pass

    
