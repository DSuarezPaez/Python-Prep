#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

a = 458  # asignamos un valor a la variable a
print(a)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))  # imprimimos el tipo de dato de la constante


# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(a))  # imprimimos el tipo de dato de la variable a


# 4) Crear una variable que contenga tu nombre

# In[2]:
# asignamos un valor a la variable nombre, en este caso una cadena de texto
nombre = 'Daniel Suarez'
print(nombre)
# 5) Crear una variable que contenga un número complejo

# In[3]:
var1 = 5j + 5  # asignamos valores con un numero imaginario para hacer del dato un dato de tipo complejo
print(var1)
# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:
print(type(var1))  # imprimimos el tipo de dato siendo este un numero complejo

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416  # asignamos a la variable pi, el valor de 3,1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:
vari1 = 'True'  # asignamos valor a la varieble vari1 con una cadena de texto 'True'
vari2 = True  # asignamos valor a la variable vari2 con un valor booleano True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:
print(type(vari1))  # imprimimos el tipo de dato para cada uno de los casos
print(type(vari2))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:
sumavar = 5 + 3.67  # en este caso se realiza una suma con un valor entero y otro decimal
print(sumavar)
# 11) Realizar una operación de suma de números complejos

# In[2]:

5j + 26j  # se realiza la suma de 2 numeros complejos
# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
5.68 + 2j  # se realiza la suma de un numero complejo y un numero real o con decimal

# 13) Realizar una operación de multiplicación

# In[5]:
5 * 5  # se realiza la operacion sencilla de una multiplicacion

# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:
pot = 2 ** 8  # se eleva a la potencia con doble asterisco en este caso la potencia 8 de 2
print(pot)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:
27 / 4  # se realiza la division sencilla del numero de la izquierda entre el numero de la derecha

# 16) De la división anterior solamente mostrar la parte entera

# In[9]:
27 // 4  # se realiza la division de los numero y devuelve un numero entero
# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:
27 % 4  # se realiza la division y devuelve el resto de la operacion

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
4 * 6 + 3
# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:


# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
'2' == 2

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:
print(int('2') == 2)
print('2' == str(2))

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:
"""a = float('3,8')"""
# no se puede convertir una cadena de texto (string) a un numero real (float).

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:
var = 3
var -= 1
print(var)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
1 << 2
"""El sistema de numeración binario utiliza sólo dos dígitos, el cero (0) y el uno (1).
En una cifra binaria, cada dígito tiene distinto valor dependiendo de la posición que ocupe. El valor 
de cada posición es el de una potencia de base 2, elevada a un exponente igual a la posición del dígito 
menos uno. Se puede observar que, tal y como ocurría con el sistema decimal, la base de la potencia 
coincide con la cantidad de dígitos utilizados (2) para representar los números.
"""

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:
"""2 + '2'"""
# esta operacion no se puede realizar porque los operadores son de distinti tipo.
# si los dos operadores fueran del mismo tipo se realizara la operacion sin errores.

# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:
v1 = 'hola, que tal? '
v2 = 4
print('repetire esta frase', v1 * v2, v2, 'veces')

# 27) Realizar una operación válida entre valores de tipo entero y string

# In[31]:
5 != 6
