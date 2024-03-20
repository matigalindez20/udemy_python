texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10:2] #extraer del 2 a las hasta el 5 pero no lo incluye.
#texo[2:] -> interpreta que es del 2 al final y si es [:5] -> del principio al 5
#texto[2:10:2] -> ese ultimo 2 siginifica que va extraer uno y saltea otro
#texto[::3] -> del incio al final, salteandose de en 3 en 3
#texto[::-1] -> muestra de atras para delante
print(fragmento)