import pygame
from libgrafica import *


if __name__ == '__main__':
	pygame.init()

	pantalla = pygame.display.set_mode([800,600])

	cuadricula = 50
	centro = [400,400]

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
	poligono5 = [ centro, m_rc, traslacion(m_rc,dif_bg),traslacion(centro,dif_bg)]

	## Cuadrados superiores
	poligono6 = [ g_rc, h_rc, traslacion(h_rc,dif_fg), traslacion(g_rc,dif_fg)]
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


	## Base y laterales traseros
	pygame.draw.polygon(pantalla,VERDE,poligono5)
	pygame.draw.polygon(pantalla,AZUL,poligono3)
	pygame.draw.polygon(pantalla,AMARILLO,poligono4)

	## Cruz 
	pygame.draw.polygon(pantalla,MORADO,poligono18)

	## Rectangulos internos 	
	pygame.draw.polygon(pantalla,PURPURA,poligono13)
	pygame.draw.polygon(pantalla,NARANJA,poligono17)
	pygame.draw.polygon(pantalla,PURPURA,poligono11)
	pygame.draw.polygon(pantalla,NARANJA,poligono16)
	pygame.draw.polygon(pantalla,NARANJA,poligono15)
	pygame.draw.polygon(pantalla,PURPURA,poligono12)
	pygame.draw.polygon(pantalla,NARANJA,poligono14)
	pygame.draw.polygon(pantalla,PURPURA,poligono10)

	## Laterales delanteros
	pygame.draw.polygon(pantalla,BLANCO,poligono1)
	pygame.draw.polygon(pantalla,ROJO,poligono2)

	## Cuadrados superiores
	pygame.draw.polygon(pantalla,VERDE,poligono6)
	pygame.draw.polygon(pantalla,VERDE,poligono7)
	pygame.draw.polygon(pantalla,VERDE,poligono8)
	pygame.draw.polygon(pantalla,VERDE,poligono9)
	

	fin = False
	while not fin:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				fin = True

		pygame.display.flip()		


	pygame.quit()