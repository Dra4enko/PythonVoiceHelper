import speech_recognition as sr
import os
import sys
import webbrowser
import pygame
from gtts import gTTS

file = 'speech.mp3'
isopen = False


def play():
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    if not isopen:
        isopen = True
        file = 'speech1.mp3 '
    else:
        isopen = False
        file = 'speech.mp3'


def tts(words):
    pgtts = gTTS(text=words, lang='ru')
    pgtts.save(file)
    play()


def talk(words):
    print(words)
    tts(words)


talk("Привет, чем я могу помочь вам?")


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
        webbrowser.open('https://itproger.com')
        talk("Уже открываю")
    elif 'стоп' in zadanie:
        # talk("Да, конечно, без проблем")
        sys.exit()
    elif 'открой файл' in zadanie:
        os.startfile(r'C:/Users/User/Desktop/img.png')  # в конечном каталоге этого пути должен быть файл 'img.png'


while True:
    makeSomething(command())
