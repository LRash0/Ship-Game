import pygame.font

class Scoreboard():
	"""Uma classe para mostrar informações sobre pontuação."""

	def __init__(self,ai_settings,screen,stats):
		"""Inicializa os atributos da pontuação."""
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		# Configurações de fonte para as informações de pontuação
		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)

		# Prepara a imagem da pontuação inicial
		self.prep_score()

	def prep_score(self):
		"""Transforma a pontuação e uma imagem renderizada."""
		# A função round arredonda um número decimal com uma quantidade definida
		# de casas decimais especificada como o segundo argumento.No entanto
		# ,se um número negativo for passado como segundo argumento,round()
		# arredondará o valor para o múltiplo mais próximo de 10,100,1000 e 
		# assim por diante
		rounded_score =  round(self.stats.score,-1)
		# Uma diretiva formatação de string diz a Python para inserir vírgulas
		# nos números ao converter um valor númerico em uma string
		score_str = "{:,}".format(rounded_score)
		
		self.score_image = self.font.render(score_str,True,self.text_color,
			self.ai_settings.bg_color)

		# Exibe a pontuação na parte superior direito da tela
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def show_score(self):
		"""Desenha a pontuação na tela."""
		self.screen.blit(self.score_image,self.score_rect)
