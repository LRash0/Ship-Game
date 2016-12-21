# o módulo pygame contém as funcionalidades necessárias para criar um jogo.
import pygame

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
	ship = Ship(screen)

	

	# Inicia o laço principal do jogo

	while True:

		gf.check_events()
		
		gf.update_screen(ai_settings,screen,ship)
		

run_game()