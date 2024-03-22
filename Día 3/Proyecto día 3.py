pregunta = input("Ingresa un texto cualquiera que desees analizar: ")
pregunta_letras = input("Ahora bien, ingrese tres letras a su elección: ")
pregunta_letras = list(pregunta_letras)

listas_palabras = pregunta.split()
total_palabras = len(listas_palabras)
reversa = listas_palabras[::-1]
reversa = " ".join(reversa)


primera = pregunta.lower().count(pregunta_letras[0].lower())
segunda = pregunta.lower().count(pregunta_letras[1].lower())
tercera = pregunta.lower().count(pregunta_letras[2].lower())

print(f"""
La letras:{pregunta_letras[0]} se repite {primera} veces
La letras:{pregunta_letras[1]} se repite {segunda} veces
La letras:{pregunta_letras[2]} se repite {tercera} veces
Este texto tiene un total de {total_palabras} palabras
La primera letra del texto es: {pregunta[0]} y la última es {pregunta[-1]}
El texto que usted escribió de forma inversa quedaría así: {reversa}
""")

find_python = "python"

if find_python in pregunta.lower():
    print("contiene la palabra Python")
else:
    print("no contiene la palabra Python")


