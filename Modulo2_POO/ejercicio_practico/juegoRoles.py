class Personaje:
  nivel = 1

  def __init__(self,nombre, daño, vida, defensa):
    self.nombre= nombre
    self.daño= daño
    self.vida= vida
    self.defensa= defensa

  def atributos(self):
    print(f"Atributos de {self.nombre}: \n- Daño: {self.daño}\n- Vida: {self.daño}\n- Defensa: {self.defensa}\n") 

  def esta_vivo(self):
    return self.vida > 0
  
  def morir(self):
    self.vida = 0;
    print(f"{self.nombre} ha muerto")

  def ataque(self,enemigo):
    return self.daño - enemigo.defesa
  
personaje1 = Personaje("Alfonso",10,100,8)
personaje1.atributos()

enemigo1 = Personaje("Enemy", 8,100,9)
enemigo1.atributos()

personaje1.ataque(enemigo1)

class Guerrero(Personaje):
  def __init__(self, nombre, daño, vida, defensa, espada, escudo):
    super().__init__(nombre, daño, vida, defensa)
    self.espada= espada
    self.escudo= escudo
  
  def estado(self):
    print(f"""
          Mi arma principal es: {self.espada} y {self.escudo }
          Mi daño es: Físico
          Mi virtud: Resistir daño
          """ )
     
  def ataque(self, enemigo):
    self.daño = self.daño * 2
    return self.daño - enemigo.defensa
  

