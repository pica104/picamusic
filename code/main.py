import keyboard
import time
import os
import sys
import pyperclip
import colorama
from colorama import Fore, Back, Style
import shutil
import webbrowser
import pyaudio
import wave
import sys
import pygame
colorama.init(autoreset=True)
pygame.mixer.init()

text = f'\n\nPlays in PicaMusic!\nDeveloper is Pica104'

os.system('cls')
print(Fore.BLACK + Back.WHITE + 'PicaMusic loading...')
time.sleep(1.5)
os.system('cls')

while True:
	a1 = pygame.mixer.Sound('playlist/1.mp3')
	a1.play()
	os.system('cls')
	print(Fore.BLACK + Back.WHITE + 'Freddie Dredd ' + Style.RESET_ALL + '-' + Fore.WHITE + Back.BLACK + ' Killin On Demand')
	print(text)
	time.sleep(130)
	a2 = pygame.mixer.Sound('playlist/2.wav')
	a2.play()
	os.system('cls')
	print(Fore.BLACK + Back.WHITE + 'keygen.exe ' + Style.RESET_ALL + '-' + Fore.WHITE + Back.BLACK + ' а сил у тебя хватит?')
	print(text)
	time.sleep(120)
	a3 = pygame.mixer.Sound('playlist/3.mp3')
	a3.play()
	os.system('cls')
	print(Fore.BLACK + Back.WHITE + 'Encassator, Madeinevil ' + Style.RESET_ALL + '-' + Fore.WHITE + Back.BLACK + ' Never Met!')
	print(text)
	time.sleep(95)
	a4 = pygame.mixer.Sound('playlist/4.mp3')
	a4.play()
	os.system('cls')
	print(Fore.BLACK + Back.WHITE + 'Prodby668 ' + Style.RESET_ALL + '-' + Fore.WHITE + Back.BLACK + ' prolly my spookiest beat (Slowed+Reverbed)')
	print(text)
	time.sleep(143)