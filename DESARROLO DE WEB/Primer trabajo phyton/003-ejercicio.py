# Solicitar al usuario velocidad en kilómetros por hora (Km/h) y tiempo en horas (h) para obtener la distancia en kilómetros (Km)
velocidad = float(input("Ingrese la velocidad en km/h: "))

tiempo = float(input("Ingrese el tiempo de horas en (h): "))

distancia = velocidad * tiempo 

print(f"La distancia recorrida es de {distancia} km")