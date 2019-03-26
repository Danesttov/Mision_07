#Autor: Daniela Estrella Tovar
# Ejecutar la opción que el usuario ingrese

def dividir(dividendo,divisor):
    numBase = dividendo  # Dividendo tecleado por el usuario
    cociente = 0  # Calcula cuantas veces cabe el divisor dentro del número

    while dividendo >= divisor:
        dividendo = dividendo - divisor
        cociente += 1

    print(numBase, "/", divisor, "=", cociente, "y sobran", dividendo)

def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor.")
    decision = 0
    numMa = 0

    while decision != -1:
        decision = int(input("Teclea el número[-1 para salir]."))
        if decision >= numMa:
            numMa= decision

    print("El número más grande es: ",numMa)

def main():
    print("""Misión 07. Ciclos While
Autor: Daniela Estrella Tovar
Matrícula: A01745753

1. Calcular Divisiones
2. Calcular el Mayor
3. Salir
""")
    opcion =10
    while opcion !=3:
        opcion =int(input("Teclea tu opción: "))
        if opcion==1:
            dividendo = int(input("Teclea el número que deseas dividir:"))
            divisor = int(input("Teclea el divisor"))
            dividir(dividendo, divisor)


        elif opcion==2:
            encontrarMayor()
        elif opcion<0 or opcion>3:
            print("""El número ingresado no es válido. 
Teclee un número válido Ó 0 para salir del programa""")

    print("Hasta luego")



main()
