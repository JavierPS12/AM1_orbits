
#=================================================================================
#=================================================================================
#                      MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES
#                                 IDR - ETSIAE - UPM
#						     AMPLIACIÓN DE MATEMÁTICAS 1
#                                Javier Pueyo Serrano
#=================================================================================
#=================================================================================


#=================================================================================
#								    MILESTONE 5
#=================================================================================


#from Orbits import Kepler_Equation
from Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Cauchy_Problem import Cauchy_Problem
import matplotlib.pyplot as plt
#from Stability_Region import Stability_Region
from numpy import array, zeros, linspace, abs, transpose, float64
from N_Body import F_NBody, Integrate_NBP, Initial_positions_and_velocities


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
print( "   ===========================    MILESTONE 5    ============================" )
print( "   ==========================================================================" )
print( "" )

Integrate_NBP()
