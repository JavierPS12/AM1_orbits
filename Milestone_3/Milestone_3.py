
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

from Temporal_Error import Error_Cauchy_Problem, Temporal_Convergence_Rate
from Orbits import Kepler_Equation
from Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Cauchy_Problem import Cauchy_Problem
from numpy import linspace, array
import matplotlib.pyplot as plt

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
print( "   ===========================    MILESTONE 3    ============================" )
print( "   ==========================================================================" )
print( "" )



# FUNCION PARA PROBAR LA FUNCION Test_Error_Cauchy_Problem
def Test_Error_Cauchy_Problem():

	N = 10000
	t = linspace(0, 10, N) 
	U_0 = array( [1, 0, 0, 1 ] )

	orden = 1 
	print("Error en la Orbita de Kepler ") 
	Error, U = Error_Cauchy_Problem( t, Kepler_Equation,  Explicit_Euler, orden, U_0 )

	plt.plot(t, Error[:,0], color = 'b' )
	plt.xlabel('$t$')
	plt.ylabel('Error')
	plt.axis('equal')
	plt.grid()
	plt.show()




# FUNCION PARA PROBAR LA FUNCION Test_Temporal_Convergence_Rate
def Test_Temporal_Convergence_Rate():
	
	N = 5000
	t = linspace(0, 10, N) 
	U_0 = array( [1, 0, 0, 1 ] )

	m = 5

	print("Orden del Esquema Euler Inverso") 
	# La pendiente es el orden del esquema
	orden, log_e, log_n = Temporal_Convergence_Rate( t, Kepler_Equation, U_0, Inverse_Euler, m )

	print( "order =", orden)
	plt.plot(log_n, log_e, color = 'b' )
	plt.xlabel('$log(N)$')
	plt.ylabel('$log(E)$')
	plt.axis('equal')
	plt.grid()
	plt.show()





Test_Error_Cauchy_Problem()
Test_Temporal_Convergence_Rate()