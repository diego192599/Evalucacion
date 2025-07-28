class Empleado:
    def __init__(self,nombre,departamento,trabajo):
        self.nombre=nombre
        self.departamento=departamento
        self.trabajo=trabajo
    def ingresar_datos(self):
        cantidad=int(input("Ingrese la cantida de trabajadores ingresara: "))
        for i in range(cantidad):
            print(f"\n Trabajador #{i+1}")
            nombre=input("Ingrese el nombre del trabajador")
    def mostrar_informacion(self):
        print("\n La informacion de los trabajadores son: ")
        print(f"Nombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Años trabajados son: {self.trabajo}")
