estudiantes = ["Ana", "Carlos", "Diana"]
print()
print("1.-Lista inicial: ", estudiantes)
print()
#insersion de estudiante
estudiantes.append("Elena")
estudiantes.insert(1, "Beatriz")

print("2.-Lista tras inserciones: ", estudiantes)
print()
print("3.-Busqueda por índice: ")
print(estudiantes[0])
print(estudiantes[2])
print(estudiantes[3])
print()

print("4.- Resultados por Slicing: ")
print("Primeros 3 estudiantes: ", estudiantes[:3])
print("Subgrupo del índice 1 al 3 ",  estudiantes[1:4])
print("Ultimos dos estudiantes: ", estudiantes[-2:])
print("Lista totalmente invertida: ", estudiantes[::-1])