# Usaremos esse módulo para sair do jogo quando o usuário desistir.
import sys

import pygame

def check_events():
	"""Responde a eventos de pressionamento de teclas e de mouse."""
	# Observe eventos de teclado e de mouse
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			sys.exit()

def update_screen(ai_settings,screen,ship):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	# Redesenha a tela a cada passagem pelo laço.

	# Por padrão,pygame cria uma tela preta
	# Vamos definir a cor de fundo
	# O método aceita apenas um argumento,uma cor.
	# Preenchemos a cor de fundo com a cor escolhida.
	screen.fill(ai_settings.get_bg_color())
	ship.blitme()
	# Deixa a tela mais recente visivel
	pygame.display.flip()