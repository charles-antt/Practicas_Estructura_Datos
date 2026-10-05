import matplotlib.pyplot as plt

datos = [42, 12, 88, 23, 7, 65, 34, 50]

# ALGORITMO DE INSERCIÓN
def insercion(arr):
    a = arr.copy()
    comp = 0
    for i in range(1, len(a)):
        clave = a[i]
        j = i - 1
        while j >= 0 and a[j] > clave:
            comp += 1
            a[j + 1] = a[j]
            j -= 1
        if j >= 0:
            comp += 1
        a[j + 1] = clave
    return a, comp

# ALGORITMO DE SELECCIÓN
def seleccion(arr):
    a = arr.copy()
    comp = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comp += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, comp

# EJECUTAMOS AMBOS ALGORITMOS
lista_ordenada, comp_ins = insercion(datos)
_, comp_Sel = seleccion(datos)

# GRAFICACIÓN (plt.subplots en plural)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(12, 3.5))

# GRÁFICO 1 INICIAL - LISTA DESORDENADA
ax1.bar(range(len(datos)), datos, color='salmon')
ax1.set_title('1.- LISTA DESORDENADA')
ax1.set_ylabel('Valor')

# GRÁFICO 2 - LISTA ORDENADA
ax2.bar(range(len(lista_ordenada)), lista_ordenada, color='green')
ax2.set_title('2.- LISTA ORDENADA')

# GRÁFICO 3 - COMPARACIONES REALIZADAS (colores en lista)
ax3.bar(['Inserción', 'Selección'], [comp_ins, comp_Sel], color=['#1f77b4', '#ac8059'])
ax3.set_title('3.- COMPARACIONES')
ax3.set_ylabel('Cantidad')

plt.tight_layout()
plt.show()