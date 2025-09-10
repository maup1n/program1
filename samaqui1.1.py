#parte 1(cadenas)
pal=input("ingrese una palabra por favor: ")
print(f"la palabra en minuscula: {pal.lower()}")
print(f"la palabra en mayuscula: {pal.upper()}")
print(f"la palabra con la primera letra mayuscula:{pal.title() }")

#parte 1.2
frase = input("Ingresá una frase: ")
palabras = frase.split()
cantidad = len(palabras)
print(f"La frase tiene {cantidad} palabras.")

#parte 1.3
palabra = input("Ingresá una palabra: ")
for vocal in "aeiouAEIOU":
    palabra = palabra.replace(vocal, "*")
print("La palabra con vocales reemplazadas es:", palabra)
