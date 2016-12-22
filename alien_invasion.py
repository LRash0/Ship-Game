# o módulo pygame contém as funcionalidades necessárias para criar um jogo.
import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf

def clean_bullen_after_top(bullets):
	""" Livra-se dos projéteis que desapareceram ."""

	for bullet in bullets.copy():

		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	
def run_game():
	# Inicializa o jogo e cria um objeto para a tela
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.get_screen_width(),ai_settings.get_screen_height()))
	pygame.display.set_caption("Alien Invasion")
	# Cria uma espaçonave
	ship = Ship(ai_settings,screen)
	
	# Cria os grupos de bullets e alien
	bullets = Group()
	aliens  = Group()
	
	# Cria a frota de alienígenas
	gf.create_fleet(ai_settings,screen,ship,aliens)
	

	

	# Inicia o laço principal do jogo

	while True:

		gf.check_events(ai_settings,screen,ship,bullets)
		ship.update()
		bullets.update()

		clean_bullen_after_top(bullets)

		gf.update_screen(ai_settings,screen,ship,aliens,bullets)
		

run_game()