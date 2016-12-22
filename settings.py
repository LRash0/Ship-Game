class Settings():
	"""Uma classe para guardar todas as configurações da Invasão Alienígena."""


	def __init__(self):
		"""Inicializa as configurações do jogo."""
		# Configuração da tela

		self.screen_width  = 800
		self.screen_height = 600
		self.bg_color 	   = (230,230,230)
		self.ship_speed_factor = 1.5
		# Configurações dos projéteis
		self.bullet_speed_factor = 1
		self.bullet_width  = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 3
		# Cofiguralções dos aliens
		self.alien_speed_factor = 1
		# Velocidade vertical
		self.fleet_drop_speed = 10
		# Fleet direction igual a  1 representa direita;
		# Fleet direction igual a -1 representa esquerda
		self.fleet_direction = 1

	def get_screen_width(self):

		return self.screen_width

	def get_screen_height(self):

		return self.screen_height

	def get_bg_color(self):

		return self.bg_color


	def get_ship_speed_factor(self):

		return self.ship_speed_factor

	def get_bullet_width(self):

		return self.bullet_width

	def get_bullet_height(self):

		return self.bullet_height

	def get_bullet_color(self):

		return self.bullet_color

	def get_bullet_speed_factor(self):

		return self.bullet_speed_factor

	def get_bullets_allowed(self):
		
		return self.bullets_allowed

	def get_alien_speed_factor(self):

		return self.alien_speed_factor


	def get_fleet_drop_speed(self):

		return self.fleet_drop_speed

	def get_fleet_direction(self):

		return self.fleet_direction

	def set_fleet_direction(self):
		self.fleet_direction *= -1