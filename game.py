import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
	# init game
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
	pygame.display.set_caption("Tatuf's Alien Game")
	ship=Ship(screen)
	while True:
		#keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#set bg color
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		#make the last drawn screen visible
		pygame.display.flip()

run_game()	