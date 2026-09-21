lista = [10,7,8,6,9,10,4,8,7,6,9,10,8,5,7]
n =len(lista)
swapped = True
while swapped:
    swapped = False
    for i in range (n-1):
        if lista[i]>lista[i+1]:
            lista[i], lista[i+1]=lista[i+1],lista[i]
            swapped = True 
print("Lista ordenada ascendente: ",lista)

print()

swapped = True
while swapped:
    swapped = False
    for i in range (n-1):
        if lista[i]<lista[i+1]:
            lista[i], lista[i+1]=lista[i+1],lista[i]
            swapped = True 
print("Lista ordenada descendente: ",lista)