
#=================================================================================
#								  CAUCHY PROBLEM
#=================================================================================

from numpy import array, zeros, linspace

def Cauchy_Problem( F, t, U_0, Temporal_Scheme ): 

    N =  len(t)-1
    N_var = len(U_0)
    U = zeros( ( N+1, N_var ) )

    U[ 0, : ] = U_0 # Al revés

    for n in range(N):

        U[ n+1, : ] = Temporal_Scheme( U[ n, : ], t[ n ], t[ n+1 ] - t[ n ],  F )

    return U