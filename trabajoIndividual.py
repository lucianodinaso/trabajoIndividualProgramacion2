# El objetivo de este trabajo es implementar de forma básica las clases Series y DataFrame,
#  con el fin de profundizar en la programación orientada a objetos y en el uso de Python 
# como lenguaje de desarrollo. Además, busca comprender el funcionamiento interno de las 
# estructuras de datos tabulares y los principios de diseño que las hacen posibles.

class Series():

    def __init__(self, lista ,name="''", dtype= None):
        self.chequeo_mismo_tipo(lista)
        self.lista = lista
        self.dtype = self.chequeo_dtype(lista , dtype)
        self.name = name
        self.len = self.__len__()

    def chequeo_mismo_tipo(self, lista):
        
        tipos_datos = ['int', 'float', 'str', 'bool', 'None']

        listaSinNone = [x  for x in lista if x is not None]

        if listaSinNone == []:
            raise TypeError("No podemos inicializar la Serie, no contiene por lo menos un tipo de dato valido")
        for i in listaSinNone:
            primer_tipo = type(listaSinNone[0]) #Guardo el tipo de dato del primer valor de la lista
            if type(i) != primer_tipo:
                raise TypeError("No podemos inicializar la Serie, por ser objetos de diferentes tipos")
                

    def chequeo_dtype(self, lista, dtype):

        tipos_datos = {'int': int,
                       'float' : float,
                        'str': str,
                        'bool': bool}
        
        listaSinNone = [x  for x in lista if x is not None]

        #Caso usuario, no pasa dtype explicito, toma el type del primer valor de la lista filtrada sin None, ya esta validada que son todas del mismo tipo de datos
        if dtype is None:
                tipo_primer_elemento = type(listaSinNone[0])
                dtype_string = str(tipo_primer_elemento)

                for k, v in tipos_datos.items():
                    if tipo_primer_elemento == v:
                        dtype_string = k
                        break
                return dtype_string
        else:       

            if dtype in tipos_datos:

                funcion_reconversion = tipos_datos[dtype] #Tomando dtype que pasa el usuario, que es un string, lo mapeo a su tipo de dato        
                lista_reconvertida = []
        

                for i in lista:

                    if dtype == 'str':
                        conversion = " '" + funcion_reconversion(i) + "' "
                        lista_reconvertida.append(conversion)
                    else:    
                        conversion = funcion_reconversion(i)
                        lista_reconvertida.append(conversion)
                
                self.lista = lista_reconvertida


                return dtype
            
    def __repr__(self):
        elementos = [str(self.lista[i]) for i in range(self.len)]
        return f" Series: {self.name} \n len: {self.len} \n dtype: {self.dtype} \n [ \n {'\n '  .join(elementos) } \n] "
    
    def __len__(self):
        return len(self.lista)
    
    def __iter__(self):
        return iter(self.lista)

    #Metodos
    def head(self, n=5):
        elementos = [str(self.lista[i]) for i in range(n)]
        return f" Series: {self.name} \n len: {n} \n dtype: {self.dtype} \n [ \n {'\n '  .join(elementos) } \n] "

    def tail(self, n=5):
        elementos = [str(i) for i in self.lista[:-n-1:-1]] #Start = último valor de la lista, stop : n -1, n no lo incluye el slicing, Step: -1 reversa
        return f" Series: {self.name} \n len: {n} \n dtype: {self.dtype} \n [ \n {'\n '  .join(elementos) } \n] "

    def clone(self):
        #Creamos una nueva instancia de la clase Serie, con los datos de la lista
        listaClon = Series(self.lista.copy())
        return listaClon
    
    def append(self, x):
        self.lista.append(x) #utilizó el metodo build in
        self.len = len(self.lista) #actualiza la longitud de la lista 
        return self.lista

    def extend(self, s):

        for i in s.lista:
            self.lista.append(i)

        self.len = len(self.lista) #actualiza la longitud de la lista 

        return self

    def filter(self, f):
        nuevaSerie = []

        for i in self.lista:

            #Aplica la funcion de la llamada , a cada elemento.
            if f(i):
                nuevaSerie.append(i)

        return Series(nuevaSerie)
    
    def where(self, f):
       
        nuevaSerie = []

        for indice, i in enumerate(self.lista):

            #Aplica la funcion de la llamada , a cada elemento.
            if f(i):
                nuevaSerie.append(indice)

        return Series(nuevaSerie)    
        
    
    def is_null(self):
       
        nuevaSerie = []

        for i in self.lista:

            if i is None:
                nuevaSerie.append(True)
            else:
                nuevaSerie.append(False)

        return Series(nuevaSerie)    

    def is_not_null(self):
       
        nuevaSerie = []

        for i in self.lista:

            if i is None:
                nuevaSerie.append(False)
            else:
                nuevaSerie.append(True)

        return Series(nuevaSerie)    
    
    def rename(self, nombre):
        self.name = nombre
        return self
    
    def sort(self, descendig = False, in_place = False):

        nuevaSerie = []

        # Por defecto crea una nueva lista el metodo
        if in_place == False:
            
            if descendig == False:
                nuevaSerie = sorted(self.lista)
            else:
                nuevaSerie = sorted(self.lista , reverse= True)
            
            return Series(nuevaSerie)
        
        else:

            if descendig == False:
                self.lista.sort()
            else:
                self.lista.sort(reverse= True)

            return self
        
    def argsort(self, descendig =  False):

        serie_indice_valor = enumerate(self.lista)

        lista_indices_ordenados = sorted(serie_indice_valor, key = lambda x : x[1])
        lista_indices_finales = [indices for indices, i in lista_indices_ordenados]
        
        
        return lista_indices_finales


