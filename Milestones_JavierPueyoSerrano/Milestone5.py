
print( "" )
print( "   ==========================================================================" )
print( "   ==========================================================================" )
print( "   ==           MASTER UNIVERSITARIO EN SISTEMAS ESPACIALES                ==" )
print( "   ==                         IDR - ETSIAE - UPM                           ==" )
print( "   ==                    AMPLIACION DE MATEMATICAS 1                       ==" )
print( "   ==                        Javier Pueyo Serrano                          ==" )
print( "   ==========================================================================" )
print( "   ==========================================================================" )
print( "" )
print( "" )
print( "" )
print( "   ==========================================================================" )
print( "   ============================    MILESTONE 5    ===========================" )
print( "   ==========================================================================" )
print( "" )

from Maths_ODEs.Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Maths_ODEs.Cauchy_Problem import Cauchy_Problem
from Physics.N_Body import F_NCuerpos, Resolver_NCuerpos

Resolver_NCuerpos()