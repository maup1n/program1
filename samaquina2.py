#parte 2(list)
#1
num=[]
for i in range (5):
 while True:
  numeros=(input("ingrese 5 numeros en su lista "))
  try:
   numeros=int(numeros)
   num.append(numeros)
   break
  
  except ValueError:
    print("ingrese un numero valido")
print(f"la lista completa es {num}")
print(f"el numero mayor de la lista es : {max(num)}")
print(f"el menor numero  de la lista es : {min(num)}")

#2
fruta=["pera", "banana","manzana"]
fruta.remove("banana")
fruta.append("uva")
print(f"la lista resultante es: {fruta}")

#3
numero=[1,2,3,4,5,6,7]
inv=numero[::-1]
print(f"la lista invertiuda:{inv}")