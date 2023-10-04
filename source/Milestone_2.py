
#=================================================================================
#=================================================================================
#                      MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES
#                                 IDR - ETSIAE - UPM
#						     AMPLIACIÓN DE MATEMÁTICAS 1
#                                Javier Pueyo Serrano
#=================================================================================
#=================================================================================


#=================================================================================
#								      HITO 2
#=================================================================================


from Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Cauchy_Problem import Cauchy_Problem
from Orbits import Kepler_Equation, Kepler_Force

from numpy import array, zeros, linspace
import matplotlib.pyplot as plt
import sys


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
print( "   ==============================    HITO 2    ==============================" )
print( "   ==========================================================================" )
print( "" )
print( "   Problema de Kepler: " )
print( "" )
print( "	  d2r/dt2 = - r / [module(r)]^3" )
print( "" )
print( "   con las condiciones iniciales r(t=0) y r_dot(t=0)." )
print( "" )
input()

print( "   INTERVALO DE TIEMPO" )
print( "" )
print( "   Seleccione el tiempo de integración que desea utilizar para la resolución." )
tf = float(input( "        tf = " ))
input()
print( "   Seleccione el número de pasos que desea utilizar para la resolución." )
N = int(input( "        N = " ))
print( "" )
input()
t = linspace( start = 0, stop = tf, num = N)

print( "   CONDICIÓN INICIAL" )
print( "" )
print( "   La condición inicial puede expresarse en forma vectorial como U_0 = [a, b, c, d]." )
print( "        a = x(t = 0)" )
print( "        b = y(t = 0)" )
print( "        c = dx/dt(t = 0)" )
print( "        d = dy/dt(t = 0)" )
print( "" )
print( "   Introduzca los valores. Recuerde que deben ser números reales." )
print( "" )
a = float(input( "        a = " ))
b = float(input( "        b = " ))
c = float(input( "        c = " ))
d = float(input( "        d = " ))
U_0 = array( [ a, b, c, d ] )
print( "" )
input()

print( "   ESQUEMA NUMÉRICO DE INTEGRACIÓN" )
print( "" )
print( "   Se dispone de varios esquemas numéricos de integración." )
print( "" )
print( "     - Método de Euler Explícito (multipaso explícito) = 1" )
print( "     - Método de Euler Inverso (multipaso implícito) = 2" )
print( "     - Método de Crank-Nicolson (multipaso implícito) = 3" )
print( "     - Método Runge-Kutta de 4 etapas (unipaso) = 4" )
print( "" )
t_sch = int(input( "   Introduzca la opción elegida (introduzca el número entero que le corresponda): " ))
print( "" )

if t_sch == 1:
    
    print( "   Ha elegido el método de Euler Explícito (multipaso explícito)" )
    input()
    U =  Cauchy_Problem( Kepler_Equation, t, U_0, Explicit_Euler )

elif t_sch == 2:

    print( "   Ha elegido el método de Euler inverso (multipaso implícito)" )
    input()
    U =  Cauchy_Problem( Kepler_Equation, t, U_0, Inverse_Euler )
    
elif t_sch == 3:

    print( "   Ha elegido el método de Crank-Nicolson (multipaso implícito)" )
    input()
    U =  Cauchy_Problem( Kepler_Equation, t, U_0, Crank_Nicolson )

elif t_sch == 4:

    print( "   Ha elegido el método Runge-Kutta de 4 etapas (unipaso explícito)" )
    input()
    U =  Cauchy_Problem( Kepler_Equation, t, U_0, RungeKutta_4 )

else:

    print( "   Error. El número introducido no se corresponde con ningún esquema de los disponibles." )
    input()
    sys.exit()


# === GRÁFICAS ===
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})
plt.axis("equal")
plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'solid' )
#plt.ylim( [ -1 , 1 ] )
#plt.xlim( [ -1 , 1 ] )
plt.plot( U[:,0] , U[:,1], color = 'b' )
plt.title(r'\textbf{Órbita}', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
if t_sch == 1:
    plt.legend(['Euler Explícito'])
elif t_sch == 2:
    plt.legend(['Euler Inverso'])
elif t_sch == 3:
    plt.legend(['Crank-Nicolson'])
elif t_sch == 4:
    plt.legend(['Runge-Kutta 4'])
plt.show()