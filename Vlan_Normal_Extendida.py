vlan = input("Ingrese el numero de VLAN") 

try:
    vlan_num = int(vlan)
    if 1 <= vlan_num <= 1005:
        print("La vlan esta dentro del rango normal (1-1005)")
    elif 1006 <= vlan_num <= 4094:
        print("La vlan esta dentro del rango extendido (1006-4094)")
except ValueError:
    print("Entrada no válida. Por favor ingrese un numero entero.")