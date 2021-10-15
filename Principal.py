import pygame
import random
from libgrafica import *


if __name__ == '__main__':
	pygame.init()

	pantalla = pygame.display.set_mode([ANCHO,ALTO])

	cuadricula = 50
	centro = [500,400]


	a = [cuadricula*3,0]
	a_r = rotacion_ah(a,30)
	a_rc = punt_cart(a_r,centro)
	b = [cuadricula*3,0]
	b_r = rotacion_ah(b,90)
	b_rc = punt_cart(b_r,a_rc)
	c = [cuadricula,0]
	c_r = rotacion_ah(c,210)
	c_rc = punt_cart(c_r,b_rc)
	d = [cuadricula*2,0]
	d_r = rotacion_ah(d, 270)
	d_rc = punt_cart(d_r,c_rc)
	e = [cuadricula,0]
	e_r = rotacion_ah(e, 210)
	e_rc = punt_cart(e_r,d_rc)
	f = [cuadricula*2,0]
	f_r = rotacion_ah(f, 90)
	f_rc = punt_cart(f_r,e_rc)
	g = [cuadricula,0]
	g_r = rotacion_ah(g, 210)
	g_rc = punt_cart(g_r,f_rc)

	## Lateral delantero derecho
	poligono1 = [centro,a_rc,b_rc,c_rc,d_rc,e_rc,f_rc,g_rc]
	
	h = [cuadricula,0]
	h_r = rotacion_ah(h,150)
	h_rc = punt_cart(h_r,g_rc)
	i = [cuadricula*2,0]
	i_r = rotacion_ah(i,270)
	i_rc = punt_cart(i_r,h_rc)
	j = [cuadricula,0]
	j_r = rotacion_ah(j,150)
	j_rc = punt_cart(j_r,i_rc)
	k = [cuadricula*2,0]
	k_r = rotacion_ah(k,90)
	k_rc = punt_cart(k_r,j_rc)
	l = [cuadricula,0]
	l_r = rotacion_ah(l,150)
	l_rc = punt_cart(l_r,k_rc)
	m = [cuadricula*3,0]
	m_r = rotacion_ah(m,270)
	m_rc = punt_cart(m_r,l_rc)

	## Lateral delantero izquierdo
	poligono2 = [centro,g_rc,h_rc,i_rc,j_rc,k_rc,l_rc,m_rc]

	dif_lg = [ l_rc[0] - g_rc[0] , l_rc[1] - g_rc[1] ]
	dif_bg = [ b_rc[0] - g_rc[0] , b_rc[1] - g_rc[1] ]
	dif_fg = [ f_rc[0] - g_rc[0] , f_rc[1] - g_rc[1] ]
	dif_cg = [ c_rc[0] - g_rc[0] , c_rc[1] - g_rc[1] ]
	dif_kg = [ k_rc[0] - g_rc[0] , k_rc[1] - g_rc[1] ]
	dif_hg = [ h_rc[0] - g_rc[0] , h_rc[1] - g_rc[1] ]

	##Vistas laterales traseras
	poligono3 = [ traslacion(pto,dif_lg) for pto in poligono1 ]
	poligono4 = [ traslacion(pto,dif_bg) for pto in poligono2 ]

	## Base
	poligono5 = [ centro, m_rc, traslacion(m_rc,dif_bg),traslacion(centro,dif_bg) ]

	## Cuadrados superiores
	poligono6 = [ g_rc, h_rc, traslacion(h_rc,dif_fg), traslacion(g_rc,dif_fg) ]
	poligono7 = [ traslacion(pto,dif_cg) for pto in poligono6 ]
	poligono8 = [ traslacion(pto,dif_kg) for pto in poligono6 ]
	poligono9 = [ traslacion(pto,dif_cg) for pto in poligono8 ]

	## Rectangulos internos
	poligono10 = [ f_rc, e_rc, traslacion(e_rc, dif_hg), traslacion(f_rc,dif_hg) ]
	poligono11 = [ traslacion(pto,dif_kg) for pto in poligono10 ]
	poligono12 = [ traslacion(pto,dif_fg) for pto in poligono10 ]
	poligono13 = [ traslacion(pto,dif_kg) for pto in poligono12 ]
	poligono14 = [ i_rc, h_rc, traslacion(h_rc, dif_fg), traslacion(i_rc,dif_fg) ] 
	poligono15 = [ traslacion(pto,dif_hg) for pto in poligono14 ]
	poligono16 = [ traslacion(pto,dif_cg) for pto in poligono14 ]
	poligono17 = [ traslacion(pto,dif_cg) for pto in poligono15 ]

	## Cruz
	poligono18 = [ e_rc, d_rc, traslacion(d_rc,dif_hg), traslacion(i_rc,dif_bg), traslacion(j_rc,dif_bg), 
					traslacion(j_rc,dif_cg), traslacion(d_rc,dif_lg), traslacion(e_rc,dif_lg), traslacion(e_rc,dif_kg),
					j_rc, i_rc, traslacion(i_rc,dif_fg) ]


	poligonos = [ poligono5, poligono3, poligono4, poligono18, poligono13, poligono17, poligono11, poligono16, poligono15,
					poligono12, poligono14, poligono10, poligono1, poligono2, poligono6, poligono7, 
 					poligono8, poligono9 ]


	dibujar_pol(poligonos, pantalla)
	

	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

			if event.type == pygame.KEYDOWN:
			## Traslacion
				if event.key == pygame.K_UP:
					poligonos2 = []
					for poligono in poligonos:
						poligono = traslacion_pol(poligono, [0,-20])
						poligonos2.append(poligono)
					poligonos = poligonos2
					dibujar_pol(poligonos2,pantalla)
				if event.key == pygame.K_DOWN:
					poligonos2 = []
					for poligono in poligonos:
						poligono = traslacion_pol(poligono, [0,20])
						poligonos2.append(poligono)
					poligonos = poligonos2
					dibujar_pol(poligonos2,pantalla)
				if event.key == pygame.K_LEFT:
					poligonos2 = []
					for poligono in poligonos:
						poligono = traslacion_pol(poligono, [-20,0])
						poligonos2.append(poligono)
					poligonos = poligonos2
					dibujar_pol(poligonos2,pantalla)
				if event.key == pygame.K_RIGHT:
					poligonos2 = []
					for poligono in poligonos:
						poligono = traslacion_pol(poligono, [20,0])
						poligonos2.append(poligono)
					poligonos = poligonos2
					dibujar_pol(poligonos2,pantalla)
			## Escalamiento
				if event.key == pygame.K_KP_PLUS:
					c = calCentro(maxmin(poligonos))
					poligonos2 = []
					for poligono in poligonos:
						poligono = escalar_pol(poligono, [1.2,1.2])
						poligonos2.append(poligono)
					poligonos = poligonos2
					poligonos = centrar(poligonos,c)
					dibujar_pol(poligonos, pantalla)
				if event.key == pygame.K_KP_MINUS:
					c = calCentro(maxmin(poligonos))
					poligonos2 = []
					for poligono in poligonos:
						poligono = escalar_pol(poligono, [0.8, 0.8])
						poligonos2.append(poligono)
					poligonos = poligonos2
					poligonos = centrar(poligonos,c)
					dibujar_pol(poligonos, pantalla)

			## Rotacion
			if event.type == pygame.MOUSEBUTTONDOWN:
				if event.button == 4:
					c = calCentro(maxmin(poligonos))
					i = 0
					for poligono in poligonos:
						poligono = rotacion_pol_ah(poligono)
						poligonos[i] = poligono
						i += 1

					poligonos = centrar(poligonos,c)
					dibujar_pol(poligonos,pantalla)
				if event.button == 5:
					c = calCentro(maxmin(poligonos))
					i = 0
					for poligono in poligonos:
						poligono = rotacion_pol_h(poligono)
						poligonos[i] = poligono
						i += 1
	
					poligonos = centrar(poligonos,c)
					dibujar_pol(poligonos,pantalla)

		pygame.display.flip()		


	pygame.quit()