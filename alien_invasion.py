# o módulo pygame contém as funcionalidades necessárias para criar um jogo.
import pygame

from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
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
	
	# Cria os grupos de bullets e alien
	bullets = Group()
	aliens  = Group()
	
	# Cria a frota de alienígenas
	gf.create_fleet(ai_settings,screen,ship,aliens)
	
	# Cria uma instância para armazenar dados estatísticos do jogo
	stats = GameStats(ai_settings)
	sb = Scoreboard(ai_settings,screen,stats)

	# Criando o botão play
	play_button = Button(ai_settings,screen,"Play")
	

	# Inicia o laço principal do jogo

	while True:

		gf.check_events(ai_settings,screen,stats,play_button,ship,aliens,
			bullets,sb)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,stats,screen,ship,bullets,aliens,sb)
			gf.update_aliens(ai_settings,stats, screen,ship,aliens,bullets)
		
		gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,
			play_button,sb)
		

run_game()