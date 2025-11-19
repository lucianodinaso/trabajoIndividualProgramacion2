# El objetivo de este trabajo es implementar de forma básica las clases Series y DataFrame,
#  con el fin de profundizar en la programación orientada a objetos y en el uso de Python 
# como lenguaje de desarrollo. Además, busca comprender el funcionamiento interno de las 
# estructuras de datos tabulares y los principios de diseño que las hacen posibles.

class Series():
    """
    Clase que representa una Serie de datos, acepta cualquier tipo de datos,
    pero todos deben ser del mismo tipo.
    """

    def __init__(self, lista ,name="''", dtype= None):
        self.lista = lista
        self.dtype = dtype
        self.name = name
        self.len = self.__len__()

        #No se admite, Serie con todos los elementos None. 
        self.caso_no_admitido(lista)

        #dtype del usuario, define el tipo de Serie.
        if dtype is not None:
            self.lista = self.conversion_lista(lista, dtype)
        #dtype = None, se infiere el tipo de Serie
        else:
            self.lista = self.validacion_mismo_tipo(lista)

    # CASO - NO ADMITE: Todos los elementos None   
    def caso_no_admitido(self, lista):
        listaSinNone = [x  for x in lista if x is not None]
        if listaSinNone == []:
             raise TypeError("No podemos inicializar la Serie, no se admiten todos los valores None")
        

    # CASO 1: dtype especificado por el usuario
    def conversion_lista(self, lista, dtype): 
         
        if dtype == 'str':
            lista = [str(x) if x is not None else None for x in lista]
            self.dtype = 'str'
        elif dtype == 'float':
            lista = [float(x) if x is not None else None for x in lista]
            self.dtype = 'float'        
        elif dtype == 'int':
            lista = [int(x) if x is not None else None for x in lista]
            self.dtype = 'int'        
        elif dtype == 'bool':
            lista = [bool(x) if x is not None else None for x in lista]
            self.dtype = 'bool'  
        
        return lista


    # CASO 2: dtype = None, se infiere el tipo.
    def validacion_mismo_tipo(self, lista):    

        listaSinNone = [x  for x in lista if x is not None]
        #El primer dato not None, se utiliza para comparar
        primer_tipo = type(listaSinNone[0]) 
        
       
        for i in listaSinNone:
            #CASO: No admite inicializacion, si hay elementos de difirente tipo
            if type(i) != primer_tipo:
                raise TypeError("No podemos inicializar la Serie, por ser objetos de diferentes tipos")
            else:
                self.dtype = primer_tipo.__name__
                return lista     


    def __repr__(self):
        elementos = [str(self.lista[i]) for i in range(self.len)]
        return f" Series: '{self.name}' \n len: {self.len} \n dtype: {self.dtype} \n [ \n {'\n '  .join(elementos) } \n] "
    
    def __len__(self):
        return len(self.lista)
    
    def __iter__(self):
        return iter(self.lista)

    #Metodos
    def head(self, n=5):
        elementos = [str(self.lista[i]) for i in range(n)]
        return f" Series: '{self.name}' \n len: {n} \n dtype: {self.dtypeString} \n [ \n {'\n '  .join(elementos) } \n] "


    def tail(self, n=5):
        elementos = [str(i) for i in self.lista[:-n-1:-1]] #Start = último valor de la lista, stop : n -1, n no lo incluye el slicing, Step: -1 reversa
        return f" Series: '{self.name}' \n len: {n} \n dtype: {self.dtypeString} \n [ \n {'\n '  .join(elementos) } \n] "

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



