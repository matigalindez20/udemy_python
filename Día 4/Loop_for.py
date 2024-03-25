lista = ['a', 'b', 'c', 'd']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra {numero_letra} es la: {letra}")

lista_2 = ['matias', 'pablo', 'victoria', 'santiago', 'julia']

for nombre_2 in lista_2:
    if nombre_2.startswith('m'):
        print(nombre_2)


lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares + numero
    else:
        suma_impares + numero
