from dataframe import DataFrame

df = DataFrame({
    "id": list(range(1, 31)),
    "nombre": [f"persona_{i}" for i in range(1, 31)],
    "edad": [20 + (i % 15) for i in range(30)],
    "activo": [i % 2 == 0 for i in range(30)],
    "puntaje": [
        round(50 + (i * 1.5) % 25, 1) if i not in (4, 11, 19, 25) else None
        for i in range(30)
    ]
})

print("*"*40)
#Verificar atributos:
print(df.height)
print(df.width)
print(df.shape)
print(df.columns)
print(df.schema)
print("*"*40)

#Seleccionar columnas:
print(df["edad"]) # Devuelve una Series

#Aplicar filtros sobre una o múltiples columnas:
print(df.filter(("edad", lambda e: e > 30)))
print(df.filter(("activo", lambda a: a), ("puntaje", lambda p: p > 60)))

#Seleccionar subconjunto de columnas:
print(df.select("nombre", "puntaje"))

#Ordenar filas según una columna:
print(df.sort("edad"))
print(df.sort("puntaje",descending=True))

#Combinar varios métodos: filtrar, seleccionar una columna y calcular una agregación:
print(df.filter(("activo", lambda a: a))["puntaje"].mean())

#Estandarizar el puntaje de las personas:
df["puntaje_z"] = (df["puntaje"] - df["puntaje"].mean()) / df["puntaje"].std()