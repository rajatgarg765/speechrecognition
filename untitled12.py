# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 22:56:19 2021

@author: info
"""

import speech_recognition as sr
import webbrowser as wb
import pyttsx3


r = sr.Recognizer()
r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
i=1
while(i<5):	
	i=i+1

	try:
        
		
		
		 #with sr.Microphone() as source2:
             
            
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
        
            
            audio2 = r.listen(source2)
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()
			print("Did you say "+MyText)
			SpeakText(MyText)
			
    except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")       