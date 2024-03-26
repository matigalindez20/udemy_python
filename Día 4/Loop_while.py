monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("Me quede sin monedas")


repsuesta = 's'

while repsuesta == 's':
    repsuesta = input("Quieres seguir s/n")
else:
    print("Gracias")



nombre = input("Tu nombre: ")
for palabra in nombre:
    if palabra == 'a':
       #break  # hace que se corte codigo donde se coloca el break
        continue # se salte la letra a y sigue con el codigo
    print(palabra)