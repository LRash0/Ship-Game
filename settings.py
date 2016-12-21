class Settings():
	"""Uma classe para guardar todas as configurações da Invasão Alienígena."""


	def __init__(self):
		"""Inicializa as configurações do jogo."""
		# Configuração da tela

		self.screen_width  = 800
		self.screen_height = 600
		self.bg_color 	   = (230,230,230)

	def get_screen_width(self):

		return self.screen_width

	def get_screen_height(self):

		return self.screen_height

	def get_bg_color(self):

		return self.bg_color
