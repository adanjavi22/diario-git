nombres = ["Ana", "Carlos", "Leo", "Beatriz", "Eva", "Fernando", "Javi", "Santiago"]


nombresCortos = []
for nombre in nombres:
    if len(nombre) < 5:
        nombresCortos.append(nombre)


#print(" Primeras 3 letras de cada nombre ")
#for nombre in nombres:
    #print(nombre[:3])


apellidos = ["García", "Martínez", "López", "Sánchez", "Pérez", "Gómez", "Rodríguez", "Fernández"]


for i in range(len(nombres)):
    print(nombres[i] + " " + apellidos[i])
            
            
