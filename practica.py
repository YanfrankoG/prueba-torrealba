
"""
class Persona(object):
	
	def __init__(self, nombre, apellido):

		self.nombre = nombre
		self.apellido = apellido



	def saludar(self):
		print(f"Hola {self.nombre} {self.apellido}, como estas?")




persona = Persona("andry", "torrealba")

print(persona)


persona.saludar()"""

"""

class Laptop(object):

	def __init__(self, ram, grafica, procesador):


		self.ram = ram
		self.grafica = grafica
		self.procesador = procesador





lenovo = Laptop(16,"Nvidia 3080TI", "Intel Core i7")


print(lenovo.ram)



class Laptop_aspecto(Laptop):

	def __init__(self, ram, grafica, procesador, color):
		super().__init__(ram, grafica, procesador)
		self.color = color
		


asus = Laptop_aspecto(32, "Nvidia 4080TI", "Intel Core i9", "azul")

print(asus.color)


"""

"""

class Entero_Romano:

	def __init__(self):

		pass

		
	def convertir_numero_entro(self, numero):

		if numero == 1:

			return "I"

		elif numero == 2:

			return "II"

		elif numero == 3:

			return "III"

		elif numero == 4:

			return "IV"

		elif numero == 5:

			return "V"


numero = Entero_Romano()

print(numero.convertir_numero_entro(5))

"""


"""

#EJERCICIO DE LA PROFESORA

class Vehiculo:
    def __init__(self, marca, modelo, year, encendido):
        self.marca = marca
        self.modelo = modelo
        self.year = year
        self.encendido = encendido

    def encender(self):
        self.encendido = True
        print(f"{self.modelo} {self.marca} ha sido encendido")

    def apagar(self):
        self.encendido = False
        print(f"{self.modelo} {self.marca} ha sido apagado")


class Carro(Vehiculo):
    def __init__(self, marca, modelo, year, tipo_carroceria):
        super().__init__(marca, modelo, year, tipo_carroceria)
        self.tipo_carroceria = tipo_carroceria

    def informacion(self):
        print(f"Carro {self.marca} {self.modelo} ({self.year}) - {self.tipo_carroceria}")


class Moto(Vehiculo):
    def __init__(self, marca, modelo, year, tipo_moto):
        super().__init__(marca, modelo, year, tipo_moto)
        self.tipo_moto = tipo_moto

    def informacion(self):
        print(f"Moto {self.marca} {self.modelo} ({self.year}) - {self.tipo_moto}")


carro = Carro("Toyota", "Corolla", 2002, "Sedan")
moto = Moto("Honda", "CBR500R", 2023, "Deportiva")

carro.encender()
carro.informacion()
carro.apagar()

moto.encender()
moto.informacion()
moto.apagar()

print("-----------------------------------------------------------------------------")
print(f"Carro {carro.marca} {carro.modelo} ({carro.year}) - {carro.tipo_carroceria}")

"""




#import datetime

from datetime import datetime

fechaActual = datetime.now()

print(fechaActual)

fecha =datetime(2002, 10, 15)

print(fecha)



class Reloj:
	def __init__(self, año, mes, dia):

		self.año = año
		self.mes = mes
		self.dia = dia


	def añadir_año(self, cantidad):

		self.año += cantidad
		
		fecha = datetime(self.año, self.mes, self.dia)

		print(fecha)



	def añadir_mes(self, cantidad):
		
		self.mes += cantidad
		
		fecha = datetime(self.año, self.mes, self.dia)

		print(fecha)


	def añadir_dia(self, cantidad):
		
		self.dia += cantidad
		
		fecha = datetime(self.año, self.mes, self.dia)

		print(fecha)

	def accion(self, opcion):

		if opcion == 1:

			cantidad_año = int(input("Ingrese el año: "))

			
			self.añadir_año(cantidad_año)
			print("Que desea hacer?\n Opcion1: añadir año \n Opcion2: añadir mes \n Opcion3: añadir dias \n")
			opcion = int(input("..."))
			self.accion(opcion)

		elif opcion == 2:
			
			cantidad_mes = int(input("Ingrese el mes: "))

			self.añadir_mes(cantidad_mes)
			print("Que desea hacer?\n Opcion1: añadir año \n Opcion2: añadir mes \n Opcion3: añadir dias \n")
			opcion = int(input("..."))
			self.accion(opcion)

		elif opcion == 3:


			cantidad_dia = int(input("Ingrese el dia: "))
			self.añadir_dia(cantidad_dia)
			print("Que desea hacer?\n Opcion1: añadir año \n Opcion2: añadir mes \n Opcion3: añadir dias \n")
			opcion = int(input("..."))
			self.accion(opcion)
			
			

		else:
			
			print("Cerrando sección")
		
		
		




reloj = Reloj(2024, 10, 30)

print("Que desea hacer?\n Opcion1: añadir año \n Opcion2: añadir mes \n Opcion3: añadir dias \n")

opcion = int(input("..."))

reloj.accion(opcion)


