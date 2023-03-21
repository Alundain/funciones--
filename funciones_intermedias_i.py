# I.- Actualizar valores en diccionarios y listas
#1.- cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 
#solución
x[1]
x[1][0]
x[1][0]=15

#2.-Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#Solución
estudiantes[0]
estudiantes[0]['last_name']="Bryant"

#3.-En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
#Solución
directorio_deportes['fútbol'][0] = ['Andrés']
#4.-Cambia el valor 20 en z a 30.
z = [ {'x': 10, 'y': 20} ]
#Solución
z[0]['y']=30


#II
"""Crea una función iterateDictionary(some_list)para 
que, dada una lista de diccionarios, la función 
recorra cada diccionarios de la lista e imprima cada 
llave y el valor asociado. Por ejemplo, dada la 
siguiente lista:"""
def iterateDictionary(some_list):
    for estudiantes in some_list:
        print(estudiantes)
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)
"""first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel"""

"""III Crea una función iterateDictionary2(key_name, some_list)
que, dada una lista de diccionarios y un nombre de 
clave, la función imprima el valor almacenado en 
esa clave para cada diccionario. Por ejemplo, 
iterateDictionary2('name', estudiantes) 
debería generar: Michael, Jordan, Marck, KB
Y iterateDictionary2('last_name', estudiantes) debería generar: Jordan, Rosales, Guillen,Tonel"""


"""IV Crea una función printInfo(some_dict)que, 
dado un diccionario cuyos valores son todos listas, 
imprima el nombre de cada clave junto con el tamaño 
de su lista, y luego imprima los valores asociados 
dentro de la lista de cada clave. Por ejemplo:
"""
"""
def printInfo(dicc):
    for llave, valores in dicc.items():
        num_valores = len(valores)
        print (f"{num_valores} {llave.upper()}")
        for valor in valores:
            print(valor)
        print('')


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)

# salida:
7 UBICACIONES
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORES
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""



