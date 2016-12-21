import pygame

class Ship():

	"""Classe da aeronave."""

	def __init__(self,screen):
		"""Inicializa a espaçonave e define sua posição inicial."""
		self.screen = screen
		# Carrega a imagem da espaçonave e obtém seu rect
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		self.screen_rect = screen.get_rect()

		# Inicializa cada nova espaçonave na pate inferior central da tela
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom  = self.screen_rect.bottom

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
	
		if self.get_moving_right():
			
			self.rect.centerx += 1

		if self.get_moving_left():

			self.rect.centerx -= 1

	def blitme(self):
		"""Desenha a espaçonave em sua posição atual."""
	
		self.screen.blit(self.image,self.rect)
