
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

def Ec_Kepler(U, t):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.
	dx_dt = U[2]		# La velocidad según x es la tercera componente del vector de estado.
	dy_dt = U[3]		# La velocidad según y es la cuarta componente del vector de estado.

	mod_r = ( x**2 + y**2 )**0.5

	return array( [ dx_dt , dy_dt , -x/mod_r**3 , -y/mod_r**3 ] )

if eleccion == 1:

	print("   Ha seleccionado el Método de Euler.")
	input()
	U = array( [ 1, 0, 0, 1])

	N = int(input("   Introduzca N = "))
	dt = float(input("   Introduzca delta_t = "))

	x = array( zeros(N) )
	y = array( zeros(N) )
	t = array( zeros(N) )

	x[0] = U[0]
	y[0] = U[1]
	t[0] = 0

	for i in range(1, N):

		t[i] = dt * i
		U = Euler_Exp(U, t, dt, Ec_Kepler)
		x[i] = U[0]
		y[i] = U[1]

	plt.figure( figsize=(6, 6) , dpi=80 , num=3)
	plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'solid' )
	plt.ylim( [ -1.15 , 1.15  ])
	plt.xlim( [ -1.15 , 1.15 ] )
	plt.plot( x , y , color = 'b')
	plt.title(r'\textbf{Órbita}', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
	plt.ylabel("$y$ (m)", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
	plt.xlabel("$x$ (m)", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
	#plt.yticks(range(20, 35))
	#plt.savefig('Orbit.svg')
	plt.show()

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
