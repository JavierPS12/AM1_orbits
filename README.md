# AMPLIACIÓN DE MATEMÁTICAS 1 (AM1_orbits)
MÁSTER UNIVERSITARIO EN SISTEMAS ESPACIALES

Javier Pueyo Serrano (javier.pueyo.serrano@alumnos.upm.es)

El repositorio de Ampliación de Matemáticas 1 está estructurado del siguiente modo: simplemente es necesario ejecutar el archivo "Milestones_JavierPueyoSerrano.py", ya que éste redirige a todos los demás hitos mediante un _input_ en el que hay que introducir el número de hito que se desea ejecutar.

Cada uno de los hitos particulares fundamentalmente contienen llamadas a otros módulos, ordenados en carpetas:
1. __Maths_Equations__
   - Eq_Systems contiene una función para calcular el Jacobiano.
   - Stochastic contiene dos funciones para representar los procesos de Wiener y Ornstein-Uhlenbeck (relacionados con el Hito 7).
   - VanDerPol contiene el operador diferencial del oscilador de Van Der Pol con diferentes condiciones de perturbación (relacionado con el Hito 7).
2. __Maths_ODEs__
1. Primer nivel
   - Elemento 1
   - Elemento 2
     1. Subelemento A
     2. Subelemento B
   - Elemento 3
2. Segundo nivel
   - Otra viñeta
     - Viñeta anidada
       - ¡Más anidación!






Dentro de la carpeta sources hay diferentes carpetas que se detallan a continuación:

1. Error: esta carpeta contiene el método de Richarson.

2. Methods: contiene toda la información relativa a:

        1. Esquemas temporales: Euler, Euler Implícito, Runge Kutta, Crank Nicolson y Leap Frog.

        2. Problema de Cauchy.

        c) Runge Kutta embebido.

        d) Jacobiano.

3) Problems: contiene la informacion para relsolver los problemas de:

        a) Función de Kepler.
        b) Problema del oscilador.
        c) Función de los N-Cuerpos.
        d) NBody.


4) Stability_Region

5) Utilities: dentro de esta carpeta se encuentra:

        a) Plots: permite graficar, de cada Milestone, los resultados.
        b) Solver.
6) Se encuentran todos los hitos.

Los hitos están estructurados de la siguiente manera:

        1)Primero se importan todos los modulos y elementos matematicos que se emplearan.
        2) Se desarrolla el hito propiamente segun el contenido solicitado.
        3)Plotear las graficas.
