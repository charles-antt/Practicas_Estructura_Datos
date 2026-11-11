def mover_torre(altura, origen, destino, intermedio):
    if altura >= 1:
        # 1. Mover n-1 discos de origen a intermedio
        mover_torre(altura - 1, origen, intermedio, destino)
        
        # 2. Mover el disco base a destino
        print(f"Mover disco {altura} de {origen} a {destino}")
        
        # 3. Mover n-1 discos de intermedio a destino
        mover_torre(altura - 1, intermedio, destino, origen)

# Ejemplo con 3 discos (Postes: 'A', 'B', 'C')
mover_torre(3, 'A', 'C', 'B')
