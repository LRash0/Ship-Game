class Settings():
	"""Uma classe para guardar todas as configurações da Invasão Alienígena."""


	def __init__(self):
		"""Inicializa as configurações do jogo."""
		# Configuração da tela

		self.screen_width  = 800
		self.screen_height = 600
		self.bg_color 	   = (230,230,230)
		self.ship_speed_factor = 1.5

	def get_screen_width(self):

		return self.screen_width

	def get_screen_height(self):

		return self.screen_height

	def get_bg_color(self):

		return self.bg_color


	def get_ship_speed_factor(self):

		return self.ship_speed_factor