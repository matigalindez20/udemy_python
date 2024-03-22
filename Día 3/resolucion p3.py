texto = input("Intruduce un texto a elección: ")
texto = texto.lower()

letras = []

letras.append(input("Intruce la primera letra: ").lower())
letras.append(input("Intruce la segunda letra: ").lower())
letras.append(input("Intruce la tercera letra: ").lower())

print("\n")
print("CANTIDAD DE LETRAS")
cantidad_letras1 = letras.count(letras[0])
cantidad_letras2 = letras.count(letras[1])
cantidad_letras3 = letras.count(letras[2])

print(f"""
Hemos encontrado la letra '{letras[0]}' repetida {cantidad_letras1} veces en el texo
Hemos encontrado la letra '{letras[1]}' repetida {cantidad_letras2} veces en el texo
Hemos encontrado la letra '{letras[2]}' repetida {cantidad_letras3} veces en el texo
""")

print("CANTIDAD DE PALABRAS DEL TEXTO")
separar_texto = texto.split()
texto_separado = len(separar_texto)
print(f"El texto contiene una cantidad de '{texto_separado} palabras'")

print("\n")
print("Iniciales del texto ->")
print(f"La primera letra del texto es '{texto[0].upper()}'")
print(f"La letra con la que finaliza el texto es '{texto[-1].upper()}'")

print("\n")
print("TEXTO INVERTIDO")
reversa = separar_texto[::-1]
reversa = " ".join(reversa)
print(f"El texto invertido quedaría de la siguiente forma: '{reversa}'")

print("\n")
print("BUSCANDO LA PALABRA PYHTON")
