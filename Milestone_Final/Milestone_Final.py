
#=================================================================================
#=================================================================================
#                      MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES
#                                 IDR - ETSIAE - UPM
#						     AMPLIACIÓN DE MATEMÁTICAS 1
#                                Javier Pueyo Serrano
#=================================================================================
#=================================================================================


#=================================================================================
#								FINAL MILESTONE
#=================================================================================


from Temporal_Schemes import Explicit_Euler, Inverse_Euler, Crank_Nicolson, RungeKutta_4
from Cauchy_Problem import Cauchy_Problem
from Equations import VanDerPol_Libre, VanDerPol_ForzadoArmonico, VanDerPol_ForzadoEstocastico, Nicolis_Prigogine_w_OrnsteinUhlenbeck
import matplotlib.pyplot as plt
from numpy import array, zeros, linspace, abs, transpose, float64, histogram2d, meshgrid, ones_like, max, min
from mpl_toolkits.mplot3d import Axes3D
#from colorspacious import cspace_converter
#import matplotlib as mpl
import matplotlib.animation as animation

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
print( "   =========================    FINAL MILESTONE    ==========================" )
print( "   ==========================================================================" )
print( "" )


#print( "   INTERVALO DE TIEMPO" )
#print( "" )
#print( "   Seleccione el tiempo de integración que desea utilizar para la resolución." )
tf = 100
#float(input( "        tf = " ))
#input()
#print( "   Seleccione el número de pasos que desea utilizar para la resolución." )
N = 10000
#int(input( "        N = " ))
print( "" )
#input()
t = linspace( start = 0, stop = tf, num = N)

U_0 = array([0.01,0])
#print(U_0)
U =  Cauchy_Problem( VanDerPol_Libre, t, U_0, Explicit_Euler )
#plt.figure()
#plt.axis("equal")
#plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
#plt.plot( U[90000:100000,0] , U[90000:100000,1], color = 'b')
#plt.title(r'\textbf{Órbita}', loc = "center", fontdict = {'fontsize':14, 'color':'k'})
#plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.xlabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.xlim([-1.5, 1.5])
#plt.ylim([-1.5, 1.5])

#plt.legend(['Runge-Kutta 4'])


#U_01 = array([2,-2])
#U1 =  Cauchy_Problem( LordRayleigh, t, U_01, RungeKutta_4 )
#plt.plot( U1[90000:100000,0] , U1[90000:100000,1], color = 'r', linestyle = 'dashed')


#plt.figure()
#plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
#plt.plot( t[90000:100000] , U[90000:100000,0], color = 'r')
#plt.ylabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.xlabel("$t$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.figure()
#plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
#plt.plot( t[90000:100000] , U[90000:100000,1], color = 'g')
#plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.xlabel("$t$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.show()


# Datos para la línea en 3D
#ta = linspace(0, 10, 100)
#xa = sin(ta)
#ya = cos(ta)
#za = ta

#plt.figure()
#plt.subplot(111, projection='3d')
#plt.plot(U[90000:100000,0], U[90000:100000,1], U[90000:100000,2],color = 'b')
#plt.xlabel('$x$')
#plt.ylabel('$y$')
#plt.gca().set_zlabel('$z$')
#plt.title('Órbita')

## Mostrar la gráfica en 3D
#plt.show()

