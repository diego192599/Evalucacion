empledos={}
class Empleado:
    def __init__(self,codigo,nombre,departamento,trabajo):
        self.codigo=codigo
        self.nombre=nombre
        self.departamento=departamento
        self.trabajo=trabajo
    def ingresar_datos(self):
        cantidad=int(input("Ingrese la cantida de trabajadores ingresara: "))
        for i in range(cantidad):
            print(f"\n Trabajador #{i+1}")
            codigo=input("Ingrese su codigo: ")
            nombre=input("Ingrese el nombre del trabajador: ")
            departamento=input("Ingrese sus departamento: ")
            trabajo=int(input("Ingrese los años trabajados en la empresa: "))
            if trabajo<=0:
                print("Los años trabajados no son validos")
            else:
                print("Datos guardados correctamente")

        empledos = {
            "codigo": {
                "nombre": nombre,
                "departamento": departamento,
                "trabajo": trabajo
            }
        }
    def mostrar_informacion(self):
        print("\n La informacion de los trabajadores son: ")
        print(f"Nombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Años trabajados son: {self.trabajo}")
