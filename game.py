import pygame
import numpy as np
import time

pygame.init()

# Ancho y alto de la pantalla
width, height = 500, 500
# Creacion de la pantalla.
screen = pygame.display.set_mode((height, width))

# Color del fondo
bg = 25, 25, 25

# Pintar el fondo con el color que definimos.
screen.fill(bg)

# Numero de celdas que tendremos en la pantalla
nxC, nyC = 25, 25

# las dimensiones que tendran las celdas
dimCW = width / nxC
dimCH = height / nyC

# Estado de las celdas. Vivas = 1; Muertas = 0
gameState = np.zeros((nxC, nyC))


# Autómata palo
gameState[5, 3] = 1
gameState[5, 4] = 1 
gameState[5, 5] = 1

# Autómata movil
#gameState[21, 21] = 1
#gameState[22, 22] = 1
#gameState[22, 23] = 1
#gameState[21, 23] = 1
#gameState[20, 23] = 1


# Bucle del juego
while True:
	# Creamos una nueva copia del estado del juego con los nuevos calculos
	newGameState = np.copy(gameState)

	# Limpiamos la pantalla
	screen.fill(bg)
	time.sleep(0.3)

	# Recorremos el arreglo y lo dibujamos en la pantalla
	for x in range(0, nxC):
		for y in range(0, nyC):
			# Calculamos el número de vecinos cercanos.
			n_neigh = gameState[(x - 1) % nxC, (y - 1) % nyC] + \
				gameState[(x) % nxC, (y - 1) % nyC] + \
				gameState[(x + 1) % nxC, (y - 1) % nyC] + \
				gameState[(x - 1) % nxC, (y) % nyC] + \
				gameState[(x + 1) % nxC, (y) % nyC] + \
				gameState[(x - 1) % nxC, (y + 1) % nyC] + \
				gameState[(x) % nxC, (y + 1) % nyC] + \
				gameState[(x + 1) % nxC, (y + 1) % nyC]

			# Rule #1: Una célula muerta con exactamente 3 vecinas vivas, "revive"
			if not gameState[x, y] and n_neigh == 3:
				newGameState[x, y] = 1
			# Rule #2: Una célula viva con menos de 2 o más de 3 vecinas vivas, "muere"
			elif gameState[x, y] and (n_neigh < 2 or n_neigh > 3):
				newGameState[x, y] = 0
			# Crear el poligono por cada cuadro
			poly = [((x) * dimCW, y * dimCH),
					((x + 1) * dimCW, y * dimCH),
					((x + 1) * dimCW, (y + 1) * dimCH),
					((x) * dimCW, (y + 1) * dimCH)
					]
			
			# Visualizamos cuadrados con borde blanco si esta muerto
			if newGameState[x, y] == 0:
				pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
			# Mas gonito si está vivo
			else:
				pygame.draw.polygon(screen, (255, 255, 255), poly, 0)

		# Actualizamos el estado del juego
		gameState = np.copy(newGameState)
		# Actualizamos la pantalla.
		pygame.display.flip()
