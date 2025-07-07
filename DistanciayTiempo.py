import math

ciudades = {
    "santiago": (-33.4489, -70.6693),
    "valparaiso": (-33.0472, -71.6127),
    "concepcion": (-36.8201, -73.0444),
    "temuco": (-38.7359, -72.5904),
    "buenos aires": (-34.6037, -58.3816),
    "córdoba": (-31.4167, -64.1833),
    "mendoza": (-32.8908, -68.8272),
    "rosario": (-32.9468, -60.6393)
}

def calcular_distancia(coord1, coord2):
    R = 6371 
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distancia_km = R * c
    distancia_mi = distancia_km * 0.621371
    return distancia_km, distancia_mi

def estimar_duracion(distancia_km, medio):
    velocidades = {
        "auto": 80,
        "bicicleta": 15,
        "a pie": 5
    }
    velocidad = velocidades.get(medio, 50)
    duracion_horas = distancia_km / velocidad
    horas = int(duracion_horas)
    minutos = int((duracion_horas - horas) * 60)
    return horas, minutos

def main():
    medios = {
        "1": "auto",
        "2": "bicicleta",
        "3": "a pie"
    }

    while True:
        print("\n Calculadora de viaje ")
        origen = input("Ciudad de Origen (Chile): ").strip().lower()
        if origen == "s":
            break
        destino = input("Ciudad de Destino (Argentina): ").strip().lower()
        if destino == "s":
            break

        if origen not in ciudades or destino not in ciudades:
            print(" Una o ambas ciudades no están en la base local.")
            continue

        print("\nSelecciona medio de transporte:")
        print("1. Auto\n2. Bicicleta\n3. A pie")
        medio_op = input("Opción: ").strip().lower()
        if medio_op == "s":
            break

        medio = medios.get(medio_op)
        if not medio:
            print(" Opción inválida.")
            continue

        coord_origen = ciudades[origen]
        coord_destino = ciudades[destino]

        distancia_km, distancia_mi = calcular_distancia(coord_origen, coord_destino)
        horas, minutos = estimar_duracion(distancia_km, medio)

        print(f"\n Resultado del viaje en {medio.upper()}:")
        print(f"Distancia: {distancia_km:.2f} km / {distancia_mi:.2f} millas")
        print(f"Duración estimada: {horas} horas y {minutos} minutos")
        print(f" Narrativa: Desde {origen.title()} hasta {destino.title()} en {medio}, "
              f"recorrerás unos {distancia_km:.2f} km en aproximadamente {horas}h {minutos}min.")

        continuar = input("\n¿Deseas calcular otro viaje? (presiona 's' para salir): ").lower()
        if continuar == "s":
            break

if __name__ == "__main__":
    main()
