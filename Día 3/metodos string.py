texto = "Voy a trabajar como programdor full stack"

frase = texto.upper() #texto[2] solo la v se pone en mayúscula
frase = texto.lower() #se hace en minúscula
frase = texto.split() #se separa entre corchetes, son listas
frase = texto.split("o") #separa teniendo en cuenta como punto de corte la letra o
print(frase)

a = "Aprender"
b = "python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])

frase = texto.find("j") # lo mismo que index pero si se busca un elemonto que no esta devuelve -1
print(frase)

frase = texto.replace("full stack","web") #reemplaza la porcion de texo que se detalla
frase = texto.replace("o","x")

print(frase)





