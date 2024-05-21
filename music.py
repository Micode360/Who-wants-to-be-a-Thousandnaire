import pygame


def Intro(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def Fail():
    pygame.mixer.init()
    pygame.mixer.music.load(r'file:///C:/Users/Miracle%20King/Documents/python_course/code/week2/Lose_Who_Wants_to_Be_a_Millionaire.mp3')
    pygame.mixer.music.play()


