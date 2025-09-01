# Este archivo corresponde al Ejercicio 1 de la guía práctica sobre Clases.
# Aquí deberás implementar la clase Camion y resolver los puntos a, b, c, d y f según las consignas
#A
class Camion:
    def __init__(self, patente,marca,carga,anio):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"

furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

print(furgon1 == furgon2) 
print(furgon1 is furgon2)
print(furgon3 == furgon4)
print(furgon3 is furgon4)
print(furgon1 == furgon4)

#print(furgon1==furgon2) devuelve true porque furgon2 es una referencia a furgon1, por lo que ambos apuntan al mismo objeto en memoria, a la clase furgon solo se creo el objeto furgon 1.
#print(furgon1 is furgon2) devuelve true porque furgon2 es una referencia a furgon1, por lo que ambos apuntan al mismo objeto en memoria, a la clase furgon solo se creo el objeto furgon 1.
#print(furgon3==furgon4) devuelve false porque furgon3 y furgon4 son dos objetos distintos de la clase camion.
#print(furgon3 is furgon4) devuelve false porque furgon3 y furgon4 son dos objetos distintos de la clase camion.
#print(furgon1==furgon4) devuelve false porque furgon1 y furgon4 son dos objetos distintos de la clase camion.

#B
class Camion:
    def __init__(self, patente,marca,carga,anio):
        self.patente = patente
        self.marca = marca
        self.carga = carga
        self.anio = anio

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    def __eq__(self, otro):
        if isinstance(otro, Camion):
            return (self.patente == otro.patente and
                    self.marca == otro.marca and
                    self.carga == otro.carga and
                    self.anio == otro.anio)
        return False
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

#c
#El atributo que hace unicos a nuestros objetos es la patente, ya que no podria haber dos camiones con la misma patente.
class Camion:
     
    def __init__(self, patente,marca,carga,anio):
        self.patente = patente
        self.patente = self.patente
        self.marca = marca
        self.carga = carga
        self.anio = anio

    def __str__(self):
        return f"Camión: #{self.patente} \nCarga: {self.carga} \nMarca: {self.marca} \nAño: {self.anio}"
    def __eq__(self,otro):
        if isinstance(otro, Camion):
            return self.patente == otro.patente
        return False
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

#d
class Camion:
    petentes_registradas=[]
    camiones=[]    
    def __init__(self, patente:str,marca:str,carga:int,anio:int):
        if patente not in Camion.petentes_registradas:
            Camion.petentes_registradas.append(patente)
        else:
            raise ValueError("La patente ya existe")
        self.patente = patente
        self.marca = marca
        self.setter_carga(carga)
        self.anio = anio
        Camion.camiones.append(self)

    def __str__(self):
        return f"Patende del camion: {self.patente}, la marca es: {self.marca}, la carga es: {self.carga}, la marca es: {self.marca}, el anio es: {self.anio}"

    def setter_carga(self,carga):
        self.carga=carga
    
furgon1 = Camion("ABC123", "Mercedes", 1000, 2020)
furgon2 = furgon1
furgon3 = Camion("DEF456", "Volvo", 2000, 2021)
furgon4 = Camion("ABC123", "Mercedes", 1000, 2020)

#f 
def registrar_camion():
    patente=input("Ingrese la patente: ")
    marca=input("Ingrese la marca: ")
    carga=int(input("Ingrese la carga: "))
    anio=int(input("Ingrese el anio: "))
    nuevo=Camion(patente,marca,carga,anio)

def modificar_carga():
    patente=input("Ingrese la patente del camion que quiere modificar: ")
    carga= int(input("Ingrese la carga: "))
    cambio=0
    for camion in Camion.camiones:
        if camion.patente==patente:
            camion.setter_carga(carga)
            cambio=1
    if cambio==0:
        print("No se encontro el camion")
    else:
        print("La carga se modifico con exito")

def camiones_registrados():
    anios=sorted(Camion.camions, key=lambda x:x.anio)
    for h in anios:
        print(h)

def marca_mas_registrada():
    marcas=[c.marca for c in Camion.camiones]
    cantidad=[]
    for i in set(marcas):
        cantidad.append(i,marcas.count(i))
    mas = max(cantidad, key=lambda x: x[1])  
    print("La marca más registrada es:", mas[0], "con", mas[1], "camiones")
    return mas[0]
        
def main():
    registrar_camion()
    modificar_carga()
    camiones_registrados()
    marca_mas_registrada()
