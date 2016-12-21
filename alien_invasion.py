# o módulo pygame contém as funcionalidades necessárias para criar um jogo.
import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
	# Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.get_screen_width(),ai_settings.get_screen_height()))
	pygame.display.set_caption("Alien Invasion")
	# Cria uma espaçonave
	ship = Ship(ai_settings,screen)
	bullets = Group()

	

	# Inicia o laço principal do jogo

	while True:

		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()
		# Livra-se dos projéteis que desapareceram
		for bullet in bullets.copy():

			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets))


		gf.update_screen(ai_settings,screen,ship,bullets)
		

run_game()