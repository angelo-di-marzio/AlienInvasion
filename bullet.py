import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

	def __init__(self, ai_settings, screen, ship):
		super().__init__()
		self.screen=screen

		#create the bullet rect and set it to good position
		self.rect=pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_heigth)
		self.rect.centerx=ship.rect.centerx
		self.rect.top= ship.rect.top
		self.y=float(self.rect.y)
		self.color=ai_settings.bullet_color
		self.speed_factor=ai_settings.bullet_speed
	def update(self):
		#move the bullet up (rect and bullet position)
		self.y-=self.speed_factor
		self.rect.y=self.y
	def draw(self):
		pygame.draw.rect(self.screen,self.color,self.rect)
