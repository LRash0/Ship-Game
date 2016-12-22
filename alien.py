import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

	"""Uma classe que representa um único alienígina da frota."""

	def __init__(self,ai_settings,screen):
		super().__init__()

		self.screen = screen
		self.ai_settings = ai_settings

		# Carrega a imagem do alienígena e define seu atributo rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()

		# Inicia cada novo alienígina próximo à parte superior esquerda da tela
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Armazena a posição exata do alienígena
		self.x = float(self.rect.x)


	def blitme(self):
		"""Desenha o alienígena em sua posição atual."""
		self.screen.blit(self.image,self.rect)


	def update(self):
		"""Move o alienígena para a direita."""
		self.x += self.ai_settings.get_alien_speed_factor()
		self.rect.x = self.x