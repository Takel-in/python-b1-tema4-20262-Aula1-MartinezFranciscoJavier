"""
Enunciado:
Realizando la entrada por consola de los datos, implementa la función 'sum'
que solicite la entrada de dos números con 'input' y devuelva la suma de los
números.

Parámetro:
No recibe ningún parámetro debido a que dentro de la función se solicita la
entrada de los números.

Ejemplo:
    Entrada:
        "Insert the first number: " 8
        "Insert the second number: " 3

    Salida:
        "Result: " 11

Enunciat:
Realitzant l'entrada per consola de les dades, implementa la funció 'sum'
que sol·liciti l'entrada de dos números amb 'input' i torni la suma dels
números.

Paràmetre:5
No rep cap paràmetre pel fet que dins de la funció se sol·licita la
entrada dels números.

Exemple:
     Entrada:
         "Insert the first number: " 8
         "Insert the second number: " 3

     Sortida:
         "Result: " 11
"""

def sum():
    # Write here your code
    # Mientras no intoeduzca dos números
    while True:
        val1 = input("Introduce el primer número: ")
        val2 = input("Introduce el segundo número: ")

        # Comprobamos que los números sean int.
        # Si son realizamos la operación. En caso contrarios volvemos a solicitar los números.
        try:
            val1 = int(val1)
            val2 = int(val2)

            res = val1 + val2

            print ("Result: ", res)
            return val1 + val2
        except ValueError:
            print ("Unos de los valores no es numérico. vueve a probar")

    



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#sum()
