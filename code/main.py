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
	music_time = 0
	music_time2 = 0
	for i in range(130):
		os.system('cls')
		print(Fore.BLACK + Back.WHITE + 'Freddie Dredd ' + Style.RESET_ALL + '-' + Fore.WHITE + Back.BLACK + ' Killin On Demand')
		if music_time == 60:
			music_time2 = music_time2 + 1
			music_time = 0
		music_time = music_time + 1
		print('  ' + Fore.WHITE, Back.BLACK + f'{music_time2}:{music_time}/2:10')
		print(text)
		time.sleep(1)
	a2 = pygame.mixer.Sound('playlist/2.wav')
	a2.play()
	music_time = 0
	music_time2 = 0
	for i in range(120):
		os.system('cls')
		print(Fore.BLACK + Back.WHITE + 'keygen.exe ' + Style.RESET_ALL + '-' + Fore.WHITE + Back.BLACK + ' а сил у тебя хватит?')
		if music_time == 60:
			music_time2 = music_time2 + 1
			music_time = 0
		music_time = music_time + 1
		print('  ' + Fore.WHITE, Back.BLACK + f'{music_time2}:{music_time}/2:00')
		print(text)
		time.sleep(1)
	a3 = pygame.mixer.Sound('playlist/3.mp3')
	a3.play()
	music_time = 0
	music_time2 = 0
	for i in range(95):
		os.system('cls')
		print(Fore.BLACK + Back.WHITE + 'Encassator, Madeinevil ' + Style.RESET_ALL + '-' + Fore.WHITE + Back.BLACK + ' Never Met!')
		if music_time == 60:
			music_time2 = music_time2 + 1
			music_time = 0
		music_time = music_time + 1
		print('  ' + Fore.WHITE, Back.BLACK + f'{music_time2}:{music_time}/1:35')
		print(text)
		time.sleep(1)
	a4 = pygame.mixer.Sound('playlist/4.mp3')
	a4.play()
	music_time = 0
	music_time2 = 0
	for i in range(143):
		os.system('cls')
		print(Fore.BLACK + Back.WHITE + 'Prodby668 ' + Style.RESET_ALL + '-' + Fore.WHITE + Back.BLACK + ' prolly my spookiest beat (Slowed+Reverbed)')
		if music_time == 60:
			music_time2 = music_time2 + 1
			music_time = 0
		music_time = music_time + 1
		print('  ' + Fore.WHITE, Back.BLACK + f'{music_time2}:{music_time}/2:23')
		print(text)
		time.sleep(1)
