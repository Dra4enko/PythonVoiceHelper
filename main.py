import speech_recognition as sr
import os
import webbrowser
import pyttsx3
import libcommands as libcmd

def talk(words):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(words)
    engine.runAndWait()


def listener():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = listener()

    return task


def command(task):
    for key, value in libcmd.commands.items():
        if task == key:
            if 'сайт' in task:
                webbrowser.open(value)

            elif 'файл' in task:
                os.startfile(value)


while True:
    command(listener())



































