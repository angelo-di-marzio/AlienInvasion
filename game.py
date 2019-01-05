import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	# init game
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
	pygame.display.set_caption("Tatuf's Alien Game")
	ship=Ship(ai_settings,screen)
	while True:
		#keyboard and mouse events
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship)

run_game()	