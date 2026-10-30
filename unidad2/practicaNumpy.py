import numpy as np
# 1.- CREAR LAS MATRICES 
# MATRIZ A = SABADO 
# MATRIX B = DOMINGO 
matriz_a = np.array([[10, 15], [20, 5]])
matriz_b = np.array([[5, 12], [15, 8]])

# 2.- CALCULAR EL DE PRODUCTOS VENDIDOS EN EL FIN DE SEMANA MEDIANTE LA SUMA MATRICIAL 
total_vendidos = matriz_a + matriz_b

# 3.- FIJAR PRECIO Y CALCULAR EL INGRESO TOTAL 
# PRECIO FIJO = 50  PESOS POR UNIDAD 
precio_unidad = 50
ingreso_total = total_vendidos *precio_unidad

# 4.- IMPRIMIR MATRIZ CON EL TOTAL DE PRODUCTOS VENDIDOS  Y LA MATRIZ CON EL INGRESO TOTAL EN DINERO 
print()
print("-- REALIZADO CON NUMPY --")
print("Total de producto vendidos (Sábado y Domingo)")
print(total_vendidos)
print()

print("Ingreso total en pesos (a 50 pesos el producto)")
print(ingreso_total)
print()

matriz_A = [[10, 15], [20, 5]]
matriz_B = [[5, 12], [15, 8]]

total_vendidos2 = [[matriz_A[i][j] + matriz_B[i][j] for j in range(len(matriz_A[0]))] for i in range(len(matriz_A))]

ingreso_total2 = [[total_vendidos2[i][j] * precio_unidad for j in range(len(total_vendidos2[0]))] for i in range(len(total_vendidos2))]

print("-- REALIZADO DE FORMA NATIVA --")
print("Total de producto vendidos (Sábado y Domingo)")
print(total_vendidos)
print()

print("Ingreso total en pesos (a 50 pesos el producto)")
print(ingreso_total)
print()
