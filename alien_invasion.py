# Usaremos esse módulo para sair do jogo quando o usuário desistir.
import sys
# o módulo pygame contém as funcionalidades necessárias para criar um jogo.
import pygame

from settings import Settings

def run_game():
	# Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.get_screen_width(),ai_settings.get_screen_height()))
	pygame.display.set_caption("Alien Invasion")

	

	# Inicia o laço principal do jogo

	while True:

		# Observe eventos de teclado e de mouse
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				sys.exit()

		
		# Redesenha a tela a cada passagem pelo laço.
		# Por padrão,pygame cria uma tela preta
		# Vamos definir a cor de fundo
		# O método aceita apenas um argumento,uma cor.
		# Preenchemos a cor de fundo com a cor escolhida.
		screen.fill(ai_settings.get_bg_color())

		# Deixa a tela mais recente visivel
		pygame.display.flip()

run_game()