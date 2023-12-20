
print( "" )
print( "   ==========================================================================" )
print( "   ==           MASTER UNIVERSITARIO EN SISTEMAS ESPACIALES                ==" )
print( "   ==                    AMPLIACION DE MATEMATICAS 1                       ==" )
print( "   ==                        Javier Pueyo Serrano                          ==" )
print( "   ==========================================================================" )
print( "" )
print( "   ==========================================================================" )
print( "   =========================    WEEKLY MILESTONES    ========================" )
print( "   ==========================================================================" )
print( "" )

print( "   Seleccione el Hito que quiere ejecutar:" )
print( "" )
print( "      - Milestone 1. Prototypes to integrate orbits without functions")
print( "      - Milestone 2. Prototypes to integrate orbits with functions")
print( "      - Milestone 3. Error estimation of numerical solutions")
print( "      - Milestone 4. Linear problems. Regions of absolute stability")
print( "      - Milestone 5. N-body problem")
print( "      - Milestone 6. Lagrange points and their stability")
print( "      - Milestone 7. Stochastic perturbation in Van der Pol oscillator")
print( "" )
eleccion = int(input("   Introduzca la opcion elegida (numero del Milestone): "))
print( "" )

if eleccion == 1:

	print("   Ha seleccionado el Milestone 1: Prototypes to integrate orbits without functions.")
	import Milestone1
	
elif eleccion == 2:
	
	print("   Ha seleccionado el Milestone 2: Prototypes to integrate orbits with functions.")
	import Milestone2

elif eleccion == 3:
	
	print("   Ha seleccionado el Milestone 3: Error estimation of numerical solutions.")
	import Milestone3

elif eleccion == 4:
	
	print("   Ha seleccionado el Milestone 4: Linear problems. Regions of absolute stability.")
	import Milestone4

elif eleccion == 5:
	
	print("   Ha seleccionado el Milestone 5: N-body problem.")
	import Milestone5


elif eleccion == 6:
	
	print("   Ha seleccionado el Milestone 6: Lagrange points and their stability.")
	import Milestone6

elif eleccion == 7:
	
	print("   Ha seleccionado el Milestone 7: Stochastic perturbation in Van der Pol oscillator.")
	import Milestone7

else:

	exit