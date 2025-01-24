carro = {
          "marca": "Mazda",
          "modelo":"626",
          "anio":"2001"
        }
        
print(type(carro)) #<class 'dict'>
print(carro) #{'marca': 'Mazda', 'modelo': '626', 'anio': '2001'}
print(carro.keys()) #dict_keys(['marca', 'modelo', 'anio'])
print(carro.values()) #dict_values(['Mazda', '626', '2001'])
print(carro.items()) #dict_items([('marca', 'Mazda'), ('modelo', '626'), ('anio', '2001')])
print(carro.get("modelo")) #626

carro.pop("modelo")
print(carro) #{'marca': 'Mazda', 'anio': '2001'}

dicccionario = dict(nombre="Alfonso",apellido="Cantillo")
print(dicccionario) #{'nombre': 'Alfonso', 'apellido': 'Cantillo'}