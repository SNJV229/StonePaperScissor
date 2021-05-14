from gtts import gTTS
import random 
import playsound
import speech_recognition as sr
import playsound
from  os  import remove    

n = 1

def speak(text):
    global n
    n +=1
    print("BOT : ", text)
    ta = gTTS(text=text, lang='en-in', slow=False)
    file = str(n)+".mp3"
    ta.save(file)
    playsound.playsound(file, True)
    remove(file)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print ('speak anything ...')
        audio = r.listen(source, phrase_time_limit=5)
        print("stop")
        try:
            said = r.recognize_google(audio,language="en-in")
            print("USER :  " + said)
        except:
            print('sorry could not recognize your voice')
            c1 = "player"
            process_gm(c1)
    return said

def process_gm(c1):

    pt_A = 0
    pt_U = 0
    nb = 0
    
    while( nb<3 ):
        speak("it is yor turn "+ c1+ "." + "what is your choice?")
        c2 = get_audio()
        ran = random.choice(["scissor", "paper", "stone"])
        nb = nb+1
        if ran == "stone":
            if c2 == "paper":
                speak("you get a point, my choice was " +ran)
                pt_U += 1
                continue
            elif c2 == "scissor":
                speak("hurra!, i got a point my choice was " + ran)
                pt_A += 1
                continue
            else:
                speak("it is a tie , my choice was also " +ran)
                continue
        elif ran == "paper":
            if c2 == "scissor":
                speak("you get a point, my choice was " +ran)
                pt_U += 1
                continue
            elif c2 == "stone":
                speak("hurra!, i got a point my choice was " + ran)
                pt_A += 1
                continue
            else:
                speak("it is a tie , my choice was also " +ran)
                continue
        elif ran == "scissor":
            if c2 == "stone":
                speak("you get a point, my choice was " +ran)
                pt_U += 1
                continue
            elif c2 == "paper":
                speak("hurrah!,i got a point my choice was " + ran)
                pt_A += 1
                continue
            else:
                speak("it is a tie , my choice was also " +ran)
                continue
        elif c2 == "stop":
            speak("ok bye "+c1)
            break
        else:
            speak("can't get try please again ")
            continue
    print ()
    speak("your point is " +str(pt_U) + " and mine is " +str(pt_A))
    if pt_U < pt_A :
        speak("My luck is so strong that beating me in this game is impossible")
    elif pt_A == pt_U:
        speak("no one wins!, its a tie")
    else:
        speak("you won, you are lucky this time!")


if __name__ == "__main__":
    speak("hi there lets play stone paper scissor. what is your name?")
    c1 = get_audio().lower()
    process_gm(c1)
        





