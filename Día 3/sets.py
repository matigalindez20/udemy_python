primer_set = set([1,2,3,4])  # no se puede reasingar ni ver el orden, si se repiten los elementos los elimina python
#print(type(primer_set))

seg_set = {1,2,3,4,(10,1,1)} # tampoco se puede poner lista, diccionarios pero SI tuples
#print(2 in seg_set) # true o false
#print(len(seg_set))
#print(seg_set)
#print(type(seg_set))

s1 = {1,2,3}
s2 = {3,4,5}
s1.add(10)
s2.remove(4) # lo elimina pero si no esta DA error
s2.discard(15) # lo elimina pero si no esta NO DA error
s3 = s1.union(s2)
print(s3)
sorte = s3.pop()
print(sorte)
s3.clear() # vaciar el set, borra todos los elementos   
print(s3)


