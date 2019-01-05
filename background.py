import pygame

class Background():
	def __init__(self,ai_settings, screen):
		self.screen=screen
		self.ai_settings=ai_settings
		self.image=pygame.image.load('images/bg.png')
		self.rect=self.image.get_rect()
		self.screen_rect= screen.get_rect()

		self.rect.centerx=self.screen_rect.centerx
		self.rect.bottom= self.screen_rect.bottom

		self.center = float(self.rect.centerx)


	def blitme(self):
		#draw ship
		self.screen.blit(self.image, self.rect)