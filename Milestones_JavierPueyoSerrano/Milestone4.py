
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
print( "   ============================    MILESTONE 4    ===========================" )
print( "   ==========================================================================" )
print( "" )

from Maths_ODEs.Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Maths_ODEs.Cauchy_Problem import Cauchy_Problem
from Maths_ODEs.Stability_Region import Region_Estabilidad
from Physics.Kepler_Equation import Kepler_Equation

from numpy import array, zeros, linspace, abs, transpose, float64
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})

# EJECUTAR PARA VER LAS REGIONES DE ESTABILIDAD (TODAS JUNTAS)


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

plt.suptitle(r'\textbf{Region de Estabilidad}', fontsize=16)
plt.tight_layout()
plt.show()