from series import Series 

print("*"*5, "Crear una serie y verificar operaciones básicas de acceso y longitud", "*"*5)
s = Series([10, 20, 30, 40, 50], name = "valores")
print(s.head(3))
print(s.tail(2))
print(len(s))
print("*"*5, "Agregar y extender una serie, manteniendo el mismo tipo de datos", "*"*5)
s1 = Series([1, 2, 3])
s2 = Series([4, 5])
s1.append(6)
print(s1)
s1.extend(s2)
print(s1)

print("*"*5, "Filtra valores según una condición y obtener sus indices", "*"*5)
s = Series([10, 25, 50, 75, 90, 100])
print(s.filter(lambda x : x < 60))
print(s.where(lambda x: x % 25 == 0))

print("*"*5, "Detectar y reemplazar valores nulos", "*"*5)
s = Series([5,None, 15, None])
print(s.is_null())
print(s.is_not_null())
print(s.fill_null(1))
print(s)


print("*"*5, "Ordenar y obtener indices de ordenamiento", "*"*5)
s = Series([42, 7, 100, 3])
print(s.sort())
print(s.argsort())



print("*"*5, "Combinar filtrado y agregaciones", "*"*5)
s = Series([5, 10, 15, 20, 15, 30])
print(s.filter(lambda x : x >10).mean())
print(s.filter(lambda x : x >10).sum())

print("*"*5,"Iterar a través de la serie", "*"*5)
for x in Series(list("xyz")):
    print(x)

print("*"*5, "Determinar si la serie contiene un valor", "*"*5)
s = Series(["a", "a", "a", None, "z"])
print("a" in s)

