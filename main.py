from enum import nonmember

empledos={}
class Empleado:
    def __init__(self,codigo,nombre,departamento,trabajo,):
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


class Evaluacion(Empleado):
    def __init__(self, puntaje):
        self.puntaje = puntaje

    def Promediode_puntuaje(self, puntuaje):
        buscar = input("Ingrese el codigo del empleado a puntuar: ")
        if buscar in empledos:
            print("Empleado encontrado...Evalue a empleado")
            puntuaje = int(
                input("Ingrese la cantidad de evaluaciones tendra el empleado (la cantida de ingresos son 3)"))
            for i in range(puntuaje):
                puntialidad = int(input("Ingrese el puntuaje de la puntualidad del empleado (0-10): "))
                trabajo_equipo = int(input("Ingrese el puntaje del empleado cuando trabaja en equipo(0-10): "))
                productividad = int(input("Ingrese el puntuaje de que tan productivo es el empleado(0-10): "))
            suma = puntialidad + trabajo_equipo + productividad
            promedio = suma / 3
            if promedio >= 7:
                print(f"\n El empleado con el nombre: {self.nombre} su desempeño es Satisfactorio")
            else:
                print(f"EL empleado puede mejorar su desempeño laboral")
        else:
            print("No se ha encontrado el empledo")

class Contacto(Empleado):
    def __init__(self,telefono,correo):
        self.telefono=telefono
        self.correo=correo
    def ingreso_datos(self):

while True:
    print("\n==MENU==")
    print("1. Ingrese datos del empleado")
    print("2. Mostrar Informacion")
    print("3. Evaluacion")
    print("4. Salir")
    opcion=int(input("Seleccione una opcion: "))
    if opcion==1:
        print("Bienvido ingrese los requisitos pedidos")
    elif opcion==2:
        print("---Mostrar Informacion---")
    elif opcion==3:
        print("---Evaluacion de Empleado---")
    elif opcion==4:
        print("!Hasta pronto¡")
        break
    else:
        print("La opcion seleccionada no se encuentra disponible....Intente nuevamente")