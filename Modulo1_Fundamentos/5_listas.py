#Definición de listas 1
frutas = ["Fresa","Papaya","Manzana","Pera","Piña","Melon"]
#Definición de listas 2, utilizando método constructor
marcas = list(("Mazda", "Renault", "Fiat"))

print(len(frutas))
print(type(frutas))
print(type(marcas))

#Mostrar varios elementos de una lista
print(frutas[1:3])

#Buscar un elemento en la lista
print("Manzana" in frutas)

#Metodos Asociados a las listas

#Adicionar
frutas.append("Naranja")
#Devuelve una copia de la lista
frutas2 = frutas.copy()
#Contar cantidad de elementos
print(frutas2.count("Naranja"))

#Extend
frutas3 =["Limon","Cereza"]
frutas.extend(frutas3)
print(frutas) #['Fresa', 'Papaya', 'Manzana', 'Pera', 'Piña', 'Melon', 'Naranja', 'Limon', 'Cereza']
#index
print(frutas.index("Piña")) #4

frutas.insert(1,"Guayaba")
print(frutas) #['Fresa', 'Guayaba', 'Papaya', 'Manzana', 'Pera', 'Piña', 'Melon', 'Naranja', 'Limon', 'Cereza']

#Elimina la ultima
frutas.pop()
print("1", frutas) #['Fresa', 'Guayaba', 'Papaya', 'Manzana', 'Pera', 'Piña', 'Melon', 'Naranja', 'Limon']

frutas.pop(2)
print(frutas) #['Fresa', 'Guayaba', 'Manzana', 'Pera', 'Piña', 'Melon', 'Naranja', 'Limon']

frutas.remove("Pera")
print(frutas) #['Fresa', 'Guayaba', 'Manzana', 'Piña', 'Melon', 'Naranja', 'Limon']

frutas.reverse()
print(frutas) #['Limon', 'Naranja', 'Melon', 'Piña', 'Manzana', 'Guayaba', 'Fresa']

frutas.sort()
print(frutas) #['Fresa', 'Guayaba', 'Limon', 'Manzana', 'Melon', 'Naranja', 'Piña']

#Recorrer la lista
for fruta in frutas:
  print(fruta)