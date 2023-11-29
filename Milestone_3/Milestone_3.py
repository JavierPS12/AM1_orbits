
#=================================================================================
#=================================================================================
#                      MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES
#                                 IDR - ETSIAE - UPM
#						     AMPLIACIÓN DE MATEMÁTICAS 1
#                                Javier Pueyo Serrano
#=================================================================================
#=================================================================================


#=================================================================================
#								    MILESTONE 3
#=================================================================================

from Temporal_Error import Test_Error_Cauchy_Problem, Error_Cauchy_Problem, Temporal_convergence_rate, Test_Temporal_convergence_rate
from Orbits import Kepler_Equation
from Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Cauchy_Problem import Cauchy_Problem
import matplotlib.pyplot as plt

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
print( "   ===========================    MILESTONE 3    ============================" )
print( "   ==========================================================================" )
print( "" )

N = 5000
t = linspace(0, 10, N) 
U_0 = array( [1, 0, 0, 1 ] )


#Test_Error_Cauchy_Problem()
order = 1 
print("Error en la Órbita de Kepler ") 
Error, U = Error_Cauchy_Problem( t, Kepler_Equation,  Explicit_Euler, order, U_0 )

plt.plot(t, Error[:,0] )
plt.axis('equal')
plt.grid()
plt.show()


#Test_Temporal_convergence_rate()
m = 5

print("Order Euler") 
order, log_e, log_n = Temporal_convergence_rate( t, Kepler_Equation, U_0, Explicit_Euler, m )

print( "order =", order)
plt.plot(log_n, log_e )
plt.axis('equal')
plt.grid()
plt.show()