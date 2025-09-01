# Ejercicio 2: Modelar una computadora
# 
# En este archivo debés crear la clase Computadora siguiendo las consignas del README.
# Recordá:
# - Definir atributos relevantes en el constructor (__init__), con valores por defecto.
# - Implementar el método __str__ para mostrar la información esencial.
# - Instanciar al menos 3 computadoras con distintos valores.
# - Llevar la cuenta de computadoras creadas (usar variable de clase).
# - Implementar al menos 2 métodos de los sugeridos (updateOS, PM, addRAM, getCapacity).
# - Crear otra clase para un componente (ej: Disco, RAM, etc.) con su propio __init__, __str__ y al menos un método.
# 
# ¡No olvides probar todos los métodos y comentar tu criterio para los valores
class Disco:
    discos=[]
    def __init__(self, id, marca, proveedor,anio):
        self.id=id
        self.marca=marca
        self.proveedor=proveedor
        self.anio=anio
    def __str__(self):
        return f"Id: {self.id}, Marca: {self.marca}, Proveedor: {self.proveedor}, Anio: {self.anio}"
disco1=Disco(1,"Seagate","Amazon",2021)
disco2=Disco(2,"Western Digital","Mercado Libre",2020)
disco3=Disco(3,"Toshiba","eBay",2022)
class computadoras:
    compus=[]
    cantidad=0
    def __init__(self, id:int,marca:str="Sin marca", modelo:str="Sin modelo", anio: int=2025, sistema_operativo:str="Windows", ram:int=6, memoria:int=256, disco:Disco=None ):
        self.id= id 
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.sistema_operativo = sistema_operativo  
        self.ram = ram
        self.memoria = memoria
        self.disco= disco
        computadoras.compus.append(self)
        computadoras.cantidad+=1
  
    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}, Sistema Operativo: {self.sistema_operativo}, RAM: {self.ram}GB, Memoria: {self.memoria}GB. Disco: {self.disco}"
    
    def setter_operativo(self,sistema_operativo):
        self.sistema_operativo=sistema_operativo
    def getter_capacity(self):
        return self.memoria
    def setter_ram(self,ram):
        self.ram=ram

def addRam():
    id=int(input("Ingrese el id de la computadora a la que le quiere cambiar la ram: "))
    ram=int(input("Ingrese la cantidad de ram que le quiere poner a la computadora: "))
    for computador in computadoras.compus:
        if computador.id==id:
            computador.setter_ram(ram)
def UpdateOS():
    id=int(input("Ingrese el id de la computadora a la que le quiere cambiar el sistema operativo: "))
    sistema_operativo=input("Ingrese el nuevo sistema operativo: ")
    for computador in computadoras.compus:
        if computador.id==id:
            computador.setter_operativo(sistema_operativo)
def getCapacity():
    id=int(input("Ingrese el id de la computadora a la que le quiere ver la capacidad: "))
    for computador in computadoras.compus:
        if computador.id==id:
            print(f"La capacidad de la computadora con ID:{id} es {computador.getter_capacity()}")
    
compu1=computadoras(123,"Lenovo","Ideapad",2021,"Windows 10",8,512,disco1)
compu2=computadoras(456,"Apple","MacBook Air",2020,"macOS 6",16,256,disco2)
compu3=computadoras(789,"HP","Pavilion",2022,"Windows 8",12,1024,disco3)   


