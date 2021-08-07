from io import open
from carro import Carro
from pista import Pista
import time
import random
import os


def portada():
    print("--------------------------------------------")
    print("           BIENVENIDO A LAS CARRERAS")
    print("--------------------------------------------")
    print()
    print("               eligeun pista")
    print()
    print("             1. Rally Montecarlo")
    print("             2. Rally Dakar")
    print("             3. Super GT")
    print()
    opcion=""
    while opcion not in ("1","2","3"):
        opcion=input("   -->")
    return opcion

os.system("cls")

opcion = portada()

if opcion == "1":
    pista = Pista("Rally Montecarlo", 8, 60, "-")
elif opcion=="2":
    pista = Pista("Rally Dakar", 10, 65, ".")
elif opcion=="3":
    pista = Pista("Super GT",6,80,"_")
    
nombres=["r","s","t","p","n","k","w","y","f","z"]
carros=[]
for i in range(pista.filas):
    carro=Carro(nombres[i])
    carros.append(carro)

for i in range(pista.filas):
    pista.poner_carro(carros[i],i,carros[i].metro)

os.system("cls")

pista.mostrar()

print()
print("los pilotos que participan hoy son ", end=" ")
for carro in carros:
    print(carro, end=" ")
print()
input("elige el piloto y pulsa 'Enter' ...")

while True:
    os.system("cls")
    carros_ganadores=[]
    
    for carro in carros:
        if carro.metro > pista.metros -20:
            carros_ganadores.append(carro)
        
    if len(carros_ganadores)>3:
        break

    for i in range(pista.filas):
        pista.poner_carro(pista.ornamento,i,carros[i].metro)

    for i in range(pista.filas):
        carros[i].avanzar()
        pista.poner_carro(carros[i],i,carros[i].metro)

    pista.mostrar()
    time.sleep(1)
    
pista.mostrar()
print("ganador primer puesto: ", end=" ")
print(carros_ganadores[0])

print("ganador segundo puesto: ", end=" ")

print(carros_ganadores[1])
print("ganador tercero puesto: ", end=" ")

print(carros_ganadores[2]) 
print()
archivo_texto=open("archivo.txt","w")
archivo_texto.write("ganador primer puesto: "+str(carros_ganadores[0])+"\n")
archivo_texto.write("ganador segundo puesto: "+str(carros_ganadores[1])+"\n")
archivo_texto.write("ganador tercer puesto: "+str(carros_ganadores[2])+"\n")
archivo_texto.close()

