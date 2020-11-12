import speech_recognition as sr
import os
import sys
import webbrowser


def talk(words):
    print(words)
    os.system("say " + words)


talk("Привет, чем я могу помочь вам")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        zadanie = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + zadanie)
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        zadanie = command()

    return zadanie


def makeSomething(zadanie):
    if 'открыть сайт' in zadanie:
        talk("Уже открываю")
        url = 'https://itproger.com'
        webbrowser.open(url)
    elif 'стоп' in zadanie:
        talk("Да, конечно, без проблем")
        sys.exit()
    elif 'имя' in zadanie:
        talk("Меня зовут Сири")


while True:
    makeSomething(command())
