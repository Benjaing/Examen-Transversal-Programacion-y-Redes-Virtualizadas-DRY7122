import requests

API_KEY = '266e2bdf-660a-4237-810f-0bd4eafd9d40' 

def geocodificar(ciudad):
    url = 'https://graphhopper.com/api/1/geocode'
    params = {
        'q': ciudad,
        'locale': 'es',
        'limit': 1,
        'key': API_KEY
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        resultados = response.json()['hits']
        if resultados:
            lat = resultados[0]['point']['lat']
            lon = resultados[0]['point']['lng']
            return f"{lat},{lon}"
        else:
            print(f"No se encontró la ciudad: {ciudad}")
            return None
    else:
        print("Error en la geocodificación:", response.text)
        return None

def obtener_datos(coord_origen, coord_destino, modo_transporte):
    url_base = 'https://graphhopper.com/api/1/route'
    params = {
        'point': [coord_origen, coord_destino],
        'vehicle': modo_transporte,
        'locale': 'es',
        'calc_points': 'true',
        'instructions': 'true',
        'key': API_KEY
    }

    response = requests.get(url_base, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al contactar GraphHopper:", response.text)
        return None

def mostrar_resultados(data):
    distancia_km = data['paths'][0]['distance'] / 1000
    distancia_mi = distancia_km * 0.621371
    duracion_seg = data['paths'][0]['time'] / 1000
    duracion_min = duracion_seg / 60
    narrativa = data['paths'][0]['instructions']

    print(f"\n Distancia: {distancia_km:.2f} km / {distancia_mi:.2f} millas")
    print(f" Duración estimada: {duracion_min:.1f} minutos")
    print("\n Narrativa del viaje:")
    for paso in narrativa:
        print(f"- {paso['text']}")

def main():
    print("🚗 Bienvenido al calculador de rutas Chile - Argentina")
    while True:
        origen = input("Ingrese la Ciudad de Origen (o 's' para salir): ")
        if origen.lower() == 's':
            break
        destino = input("Ingrese la Ciudad de Destino (o 's' para salir): ")
        if destino.lower() == 's':
            break
        print("Medios de transporte disponibles: car, bike, foot, scooter, etc.")
        transporte = input("Ingrese el medio de transporte: ")

        coord_origen = geocodificar(origen)
        coord_destino = geocodificar(destino)

        if coord_origen and coord_destino:
            datos = obtener_datos(coord_origen, coord_destino, transporte)
            if datos:
                mostrar_resultados(datos)

if __name__ == "__main__": 
        main()