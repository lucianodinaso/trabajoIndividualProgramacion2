from series import Series


class DataFrame:

    def __init__(self, data = None):
        self.data = data #Diccionario con los datos
        self.columns = list(data.keys()) #Lista de nombre de las columnas
        self.dtypes = [] #Lista con los tipos de datos por columna
        self.shape = (0, 0) #Tupla (filas, columnas)
        self.schema = {} #Diccionario que mapea las columnas a su tipo
        self.height = 0 #Cantidad de filas
        self. width = 0 #Cantidad de columnas

        if data is not None:
            self.validar_dic(data)
            self.validar_mismo_tipo(data)
            self.calcular_dimension()
            self.inferir_types()

    def validar_dic(self, data):
        '''
            Valida que el dato pasado por el usuario sea un diccionario,
            también que la cantidad de filas por columnas sean iguales.
        '''

        if not isinstance(data, dict):
            raise TypeError("Los datos deben ser un diccionario")
        
        #Validacion igual cantidad de filas por columas
        longitudes = [len(valores) for valores in data.values()]
        primer_elemento = longitudes[0]

        for i in longitudes:
            if i != primer_elemento:
                raise TypeError("Las columnas son de diferentes dimensiones")
    

    def validar_mismo_tipo(self, data):
        '''
        Valida que cada columna tenga elementos del mismo tipo
        y actualiza el atributo dtype con los tipos de cada columna
        '''

        self.dtypes = []
        

        for columna, valores in self.data.items():

            #Filtramos los valores None
            listaSinNone = [x  for x in valores if x is not None]
        
            #El primer dato not None, se utiliza para comparar
            primer_tipo = type(listaSinNone[0]) 

            for i in listaSinNone:
                #CASO: No admite inicializacion, si hay elementos de difirente tipo
                if type(i) != primer_tipo:
                    raise TypeError("No podemos inicializar la Serie, por ser objetos de diferentes tipos")
                
            self.dtypes.append(primer_tipo.__name__)
            self.schema.update({columna : primer_tipo.__name__})
                    
            


    def calcular_dimension(self):
        self.width = len(self.columns)
        #Obtengo el nombre de la primer columna
        primer_columna = self.columns[0] 
        lista_primer_columna = [x for x in self.data[primer_columna] ]
        self.height = len(lista_primer_columna)
        self.shape = (self.height, self.width)

    def inferir_types(self):
        
        for columna in self.columns:
            valores_columna = self.data[columna]
            
            serie_temp = Series(valores_columna)
            serie_temp.validacion_mismo_tipo(valores_columna)

        

    def __len__(self):
        return self.height

    def __repr__(self):

        #Encabezado
        header = " | ".join(self.columns)

        #Separador
        separador = "-"*len(header)

        #Filas
        filas = []

        for i in range(self.height):

            valores_filas_str = []

            for columna in self.columns:
                valor = self.data[columna][i]
                # .ljust Alinea cada valor al ancho de su columna
                valores_filas_str.append(str(valor).ljust(len(columna)))

            filas_str = " | ".join(valores_filas_str)
            filas.append(filas_str)


        
        tabla = "\n".join([separador, header , separador] + filas + [separador])

        return f" shape: {self.shape} \n {tabla}  "
    
      
    '''
    METODOS PARA MANIPULAR DATOS
    '''
    def head(self, n=5):
        '''
        Muestra las primeras n filas del DataFrame
        n=5 por defecto
        '''

        # Limita n al número máximo de filas disponibles
        n = min(n, self.height)

        
        #Encabezado
        header = " | ".join(self.columns)

        #Separador
        separador = "-"*len(header)

        #Filas
        filas = []
        height_temp = n

        for i in range(n):

            valores_filas_str = []

            for columna in self.columns:
                valor = self.data[columna][i]
                # .ljust Alinea cada valor al ancho de su columna
                valores_filas_str.append(str(valor).ljust(len(columna)))

            filas_str = " | ".join(valores_filas_str)
            filas.append(filas_str)


        
        tabla = "\n".join([separador, header , separador] + filas + [separador])

        return f" shape: ({height_temp}, {self.width}) \n {tabla}  "
    


    

    def tail(self, n=5):
        '''
        Muestra las últimas n filas del DataFrame
        n=5 por defecto
        '''

        # Limita n al número máximo de filas disponibles
        n = min(n, self.height)
        height_temp = n

        
        #Encabezado
        header = " | ".join(self.columns)

        #Separador
        separador = "-"*len(header)

        #Filas
        filas = []

        #Inicio 
        inicio = self.height - n

        for i in range(inicio, self.height):

            valores_filas_str = []

            for columna in self.columns:
                valor = self.data[columna][i]
                # .ljust Alinea cada valor al ancho de su columna
                valores_filas_str.append(str(valor).ljust(len(columna)))

            filas_str = " | ".join(valores_filas_str)
            filas.append(filas_str)


        
        tabla = "\n".join([separador, header , separador] + filas + [separador])

        return f" shape: ({height_temp}, {self.width}) \n {tabla}  "
    


    def select(self, *columns):
        '''
        Devuelve un nuevo DataFrame con solo las columnas indicadas
        '''

        columnas = list(columns)
        
        # Verificar que las columnas existen
        for columna in columnas:
            if columna not in self.data:
                raise TypeError("No existe la columna ingresada")


        temp_width = len(columnas)

        #Encabezado
        header = " | ".join(columnas)

        #Separador
        separador = "-"*len(header)

        #Filas
        filas = []

        for i in range(self.height):

            valores_filas_str = []

            for columna in columnas:
                valor = self.data[columna][i]
                # .ljust Alinea cada valor al ancho de su columna
                valores_filas_str.append(str(valor).ljust(len(columna)))

            filas_str = " | ".join(valores_filas_str)
            filas.append(filas_str)


        
        tabla = "\n".join([separador, header , separador] + filas + [separador])

        return f" shape: ({self.height}, {temp_width}) \n {tabla}  "
    

    def filter(self, *predicates):
        '''
        Filtra filas del DataFrame basado en múltiples condiciones
    
        Args:
             *predicates: Tuplas (columna, función):
                columna: nombre de la columna 
                función: función que recibe un valor y retorna bool
    
        Returns:
            Nuevo DataFrame con las filas que cumplen con las condiciones
 
        '''

    
        # Verificar que las columnas existen
        for condicion in predicates:
                columna, funcion = condicion
                if columna not in self.data:
                    raise TypeError("No existe la columna ingresada")


        # Identificar las filas que cumplen todas las condiciones
        nuevo_dataFrame_indices = []

        for indice_fila in range(self.height):
            cumple_condiciones = True

            #Verificamos que la fila pase las condiciones
            for columna, funcion in predicates:
                valor = self.data[columna][indice_fila]

                # Aplicar la función condición al valor
                if not funcion(valor):
                    # Si una condición falla, esta fila NO cumple
                    cumple_condiciones = False
                    break
            
            # Si la fila pasó todas las condiciones, guardar su índice
            if cumple_condiciones:
                nuevo_dataFrame_indices.append(indice_fila)

        # Retornar nuevo DataFrame con los datos filtrados
        nuevo_dataFrame = {}

        for columna in self.columns:
            nuevo_dataFrame [columna] = [
                self.data[columna][indice] for indice in nuevo_dataFrame_indices
            ]
        return DataFrame(nuevo_dataFrame)


#Sentencias de prueba
df = DataFrame({'x': [1, 2, 3, 4, 5, 6],
                'y': [10,20,30,40,50,60],
                'z': ["a","b","c","d","e","f"]})

#print(df)
# print(df.columns)
#print(df.dtypes)
# print(df.shape)
# print(df.height)
# print(df.width)
# print(df.dtypes)
#print(df.schema)

# print(df.head(1))
# print(df.tail(2))
#print(df.select('puesto'))
print(df.filter(
    ("x", lambda x: x % 2 != 0),
    ("y", lambda x: x > 30)
))
