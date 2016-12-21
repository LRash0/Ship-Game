import pygame
# Ao usar sprites,podemos agrupar elementos relacionados no jogo e atuar em 
# todos os elementos agrupados de uma só vez.
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""Uma classe que adminisra projéteis disparados pela nave."""

	def __init__(self,ai_settings,screen,ship):
		"""Cria um objeto para o projétil na posição atual da espaçonave."""
		# Atribui valores a todos os atributos da classe pai
		super().__init__()
		self.screen = screen


		# Cria um retângulo para o projetil em (0,0) e,em seguida,define a
		# posição correta

		self.rect = pygame.Rect(0,0,ai_settings.get_bullet_width(),
			ai_settings.get_bullet_height())


		self.rect.centerx= ship.rect.centerx
		self.rect.top = ship.rect.top


		# Armazena a posição do projetl como um valor decimal
		self.y = float(self.rect.y)

		# Armazenamos a cor e as cofiguraões de velocidade do projétil
		self.color = ai_settings.get_bullet_color()
		self.speed_factor = ai_settings.get_bullet_speed_factor()

	def update(self):
		"""Move o projétil para cima na tela."""

		# Atualiza a posição decimal do projétil
		self.y -= self.get_speed_factor()
		
		#Atualiza a posição do rect
		self.rect.y = self.y

	def draw_bullet(self):
		"""Desenha o projétil na tele."""

		pygame.draw.rect(self.screen,self.color,self.rect)

	def get_speed_factor(self):

		return self.speed_factor