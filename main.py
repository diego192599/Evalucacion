empleados = {}

class Empleado:
    def __init__(self, codigo, nombre, departamento, trabajo):
        self.codigo = codigo
        self.nombre = nombre
        self.departamento = departamento
        self.trabajo = trabajo

    def mostrar_informacion(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Años trabajados: {self.trabajo}")


class Evaluacion:
    def __init__(self):
        pass

    def promediar_puntaje(self):
        codigo = input("Ingrese el código del empleado a evaluar: ")
        if codigo in empleados:
            print("Empleado encontrado... Evalue al empleado")
            puntualidad = int(input("Ingrese el puntaje de puntualidad (0-10): "))
            trabajo_equipo = int(input("Ingrese el puntaje de trabajo en equipo (0-10): "))
            productividad = int(input("Ingrese el puntaje de productividad (0-10): "))

            suma = puntualidad + trabajo_equipo + productividad
            promedio = suma / 3
            empleado = empleados[codigo]

            if promedio >= 7:
                print(f"\nEl empleado {empleado.nombre} tiene un desempeño SATISFACTORIO.")
            else:
                print(f"\nEl empleado {empleado.nombre} puede mejorar su desempeño.")
        else:
            print("No se encontró al empleado.")


def ingresar_datos():
    cantidad = int(input("Ingrese la cantidad de trabajadores a ingresar: "))
    for i in range(cantidad):
        print(f"\n--- Trabajador #{i + 1} ---")
        codigo = input("Código: ")
        nombre = input("Nombre: ")
        departamento = input("Departamento: ")
        trabajo = int(input("Años trabajados: "))
        if trabajo <= 0:
            print("Los años trabajados no son válidos.")
        else:
            empleados[codigo] = Empleado(codigo, nombre, departamento, trabajo)
            print("Datos guardados correctamente.")


def mostrar_todos():
    if empleados:
        print("\n--- Información de todos los empleados ---")
        for empleado in empleados.values():
            empleado.mostrar_informacion()
    else:
        print("No hay empleados registrados.")


evaluador = Evaluacion()

while True:
    print("\n== MENU ==")
    print("1. Ingresar datos del empleado")
    print("2. Mostrar información de empleados")
    print("3. Evaluación del empleado")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        ingresar_datos()
    elif opcion == "2":
        mostrar_todos()
    elif opcion == "3":
        evaluador.promediar_puntaje()
    elif opcion == "4":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
