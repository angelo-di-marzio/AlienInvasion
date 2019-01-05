import pygame
from settings import Settings
from ship import Ship
from background import Background
import game_functions as gf


def run_game():
	# init game
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
	pygame.display.set_caption("Tatuf's Alien Game")
	ship=Ship(ai_settings,screen)
	background=Background(ai_settings,screen)
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 30)
	while True:
		#keyboard and mouse events
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings,screen,ship,background)

		fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
		screen.blit(fps, (50, 50))
		pygame.display.flip()
		clock.tick(60)

run_game()	