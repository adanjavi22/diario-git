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


hora = "21:00"

horas = int(hora[:2])
minutos = int(hora[3:])

total = horas * 60 + minutos

print("Minutos desde medianoche:", total)