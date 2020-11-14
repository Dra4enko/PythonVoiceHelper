import speech_recognition as sr
import os
import sys
import webbrowser
import pygame
import pyttsx3

def talk(words):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(words)
    engine.runAndWait()

talk("Привет")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = command()

    return task

def command_sitename():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Название сайта")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = command_sitename()

    return task

def makeSomething(task):
    if 'открой сайт' or 'открыть сайт' in task:
        talk("Уже открываю")
        # webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")
        webbrowser.open("http://" + command_sitename())

    elif 'стоп' in task:
        sys.exit()

    elif 'открой файл' in task:
        os.startfile(r'C:/Users/User/Desktop/img.png')  # в конечном каталоге этого пути должен быть файл 'img.png'


while True:
    makeSomething(command())
