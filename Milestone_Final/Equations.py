
#=================================================================================
#								 MATH EQUATIONS
#=================================================================================


from numpy import array, cos, sin, arange, sqrt
from numpy.random import randn


def VanDerPol_Libre( U, t ):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.

	return array( [y , 0.1*(x**2-1)*y - 1*x  ] )


def VanDerPol_ForzadoArmonico( U, t ):

	x = U[0]			# La coordenada x es la primera componente del vector de estado.
	y = U[1]			# La coordenada y es la segunda componente del vector de estado.

	return array( [y , -0.01 * (x**2-1) * y - 1 * x + 2*cos(t)  ] )


def VanDerPol_ForzadoEstocastico( U, t ):
    mu = -1
    w0 = 1
    tau = 0.1
    D = 1000000
    h = 0.01
    return array([U[1], -mu*(U[0]**2 - 1)*U[1] - (w0)*U[0] - U[2], -U[2]/tau + sqrt(D)*sqrt(h)*randn()])


def Nicolis_Prigogine_w_OrnsteinUhlenbeck(U,t):
    a = 1
    b = 2
    tau = 0.1
    D = 50
    dt = 0.01
    return array([a-(1+b)*U[0]+U[1]*U[0]**2, (b + U[2])*U[0]-U[1]*U[0]**2, -U[2]/tau + sqrt(D)*sqrt(1/dt)*randn()])