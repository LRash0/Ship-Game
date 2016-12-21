# Usaremos esse módulo para sair do jogo quando o usuário desistir.
import sys

import pygame

from bullet import Bullet


def fire_bullet(ai_settings,screen,ship,bullets):
	"""Dispara m projétil se o limite ainda não foi alcançado."""

	#Cria um novo projétil e o adiciona ao gupo de projéteis
		if len(bullets)< ai_settings.get_bullets_allowed():

			new_bullet = Bullet(ai_settings,screen,ship)
	
			bullets.add(new_bullet)


def check_keydown_events(event,ai_settings,screen,ship,bullets):
	"""Responde a pressionamentos de tecla."""
	
	if event.key == pygame.K_RIGHT:
		# Mova a espaçonave para a direita
	
		ship.set_moving_right(True)
	
	elif event.key == pygame.K_LEFT:
		# Move a espaçonave para a esquerda

		ship.set_moving_left(True)

	elif event.key == pygame.K_SPACE:

		fire_bullet(ai_setting,screen,ship,bullets)




def check_keyup_events(event,ship):
	"""Responde a solturas de tecla."""

	if event.key == pygame.K_RIGHT:
		# Quando soltar a tecla,parar a nave
		
		ship.set_moving_right(False)

	elif event.key == pygame.K_LEFT:
		# Quando soltar a tecla,parar a nave
		
		ship.set_moving_left(False)


def check_events(ai_settings,screen,ship,bullets):
	"""Responde a eventos de pressionamento de teclas e de mouse."""
	# Observe eventos de teclado e de mouse
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:

			check_keyup_events(event,ship)



def update_screen(ai_settings,screen,ship,bullets):
	"""Atualiza as imagens na tela e alterna para a nova tela."""
	# Redesenha a tela a cada passagem pelo laço.

	# Por padrão,pygame cria uma tela preta
	# Vamos definir a cor de fundo
	# O método aceita apenas um argumento,uma cor.
	# Preenchemos a cor de fundo com a cor escolhida.
	screen.fill(ai_settings.get_bg_color())

	# Redeseha todos os os projéteis atrás da espaçonave e dos alienígenas
	for bullet in bullets:
		bullet.draw_bullet()

	ship.blitme()
	# Deixa a tela mais recente visivel
	pygame.display.flip()