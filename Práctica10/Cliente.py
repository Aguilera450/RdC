'''
             ---->  Equipo 4:<
Adrián Aguilera Moreno         Num.C:421005200
Francisco Contreras Ibarra     Num.C: 316083786
Aldo Daniel Licona Gómez       Num.C: 316263863
'''

import socket

# Crear un socket TCP (STREAM)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto al que se desea conectar
host = "localhost"  #host = "LocalHost"  # Puede ser una dirección IP o un nombre de dominio
port = 5656         # Puerto al que desea conectarse

# Conectar al dispositivo remoto
sock.connect((host, port))

ok = "inicio"
sock.sendall(ok.encode())
#bienvenida = "Conexión válida con "
#bienvenida += host
#sock.sendall(bienvenida.encode())
respuesta = sock.recv(1024)
print("    -> Servidor:", respuesta.decode())

try:
    while True:
        # Esperar a que el usuario ingrese un mensaje para enviar
        mensaje_enviar = input(" Cliente: ")
        
        # Enviar el mensaje al servidor
        sock.sendall(mensaje_enviar.encode())
        
        if mensaje_enviar.lower() == 'exit':  # Salir del bucle si el comando es 'exit'
            print(" Servidor fuera de línea ...")
            break 
        
        # Recibir la respuesta del servidor
        respuesta = sock.recv(1024)  # Tamaño del búfer
        
        # Decodificar y mostrar la respuesta
        print("    -> Servidor:", respuesta.decode())
        
except KeyboardInterrupt:
        print("Cliente desconectado.")

sock.close() # Cerrar el socket cuando termine la comunicación
