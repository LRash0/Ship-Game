from file import File

class GameStats():
	"""Armazena dados estatísticos da Invasão Alienígena."""

	def __init__(self,ai_settings):
		"""Inicializa os dados estatísticos."""
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = False
		self.high_score = None
		self.file = File()
		self.start_high_score()


	def reset_stats(self):
		"""Inicializa os dados estatísticos que podem mudar durante o jogo."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1


	def start_high_score(self):
		self.high_score = self.file.read_high_score()
				