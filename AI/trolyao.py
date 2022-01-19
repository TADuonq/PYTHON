import speech_recognition
import pyttsx3
from datetime import datetime, date

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = ""
while True:
    with speech_recognition.Microphone() as mic:
        print ("Robot: I'm Listening")
        audio = robot_ear.listen(mic)
    print("Robot: ...")
    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

    if you == "":
        robot_brain = "I can't hear you, try again"
    elif "hey" in you:
        robot_brain = "Hello Sir. What I can help Sir"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "girlfriend" in you:
        robot_brain = "No sir, nobody"
    elif "bye" in you:
        robot_brain = "Goodbye Sir. See you again Sir"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm don't know"

    print("Robot: " + robot_brain)


    # voices = robot_mouth.getProperty("voices")
    # vi_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
    # robot_mouth.setProperty("voice", vi_voice_id)

    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()