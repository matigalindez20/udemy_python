mi_bool = 100.0 == 100
mi_bool = 100.0 != 100
mi_bool = 100.0 == 50+50
mi_bool = 6 >= 5+1
mi_bool = "blanco" == "Blanco".lower()
mi_bool = 100.0 == "100"
#print(mi_bool)

habla_ingles = True
sabe_python = False


if habla_ingles and not sabe_python:
    print("Cumples con los requisitos para postularte")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
elif not habla_ingles and sabe_python:
    print("Para postularte, necesitas tener conocimientos de inglés")
else:
    print("Para postularte, necesitas saber programar en Python")


