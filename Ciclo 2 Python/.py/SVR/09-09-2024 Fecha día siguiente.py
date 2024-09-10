def es_bisiesto(anio):
    """Determina si un año es bisiesto."""
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def obtener_dia_siguiente(fecha):
    """Calcula la fecha del día siguiente."""
    # Descomponer la fecha
    dia = int(fecha[:2])
    mes = int(fecha[2:4])
    anio = int(fecha[5:])
    
    # Días en cada mes
    dias_en_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Ajustar febrero si el año es bisiesto
    if es_bisiesto(anio):
        dias_en_mes[1] = 29
    
    # Incrementar el día
    dia += 1
    
    # Verificar si el día supera los días del mes actual
    if dia > dias_en_mes[mes - 1]:
        dia = 1
        mes += 1
    
    # Verificar si el mes supera diciembre
    if mes > 12:
        mes = 1
        anio += 1
    
    # Formatear la nueva fecha
    nueva_fecha = f"{dia:02d}-{mes:02d}-{anio}"
    return nueva_fecha

# Solicitar la fecha al usuario
fecha = input("Introduce la fecha en formato DIAMES-AÑO: ")

# Obtener y mostrar la fecha del día siguiente
dia_siguiente = obtener_dia_siguiente(fecha)
print("La fecha del día siguiente es:", dia_siguiente)
