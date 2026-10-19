from collections import deque
import time 
cola_reproduccion =deque()
cola_reproduccion.append("1.- Mis hitoria entre tus dedos")
cola_reproduccion.append("2.- Luna")
cola_reproduccion.append("3.- Penurias")

#MOSTRAR LAS CANCIONES EN ESPERA

print("canciones en eespera.")
for cancion in cola_reproduccion:
    print(" -", cancion)
    print("iniciando reproduccion ...")
#EL REPODUCTOR PROCESA LA COLA CANCION POR CANCION (DESENCOLAR)
while cola_reproduccion:
    cancion_actual=cola_reproduccion.popleft()
    print(f"Sonando ahora {cancion_actual}")
    time.sleep(1) #simula la duración dle tema
    print(f"finalizó: {cancion_actual}")
    #Muestran cunatas canciones quedan en la cola 
    print(f"Quedan{len(cola_reproduccion)}) canciones en la cola")
    print("la cola de reproduccion a terminado")