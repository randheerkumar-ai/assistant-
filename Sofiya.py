import pyttsx3 
import speech_recognition as sr  # for recognize seach
import datetime   # for see date & time 
import pyjokes   # for jocks
import pywhatkit  # for play some music video 
import pyautogui  # for open chrome or something in pc ( open software) 
import wikipedia  # for knowing about someting like( (who is Narendra-modi)
import os         # for shutdown & restart pc
import webbrowser  # for search something on internet
import sympy as sp  # for mathematical operation


def speak (text):
    engine  = pyttsx3.init()
    voices = engine.getProperty('voices')
    Id = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
    engine.setProperty('voice',Id)
    engine.say(text=text)
    engine.runAndWait()
    print(text)

#speech_recognition fun
def speechrecognition():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.......")
        r.pause_threshold = 1
        audio =r.listen(source,0,5)
    
    try:
       print("Recognizing......")
       query = r.recognize_google(audio,language ="en")
       return query.lower()
    

    except:
       return "" 

#datetime function
def greeting():  
    current_time = datetime.datetime.now()
    hour = current_time.hour
    print(current_time, hour)
    if 4<=hour < 12:
        speak('good morning sir!')
    elif 12<= hour < 16:
        speak('Good afternoon sir!')
    elif 16<= hour <20: 
        speak('its evening sir!')
    else:
        speak('its night sir!')

 #Main function of jarvis
def run_sofiya():
    command = speechrecognition()
    print(f"Command recognized: {command}")
    if 'hello' in command: 
        print(command)
        speak('hi boss how are you ?')

    
    #pyjokes use
    elif 'jokes' in command: 
        print(command)
        speak(pyjokes.get_jokes())

    elif 'exit' in command:
        print(command)
        speak('goodbyy sir !')
        return "exit"  # Return exit to break the loop
    
    # pywhatkit use for play form youtube music
    elif 'play' in command:
        print(command)
        speak('playing' + command)
        pywhatkit.playonyt(command)   

    elif 'time' in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print(time)
        speak("current time is " + time)

    #pyautogui use for open something
    elif 'open' in command:
        command = command.replace('open'," ")
        pyautogui.press('super')
        pyautogui.typewrite(command)
        pyautogui.sleep(1)
        pyautogui.press('enter')
        print(command)
        speak('opening' + command)

    
    # for video pose or play
    elif 'stop' in command or 'start' in command:
        pyautogui.press('k')
        print(command)
        speak('done sir!')

    # for get full screen of video
    elif 'full screen' in command:
        pyautogui.press('f')
        print(command)
        speak('done sir!')

    # for get theater screen of videok
    elif 'Theater screen' in command:
        pyautogui.press('t')
        print(command)
        speak('done sir!')

    elif 'close' in command:
        pyautogui.hotkey('alt', 'f4')
        print(command)
        speak('closing sir!')

    #wikipedia use
    elif 'who is' in command:
        persion = command.replace('who is'," ")
        info = wikipedia.summary(persion,2)
        print(speak(info))
        

    # for remember someting 
    elif 'remember that' in command:
        rememberMassage = command.replace('remember that'," ")
        speak('You told me to remember that'+ rememberMassage)
        remember = open('remember.txt', "a")
        remember.write(rememberMassage)
        remember.close()

    # for asking 'what remembered'
    elif 'what do you remember' in command:
        remember = open('remember.txt', 'r')
        speak('YOu told me to remember'+ remember.read())

    elif 'clear remember file' in  command:
        file = open('remember.txt', 'w')
        file.write(f" ") 
        print(command)
        speak('done sir! everything i remember has been deleted.')

    elif 'shutdown' in command:
        speak('closing the pc in ') 
        speak('3. 2. 1')
        os.system('shutdown /s /t 1')
        print(command)

    elif 'restart' in command:
        speak('restarting the pc in ')
        speak('3. 2. 1')
        os.system('shutdown /r /t 1')
        print(command)

   # for search on web-browser
    elif 'search' in command:
        user_query = command.replace('search', '').strip()
        user_query = user_query.lower().replace(' ', '%20')
        webbrowser.open(f"https://www.google.com/search?q={user_query}")
        print(command)
        print(speak('this is what I found on the internet'))
        
    
    # for mathematical calculation
    elif 'calculate' in command:
        user_query = command.replace('calculate', '').strip()
        user_query = user_query.replace('x','*')
        result = sp.sympify(user_query)
        print(command)
        speak(f"The result is {result}")
        print(result)



    else:
        speak('  ')
 
speak("hello sir i am Sofiya")

greeting()

# Remove the infinite loop and modify to allow exit
while True:
    if run_sofiya() == "exit":
        break

# Now this line is reachable
print(speechrecognition())
