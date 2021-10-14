import math

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
	xp = int((p[0]*math.cos(a)) + (p[1]*math.sin(a)))
	yp = int((- p[0]*math.sin(a)) + (p[1]*math.cos(a)))

	return [xp,yp]

def rotacion_h(p,angulo):
	a = math.radians(angulo)
	xp = int((p[0]*math.cos(a)) - (p[1]*math.sin(a)))
	yp = int((p[0]*math.sin(a)) + (p[1]*math.cos(a)))

	return [xp,yp]


def maxmin(puntos):
	max_x = 0
	max_y = 0
	min_x = 10000
	min_y = 10000

	for punto in puntos:
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

def centrar(puntos, centro):
	centroActual = calCentro(maxmin(puntos))
	dx = centroActual[0] - centro[0]
	dy = centroActual[1] - centro[1]

	for punto in puntos:
		punto[0] -= dx
		punto[1] -= dy

	return puntos

def traslacion_pol(poligono, t):
	poligono_2 = []

	for pto in poligono:
		poligono_2.append( traslacion(pto, t) )

	return poligono_2