# import speech_recognition as sr
import sys
import webbrowser
import pygame
from gtts import gTTS

file = 'speech.mp3'


def play():
    open('speech.mp3')
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
    print(words)
    tts(words)


talk("Привет, чем я могу помочь вам?")


def command():
    return 0


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


def makesomething(zadanie):
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
    makesomething(command())
