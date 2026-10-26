import numpy as np
#MATRIZ A Y B 
A = np.array([[1,2], [3,4]])
B = np.array([[5,6], [7,8]])

#SUMA DE LOS ELEMENTOS
suma= A+B
print("-- SUMA (A+B) --")
print(suma)
print()

#MULTIPLICACION DE ELEMETOS 
prod_elem= A*B
print("-- MULTIPLICACION (A*B)")
print(prod_elem)
print()

#PRODUCTO MATRICIAL 
prod_mat=A@B
print("-- PRODUCTO MATRICIAL (A@B)--")
print(prod_mat)
print()

#TRANSPUESTA    
transpuesta = A.T
print("-- TRANSPUESTA (A.T) --")
print(transpuesta)
print()

#DETERMINANTE E INVERSA 
det = np.linalg.det(A)
inv = np.linalg.det(B)
print("-- DETERMINANTE DE A --")
print(det)
print("--INVERSA DE B --")
print(inv)