pila_platos = []

print("--- Apilando 10 platos ---")
for i in range(1, 11):
    plato = f"Plato {i}"
    pila_platos.append(plato)
    print(f"Ingresó a la pila: {plato}")
print(f"Pila actual: {pila_platos}\n")
print()

cima = pila_platos[-1] 
print(f" Plato en la cima (Top/Peek): {cima}\n")
print()

print("--- Desapilando 4 platos ---")
for _ in range(4):
    plato_retirado = pila_platos.pop()
    print(f"Plato retirado de la cima: {plato_retirado}")
print(f"Pila después de desapilar 4 elementos: {pila_platos}\n")
print()

tamanio_actual = len(pila_platos)
esta_vacia = len(pila_platos) == 0

print(f" Tamaño actual de la pila: {tamanio_actual}")
print(f" ¿La pila está vacía?: {esta_vacia}\n")
print()

print("--- Vaciando la pila restante por completo ---")
while pila_platos:
    plato_saliente = pila_platos.pop()
    print(f"Retirando: {plato_saliente} | Quedan en pila: {len(pila_platos)}")

print()
print(f"\n La pila ha sido vaciada por completo. ¿Está vacía ahora?: {len(pila_platos)  == 0}")