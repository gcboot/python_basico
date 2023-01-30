# Variables

# ? Regla general:

# Usar nombres para variables (Ejemplo article)
# Usar verbos para funciones (Ejemplo get_article)
# Usar adjetivos para booleanos (Ejemplo available)

# ? Asignación

# nombre = valor
 
total_population = 157503
print(total_population)

avg_temperature = 16.8
print(avg_temperature)

city_name = 'Guatemala'
print(city_name)

type_boolean = True

# Constantes
SOUND_SPEED = 343.2
print(SOUND_SPEED)

WATER_DENSITY = 997
print(WATER_DENSITY)

EARTH_NAME = 'La tierra'
print(EARTH_NAME)

PI = 3.1415
print(PI)

# Asignación multiple

# tres = three = drei = 3

# Asignando una variable a otra variable

people = 15703
total_population = people
print(total_population)

# Conocer tipo de variable
print(type(total_population))
print(type(avg_temperature))
print(type(EARTH_NAME))
print(type(type_boolean))

# Mutabilidad

# ? Si realizamos la asignación de una variable a un valor lo que está ocurriendo es que el nombre de la variable es una referencia al valor, no al valor en sí mismo.

# ? Función id() permite conocer la direccíon en memoria de un objeto en python
a = 5
print(a)
print(id(a))

# Si ahora le colocamos el valor de a en otra variable b se podría esperar que hubiera otro espacio en memoria para dicho valor, pero como se ha dicho, son referencias en memoria

b = a
print(b)
print(id(b))

# Se puede comprobar que los dos objetos apuntan a la misma zona de memoria

# Objetos mutables e inmutables
# * Inmutable -  Mutable
#   bool      -  list
#   int       -  set
#   float     -  dict
#   str       - 
#   tuple 

# El hecho de que un tipo de dato sea inmutable, no significa que no podemos modificar su valor.



