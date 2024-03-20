mi_texto = "Esto es una prueba"
resultado = mi_texto[-1]
resultado = mi_texto.index("n")
resultado = mi_texto.index("prueba")
resultado = mi_texto.index("e",6,16) # indica desde que índice se va realizar la búsqueda y le podes incluir hasta donde
resultado = mi_texto.rindex("a") # me busca de derecha a izquierda
print(resultado)

palabra = "ordenador"
print(palabra[4])
print(palabra.rindex("o"))

