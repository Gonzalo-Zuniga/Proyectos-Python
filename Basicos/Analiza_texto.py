"""Condiciones del trabajo: Crear programa que ingrese un texto a libre eleccion, debe pedir 3 letras de libre eleccion para realizar 
nuestro analisis con 5 tipos de analis, 1.cuantas veces aparece cada letra; 2.cuantas palabras hay en total dentro del texto, 
3.debe mostrar la primera y la ultima letra del texto; 4.Debe escribir las palabras en orden inverso; 
5. Debe buscar si la palabra 'Python'se encuentra en el texto"""
import time

texto = input("Ingresa un texto a elección: \n")
letras = []
time.sleep(1)
texto = texto.lower()

print("Ingrese Las letras que desea verificar su cantidad en el texto")
time.sleep(1)
letras.append(input("Ingresa la primera letra: \n".lower()))
letras.append(input("Ingresa la segunda letra: \n".lower()))
letras.append(input("Ingresa la tercera letra: \n".lower()))

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces")
time.sleep(1)
print("\n")
print("CANTIDAD DE PALABRAS")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras en tu texto")
time.sleep(1)
print("\n")
print("LETRAS DE INICIO Y DE FIN")
letra_inicio = texto[0]
letra_final = texto[-1]
print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")
time.sleep(1)
print("\n")
print("TEXTO INVERTIDO")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al revés va a decir: '{texto_invertido}'")
time.sleep(1)
print("\n")
print("BUSCANDO LA PALABRA PYTHON")
buscar_python = 'python' in texto
dic = {True:"sí", False:"no"}
print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
time.sleep(5)
print("Hasta Pronto..")

"""Fin del programa"""