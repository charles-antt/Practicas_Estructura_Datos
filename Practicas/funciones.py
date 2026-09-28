import random

#Funcion con argumentos 
def fav_lenguaje(nombre,lenguaje):
    print(f"Hola, soy {nombre} y mi lenguaje de programación favorito es {lenguaje}")
fav_lenguaje("Carlos", "Python")
print()

def futbolista(nombre,posicion):
    print(f"Su jugador se llama {nombre} y juega de {posicion}")
futbolista("Chuky Lozano", "Extremo izquierdo")
print()

#Funcion sin argumentos 
def error_transacción():
    print ("Lo sentimos, ocurrió un error en su transacción bancaria, intenelo de nuevo")
error_transacción()
print()

def lanzar_dado():
    resultado = random.randint(1, 6)
    print(f"El número del dado es: {resultado}")
lanzar_dado()