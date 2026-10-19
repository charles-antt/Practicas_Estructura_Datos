historial_navegacion=[]
#OPREACION PARA APILAR PUSH
historial_navegacion.append("google.com")
historial_navegacion.append("youtube.com")
historial_navegacion.append("wikipedia.org")
print()
print("historial cargado", historial_navegacion)
print()

#OPERACION (TOP-PEEK)
pagina_actual=historial_navegacion[-1]
print("página actual en pantalla:", pagina_actual)
print()

#OPERACION PARA DESAPILAR (POP)
pagina_desapilada=historial_navegacion.pop()
print("Saliendo de:", pagina_desapilada)
print("historial despues de presionar 'Atras': ", historial_navegacion)
print()

#"OPERACION TAMAÑO (SIZE)"
total_paginas=len(historial_navegacion)
print("pagins guardadas: ", total_paginas)
print()

#OPERACION VACIA (EMPTY)
sin_paginas=len(historial_navegacion)==0
print("¿El historial esta vacio?: ", sin_paginas)