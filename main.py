import speech_recognition as sr
import os
import sys
import webbrowser
import pygame
from gtts import gTTS
import pyttsx3

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
        talk("говорите")
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

    try:
        task = r.recognize_google(audio, language='ru-RU').lower()
    except sr.UnknownValueError:
        talk("Не поняла название сайта")
        task = listen_sitename()

    return task


def makeSomething(task):
    if 'открой сайт' or 'открыть сайт' in task:
        webbrowser.open(listen_sitename())
        talk("Уже открываю")

    elif 'стоп' in task:
        # talk("Да, конечно, без проблем")
        sys.exit()

    elif 'открой файл' in task:
        os.startfile(r'C:/Users/User/Desktop/img.png')  # в конечном каталоге этого пути должен быть файл 'img.png'


while True:
    makeSomething(command())