plt.figure()
plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
plt.plot( t[90000:100000] , U[90000:100000,0], color = 'r')
plt.ylabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlabel("$t$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.figure()
plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
plt.plot( t[90000:100000] , U[90000:100000,1], color = 'g')
plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.xlabel("$t$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.figure()
#plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
#plt.plot( t[90000:100000] , U[90000:100000,2], color = 'b')
#plt.ylabel("$z$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.xlabel("$t$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
plt.show()

#plt.figure()
#plt.grid( axis = 'both' , color = 'gainsboro' , linestyle = 'none' )
#plt.plot( U[:,0] , U[:,1], color = 'r')
#plt.ylabel("$y$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.xlabel("$x$", fontdict = {'fontsize':12, 'fontweight':'normal', 'color':'k'})
#plt.show()



# Crear la figura usando plt.figure
plt.figure()
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Animación de Vector')
plt.axis('equal')
plt.xlim([-0.015 , 0.015])
#plt.ylim([-2 , 2])

# Crear una línea vacía que se actualizará en la animación
line, = plt.plot([], [], '-',color='blue')

# Función de inicialización: se llama para crear la trama base vacía
def init():
    line.set_data([], [])
    #plt.axis([U[:, 0].min(), U[:, 0].max(), U[:, 1].min(), U[:, 1].max()])
    return line,

# Función de actualización para cada cuadro de la animación
def update(frame):
    x = U[:frame, 0]  # Obtener datos hasta el cuadro actual
    y = U[:frame, 1]
    line.set_data(x, y)
    return line,

# Crear la animación
ani = animation.FuncAnimation(plt.gcf(), update, frames=U.shape[0], init_func=init, blit=True, interval=1)
ani.save('animacion.gif', writer='pillow', fps=30)

# Mostrar la animación
plt.show()

#plt.show()

# with warnings.catch_warnings():
#     warnings.simplefilter("ignore", category=UserWarning)
#     hexbin_plot = plt.hexbin(U2[0,:], U2[1,:], gridsize=25, cmap='viridis', mincnt=1)
# counts = hexbin_plot.get_array()
# min_count = min(counts)
# max_count = max(counts)
# common_value = median(counts)
# uncommon_value = min(counts)
# # legend = plt.colorbar(hexbin_plot, label='Frecuencia')
# legend = plt.colorbar(hexbin_plot)
# legend.set_ticks([uncommon_value, common_value, max_count])
# # legend.set_ticklabels(['Menos común', 'Más común', ''])
# legend.ax.set_yticklabels(['', 'Menos común', 'Más común'])
# plt.title('Histograma 2D con leyenda de colores')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.axis('equal')
# plt.show()

#hist, xedges, yedges = histogram2d(U[:,0], U[:,1], bins=25)
#x_centers = (xedges[:-1] + xedges[1:]) / 2
#y_centers = (yedges[:-1] + yedges[1:]) / 2
#fig = plt.figure(figsize=(10, 8))
#ax = fig.add_subplot(111, projection='3d')
#x_mesh, y_mesh = meshgrid(x_centers, y_centers)
#ax.bar3d(x_mesh.flatten(), y_mesh.flatten(), 0, 1, 1, hist.flatten(), shade=True)
#ax.set_xlabel('X')
#ax.set_ylabel('Y')
#ax.set_zlabel('Frecuencia')
#plt.title('Histograma 3D')
#plt.axis('equal')
#plt.show()





# Datos de ejemplo (sustituye estos con tus propios datos)
data_x = U[:,0]
data_y = U[:,1]

# Crear el histograma bidimensional
plt.figure(figsize=(8, 6))
plt.hist2d(data_x, data_y, bins=50, cmap='viridis')

# Agregar etiquetas y título
plt.colorbar(label='Frecuencia')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.title('Histograma 2D de Datos')

## Mostrar el gráfico
#plt.show()


# Calcular el histograma tridimensional
hist, x_edges, y_edges = histogram2d(data_x, data_y, bins=50)

# Obtener las coordenadas para el gráfico 3D
xpos, ypos = meshgrid(x_edges[:-1] + 0.25, y_edges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Tamaños de los cuadrados en el gráfico
dx = dy = 0.5 * ones_like(zpos)
dz = hist.ravel()

# Crear la figura y el eje 3D
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Graficar el histograma tridimensional
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average', cmap='viridis')

# Etiquetas y título
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('Frecuencia')
ax.set_title('Histograma 3D')
ax.set_zlim([0, 500])

# Mostrar el gráfico
plt.show()