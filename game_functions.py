# Usaremos esse módulo para sair do jogo quando o usuário desistir.
import sys

import pygame

from time import sleep

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



def check_play_button(stats,play_button,mouse_x,mouse_y):
	"""Inicia um novo jogo quando o jogador clicar em Play."""

	if play_button.rect.collidepoint(mouse_x,mouse_y):
		stats.game_active = True


def check_events(ai_settings,screen,stats,play_button,ship,bullets):
	"""Responde a eventos de pressionamento de teclas e de mouse."""
	# Observe eventos de teclado e de mouse
	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			
			sys.exit()

		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(stats,play_button,mouse_x,mouse_y)


		elif event.type == pygame.KEYDOWN:
			
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:

			check_keyup_events(event,ship)



def update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button):
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

	# Desenha o botão Playse  jogo estiver inativo

	if not stats.game_active:
		play_button.draw_button()

	# Deixa a tela mais recente visivel
	pygame.display.flip()



def create_fleet(ai_settings,screen,ship,aliens):
	"""Cria uma frota completa de alienígenas."""
	# Cria um alienígena e calcula o número de alienígens em uma linha
	# O espaçemento entre os alienígenas é igual a largura de um alienígena

	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

	# Cria a primeira linha de alienígenas
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			create_alien(ai_settings,screen,aliens,alien_number,row_number)
		


def get_number_aliens_x(ai_settings,alien_width):
	"""Determina o número de alieníginas que cabem em uma linha."""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width ))

	return number_aliens_x


def create_alien(ai_settings,screen,aliens,alien_number,row_number):
	# Cria um alienígena e posiciona na linha
		alien   = Alien(ai_settings,screen)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number 
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		aliens.add(alien)


def get_number_rows(ai_settings,ship_height,alien_height):
	"""Determina o número de linhas cm alieníginas que cabem na tela."""
	available_space_y = (ai_settings.get_screen_height() -
						(3 * alien_height) - ship_height)

	number_rows = int(available_space_y/ (2 * alien_height))

	return number_rows


def update_aliens(ai_settings,stats,screen,ship,aliens,bullets):
	"""Verifica se a frota está em uma das bordas e então 
	atualiza as posições de todos os alienígenas da frota."""
	check_fleet_edges(ai_settings,aliens)
	aliens.update()

	# Verifica se houve colisões entre alienígenas e a espaçonave
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
	# Verifica se há algum alienígena que atingiu a parte interior da tela
	check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets)


def check_fleet_edges(ai_settings,aliens):
	"""Responde apropriadamente se algum aliegnígena alcançou a borda."""

	for alien in aliens.sprites():
		
		if alien.check_edges():
		
			change_fleet_direction(ai_settings,aliens)
		
			break

def change_fleet_direction(ai_settings,aliens):
	"""Faz toda a frota descer e muda a sua direção."""

	for alien in aliens.sprites():

		alien.rect.y += ai_settings.get_fleet_drop_speed()
	ai_settings.set_fleet_direction()


def update_bullets(ai_settings,screen,ship,bullets,aliens):
	"""Atualizaa posção dos projeteis e se livra dos projéteis antigos."""

	# Atualiza as posições dos projéteis
	bullets.update()

	# Livra-se dos projéteis que desapareceram 
	for bullet in bullets.copy():

		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)

	

	

def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
	"""Responde a colisões entre projéteis e alienígenas."""
	
	#Remove qualquer projétil e alienígena que tenham colidido
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	if len(aliens) == 0:
		# Destrói os projéteis existentes e cria uma nova frota
		bullets.empty()
		create_fleet(ai_settings,screen,ship,aliens)


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
	"""Responde ao fato de a espaçonave ter sido atingida pr um alienígena."""
	# Decrementa ships_left
	if stats.ships_left >0:
		stats.ships_left -= 1

		# Esvazia alista de alienígenas e de projéteis
		aliens.empty()
		bullets.empty()

		# Cria uma nova frota e centraliza a espaçonave
		create_fleet(ai_settings,screen,ship,aliens)
		ship.center_ship()

		# Faz uma pausa
		sleep(0.5)
	else:
		stats.game_active = False

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
	"""Verifica se algum alienígena alcançou a parte inferior da tela."""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			# Trata esse caso do mesmo mod que é feito quando a espaçonave é
			# atingida
			ship_hit(ai_settings,stats,screen,ship,aliens,bullets)
			break