
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

from numpy import array, zeros, linspace
import matplotlib.pyplot as plt
from scipy.optimize import newton

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})

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
print( "   ============================    MILESTONE 1    ===========================" )
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

U0 = array( [ 1, 0, 0, 1 ] )
N = int(input("   Introduzca N = "))
dt = float(input("   Introduzca delta_t = "))
U = array( zeros ( [ N , len(U0) ] ) ) 
U[0,:] = U0

x = array( zeros(N) )
y = array( zeros(N) )
t = array( zeros(N) )

x[0] = U[0,0]
y[0] = U[0,1]
t[0] = 0

def Ec_Kepler( U, t ):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.
	dx_dt = U[2]		# La velocidad según x es la tercera componente del vector de estado.
	dy_dt = U[3]		# La velocidad según y es la cuarta componente del vector de estado.

	mod_r = ( x**2 + y**2 )**0.5

	return array( [ dx_dt , dy_dt , -x/mod_r**3 , -y/mod_r**3 ] )


if eleccion == 1:

	print("   Ha seleccionado el Método de Euler (explícito).")
	input()

	for i in range(1, N):

		t[i] = dt * i
		F = Ec_Kepler( U = U[i-1,:] , t = t[i-1])
		U[i,:] = U[i-1,:] + dt * F
		x[i] = U[i,0]
		y[i] = U[i,1]

	plt.figure( figsize=(6, 6) , dpi=80 , num=2)
	plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'solid' )
	plt.ylim( [ -1.15 , 1.15  ])
	plt.xlim( [ -1.15 , 1.15 ] )
	plt.plot( x , y , color = 'b')
	plt.title(r'\textbf{Órbita} (Método de Euler)', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
	plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
	plt.xlabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
	plt.show()
	
	
elif eleccion == 2:
	
	print("   Ha seleccionado el Método Crank-Nicolson.")
	input()

	def G(X):
		return X - a - dt/2 * ( F(a,t[i-1]) + F(X,t[i]) )

	for i in range(1,N):

		t[i] = dt * i
		F = Ec_Kepler
		a = U[i-1,:]
		U[i,:] = newton( func = G , x0 = U[i-1,:] )
		x[i] = U[i,0]
		y[i] = U[i,1]

	plt.figure( figsize=(6, 6) , dpi=80 , num=2)
	plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'solid' )
	plt.ylim( [ -1.15 , 1.15  ])
	plt.xlim( [ -1.15 , 1.15 ] )
	plt.plot( x , y , color = 'b')
	plt.title(r'\textbf{Órbita} (Método Crank-Nicolson)', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
	plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
	plt.xlabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
	plt.show()


elif eleccion == 3:
	
	print("   Ha seleccionado el Método Runge-Kutta de 4 etapas.")
	input()

	for i in range(1, N):

		t[i] = dt * i
		F = Ec_Kepler

		k1 = F( U[i-1,:] , t[i-1])
		k2 = F( U[i-1,:] + dt * k1/2 , t[i-1] + dt/2 )
		k3 = F( U[i-1,:] + dt * k2/2 , t[i-1] + dt/2 )
		k4 = F( U[i-1,:] + dt * k3 ,   t[i-1] + dt   )
		U[i,:] = U[i-1,:] + dt * ( k1 + 2*k2 + 2*k3 + k4 ) / 6

		x[i] = U[i,0]
		y[i] = U[i,1]

	plt.figure( figsize=(6, 6) , dpi=80 , num=2)
	plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'solid' )
	plt.ylim( [ -1.15 , 1.15  ])
	plt.xlim( [ -1.15 , 1.15 ] )
	plt.plot( x , y , color = 'b')
	plt.title(r'\textbf{Órbita} (Método Runge-Kutta 4)', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
	plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
	plt.xlabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
	plt.show()


else:

	exit
