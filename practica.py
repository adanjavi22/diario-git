nombre = "Bahía"
capacidad = 5000
tipo = "escenario"

print(nombre, type(nombre))
print(capacidad, type(capacidad))
print(tipo, type(tipo))


capacidad = 3000
entradas = 2450

libres = capacidad - entradas
porcentaje = entradas / capacidad * 100

print("Entradas libres:", libres)
print("Porcentaje vendido:", porcentaje, "%")


bahia = 5000
faro = 4000

print("Bahía tiene más aforo:", bahia > faro)


artista = "Kortatu Berri"

print("Longitud:", len(artista))
print("Tres primeras letras:", artista[:3])
print("Tres últimas letras:", artista[-3:])


horaInicio = input("Introduce la hora de inicio del concierto (formato 24h): ")
horaFin = input("Introduce la hora de fin del concierto (formato 24h): ")
horasInicio=int(horaInicio[:2])
minutosInicio=int(horaInicio[3:5])
horasFin=int(horaFin[0:2])
minutosFin=int(horaFin[3:5])
print("El concierto dura", (horasFin-horasInicio), "horas y", (minutosFin-minutosInicio), "minutos")
