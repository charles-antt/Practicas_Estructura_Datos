from collections import deque 
import time  

cola_turnos = deque()

cola_turnos.append("1.- Jessica Gutierrez Lecona  ")
cola_turnos.append("2.- Juan Fernando Hernandez Lopez")
cola_turnos.append("3.- Brian Isael Ramirez Cortez")


print("\nTurnos emitidos - Personas en espera:")
for turno in cola_turnos:
    print(f"  {turno}")

print(f"\nTotal en fila: {len(cola_turnos)} personas\n")


while cola_turnos:
    cliente_actual = cola_turnos.popleft()
    print(f" Atendiendo en ventanilla a: {cliente_actual}...")
    
    time.sleep(1)
    
    restantes = len(cola_turnos)
    print(f" {cliente_actual} ha sido atendido.")
    print(f" Clientes restantes en la fila: {restantes}\n")

print(" ¡Todos los clientes han sido atendidos con éxito!")