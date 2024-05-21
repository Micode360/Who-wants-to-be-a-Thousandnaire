import pygame


def Intro(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def Fail():
    pygame.mixer.init()
    pygame.mixer.music.load(r'.\Who_Wants_To_Be_A_Millionaire Full_Theme.mp3')
    pygame.mixer.music.play()


