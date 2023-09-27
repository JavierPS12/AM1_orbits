
#=================================================================================
#=================================================================================
#                      MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES
#                                 IDR - ETSIAE - UPM
#						     AMPLIACIÓN DE MATEMÁTICAS 1
#                                Javier Pueyo Serrano
#=================================================================================
#=================================================================================



#=================================================================================
#								      HITO 1
#=================================================================================



#=================================================================================
# PROBLEMA DE KEPLER
#
# En Mecánica Clásica, el Problema de Kepler es un caso especial del Problema de los Dos Cuerpos, en el que los dos cuerpos 
# interactúan por medio de una fuerza central que varía en intensidad según una ley cuadrática inversamente proporcional en 
# función de la distancia entre ambos.
#
#		d2r / dt2 = - r / |r|^3 
#		r (t = 0)
#		dr / dt (t = 0)
#
# Nótese que r es un vector de dos componentes, x e y. Al ser la ecuación de segundo orden (por tener una derivada segunda),
# en primer lugar es necesario reducir el problema a un sistema de primer orden.
#		
#		r = ( x , y )
#		|r| = ( x^2 + y^2 )^(1/2)		
#		dr/dt = ( vx , vy )
#		U = ( r , dr/dt )
#		dU/dt = ( dr/dt , d2r/dt2 ) = ( dr/dt , -r/|r|^3 ) = F ( t , U(t) )
# 
# Se puede ver que en este caso no hay una dependencia explícita con el tiempo. Al vector U se le denomina vector de estado.
#


#from numpy import array 


print( "" )
print( "   ==========================================================================" )
print( "   ==========================================================================" )
print( "   ==           MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES                ==" )
print( "   ==                         IDR - ETSIAE - UPM                           ==" )
print( "   ==                    AMPLIACIÓN DE MATEMÁTICAS 1                       ==" )
print( "   ==                        Javier Pueyo Serrano                          ==" )
print( "   ==========================================================================" )
print( "   ==========================================================================" )
print( "" )
print( "" )
print( "" )
print( "   ==========================================================================" )
print( "   ==============================    HITO 1    ==============================" )
print( "   ==========================================================================" )
print( "" )
print( "   Problema de Kepler: ")
print( "" )
print( "	  d2r/dt2 = - r / [module(r)]^3")
print( "" )
print( "   con las condiciones iniciales r(t=0) y r_dot(t=0).")
print( "" )
input()
print( "   Seleccione el esquema numérico que desea utilizar para la resolución:")
print( "" )
print( "     1. Método de Euler (multipaso explícito)")
print( "     2. Método de Crank-Nicolson (multipaso implícito)")
print( "     3. Método Runge-Kutta de 4 etapas (unipaso)")
print( "" )
eleccion = int(input("   Introduzca la opción elegida: "))
print( "" )

if eleccion == 1:

	print("   Ha seleccionado el Método de Euler.")
	input()
	import Hito_1_Euler
	Hito_1_Euler.Hito_1_ExpEuler()

elif eleccion == 2:
	
	print("   Ha seleccionado el Método de Crank-Nicolson.")
	input()
	import Hito_1_CraNic
	Hito_1_CraNic.Hito_1_CN()

elif eleccion == 3:
	
	print("   Ha seleccionado el Método Runge-Kutta de 4 etapas.")
	input()
	import Hito_1_RK4
	Hito_1_RK4.Hito_1_RK4()

else:

	exit