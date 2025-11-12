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
        self.len = len(self.lista)

    def chequeo_mismo_tipo(self, lista):
        
        tipos_datos = ['int', 'float', 'str', 'bool']
        mismo_tipo = False
        primer_tipo = type(lista[0]) #Guardo el tipo de dato del primer valor de la lista

        for i in lista:
            if type(i) != primer_tipo:
                mismo_tipo = False
                raise "No podemos inicializar la Serie, por ser objetos de diferentes tipos"
        else:
            mismo_tipo = True
         

    def chequeo_dtype(self, lista, dtype):

        tipos_datos = {'int': int,
                       'float' : float,
                        'str': str,
                        'bool': bool}
        

        #Caso usuario, no pasa dtype explicito, toma el type del primer valor de la lista, ya esta validada que son todas del mismo tipo de datos
        if dtype is None:
                tipo_primer_elemento = type(lista[0])
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


a = Series([True, True], dtype= 'bool')        

print("*"*40)
print("*"*15, "Ejemplo 1", "*"*14)
print("*"*40)
serie = Series([1,2,3,4])
print(serie)


print("*"*40)
print("*"*15, "Serie nombrada", "*"*14)
print("*"*40)
serie = Series([1.0, 2.0, 3.0], name = 'x')
print(serie)

print("*"*40)
print("*"*10, "Serie nombrada y tipo explicito", "*"*14)
print("*"*40)
serie = Series([1.4, 2.5, 2.5], name = 'cantidad', dtype= 'float')
print(serie)