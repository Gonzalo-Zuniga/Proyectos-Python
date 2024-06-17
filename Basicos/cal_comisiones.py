"""Condiciones del trabajo: los vendedores reciben un 13% por sus ventas totales,el programa debe contener y consultar nombre del vendedor
cuanto han vendido, como respuesta el usuario debe verificar por pantalla las comisiones que le correspondan"""
import time

"""obtencion del 13%"""
porcentaje= 13/100 


nombre = input("Cual es Tu nombre?\n")
print (f"Bienvenido {nombre}: \n Para Comenzar necesitamos unos datos..")
time.sleep(1)
vendido = input(f"{nombre} cuanto has vendido este mes?\n")
print("Comenzamos a calcular por favor espere... ")
time.sleep(2)

comision = int(vendido) * porcentaje
round(comision,2)

print("Estamos listos...")
time.sleep(1)
print(f"{nombre}, la comision que te corresponde este mes es de: ${comision} pesos")
time.sleep(4)
print(f"Hasta pronto {nombre}, que tengas un buen dia")

"""Fin del programa"""


