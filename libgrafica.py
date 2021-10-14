import math
import pygame 

BLANCO = [255,255,255]
NEGRO = [0,0,0]
AZUL = [0,0,255]
ROJO = [255,0,0]
VERDE = [0,255,0]
PURPURA = [255,100,255]
AMARILLO = [255,233,0]
NARANJA = [210,105,30]
MORADO = [153,50,204]

colores = [ BLANCO,NEGRO,AZUL,ROJO,VERDE,PURPURA,AMARILLO,NARANJA,MORADO ]

ANCHO = 1000
ALTO = 600

def punt_cart(p,c):
	xp = p[0] + c[0]
	yp = p[1] + c[1]

	return [xp,yp]
	
def escalar(p,s):
	xp = p[0]*s[0]
	yp = p[1]*s[1]

	return [int(xp),int(yp)]

def traslacion(p,t):
	xp = p[0] + t[0]
	yp = p[1] + t[1]
	return [xp,yp]

def rotacion_ah(p,angulo):
	a = math.radians(angulo)
	xp = (p[0]*math.cos(a)) + (p[1]*math.sin(a))
	yp = (- p[0]*math.sin(a)) + (p[1]*math.cos(a))

	return [xp,yp]

def rotacion_h(p,angulo):
	a = math.radians(angulo)
	xp = (p[0]*math.cos(a)) - (p[1]*math.sin(a))
	yp = (p[0]*math.sin(a)) + (p[1]*math.cos(a))

	return [xp,yp]


def maxmin(poligonos):
	max_x = 0
	max_y = 0
	min_x = 10000
	min_y = 10000
	for poligono in poligonos:
		for punto in poligono:
			if punto[0] > max_x:
				max_x = punto[0]
			if punto[1] > max_y:
				max_y = punto[1]
			if punto[0] < min_x:
				min_x = punto[0]
			if punto[1] < min_y:
				min_y = punto[1]

	#print( [ [max_x,min_x] , [max_y,min_y] ])
	return [ [max_x,min_x] , [max_y,min_y] ]

def calCentro(mm):
	centro = []

	centro.append( int( (mm[0][0]-mm[0][1]) / 2 ) + mm[0][1])
	centro.append( int( (mm[1][0]-mm[1][1]) / 2 ) + mm[1][1])

	return centro

def centrar(poligonos, centro):
	centroActual = calCentro(maxmin(poligonos))
	dx = centroActual[0] - centro[0]
	dy = centroActual[1] - centro[1]

	for poligono in poligonos:
		for punto in poligono:
			punto[0] -= dx
			punto[1] -= dy

	return poligonos

def traslacion_pol(poligono, t):
	poligono_2 = []

	for pto in poligono:
		poligono_2.append( traslacion(pto, t) )

	return poligono_2

def dibujar_pol(poligonos, pantalla):
	pantalla.fill(NEGRO)
	## Base y laterales traseros
	pygame.draw.polygon(pantalla,VERDE,poligonos[0])
	pygame.draw.polygon(pantalla,AZUL,poligonos[1])
	pygame.draw.polygon(pantalla,AMARILLO,poligonos[2])

	## Cruz 
	pygame.draw.polygon(pantalla,MORADO,poligonos[3])

	## Rectangulos internos 	
	pygame.draw.polygon(pantalla,PURPURA,poligonos[4])
	pygame.draw.polygon(pantalla,NARANJA,poligonos[5])
	pygame.draw.polygon(pantalla,PURPURA,poligonos[6])
	pygame.draw.polygon(pantalla,NARANJA,poligonos[7])
	pygame.draw.polygon(pantalla,NARANJA,poligonos[8])
	pygame.draw.polygon(pantalla,PURPURA,poligonos[9])
	pygame.draw.polygon(pantalla,NARANJA,poligonos[10])
	pygame.draw.polygon(pantalla,PURPURA,poligonos[11])

	## Laterales delanteros
	pygame.draw.polygon(pantalla,BLANCO,poligonos[12])
	pygame.draw.polygon(pantalla,ROJO,poligonos[13])

	## Cuadrados superiores
	pygame.draw.polygon(pantalla,VERDE,poligonos[14])
	pygame.draw.polygon(pantalla,VERDE,poligonos[15])
	pygame.draw.polygon(pantalla,VERDE,poligonos[16])
	pygame.draw.polygon(pantalla,VERDE,poligonos[17])

def rotacion_pol_ah(poligono):
	poligono_2 = []
	for pto in poligono:
		poligono_2.append( rotacion_ah(pto, 5) )

	return poligono_2

def rotacion_pol_h(poligono):
	poligono_2 = []
	for pto in poligono:
		poligono_2.append( rotacion_h(pto, 5) )

	return poligono_2