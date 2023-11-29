
#=================================================================================
#								      HITO 3
#								 TEMPORAL SCHEMES
#=================================================================================


from numpy import array, zeros, linspace
from scipy.optimize import newton


#=================================================================================
# MÉTODO DE EULER (EXPLÍCITO)
#
# El método de Euler (explícito) viene dado por:
#
#		U(n+1) = U(n) + delta_t * F( t_n , U(n) )

def Explicit_Euler( U, t, dt, F ):

	return U + dt * F( U, t )



#=================================================================================
# MÉTODO DE EULER INVERSO (IMPLÍCITO)
#
# El método de Euler inverso (implícito) viene dado por:
#
#		U(n+1) = U(n) + delta_t * F( t_n , U(n+1) )

def Inverse_Euler( U, t, dt, F ):

    def G(X): 

          return X - U - dt * F( X, t )

    return newton( func = G, x0 = U ) 



#=================================================================================
# MÉTODO CRANK-NICOLSON (IMPLÍCITO)
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

def Crank_Nicolson( U, t, dt, F ):

    def G(X): # G = U(n+1)
         
         return  X - U - dt/2 * F( U, t ) - dt/2 * F( X, t + dt )

    return newton( func = G, x0 = U )



#=================================================================================
# MÉTODO RUNGE-KUTTA DE 4 ETAPAS (EXPLÍCITO)
#
# El método Runge-Kutta de 4 etapas (RK4), para este problema viene dado por la siguiente ecuación:
#
#		U(n+1) = U(n) + (1/6) * delta_t * [ k1 + 2*k2 + 2*k3 + k4 ],
#
# siendo:
#
#		k1 = F( t_n , U(t_n) )
#		k2 = F( t_n + 1/2 * delta_t , U(t_n) + 1/2 * k1 * delta_t )
#		k3 = F( t_n + 1/2 * delta_t , U(t_n) + 1/2 * k2 * delta_t )
#		k4 = F( t_n + delta_t , U(t_n) + k3 * delta_t )

def RungeKutta_4( U, t, dt, F ):
	
	k1 = F( U, t )
	k2 = F( U + dt * k1/2, t + dt/2 )
	k3 = F( U + dt * k2/2, t + dt/2 )
	k4 = F( U + dt * k3,   t + dt   )

	return  U + dt * ( k1 + 2*k2 + 2*k3 + k4 ) / 6