# ****************SENTENCIAS DE PRUEBA************************

# a = Series([True, True], dtype= 'bool')        

# print("*"*40)
# print("*"*15, "Ejemplo 1", "*"*14)
# print("*"*40)
# serie = Series([1,2,3,4])
# print(serie)


# print("*"*40)
# print("*"*15, "Serie nombrada", "*"*14)
# print("*"*40)
# serie = Series([1.0, 2.0, 3.0], name = 'x')
# print(serie)

# print("*"*40)
# print("*"*10, "Serie nombrada y tipo explicito", "*"*14)
# print("*"*40)
# seriePrueba = Series([1.1, 1.2, 1.3, 1.4, 1.5, 2.1,2.2,2.3,2.5,95.0,96.0,97.0,98.0,99.0], name = 'cantidad', dtype= 'float')
# print(seriePrueba)

# seriePrueba2 = Series([1,2,3,4,5,6,7,8,9,10])

# print("*"*60)
# print(seriePrueba2.head())


# print("*"*60)
# print(seriePrueba2.tail(3))

# seriePruebaClone = Series(list("ABCD"))
# print(seriePruebaClone)

# print("*"*30)
# print("LISTA CLONADA")
# listaClonada = seriePruebaClone.clone()
# print(listaClonada)

# listaClonada.append('E')
# listaClonada.append('F')
# print(listaClonada)

# print("*"*30)
# serie = Series([1,2,3,4,5,6,7,8,9])
# print(serie)
# print(serie.filter( lambda x: x > 5))

# s1 = Series([1,2,3])
# s2 = Series([4,5,6])
# print(s1.extend(s2))


# print("*"*30)
# serie = Series([1,2,3,4,5,6,7,8,9])
# print(serie)
# print(serie.filter( lambda x: x > 5))

# s = Series([1, 20, 50, 2, 100, 3])
# indices = s.where(lambda x : x < 20)

# print(indices)

# s = Series([1, 20, 50, 2, 100, 3])
# print(s.is_null())

# s2 = Series([None, None])
# print(s2.is_null())

# s3 = Series([1, 20, 50, 2, 100, 3])
# print(s3.is_not_null())

# s4 = Series([None, None])
# print(s4.is_not_null())

# serieA = Series([1,2,3,4,5], name = 'Primeros')
# print(serieA)

# serieA.rename('Segundos')
# print(serieA)

# s = Series([128.0, 256.0, 42.5, 35.0])
# print(s)

# print('*'*20, 'PRUEBA SORT - ORDEN ASCENDENTE POR DEFECTO')
# print(s.sort())
# print(s)


# print('*'*20, 'PRUEBA SORT + ORDEN DESCENDENTE')
# print(s.sort(descendig= True))
# print(s)

# print('*'*20, 'PRUEBA SORT - ORDEN ASCENDENTE POR DEFECTO + MODIFICA SERIE ORIGINAL')
# print(s.sort(in_place= True))
# print(s)

# print('*'*20, 'PRUEBA SORT - ORDEN DESCENDENTE + MODIFICA SERIE ORIGINAL')
# print(s.sort(descendig= True ,in_place= True))
# print(s)

# s = Series([128, 256, 42, 35])
# indices = s.argsort()
# print(indices)

#-----PRUEBA DE INICIALIZACION CON VALORES None-----

# #Lanzamiento de errores, la serie no admite solo None
# SerieNone = Series([None, None, None, None])
# print(SerieNone)

# #Lanzamiento de errores, la serie no se inicializa con datos de diferentes tipos.
# SerieDiferentesTipos = Series([2,3,5.6])
# print(SerieDiferentesTipos)