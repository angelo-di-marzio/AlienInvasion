import sys
import pygame
from bullet import Bullet

def check_events(ai_settings, screen, ship,bullets):
	# KEY + MOUSE EVENTS
	for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type==pygame.KEYDOWN:
				check_keydown_events(event,ai_settings, screen, ship, bullets)
			elif event.type==pygame.KEYUP:
				check_keyup_events(event,ship)
def check_keyup_events(event,ship):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=False
	elif event.key==pygame.K_LEFT:
		ship.moving_left=False
def check_keydown_events(event,ai_settings, screen, ship, bullets):
	if event.key==pygame.K_RIGHT:
		ship.moving_right=True
	elif event.key==pygame.K_LEFT:
		ship.moving_left=True
	elif event.key==pygame.K_SPACE:
		fire_bullet(event,ai_settings, screen, ship, bullets)
def fire_bullet(event,ai_settings, screen, ship, bullets):
	if len(bullets)<=ai_settings.bullets_allowed:
		new_bullet=Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship,background, bullets):
	#set bg color
	screen.fill(ai_settings.bg_color)
	screen.blit(background.image, background.rect)
	# background.blitme()
	ship.blitme()
	for bullet in bullets.sprites():
		bullet.draw()
	#make the last drawn screen visible
	pygame.display.flip()
def update_bullets(bullets):
	bullets.update()
	#DELETE all bullets non visible
	for bullet in bullets.copy():
		if bullet.rect.bottom<=0:
			bullets.remove(bullet)
	print(len(bullets))