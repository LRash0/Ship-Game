class Settings():
	"""Uma classe para guardar todas as configurações da Invasão Alienígena."""


	def __init__(self):
		"""Inicializa as configurações do jogo."""
		
		# Configuração da tela

		self.screen_width  = 800
		self.screen_height = 600
		self.bg_color 	   = (230,230,230)
		
		
		# Configurações dos projéteis
		
		self.bullet_width  = 3
		self.bullet_height = 15
		self.bullet_color = 60,60,60
		self.bullets_allowed = 6
		
		# Cofiguralções dos aliens
		
		
		# Velocidade vertical
		self.fleet_drop_speed = 10
		# Fleet direction igual a  1 representa direita;
		# Fleet direction igual a -1 representa esquerda
		
		
		# Configurações da espaçonave
		self.ship_limit = 3

		# A taxa de velocidade do jogo aumenta
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""Inicializa as confgurações que mudam no decorrer do jogo."""
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 2
		self.alien_speed_factor = 1


		# fleet_direction igual a 1 representa direita;-1 representa a esquerda
		self.fleet_direction = 1

		# Potuação 
		self.alien_points = 50


	def increase_speed(self):
		"""Aumenta as configurações de velocidade."""
		self.ship_speed_factor *= self.speedup_scale
		# self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		if self.bullets_allowed > 3:
			self.bullets_allowed -= 1


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