# Define una variable de cada tipo de primitivo.


mi_Int = 1
# Int es una variable que se utiliza para representar valores númericos
# de tipo entero, ya sea positivos o negativos.

mi_Float = 3
# Float es una variable para representar valores númericos de tipo
# coma flotante o decimales.

mi_Str = "Hola"
# String es una variable para representar valores caracteres que forman cadenas
# para formar un mensaje o oración generalmente. 
# Se pueden crear usando comillas simples, dobles o triples. 

mi_Bool = True
# Es una variable que contiene tipos de datos binarios,
# es decir que pueden tomar los valores: Verdadero (True) y Falso (False). 
# Son útiles para expresiones con condicionales y de comparaciones.

mi_Complex = 3 + 5j
# Es una variable que se utiliza para representar números complejos. 
# Los números complejos tienen una parte real y una parte imaginaria, 
# y se pueden crear en Python sin tener que importar ninguna librería.
# Por ejemplo, para crear un número complejo con una parte real de 1 
# y una parte imaginaria de 2, se representaría como: miComplex = 1 + 2j


## Concatena a la cadena las otras variables aplicando la conversión correcta
# para funcionar, guarda el resultado en una variable.


mi_Int = 3
mi_Float = 4.5
mi_Str = " Hola "
mi_Bool = True
mi_Complex = 3 + 5j

vari_primitivas = str(mi_Int) + str(mi_Float) + mi_Str + str(mi_Bool) + str(mi_Complex)
print(vari_primitivas)

### Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos
# como comentarios en el archivo


# En Python, los enteros (int) tienen precisión ilimitada. Esto significa que
# puedes trabajar con números enteros tan grandes como lo permita la memoria 
# de tu computadora. En otras palabras, no hay un límite predefinido para el
# tamaño de un entero en Python.

# Por otro lado, los números de coma flotante (float) tienen una precisión 
# limitada. En la mayoría de las máquinas, los float se implementan usando
# el tipo double de C y tienen una precisión de alrededor de 15-17 dígitos
# decimales. La representación interna de los números en coma flotante puede 
# variar dependiendo de la máquina en la que se ejecuta tu programa. Puedes
# obtener más información sobre la precisión y la representación interna de
# los números en coma flotante en tu máquina consultando el objeto
# sys.float_info1.

# Importante tener en cuenta que, debido a la forma en que se representan
# los números en coma flotante en la memoria, pueden ocurrir errores de redondeo
# al realizar operaciones aritméticas con ellos. Por ejemplo, el resultado de sumar
# 0.1 y 0.2 puede no ser exactamente 0.3 debido a estos errores de redondeo.
# Si necesitas realizar cálculos con una precisión muy alta, puedes considerar usar
# la librería decimal, que proporciona soporte para aritmética decimal con precisión
# arbitraria.


#### Aplica la fórmula de la suma de los primeros n números pares (investigar),
# tomando como n la variable de tipo entero y almacenar el resultado en una variable.


# La fórmula para calcular la suma de los primeros n números pares es n * (n + 1)1.
# Esta fórmula se obtiene usando la suma de términos en una fórmula de progresión
# aritmética. 

n = 10
n_pares = n * (n + 1)
print(n_pares)




