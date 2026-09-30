print()
def reporte_notas():
    print("===== UNIVERSIDAD TECNOLÓGICA DE XICOTEPEC DE JUÁREZ =====")
    print("===== SISTEMA DE REPORTE DE NOTAS DE ESTUDIANTES =========")


def nota_minima_aprobatoria():
    return 6.0


def evaluar_rendimiento(nota_final):
    if nota_final < 7.0:
        return "Reprobado"
    elif 7.0 <= nota_final <= 9.4:
        return "Aprobado"
    elif 9.5 <= nota_final <= 10.0:
        return "Excelente"
    else:
        return "Nota fuera de rango"


def calcular_promedio_ponderado(nota_examenes, nota_tareas):
    nota_final = (nota_examenes * 0.70) + (nota_tareas * 0.30)
    return round(nota_final, 1)


def generar_boleta(nombre_alumno, nota_examenes, nota_tareas):
    nota_final = calcular_promedio_ponderado(nota_examenes, nota_tareas)
    nota_minima = nota_minima_aprobatoria()
    estado_academico = evaluar_rendimiento(nota_final)
    necesita_extraordinario = "SÍ" if nota_final < nota_minima else "NO"

    # Mover los prints AQUÍ ADENTRO (con su respectiva sangría/indentación)
    reporte_notas()
    print(f"Nombre del Alumno: {nombre_alumno}")
    print(f"Nota Exámenes: {nota_examenes}")
    print(f"Nota Tareas: {nota_tareas}")
    print("----------------------------------------")
    print(f"Calificación final: {nota_final}")
    print(f"Estado Académico: {estado_academico}")
    print(f"Necesita Extraordinario: {necesita_extraordinario}")
    print()


generar_boleta("Brian Gutierrez", 6.7, 8.8)

generar_boleta("Jessica Cortez", 5.5, 6.0)