import sys
import pygame

def check_events(ship):
	# KEY + MOUSE EVENTS
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				check_keydown_events(event,ship)
			elif event.type==pygame.KEYUP:
				check_keyup_events(event,ship)
def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
def check_keydown_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True

def update_screen(ai_settings, screen, ship,background):
	#set bg color
	screen.fill(ai_settings.bg_color)
	screen.blit(background.image, background.rect)
	# background.blitme()
	ship.blitme()
	#make the last drawn screen visible
	pygame.display.flip()

