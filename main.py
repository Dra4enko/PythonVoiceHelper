import speech_recognition as sr
import os
import sys
import webbrowser
import pygame
from gtts import gTTS
import pyttsx3
<<<<<<< HEAD
from speech_recognition import Recognizer
=======
>>>>>>> e9cb97e666973865496ec9a52f3c5d95ee0b0d54

file = 'speech.mp3'


def play():
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.mixer.music.get_pos() / 1000


def tts(words):
    pgtts = gTTS(text=words, lang='ru')
    pgtts.save(file)
    play()


def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()


talk("Привет, чем я могу помочь вам?")


def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говорите")
<<<<<<< HEAD
        talk("Говорите")
=======
        talk("говорите")
>>>>>>> e9cb97e666973865496ec9a52f3c5d95ee0b0d54
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="ru-RU").lower()
    except sr.UnknownValueError:
        talk("Я вас не поняла")
        task = command()

    return task


def listen_sitename():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Название сайта")
        talk("Название сайта")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

<<<<<<< HEAD
def makeSomething(zadanie):
    if 'открыть сайт' in zadanie:
        if isopen in 'открыть сайт':
            isopen = sr.Recognizer()
        webbrowser.open(i)
=======
    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
    except sr.UnknownValueError:
        talk("Не поняла название сайта")
        task = listen_sitename()

    return task


def makeSomething(task):
    if 'открой сайт' or 'открыть сайт' in task:
        webbrowser.open(listen_sitename())
>>>>>>> e9cb97e666973865496ec9a52f3c5d95ee0b0d54
        talk("Уже открываю")

    elif 'стоп' in task:
        # talk("Да, конечно, без проблем")
        sys.exit()

    elif 'открой файл' in task:
        os.startfile(r'C:/Users/User/Desktop/img.png')  # в конечном каталоге этого пути должен быть файл 'img.png'


while True:
    makeSomething(command())
