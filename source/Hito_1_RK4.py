
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
# MÉTODO RUNGE-KUTTA DE 4 ETAPAS
#
# Dado un Problema de Valor Inicial (problema de Cauchy)
#
#		dU(t)/dt = F(t,U(t))
#		U(t_0) = U_0
#
# El método Runge-Kutta de 4 etapas (en adelante, RK4), para este problema viene dado por la siguiente ecuación:
#
#		U(n+1) = U(n) + (1/6) * delta_t * [ k1 + 2*k2 + 2*k3 + k4 ],
#
# siendo:
#
#		k1 = F( t_n , U(t_n) )
#		k2 = F( t_n + 1/2 * delta_t , U(t_n) + 1/2 * k1 * delta_t )
#		k3 = F( t_n + 1/2 * delta_t , U(t_n) + 1/2 * k2 * delta_t )
#		k4 = F( t_n + delta_t , U(t_n) + k3 * delta_t )
#


def Hito_1_RK4():

	U = array( [ 1, 0, 1, 0])

	N = int(input("   Introduzca N = "))
	dt = float(input("   Introduzca delta_t = "))

	x = array( zeros(N) )
	y = array( zeros(N) )
	t = array( zeros(N) )

	x[0] = U[0]
	y[0] = U[1]
	t[0] = 0

	for i in range(1,N):

		t[i] = dt * i
		U = RungeKutta_4(U, t, dt, Ec_Kepler)
		x[i] = U[0]
		y[i] = U[1]

	for j in range(1, N):
		
		print(t[j-1], x[j-1], y[j-1])

	plt.figure( figsize=(6, 6) , dpi=80 , num=4)
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


def RungeKutta_4(U, t, dt, F):
	
	k1 = F( U , t)
	k2 = F( U + dt * k1/2 , t + dt/2 )
	k3 = F( U + dt * k2/2 , t + dt/2 )
	k4 = F( U + dt * k3 ,   t + dt   )

	return  U + dt * ( k1 + 2*k2 + 2*k3 + k4 )/6
#
#