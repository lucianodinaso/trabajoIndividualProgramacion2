# El objetivo de este trabajo es implementar de forma básica las clases Series y DataFrame,
#  con el fin de profundizar en la programación orientada a objetos y en el uso de Python 
# como lenguaje de desarrollo. Además, busca comprender el funcionamiento interno de las 
# estructuras de datos tabulares y los principios de diseño que las hacen posibles.

class Series():

    def __init__(self, lista ,name="''", dtype= None):
        self.chequeo_mismo_tipo(lista)
        self.lista = lista
        self.dtype, self.dtypeString = self.chequeo_dtype(lista , dtype)
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
                return tipo_primer_elemento, dtype_string
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


                return funcion_reconversion, dtype
            
    def __repr__(self):
        elementos = [str(self.lista[i]) for i in range(self.len)]
        return f" Series: {self.name} \n len: {self.len} \n dtype: {self.dtypeString} \n [ \n {'\n '  .join(elementos) } \n] "
    
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
    
    def fill_null(self, x):

        if type(x) == self.dtype:

            for indice, v in enumerate(self.lista):
                if v is None:
                    self.lista[indice] = x

        else:
            raise TypeError('No se puede completar la Serie con diferentes tipos de datos')



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
    
    def chequeo_serie_nuemrica(self):

        if self.dtypeString not in ['int', 'float']:
            raise TypeError('La función requiere valores númericos')
        else:
            return True
        
    def get_lista_numerica(self):
        listaSinNone = [x  for x in self.lista if x is not None]
        
        return listaSinNone
    

    def min(self):
        self.chequeo_serie_nuemrica()
        return min(self.get_lista_numerica())

    def max(self):
        self.chequeo_serie_nuemrica()
        return max(self.get_lista_numerica())

    def sum(self):
        self.chequeo_serie_nuemrica()
        return sum(self.get_lista_numerica())
    
    def mean(self):
        self.chequeo_serie_nuemrica()
        lenListaSinNone = len([x  for x in self.lista if x is not None])
        return sum(self.get_lista_numerica()) / lenListaSinNone

    
    def product(self):
        self.chequeo_serie_nuemrica()
        resultado = 1

        for i in self.get_lista_numerica():
            resultado *= i

        return resultado
    
    def var(self):
        self.chequeo_serie_nuemrica()
        listaNumerica = self.get_lista_numerica()
        lenListaSinNone = len(listaNumerica)
        media = self.mean()
        resultado = 0


        for i in listaNumerica:
            resultado += (i - media) ** 2

        return resultado / lenListaSinNone
    
    def std(self):
        return self.var()**0.5




s1 = Series([1, 4, 5, 2, 10, 6, 3, 7, 8, 9])
s2 = Series([True, True, False, True])

print(s1.min()) # 1
#print(s2.min())     
print(s1.max())      # 10
#print(s2.max()) 
print(s1.sum())     # 55
print(s1.mean())     # 5.5
print(s1.product()) # 3628800
print(s1.std())     # 2.87228
print(s1.var())     # 8.25