
def checksum(bits):
    # Verificamos que la cadena tenga 16 bits 
    if len(bits) != 32: # Modificar en caso de querer pasar 64 bits.
        raise ValueError("La cadena debe contener exactamente 32 bits")

    # Convertimos la cadena de bits en una lista de enteros
    cadena = list(map(int, bits))

    # Separamos dos segmentos de bits (nuestras "palabras"):
    P_1 = cadena[:(len(cadena) // 2)]
    P_2 = cadena[(len(cadena) // 2):]
    
    complemento = [(1 - bit) for bit in sumar2(P_1, P_2)]

    checksum = cadena + complemento
    
    nueva_cadena = ''.join(map(str, checksum))
    return nueva_cadena

def sumar2(P_1, P_2):
    # Verificamos que ambas cadenas sean del mismo tamanio.
    if len(P_1) != len(P_2):
        raise ValueError("Error, las cadenas tienen tamanio distinto.")

    lista = []
    valor_extra = 0
    P_3 = reversed(P_1)
    P_4 = reversed(P_2)
    for elem1, elem2 in zip(P_3, P_4):
        if((elem1 == 0) and (elem2 == 0)):
            if (valor_extra == 1):
                lista.insert(0, 1)
                valor_extra = 0
            else:
                lista.insert(0, 0)
        elif((elem1 == 1) and (elem2 == 1)):
            if (valor_extra == 1):
                lista.insert(0, 1)
            else:
                lista.insert(0, 0)
            valor_extra = 1
        elif((elem1 == 1) and (elem2 == 0)):
            if (valor_extra == 1):
                lista.insert(0, 0)
                valor_extra = 1
            else:
                lista.insert(0, 1)
        elif((elem1 == 0) and (elem2 == 1)):
            if (valor_extra == 1):
                lista.insert(0, 0)
                valor_extra = 1
            else:
                lista.insert(0, 1)
    
    if(valor_extra == 1):
        lista.insert(0, 1)

    return lista

def sumar3(bits):
    cadena = list(map(int, bits))
    tercios = (len(cadena) // 3)
    P_1 = cadena[:tercios]
    P_2 = cadena[tercios:(2*tercios)]
    P_3 = cadena[(2*tercios):len(bits)]

    R  = sumar2(P_1, P_2)
    RP = sumar2(R, P_3)
    RT = ''.join(map(str, RP))
    return RT

# Ejemplo de uso
print("Orden:         Cadena original                 :                Checksum añadido                  :  Comprobación.")
cadena_bits = "01100110011001100101010101010101"
resultado = checksum(cadena_bits)
comprobacion = sumar3(resultado)
print(f"Checksum para {cadena_bits} : {resultado} : {comprobacion}")
