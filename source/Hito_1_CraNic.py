
#=================================================================================
#								      HITO 1
#=================================================================================


from numpy import array, zeros
from scipy.optimize import newton, fsolve
import matplotlib.pyplot as plt


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})


#=================================================================================
# MÉTODO CRANK-NICOLSON
#
# Dado un Problema de Valor Inicial (problema de Cauchy)
#
#		dU(t)/dt = F(t,U(t))
#		U(t_0) = U_0
#
# El método de Crank-Nicolson:
#
#       U(n+1) = U(n) + (1/2) * delta_t * [ F(n+1) + F(n) ],
#
# Será necesario resolver un sistema de ecuaciones en cada paso, al depender U(n+1) de F(n+1)
#
#		U(n+1) - U(n) - (1/2) * delta_t * F(n+1) - (1/2) * delta_t * F(n) = 0
#
# Al no ser lineal el sistema de ecuaciones, se va a emplear el método de Newton-Rhapson


def Hito_1_CN():

	U = array( [ 1, 0, 0, 1])

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
		U = Crank_Nicolson( U, t, dt, Ec_Kepler )
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


def Crank_Nicolson( U, t, dt, F ): 

    def eqsystem_CN(Un_1): # Un_1 = U(n+1)
         
         return  Un_1 - U - dt/2 * F( U, t) - dt/2 * F(Un_1, t + dt)

    return fsolve( eqsystem_CN, U )