import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

	"""Classe da aeronave."""

	def __init__(self,ai_settings,screen):
		
		super().__init__()

		"""Inicializa a espaçonave e define sua posição inicial."""
		self.screen = screen
		self.ai_settings = ai_settings
		# Carrega a imagem da espaçonave e obtém seu rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		self.screen_rect = screen.get_rect()

		# Inicializa cada nova espaçonave na pate inferior central da tela
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom

		# Armazena um valor decimal para o centro da espaçonave
		self.center = float(self.rect.centerx)

		#Flag do movimento
		self.moving_right = False
		self.moving_left = False


	def set_moving_right(self,validation):
		""" Permite  ou nao mover a nave para a direita.
		Dependendo das ações do jogador."""
		if validation:

			self.moving_right = True

		else:

			self.moving_right = False

	def set_moving_left(self,validation):
		""" Permite  ou nao mover a nave para a esquerda.
		Dependendo das ações do jogador."""
		if validation:
			
			self.moving_left = True
		
		else:

			self.moving_left = False

	def get_moving_right(self):
		"""Devolve o atual valor de moving_right."""
		return self.moving_right

	def get_moving_left(self):
		"""Devolve o atual valor de moving_left."""
		return self.moving_left


	def update(self):
		"""Atualiza a posição da espaçonave de acordo com a flag de movimento."""
	
		if ( self.get_moving_right() and
		 (self.rect.right < self.screen_rect.right)):
			
			self.center += self.ai_settings.get_ship_speed_factor()

		if self.get_moving_left() and (self.rect.left > 0):

			self.center -= self.ai_settings.get_ship_speed_factor()

		# Atualiza o objeto rect de acordo com self.center
		self.rect.centerx = self.center

	def blitme(self):
		"""Desenha a espaçonave em sua posição atual."""
	
		self.screen.blit(self.image,self.rect)

	def center_ship(self):
		"""Centraliza a espaçonave na tela."""
		self.center = self.screen_rect.centerx