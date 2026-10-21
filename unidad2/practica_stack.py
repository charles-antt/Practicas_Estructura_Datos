# Paso 1: Crear la estructura (Constructor)
# Inicializa una lista vacía que servirá como el contenedor principal de la pila. 
pila_platos = []

# Paso 2: Apilar 10 elementos (Push)
# Agrega 10 elementos consecutivos a la pila usando la función .append(). Puedes automatizarlo con un bucle for:
print("--- Apilando 10 platos ---")
for i in range(1, 11):
    plato = f"Plato {i}"
    pila_platos.append(plato)
    print(f"Ingresó a la pila: {plato}")
print(f"Pila actual: {pila_platos}\n")

# Paso 3: Consultar el elemento en la Cima (Top / Peek)
# Verifica qué plato se encuentra arriba del todo mediante el índice [-1] sin sacarlo de la lista
cima = pila_platos[-1]
print(f" Plato en la cima (Top/Peek): {cima}\n")

# Paso 4: Desapilar 4 elementos (Pop)
# Retiramos 4 platos uno a uno con .pop() para comprobar la regla LIFO (último en entrar, primero en salir)
print("--- Desapilando 4 platos ---")
for _ in range(4):
    plato_retirado = pila_platos.pop()
    print(f"Plato retirado de la cima: {plato_retirado}")
print(f"Pila después de desapilar 4 elementos: {pila_platos}\n")

# Paso 5: Consultar Tamaño (Size) and Estado Vacío (Empty)
# Calculamos cuántos elementos quedan con len() y evaluamos si está vacía
tamanio_actual = len(pila_platos)
esta_vacia = len(pila_platos) == 0

print(f" Tamaño actual de la pila: {tamanio_actual}")
print(f" ¿La pila está vacía?: {esta_vacia}\n")

# EXTRA - Paso 6: Vaciar la pila por completo
# Implementamos un ciclo while que retira elementos hasta que la pila quede vacía
print("--- Vaciando la pila restante por completo ---")
while pila_platos:
    plato_saliente = pila_platos.pop()
    print(f"Retirando: {plato_saliente} | Quedan en pila: {len(pila_platos)}")

# Comprobación final del estado vacío
print(f"\n La pila ha sido vaciada por completo. ¿Está vacía ahora?: {len(pila_platos) == 0}")