
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
print( "   ============================    MILESTONE 6    ===========================" )
print( "   ==========================================================================" )
print( "" )

from Maths_ODEs.Cauchy_Problem import Cauchy_Problem
from Maths_ODEs.Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4, RungeKutta_Embedded
from Maths_ODEs.Stability_Region import Region_Estabilidad
from Maths_ODEs.Temporal_Error import Error_Cauchy_Problem, Temporal_Convergence_Rate

from Physics.Kepler_Equation import Kepler_Equation
from Physics.N_Body import F_NCuerpos, Resolver_NCuerpos
from Physics.CR3BP import CR3BP, Puntos_Lagrange, Estabilidad_Lagrange

from Plotting.Graphics import Plot_2D

from scipy.integrate import solve_ivp
from scipy.optimize import newton
import matplotlib.pyplot as plt
import matplotlib.path as mpath
from numpy import array, concatenate, hstack, linspace, cos, sin, pi, abs, sqrt, zeros, random

# MASAS DE LOS PLANETAS (Sistema Tierra-Luna)
m1 = 5.974E24       # kg
m2 = 7.348E22       # kg
REL = m2 / (m1 + m2)

# DOMINIO TEMPORAL
t_0 = 0
t_f = 100
N = 10000
t = linspace(t_0, t_f, N)

# NUMERO DE PUNTOS DE LAGRANGE
Np = 5

# CONDICIONES INICIALES PARA QUE RESUELVA NEWTON
U_0 = zeros([Np,4])

U_0[0, :] = [0.1, 0, 0, 0]
U_0[1, :] = [0.8, 0.6, 0, 0]
U_0[2, :] = [-0.1, 0, 0, 0]
U_0[3, :] = [0.8, -0.6, 0, 0]
U_0[4, :] = [1.01, 0, 0, 0]

# OBTENER LOS PUNTOS DE LAGRANGE
LagrangeP = Puntos_Lagrange(U_0, Np, REL)

# SACAR POR PANTALLA LOS PUNTOS DE LAGRANGE CALCULADOS
print("Puntos de Lagrange:")

for i, Punto in enumerate(LagrangeP, start = 1):

    print(f"LP{i} =", Punto)

# ELECCION DE UN PUNTO DE LAGRANGE
Punto_a_estudiar = float(input("Introduzca el numero del punto de Lagrange del que quiere estudiar su estabilidad: "))

try:
    Int_Punto = int(Punto_a_estudiar)
    # Comprobacion
    if 1 <= Int_Punto <= Np:
        Punto_Elegido = LagrangeP[Int_Punto - 1]
        print(f"Ha elegido el punto {Int_Punto}: {Punto_Elegido}")
    else:
        print("Invalido. Introduzca un numero valido.")
except ValueError:
    print("Invalido. Introduzca un numero valido.")

# CONDICIONES INICIALES PARA LA ÓRBITA ALREDEDOR DEL PUNTO DE LAGRANGE
U0 = zeros(4)
U0[0:2] = LagrangeP[Int_Punto - 1,:]
eps = 1e-4*random.random()             
U0 = U0 + eps

def F(U,t):
   return CR3BP(U, REL)

U = Cauchy_Problem(F, t, U0, RungeKutta_4)

# ESTABILIDAD DEL PUNTO DE LAGRANGE
U0_Stability = zeros(4)
U0_Stability[0:2] = LagrangeP[Int_Punto - 1, :]
Autovalores = Estabilidad_Lagrange(U0_Stability, REL)

# GRAFICOS
Nombres_PuntosLagrange = ['L1', 'L2', 'L3', 'L4', 'L5']

Plot_2D(U[:, 0], U[:, 1],'','')

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(U[:, 0], U[:, 1], '-', color="r")
ax1.plot(-REL, 0, 'o', color="g")
ax1.plot(1 - REL, 0, 'o', color="b")
for i in range(Np):
    ax1.plot(LagrangeP[i, 0], LagrangeP[i, 1], 'o', color="k")

ax2.plot(U[:, 0], U[:, 1], '-', color="r")

ax2.plot(LagrangeP[Int_Punto - 1, 0], LagrangeP[Int_Punto - 1, 1], 'o', color="k")
fig.suptitle(f"Orbita alrededor de {Nombres_PuntosLagrange}")



plt.show()