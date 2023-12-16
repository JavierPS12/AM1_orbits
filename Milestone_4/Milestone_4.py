
#=================================================================================
#=================================================================================
#                      MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES
#                                 IDR - ETSIAE - UPM
#						     AMPLIACIÓN DE MATEMÁTICAS 1
#                                Javier Pueyo Serrano
#=================================================================================
#=================================================================================


#=================================================================================
#								    MILESTONE 4
#=================================================================================


from Orbits import Kepler_Equation
from Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Cauchy_Problem import Cauchy_Problem
import matplotlib.pyplot as plt
from Stability_Region import Region_Estabilidad
from numpy import array, zeros, linspace, abs, transpose, float64


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
print( "   ===========================    MILESTONE 4    ============================" )
print( "   ==========================================================================" )
print( "" )


plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})

# EJECUTAR PARA VER LAS REGIONES DE ESTABILIDAD TODAS JUNTAS


plt.figure(figsize=(7.5, 7.5))
rho, x, y  = Region_Estabilidad(Explicit_Euler, 1000, -4, 4, -4, 4)
plt.subplot(2, 2, 1)
plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'dashed' )
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
plt.title(r'Euler', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
plt.ylabel("$Im(\omega)$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlabel("$Re(\omega)$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlim(-3,1)
plt.ylim(-2,2)

plt.subplot(2, 2, 2)
rho, x, y  = Region_Estabilidad(Inverse_Euler, 100, -4, 4, -4, 4)
plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'dashed' )
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
plt.title(r'Euler Inverso', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
plt.ylabel("$Im(\omega)$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlabel("$Re(\omega)$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlim(-1,3)
plt.ylim(-2,2)

plt.subplot(2, 2, 3)
rho, x, y  = Region_Estabilidad(RungeKutta_4, 100, -4, 4, -4, 4)
plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'dashed' )
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
plt.title(r'Runge-Kutta 4', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
plt.ylabel("$Im(\omega)$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlabel("$Re(\omega)$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlim(-4,2)
plt.ylim(-4,4)

plt.subplot(2, 2, 4)
rho, x, y  = Region_Estabilidad(Crank_Nicolson, 100, -4, 2, -4, 4)
plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'dashed' )
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
plt.title(r'Crank-Nicolson', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
plt.ylabel("$Im(\omega)$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlabel("$Re(\omega)$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlim(-3,1)
plt.ylim(-2,2)

plt.suptitle(r'\textbf{Región de Estabilidad}', fontsize=16)
plt.tight_layout()
plt.show()