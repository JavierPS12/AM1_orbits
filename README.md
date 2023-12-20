# AMPLIACIÓN DE MATEMÁTICAS 1 (AM1_orbits)
MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES

Javier Pueyo Serrano (javier.pueyo.serrano@alumnos.upm.es)

El repositorio de __Ampliación de Matemáticas 1__ está estructurado del siguiente modo: simplemente es necesario ejecutar el archivo _"Milestones_JavierPueyoSerrano.py"_, ya que éste redirige a todos los demás hitos mediante un _input_ en el que hay que introducir el número de hito que se desea ejecutar.

La __estructura jerárquica__ puede apreciarse en la siguiente imagen:
<p align="center">
  <img src=".\Estructura.png" alt="Descripción de la imagen">
</p>

Cada uno de los hitos particulares fundamentalmente contiene _llamadas_ a otros módulos, ordenados en carpetas:
1. __Maths_Equations__
   - Eq_Systems contiene una función para calcular el Jacobiano.
   - Stochastic contiene dos funciones para representar los procesos de Wiener y Ornstein-Uhlenbeck (relacionados con el Hito 7).
   - VanDerPol contiene el operador diferencial del oscilador de Van Der Pol con diferentes condiciones de perturbación (relacionado con el Hito 7).
2. __Maths_ODEs__
   - Cauchy_Problem contiene el algoritmo para la resolución del problema del valor inicial.
   - Stability_Region contiene el algoritmo para representar la región de estabilidad absoluta de diferentes esquemas de integración numérica temporal.
   - Temporal_Error contiene el algoritmo para la extrapolación de Richardson.
   - Temporal_Schemes contiene diferentes esquemas temporales de integración numérica.
3. __Physics__
   - CR3BP contiene todas las funciones relacionadas con el problema reducido de los tres cuerpos.
   - Kepler_Equation contiene el operador diferencial de la ecuación de Kepler.
   - N_Body contiene el algoritmo para la resolución del problema de los N cuerpos.
4. __Plotting__
   - Animation contiene el algoritmo para realizar animaciones GIF de las representaciones gráficas.
   - Graphics contiene el algoritmo para realizar representaciones bidimensionales y tridimensionales.
   - Histogram contiene los algoritmos para dibujar histogramas bidimensionales (mediante códigos de colores) y tridimensionales (mediante barras).

Los hitos están estructurados de la siguiente manera:
1. Primero se importan todos los módulos y funciones internas de Python que se emplearán.
2. Se desarrolla el hito propiamente según el contenido solicitado.
3. Se realizan las representaciones gráficas pertinentes.
