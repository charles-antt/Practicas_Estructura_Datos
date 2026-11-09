class Nodo: 
    def __init__(self, dato):
        self.dato= dato
        self.siguiente= None
# CRACION DE UN NODO INDIVIDUAL
nodo_singular = Nodo("Primer Dato")
print (nodo_singular.dato)
print(nodo_singular.siguiente)