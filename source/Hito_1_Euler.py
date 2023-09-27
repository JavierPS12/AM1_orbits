
#=================================================================================
#								      HITO 1
#=================================================================================


from numpy import array, zeros
import matplotlib.pyplot as plt


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})


#=================================================================================
# MÉTODO DE EULER
#
# Dado un Problema de Valor Inicial (problema de Cauchy)
#
#		dU(t)/dt = F(t,U(t))
#		U(t_0) = U_0
#
# El método de Euler (explícito) viene dado por:
#
#		U(n+1) = U(n) + delta_t * F( t_n , U(n) )
#

def Hito_1_v1():

	print( "   Método de Euler" )
	print("")
	input()

	U = array( [ 1, 0, 0, 1])

	N = 1000

	x = array( zeros(N) )
	y = array( zeros(N) )

	x[0] = U[0]
	y[0] = U[1]
	# Si se pone U = [1, 0, 0, 1], es una lista, y las operaciones vectoriales no se pueden ejecutar
	
	dt = 0.01

	for i in range(1, N):

		F = array( [ U[2], U[3], -U[0] / (U[0]**2+U[1]**2)**1.5, -U[1] / (U[0]**2+U[1]**2)**1.5 ] )
		U = U + dt * F
		x[i] = U[0]
		y[i] = U[1]

	for j in range(1, N):
		
		print(x[j-1], y[j-1])

	plt.figure( figsize=(6, 6) , dpi=80 , num=1)
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
	

def Hito_1_v2():

	U = array( [ 1, 0, 0, 1])

	N = 10000

	x = array( zeros(N) )
	y = array( zeros(N) )
	t = array( zeros(N) )

	x[0] = U[0]
	y[0] = U[1]
	#t[0] = 0
	
	dt = 0.001

	for i in range(1, N):

		#t[i] = dt * i
		F = Ec_Kepler(U,t)
		U = U + dt * F
		x[i] = U[0]
		y[i] = U[1]

	plt.figure( figsize=(6, 6) , dpi=80 , num=2)
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


def Hito_1_ExpEuler():

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


def Ec_Kepler(U, t):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.
	dx_dt = U[2]		# La velocidad según x es la tercera componente del vector de estado.
	dy_dt = U[3]		# La velocidad según y es la cuarta componente del vector de estado.

	mod_r = ( x**2 + y**2 )**0.5

	return array( [ dx_dt , dy_dt , -x/mod_r**3 , -y/mod_r**3 ] )


def Euler_Exp(U, t, dt, F):

	return U + dt * F(U, t)
	# U(n+1) = U(n) + delta_t * F( t_n , U(n) )
