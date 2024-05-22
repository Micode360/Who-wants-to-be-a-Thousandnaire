import pygame


def Intro(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def Fail():
    pygame.mixer.init()
    pygame.mixer.music.load(r'C:\Users\MIYIAGI\Documents\T4S\python\newtest\Who-wants-to-be-a-Thousandnaire\Lose_Who_Wants_to_Be_a_Millionaire.mp3')
    pygame.mixer.music.play()


