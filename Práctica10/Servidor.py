'''
             ---->  Equipo 4:
Adrián Aguilera Moreno         Num.C:421005200
Francisco Contreras Ibarra     Num.C: 316083786
Aldo Daniel Licona Gómez       Num.C: 316263863
'''


import socket
import sys

# Crear un socket TCP (STREAM)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto al que se desea conectar
host = "localhost"  # Puede ser una dirección IP o un nombre de dominio
port = 5656         # Puerto al que desea conectarse

# Conectar al dispositivo remoto
server.bind((host, port))

server.listen(3)

print("En espera de conexiones ...")
active, addr= server.accept()


while True:
    recibido = active.recv(1024)
    print("    -> Cliente: ", recibido.decode())
        
    if recibido.decode().lower() == 'exit':  # Salir del bucle si el comando es 'exit'
        active.close()
        server.close()
        break
    
    if recibido.decode() == "mkdir":
        cadena  = "\n    ----------------------------------------------------------------------------------------------------"  
        cadena += "              mkdir: comando usado para crear directorios desde su terminal.\n"
        cadena += "                                 E.g.   mkdir Docs\n"
        cadena += "           Crea un directorio llamado Docs, esto desde el directorio en el que se encuentre.\n"
        cadena += "    ----------------------------------------------------------------------------------------------------"
        active.sendall(cadena.encode())
    elif recibido.decode() == "ls":
        cadena  = "\n    ----------------------------------------------------------------------------------------------------"  
        cadena += "                            ls: Muestra el contenido del directorio actual.\n"
        cadena += "                                              E.g.   ls\n"
        cadena += "    ----------------------------------------------------------------------------------------------------"
        active.sendall(cadena.encode())
    elif recibido.decode() == "clear":
        cadena  = "\n    ----------------------------------------------------------------------------------------------------"  
        cadena += "              clear: Limpia la terminal después de haberla usado, e incluso si esta no esta en uso.\n"
        cadena += "                                            E.g.   clear\n"
        cadena += "           Elimina el cache temporal y limpia la terminal si es que existe algo que limpiar.\n"
        cadena += "    ----------------------------------------------------------------------------------------------------"
        active.sendall(cadena.encode())
    elif recibido.decode() == "cd":
        cadena  = "\n    ----------------------------------------------------------------------------------------------------"  
        cadena += "              cd: Ingresa por directorios.\n"
        cadena += "                                 E.g.   cd Document/CC/RdC/Práctica10\n"
        cadena += "           Ingresa de manera explícita desde el directorio en el que te encuentras.\n"
        cadena += "    ----------------------------------------------------------------------------------------------------"
        active.sendall(cadena.encode())
    elif recibido.decode() == "tree":
        cadena  = "\n    ----------------------------------------------------------------------------------------------------"  
        cadena += "              tree: Nos regresa el árbol que representa la estructura del directorio.\n"
        cadena += "                                 E.g.   tree Docs  o tree\n"
        cadena += "           Desglosa la estructura del directorio tree o del directorio en dónde lo invoquen.\n"
        cadena += "    ----------------------------------------------------------------------------------------------------"
        active.sendall(cadena.encode())
    elif recibido.decode() == "touch":
        cadena  = "\n    ----------------------------------------------------------------------------------------------------"  
        cadena += "              touch: comando usado para crear archivos desde su terminal y con extensión.\n"
        cadena += "                                 E.g.   mkdir Practica.tex\n"
        cadena += "           Crea un archivo llamado Practico, esto se encuentra en el directorio en el que se invoque.\n"
        cadena += "    ----------------------------------------------------------------------------------------------------"
        active.sendall(cadena.encode())
    elif recibido.decode().lower() == "inicio":
        print("    -> Cliente: ", recibido.decode())
        bienvenida = "Hola, bienvenido al servidor del Equipo 04."
        active.sendall(bienvenida.encode())
    else:
        if recibido.decode().lower() != 'exit':
            c = "Comando no reconocido ..."
            active.sendall(c.encode())


    #enviar = input(" Server: ")
    #active.sendall(enviar.encode())

active.close()
server.close()
