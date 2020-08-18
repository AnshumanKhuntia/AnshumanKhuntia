import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import random
import pyautogui
import pause
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('someone@gmail.com', 'password')
    server.sendmail('someone@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif("take screenshot 1")in query:
            screenshot = pyautogui.screenshot()
            speak('Taking screenshot')
            screenshot.save("screenshot1.png")
            speak('Screenshot saved')

        elif("take screenshot to") in query:
            screenshot = pyautogui.screenshot()
            speak('Taking screenshot')
            screenshot.save("screenshot2.png")
            speak('Screenshot saved')

        elif("take screenshot three")in query:
            screenshot = pyautogui.screenshot()
            speak('Taking screenshot')
            screenshot.save("screenshot3.png")
            speak('Screenshot saved')

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'the date' in query:
            year = int(datetime.datetime.now().year)
            month = int(datetime.datetime.now().month)
            date = int(datetime.datetime.now().day)
            speak("the current Date is")
            speak(date)
            speak(month)
            speak(year)


        elif 'open my default browser' in query:
            webbrowser.open("www.microsoft edge.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
            speak('Opening stackoverflow')

        elif 'open google chrome' in query:
            webbrowser.open("www.google chrome.com")
            speak('Opening Google chrome')

        elif 'open amazon' in query:
            webbrowser.open("www.amazon.com")
            speak('Opening amazon')

        elif 'open gmail' in query:
            webbrowser.open("www.gmail.com")
            speak('Opening gmail')

        elif 'open flipkart' in query:
            webbrowser.open("www.flipkart.com")
            speak('Opening flipkart')

        elif 'open github' in query:
            webbrowser.open("www.github.com")
            speak('Opening github')

        elif 'open rediffmail' in query:
            webbrowser.open("www.rediffmail.com")
            speak('Opening rediffmail')

        elif 'open whatsapp' in query:
            webbrowser.open("www.whatsapp.com")
            speak('Opening Whatsapp')

        elif 'open unspalash' in query:
            webbrowser.open("www.https://source.unsplash.com/.com")
            speak('Opening unspalash')

        elif'open snapdeal' in query:
            webbrowser.open("www.snapdeal.com")
            speak('Opening snapdeal')

        elif 'open zoom' in query:
            zoom = 'C:\\Users\\ANSHUMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Zoom\\Start Zoom.lnk'
            os.startfile(zoom)
            speak('Opening zoom')

        elif 'open pycharm' in query:
            pycha = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2020.1.4.lnk'
            os.startfile(pycha)
            speak('Opening Pycharm')

        elif 'open java' in query:
            java = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\\Itellija java.lnk'
            os.startfile(java)
            speak('Opening Itellija Idea')

        elif 'open eclipse' in query:
            eclipse = 'C:\\Users\\ANSHUMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Eclipse\\Eclipse IDE for Java Developers - 2020-03.lnk'
            speak('Opening Eclipse')
            os.startfile(eclipse)

        elif 'play music' in query:
            music_dir = 'C:\\Music'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\ANSHUMAN\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)
            speak('Opening code')

            
        if 'email to sister' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sister@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                    print(e)
                    speak("Sorry sir. I am not able to send this email")
                
        elif 'email to father' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "father@gmail.com"
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                        print(e)
                        speak("Sorry sir. I am not able to send this email")

        elif 'wait' in query:
            if 'wait' in query:
                sleep = int(input('Till how much I will wait:'))
                wait = pause.sleep(sleep)


        elif 'quit' in query:
            speak('Ok sir bye bye')
            quit()

        elif 'exit' in query:
            speak('Ok sir shuting down the system')
            exit()

