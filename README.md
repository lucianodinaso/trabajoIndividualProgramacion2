TRABAJO FINAL - PROGRAMACION 2 - CARRERA CIENCIAD DE DATOS - UNR
El objetivo de este trabajo es implementar de forma básica las clases Series y DataFrame,
 con el fin de profundizar en la programación orientada a objetos y en el uso de Python 
como lenguaje de desarrollo. Además, busca comprender el funcionamiento interno de las 
estructuras de datos tabulares y los principios de diseño que las hacen posibles.

2 Clase Series
Una Series representa una estructura unidimensional de datos, similar a un vector o una columna. En nuestro caso, soportan cuatro tipos de datos: numéricos enteros (int), numéricos flotantes (float), texto (str) y booleanos (bool). Las series pueden también incluir valores nulos, representados por None.

2.1 Inicialización
Para inicializar una Series se necesita una secuencia de valores del mismo tipo. Opcionalmente, se pasan valores para los argumentos name y dtype. El primero le asigna un nombre a la serie y el segundo un tipo de dato. El nombre de la serie es una cadena de texto y el tipo puede ser "int", "float", "str" o "bool".

2.2 Atributos
Los objetos de la clase Series tienen los siguientes atributos públicos:

Método	Descripción
dtype	Tipo de dato ("int", "float", "str", "bool")
name	El nombre de la serie
len	La longitud de la serie

2.3 Métodos para manipular de datos
La clase Series disponibiliza los siguientes métodos para la manipulación de datos:

Método	Descripción
clone(self)	Devuelve una nueva serie, idéntica a la original.
head(self, n=5)	Devuelve una nueva serie con los primeros n valores.
tail(self, n=5)	Devuelve una nueva serie con los últimos n valores.
append(self, x)	Agrega el elemento x al final de la serie.
extend(self, s)	Extiende la serie con los elementos de la serie s.
filter(self, f)	Devuelve una nueva serie con los elementos de la serie que al ser pasados a f devuelven un valor verdadero. Por ejemplo, serie.filter(lambda x: x > 5) devuelve una serie con los valores que son mayores a 5.
where(self, f)	Devuelve una nueva lista con los índices de los elementos que al ser pasados a f devuelven True
is_null(self)	Devuelve una serie de valores booleanos.
Cada elemento será True si el elemento original es nulo.
is_not_null(self)	Devuelve una serie de valores booleanos.
Cada elemento será True si el original es no nulo.
fill_null(self, x)	Reemplaza los valores nulos por x.
rename(self, name)	Cambia el nombre de la serie por name.
sort(self, ...)	Ordena la serie. El parámetro descending determina si se ordena de forma ascendente (por defecto) o descendente. y el parámetro in_place determina si se modifica la serie in-place o si se devuelve una nueva (por defecto).
argsort(self, ...)	Devuelve una lista con los índices que ordenan a la serie. El parámetro descending determina si se ordena de forma ascendente (por defecto) o descendente.

2.4 Métodos para calcular agregaciones
Los siguientes métodos obtienen un valor a partir de todos los valores de la serie. En todos los casos se ignoran los valores nulos. Solo se pueden aplicar a series numéricas.

Método	Descripción
min(self)	El valor más pequeño.
max(self)	El valor más grande.
sum(self)	La suma de los elementos.
mean(self)	El promedio de los elementos.
product(self)	El producto de los elementos.
std(self)	El desvío estándar.
var(self)	La varianza.

2.5 Métodos especiales
Aritméticos
Estos operadores solo se pueden utilizar con series de tipo numérico. Si other es un número, se recicla para todos los elementos de la serie. Por ejemplo:

s = Series([5, 6, 7])
s * 3.0
# Series: ''
# len: 3
# dtype: float
# [
#     15.0
#     18.0
#     21.0
# ]

Si other es otra Series, deben tener la misma longitud y la operación se hace elemento a elemento. Por ejemplo:

s1 = Series([10, 20, 30])
s2 = Series([5, 25, 28])
s1 > s2
# Series: ''
# len: 3
# dtype: bool
# [
#     True
#     False
#     True
# ]

Los métodos a implementar se resumen en la siguiente tabla:

Método	Descripción
__eq__(self, other)	Igual a
__gt__(self, other)	Mayor que
__ge__(self, other)	Mayor o igual que
__lt__(self, other)	Menor que
__le__(self, other)	Menor o igual que
__add__(self, other)	Suma
__sub__(self, other)	Resta
__mul__(self, other)	Multiplicación
__truediv__(self, other)	División flotante
__pow__(self, other)	Potencia
