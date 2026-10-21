#Importa deque desde collections para manipular la cola de turnos de manera eficiente.

from collections import deque 
#Importa time para simular la duración de la atención en ventanilla
import time  

#Crea una variable cola_turnos asignándole la estructura de datos deque()
cola_turnos = deque()

#Agrega al menos 3 clientes a la cola utilizando el método .append().
cola_turnos.append("1.- Jessica Gutierrez Lecona  ")
cola_turnos.append("2.- Juan Fernando Hernandez Lopez")
cola_turnos.append("3.- Brian Isael Ramirez Cortez")

#Recorre la cola e imprime la lista inicial de personas esperando en la fila
print("\nTurnos emitidos - Personas en espera:")
for turno in cola_turnos:
    print(f"  {turno}")

print(f"\nTotal en fila: {len(cola_turnos)} personas\n")

#Implementa un bucle while que permanezca activo mientras existan turnos en la cola.
while cola_turnos:
    #Remueve al primer cliente en llegar usando .popleft().
    cliente_actual = cola_turnos.popleft()
    print(f" Atendiendo en ventanilla a: {cliente_actual}...")
    
    #Simula el tiempo de atención en la ventanilla con time.sleep(1)
    time.sleep(1)
    
    #Muestra la cantidad de clientes restantes en la fila usando len(cola_turnos)
    restantes = len(cola_turnos)
    print(f" {cliente_actual} ha sido atendido.")
    print(f" Clientes restantes en la fila: {restantes}\n")

print(" ¡Todos los clientes han sido atendidos con éxito!")