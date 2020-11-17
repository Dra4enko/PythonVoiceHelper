import speech_recognition as sr
import os
import pyautogui as pag
import webbrowser
import pyttsx3


def talk(words):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(words)
    engine.runAndWait()


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
        print("Введите название сайта: ")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
    except sr.UnknownValueError:
        talk("Я вас не поняла.")
        task = command_sitename()

    return task


# def makeSomething(task):
#     if task == 'открой сайт':
#         talk('Открываю сайт')
#         webbrowser.open("http://" + command_sitename())
#
#     elif task == 'открой файл' or task == 'открой программу':
#         talk("Открываю файл")
#         talk("Введите путь до файла: ")
#         path = input()
#         os.startfile(path)

def makeSomething(task):
    if task == 'открой вк':
        webbrowser.open("https://vk.com")
        # webbrowser.open("http://" + command_sitename())
    elif task == 'открой стим':
        os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")

    elif task == 'открой дискорд':
        os.startfile(r"C:\Users\User\AppData\Local\Discord\Update.exe")


def command_inputtext():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Текст: ")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="en-EN").lower()
    except sr.UnknownValueError:
        talk("Я вас не поняла.")
        task = command_inputtext()

    return str(task)


while True:
    makeSomething(command())
