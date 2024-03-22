my_list = ["a", "b", "c"]
my_list2 = ["d", "f", "g"]
#print(type(my_list))
#print(len(my_list))
resultado = my_list[0:2]
#print(resultado)

my_list3 = my_list + my_list2

my_list3[0] = "z" #cambiar el contendio del indice 0 y remplaza por el de comillas

my_list3.append("agregando") #agregar elemento al último
my_list3.pop(0) # cuando esta vacío elimina el último elemento
print(my_list3)


lista = ["f", "m", "v", "a"]
lista.sort() #no se puede asignar a una variable el la lista ordenada -> si lo haces devuelte un nonetype
# Se puede hacer lo siguiente ->
lista2 = lista
print(lista)
print(lista2)
lista2.reverse()
print(lista2)

#metodo join para unir con espacios las listas ->

prueba =["primera","palabra","muchas"]
final = " ".join(prueba)
print(final)