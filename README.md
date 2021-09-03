
# Gröbner Basis 

An implementation of Buchbergers algorithm 
to compute the gröbner basis of an ideal in a polynomial
ring over the rationals.
For proof of the algorithm please refer to 
9.26 in Abstract Algebra by Dummit and Foote.
Can be extended to n variables and extensons of the rationals. 

Format: 
        (f(x_1,x_2), ... , f_n(x_1, x_2))
Output:    
        Gröbner basis: {g_1, .. g_m}
        Reduced Gröbner basis:{h_1, .. h_k}
