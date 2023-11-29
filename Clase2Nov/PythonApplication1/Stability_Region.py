from numpy import zeros, array, linspace, float64, abs, transpose
import matplotlib.pyplot as plt
from Temporal_Schemes import Explicit_Euler, Inverse_Euler, RungeKutta_4, Crank_Nicolson

def Stability_Region(Scheme, N, x0, xf, y0, yf):

	x, y = linspace(x0,xf,N), linspace(y0,yf,N)
	rho = zeros((N,N), dtype =float64)

	for i in range(N):
		for j in range(N):

			w = complex(x[i],y[j])
			r = Scheme(1.,0.,1.,lambda u, t: w*u)# La parte de la lambda es una función anónima.
			rho[i,j]=abs(r)
	return rho, x, y

def test():
	schemes = [RungeKutta_4,Inverse_Euler]

	for scheme in schemes:
		rho, x, y = Stability_Region(scheme, 100, -4, 4, -4, 4)
		plt.contour(x,y,transpose(rho),linspace(0,1,11)) # El linspace pinta las curvas de nivel
		plt.axis('equal')
		plt.grid()
		plt.show()

#if __name__ = "__main__"
test()
