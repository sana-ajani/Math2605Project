# Math2605Project
Calc 3 for CS project

LU Decomposition
Author: Eduardo Mestanza

In order to test out the LU Decomposition just type into the command line:

python luDecomposition.py

This will run the code for both the lu_fact and solve_lu_b which ouput the L and U Matrixes
for the given Pascal Matrix, the error value of ||LU - A||, the Xsolution vector, the error
value of ||LU - P|| and finally the error value of ||Px - b||. It will iterate through and solve the L and U Matrix for n = 1, 2, 3, ... , 12 pascal matrix.

There is also an excel file with the information on ||LU - P|| error and ||Px - b|| error for each of the pascal matrixes. The information has been plotted into a logarithmic graph which shows the ||Px - b|| error vs the dimensions of the PAscal Matrix

QR Decomposition
To test Householder's, type into the command line:

python qr_fact_househ

To test Given's, type into the command line:

python qr_fact_givens

These will return Q, R, the error ||QR - A|| and the obtain the solution to a system Ax = b
(no scatterplot included)

Iterative Methods
Author: Eduardo Mestanza

In order to test out the Jacobi and Gauss-Seidel iterations just type into the command line:

python IterativeMethods.py

This will run the code for both the jacobi_iter and gs_iter functions. They will go and find the Xsolution for 100 randomly generated vectors. Although only the following will be printed
from each one of the functions.

 - The solution from the last randomly generated the Xsolution vector.
 - Number of iterations to it took to get the Xsolution.
 - The average approximation error for all 100 of the randomly generated vectors.
 - The average number of iterations needed to reach the Xsolution vector.

In the end it will also print out the ratio of Jacobi iterations / Gauss-Seidel iteration

Information on the ||X0 - Xexact|| and number of iteration per random X vector will be given in two excel files. These two files contain this information for each of the iterative methods.
They also contain the graphical representation of the ||X0 - Xexact|| error.


Power Method
To test this file, type this into the command line:

python power_method.py

This returns the number of iterations, approximate eigenvalue and eigenvector. It will run with the values of the matrix in the file, but to test different matrices, simply edit the file.
(no scatterplot included)
