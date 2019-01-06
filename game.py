import pygame
from settings import Settings
from ship import Ship
from background import Background
import game_functions as gf
from pygame.sprite import Group

def run_game():
	# init game
	pygame.init()
	ai_settings=Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_heigth))
	pygame.display.set_caption("Tatuf's Alien Game")
	#make a ship
	ship=Ship(ai_settings,screen)
	#create background
	background=Background(ai_settings,screen)
	#make a group to store bullets
	bullets=Group()
	clock = pygame.time.Clock()
	font = pygame.font.Font(None, 30)
	while True:
		#keyboard and mouse events
		gf.check_events(ai_settings,screen,ship,bullets)
		
		ship.update()
		
		gf.update_bullets(bullets)
		gf.update_screen(ai_settings,screen,ship,background,bullets)

		fps = font.render(str(int(clock.get_fps())), True, pygame.Color('white'))
		screen.blit(fps, (50, 50))
		pygame.display.flip()
		clock.tick(240)

run_game()	