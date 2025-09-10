#3 lista anidadas(matfrices)
matriz=[]
for i in range(2):
    fila=[]
    for j in range (2):
        num=int(input(f"ingrese los numeros {i+1}, {j+1}: "))
        fila.append(num)
    matriz.append(fila)

print("matriz 2x2")
for fila in matriz :
    for elemnetos in fila:
        print(elemnetos , end= "    ")
    print()

# 3.2
# Definir la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz 3x3:")
for fila in matriz:
    for elemento in fila:
        print(elemento, end="  ")
    print()
suma=0
for fila in matriz:
    for elemento in fila:
        suma=suma+elemento

print("\nLa suma de todos los elementos es:", suma)

    
    