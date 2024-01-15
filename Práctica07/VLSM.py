import math

"""
Equipo 4:Implementar una calculadora VLSM.

Adrián Aguilera Moreno Num.C:421005200
Francisco Contreras Ibarra Num.C: 316083786
Aldo Daniel Licona Gómez Num.C: 316263863
"""

# Función que encuentra el número de bits que ocupan los hosts. 
def encontrar_n(lista_hosts):
    # :param: lista_hosts que tiene el número de hosts en orden decreciente.
    lista_n = []
    for x in lista_hosts:
        lista_n.append(math.ceil(math.log(x, 2)))
    return lista_n

# Función que encuentra el número de hosts útiles.
def encontrar_hosts_utiles(lista_n):
    # :param: bits que ocupan los hosts.
    lista_u = []
    for x in lista_n:
        lista_u.append(pow(2, x) - 2)
    return lista_u

# Nos indica la máscara en forma de prefijo.
def encontrar_mascara(lista_n):
    # :param: lista_n bits que ocupan los hosts.
    lista_m = []
    for x in lista_n:
        lista_m.append(32 - x)
    return lista_m

# Encuentra el valor para el último octeto.
def ultimo_octeto(lista_m):
    # :param: lista_m es la sub-máscara para cada subred.
    lista_ultimo_octeto = []
    for x in lista_m:
        sum = 0
        if x > 24 and x <= 32:
            for i in range(7, 7 - (x - 24), -1):
                sum += pow(2, i)
            lista_ultimo_octeto.append(sum)
        elif x > 16:
            for i in range(7, 7 - (x - 16), -1):
                sum += pow(2, i)
            lista_ultimo_octeto.append(sum)
        elif x > 8:
            for i in range(7, 7 - (x - 8), -1):
                sum += pow(2, i)
            lista_ultimo_octeto.append(sum)
        elif x >= 0:
            for i in range(7, 7 - x, -1):
                sum += pow(2, i)
            lista_ultimo_octeto.append(sum)
    return lista_ultimo_octeto

# Encuentra el número mágico por subred. Estos son los valores del rango válido.
def encontrar_magico(lista_ultimo_octeto):
    # :param: lista_ultimo_octeto valor para el último octeto
    lista_magicos = []
    for x in lista_ultimo_octeto:
        lista_magicos.append(256 - x)
    return lista_magicos

# ---------------------------------------------------------------------------------------- Zona de ejecución.
print(" ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ VLSM ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")
print("Introduce la dirección IP por octetos (32 bits):\n")

octeto01 = input("      Escribe el octeto 01 en decimal: ")
octeto02 = input("      Escribe el octeto 02 en decimal: ")
octeto03 = input("      Escribe el octeto 03 en decimal: ")
octeto04 = input("      Escribe el octeto 04 en decimal: ")
prefijo  = input("\n      Ingresa el prefijo asociado a la máscara: ")

print("\n       --> IP: " + octeto01 + "." + octeto02 + "." + octeto03 + "." + octeto04 + "/" + prefijo + "\n")

try:
    hosts = int(input("Introduce la cantidad de subredes deseada en orden decendente: "))
except ValueError:
    print("El número de subredes de ser un valor entero positivo, parece que te has equivocado :(")
    
lista_hosts = []
contador = 0
while contador < hosts:
    contador += 1
    try:
        temporal = int(input("   Ingresa el número de host para la red " + str(contador) + ": "))
    except ValueError:
        print("El número valor del host debe ser un valor entero positivo, parece que te has equivocado :(")
    lista_hosts.append(temporal)

lista_n = encontrar_n(lista_hosts)
lista_u = encontrar_hosts_utiles(lista_n)
lista_m = encontrar_mascara(lista_n)
lista_ultimo_octeto = ultimo_octeto(lista_m)
lista_magicos = encontrar_magico(lista_ultimo_octeto)


contador = 0
while contador < hosts:
    contador += 1
    representacion = "Subred " + str(contador) + ":\n"
    if contador - 1 != 0:
        representacion += "    ---> IP: " + octeto01 + "." + octeto02 + "." + octeto03 + "." + str(lista_ultimo_octeto[contador - 2] + int(octeto04)) + "/" + str(lista_m[contador - 1]) + "\n"
    else:
        representacion += "    ---> IP: " + octeto01 + "." + octeto02 + "." + octeto03 + "." + octeto04 + "/" + str(lista_m[contador - 1]) + "\n"
    representacion +=     "         Rango de direcciones: " + str(lista_magicos[contador - 1]) + "         Broadcast: " + octeto01 + "." + octeto02 + "." + octeto03 + "." + str(lista_ultimo_octeto[contador - 1] + int(octeto04) - 1) + "\n"
        
    print(representacion)
