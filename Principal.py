import pygame
from libgrafica import *


if __name__ == '__main__':
	pygame.init()

	pantalla = pygame.display.set_mode([600,400])

	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		pygame.display.flip()		


	pygame.quit()