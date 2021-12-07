# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 20:54:55 2021

@author: info
"""

import speech_recognition as sr
import webbrowser as wb

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print("[Search instagram : Search youtube")
    print("Speak Now")
    audio=r3.listen(source)
    
if 'how are you' in r2.recognize_google(audio):
    r2=sr.Recognizer()
    url='https://www.google.com/search?q='
    with sr.Microphone() as source:
        print("Search your query")
        audio=r2.listen(source)
        
        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)
        except sr.UnknownValueError:
            print('error')
        except sr.RequestError as e:
            print('failed'.format(e))
