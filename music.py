import pygame
import time

def Intro(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def StopMusic(): 
    pygame.mixer.music.stop()

def Lose():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(r'.\Who-wants-to-be-a-Thousandnaire\Lose_Who_Wants_to_Be_a_Millionaire.mp3')
    pygame.mixer.music.play()

def Winner():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(r'.\Who-wants-to-be-a-Thousandnaire\Winner.mp3')
    pygame.mixer.music.play()

def Final():
    pygame.mixer.music.stop()
    pygame.mixer.music.load(r'.\Who-wants-to-be-a-Thousandnaire\Final Answer.mp3')
    pygame.mixer.music.play()
    


