print("--- EJERCICIO 1 ---")
print()
def limpiar_feed(publicaciones: list) -> list:
    
    if len(publicaciones) <= 1:
        return publicaciones
    
    if publicaciones[0] == publicaciones[1]:
        return limpiar_feed(publicaciones[1:])
    else:

        return [publicaciones[0]] + limpiar_feed(publicaciones[1:])

print(limpiar_feed(["Post A", "Post B", "Post B", "Post C", "Post B"]))
print()

print("--- EJERCICIO 2 ---")
print()
def calcular_saldo_final(depositos: list, tasa_interes: float) -> float:
    
    if not depositos:
        return 0.0
    
    return (calcular_saldo_final(depositos[:-1], tasa_interes) + depositos[-1]) * (1 + tasa_interes)

saldo = calcular_saldo_final([1000, 2000, 1500], 0.05)
print(f"{saldo:.2f}")
print()

print("--- EJERCICIO 3 ---")
print()
def maxima_profundidad(comentarios: list) -> int:

    if not comentarios:
        return 0
    
    profundidad_max = 0

    for elem in comentarios:
        if isinstance(elem, list):
            prof_actual = 1 + maxima_profundidad(elem)
        else:
            prof_actual = 1
            
        if prof_actual > profundidad_max:
            profundidad_max = prof_actual

    return profundidad_max

hilo = ["Comentario 1", ["Respuesta 1.1", ["Respuesta 1.1.1"]], "Comentario 2"]
print(maxima_profundidad(hilo))
print()



