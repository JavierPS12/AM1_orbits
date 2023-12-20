
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
print( "   ============================    MILESTONE 2    ===========================" )
print( "   ==========================================================================" )
print( "" )


from Maths_ODEs.Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Maths_ODEs.Cauchy_Problem import Cauchy_Problem
from Physics.Kepler_Equation import Kepler_Equation

from numpy import array, zeros, linspace
import matplotlib.pyplot as plt


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
print( "   Seleccione el tiempo de integracion que desea utilizar para la resolucion." )
tf = float(input( "        tf = " ))
input()
print( "   Seleccione el numero de pasos que desea utilizar para la resolucion." )
N = int(input( "        N = " ))
print( "" )
input()
t = linspace( start = 0, stop = tf, num = N)

print( "   CONDICION INICIAL" )
print( "" )
print( "   La condicion inicial puede expresarse en forma vectorial como U_0 = [a, b, c, d]." )
print( "        a = x(t = 0)" )
print( "        b = y(t = 0)" )
print( "        c = dx/dt(t = 0)" )
print( "        d = dy/dt(t = 0)" )
print( "" )
print( "   Introduzca los valores. Recuerde que deben ser numeros reales." )
print( "" )
a = float(input( "        a = " ))
b = float(input( "        b = " ))
c = float(input( "        c = " ))
d = float(input( "        d = " ))
U_0 = array( [ a, b, c, d ] )
print( "" )
input()

print( "   ESQUEMA NUMERICO DE INTEGRACION" )
print( "" )
print( "   Se dispone de varios esquemas numericos de integracion." )
print( "" )
print( "     - Metodo de Euler Explicito (multipaso explicito) = 1" )
print( "     - Metodo de Euler Inverso (multipaso implicito) = 2" )
print( "     - Metodo de Crank-Nicolson (multipaso implicito) = 3" )
print( "     - Metodo Runge-Kutta de 4 etapas (unipaso) = 4" )
print( "" )
t_sch = int(input( "   Introduzca la opcion elegida (introduzca el numero entero que le corresponda): " ))
print( "" )

if t_sch == 1:
    
    print( "   Ha elegido el metodo de Euler Explicito (multipaso explicito)" )
    input()
    U =  Cauchy_Problem( Kepler_Equation, t, U_0, Explicit_Euler )

elif t_sch == 2:

    print( "   Ha elegido el metodo de Euler inverso (multipaso implicito)" )
    input()
    U =  Cauchy_Problem( Kepler_Equation, t, U_0, Inverse_Euler )
    
elif t_sch == 3:

    print( "   Ha elegido el metodo de Crank-Nicolson (multipaso implicito)" )
    input()
    U =  Cauchy_Problem( Kepler_Equation, t, U_0, Crank_Nicolson )

elif t_sch == 4:

    print( "   Ha elegido el metodo Runge-Kutta de 4 etapas (unipaso explicito)" )
    input()
    U =  Cauchy_Problem( Kepler_Equation, t, U_0, RungeKutta_4 )

else:

    print( "   Error. El numero introducido no se corresponde con ningun esquema de los disponibles." )
    input()
    sys.exit()


# === GRAFICAS ===
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman"],
})
plt.axis("equal")
plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
#plt.ylim( [ -1 , 1 ] )
#plt.xlim( [ -1 , 1 ] )
plt.plot( U[:,0] , U[:,1], color = 'b')
plt.title(r'\textbf{Orbita}', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
if t_sch == 1:
    plt.legend(['Euler Explicito'])
elif t_sch == 2:
    plt.legend(['Euler Inverso'])
elif t_sch == 3:
    plt.legend(['Crank-Nicolson'])
elif t_sch == 4:
    plt.legend(['Runge-Kutta 4'])
plt.show()
