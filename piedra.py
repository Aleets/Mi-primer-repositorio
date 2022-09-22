#Scriot que juega Piedra papel y tijera con el Usuario
from platform import machine
import random
from re import U
#Leer eleccion del Usuario
user = input("Elege: Piedra, Papel y Tijera: ")
#Generar eleccion de la Maquina
aleatorio = random.randint(1,3)
if aleatorio == 1:
    machine = "piedra"
elif aleatorio == 2:
    machine = 'papel'
else:
    aleatorio = 'tijera'
#Comparar para determinar quien gana.
print(f"El usuario eligio {user} y la maquina eligio {machine}")
if user == "piedra" and machine == "tijera":
    print("gana el usuario")
elif user == "papel" and machine == "tijera":
    print("gana la maquina")
elif user == "tijera" and machine == "tijera":
    print("es un empate")
elif user == "piedra" and machine == 'papel':
    print("gana la maquina")
elif user == "papel" and machine == 'papel':
    print("es un empate")
elif user == "tijera" and machine == 'papel':
    print("gana el usuario")
elif user == "piedra" and machine == 'piedra':
   print("es un empate")
elif user == "papel" and machine == 'piedra':
    print("gana la maquina")
elif user == "tijera" and machine == 'piedra':
    print("gana la maquina")
else:
    print("Escribe corectamente tu eleccion")