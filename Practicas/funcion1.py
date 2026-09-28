import datetime
def saludar():
    print("Hola, Bienvenidos")
saludar()

def mostrar_hora():
    hora_actual=datetime.datetime.now().strftime("%H, %M, %S")
    print (f"La hora actual es:{hora_actual}")
mostrar_hora()

    # Now() Consulta el reloh o la hora del SO 
    #Strftime convertir la fecha y hora en texto, usando el formato establecido
    #f-string la letra f indica a pythonque procese el texto
    # e inderte las variables dentro de las llaves 
    #{hora_actual} se toma el valor almacenado en la variable de hora_actual
    #y lo reemplaza ahí mismo