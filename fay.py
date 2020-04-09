import speech_recognition as sr 
import playsound
from gtts import gTTS
from selenium import webdriver
import os
import pyaudio
from selenium import webdriver

num = 1
def assistant(output):
    global num
    num += 1

    print("fay: ", output)

    speak = gTTS(text = output, lang = 'en-uk' ,slow = False)

    file = str(num) + "mp3"
    speak.save(file)

    playsound.playsound(file, True)
    os.remove(file)

def get_audio():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak...")
        listener.adjust_for_ambient_noise(source,duration=1) 
        audio = listener.listen(source, None)
    #try:
       # text = listener.recognize_google(audio, lenguage = 'en-UK')
        #print ("you: ", text )
       # return text
   # except:
       # assistant("I did not understand you")
        #return 0

if __name__ == "__main__": 
    assistant("What's your name, Human?") 
    name = get_audio() 
    assistant("Hello," + name) 
   
    while(1): 
  
        assistant("What can i do for you?") 
        text = get_audio().lower() 
  
        if text == 0: 
            continue
  
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
            assistant("Ok bye, "+ name+'.') 
            break
  