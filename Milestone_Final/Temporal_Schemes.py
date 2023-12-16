
#=================================================================================
#								 TEMPORAL SCHEMES
#=================================================================================


from numpy import array, zeros, linspace
from scipy.optimize import newton


#=================================================================================
# MÉTODO DE EULER (EXPLÍCITO)

def Explicit_Euler( U, t, dt, F ):

	return U + dt * F( U, t )


#=================================================================================
# MÉTODO DE EULER INVERSO (IMPLÍCITO)

def Inverse_Euler( U, t, dt, F ):

    def G(X): 

          return X - U - dt * F( X, t )

    return newton( func = G, x0 = U ) 


#=================================================================================
# MÉTODO CRANK-NICOLSON (IMPLÍCITO)

def Crank_Nicolson( U, t, dt, F ):

    def G(X): # G = U(n+1)
         
         return  X - U - dt/2 * F( U, t ) - dt/2 * F( X, t + dt )

    return newton( func = G, x0 = U )


#=================================================================================
# MÉTODO RUNGE-KUTTA DE 4 ETAPAS (EXPLÍCITO)

def RungeKutta_4( U, t, dt, F ):
	
	k1 = F( U, t )
	k2 = F( U + dt * k1/2, t + dt/2 )
	k3 = F( U + dt * k2/2, t + dt/2 )
	k4 = F( U + dt * k3,   t + dt   )

	return  U + dt * ( k1 + 2*k2 + 2*k3 + k4 ) / 6