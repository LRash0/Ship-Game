# Usaremos esse módulo para sair do jogo quando o usuário desistir.
import sys

import pygame

from bullet import Bullet
from alien import Alien


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

		fire_bullet(ai_settings,screen,ship,bullets)

	elif event.key == pygame.K_q:
		sys.exit()




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



def update_screen(ai_settings,screen,ship,aliens,bullets):
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
	# Quando draw é chamado em um grupo,o Pygame dsenha automaticamente cada
	# elemento do grupo na posição definida pel seu atributo rect.
	aliens.draw(screen)
	# Deixa a tela mais recente visivel
	pygame.display.flip()



def create_fleet(ai_settings,screen,aliens):
	"""Cria uma frota completa de alienígenas."""
	# Cria um alienígena e calcula o número de alienígens em uma linha
	# O espaçemento entre os alienígenas é igual a largura de um alienígena

	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	

	# Cria a primeira linha de alienígenas
	for alien_number in range(number_aliens_x):
		create_alien(ai_settings,screen,aliens,alien_number)
		


def get_number_aliens_x(ai_settings,alien_width):
	"""Determina o número de alieníginas que cabem em uma linha."""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width ))

	return number_aliens_x


def create_alien(ai_settings,screen,aliens,alien_number):
	# Cria um alienígena e posiciona na linha
		alien   = Alien(ai_settings,screen)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number 
		alien.rect.x = alien.x
		aliens.add(alien)