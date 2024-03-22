cliente = {'nombre':'Matias','apellido':'Galindez','peso':'76Kg'}
consulta = cliente['apellido']
#print(consulta)

dic = {'c1':['a','b','c'],'c2':['d','e','f']}
resultado = dic['c2'][1].upper()
#print(resultado)

agregar = {1:'a',2:'b'}
#print(agregar)
agregar[3] = 'c'
#print(agregar)
agregar[2] = 'B'
#print(agregar)
#print(agregar.keys()) #trae todas las claves del diccionario
#print(agregar.values()) #trae todos los valores
#print(agregar.items()) # trae todo -> tuples

mi_dict = {'valores_1':{'v1':3,'v2':6},'puntos':{'points1':9,'points2':[10,300,15]}}
#print(mi_dict['puntos']['points2'][1])

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['apellido'] = "Jurgens"
mi_dic['edad'] = 36
mi_dic['ocupacion'] = "Editora"
mi_dic['pais'] = "Colombia"
print(mi_dic)