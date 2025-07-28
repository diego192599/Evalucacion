empleados = {}

class Contacto:
    def __init__(self, datos):
        self.telefono = datos["telefono"]
        self.correo = datos["correo"]

    def mostrar_contacto(self):
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")


class Empleado:
    def __init__(self, datos):
        self.nombre = datos["nombre"]
        self.departamento = datos["departamento"]
        self.trabajo = datos["trabajo"]

    def mostrar_info(self):
        print(f"\nNombre: {self.nombre}")
        print(f"Departamento: {self.departamento}")
        print(f"Años trabajados: {self.trabajo}")


class Evaluacion:
    def __init__(self, datos):
        self.puntualidad = datos.get("puntualidad", 0)
        self.trabajo_equipo = datos.get("trabajo_equipo", 0)
        self.productividad = datos.get("productividad", 0)

    def calcular_promedio(self):
        return (self.puntualidad + self.trabajo_equipo + self.productividad) / 3


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
            continue

        telefono = input("Teléfono de contacto: ")
        correo = input("Correo electrónico: ")

        empleados[codigo] = {
            "info": {
                "nombre": nombre,
                "departamento": departamento,
                "trabajo": trabajo
            },
            "contacto": {
                "telefono": telefono,
                "correo": correo
            },
            "evaluacion": {}
        }
        print("Datos guardados correctamente.")


def mostrar_todos():
    if empleados:
        print("\n--- Información de todos los empleados ---")
        for codigo, datos in empleados.items():
            emp = Empleado(datos["info"])
            emp.mostrar_info()

            cont = Contacto(datos["contacto"])
            cont.mostrar_contacto()

            if datos["evaluacion"]:
                evalua = Evaluacion(datos["evaluacion"])
                promedio = evalua.calcular_promedio()
                print(f"Promedio de evaluación: {promedio:.2f}")
    else:
        print("No hay empleados registrados.")


def evaluar_empleado():
    codigo = input("Ingrese el código del empleado a evaluar: ")
    if codigo in empleados:
        print("Empleado encontrado... Evalue al empleado")
        puntualidad = int(input("Puntaje de puntualidad (0-10): "))
        trabajo_equipo = int(input("Puntaje de trabajo en equipo (0-10): "))
        productividad = int(input("Puntaje de productividad (0-10): "))

        empleados[codigo]["evaluacion"] = {
            "puntualidad": puntualidad,
            "trabajo_equipo": trabajo_equipo,
            "productividad": productividad
        }

        evaluacion = Evaluacion(empleados[codigo]["evaluacion"])
        promedio = evaluacion.calcular_promedio()
        nombre = empleados[codigo]["info"]["nombre"]

        if promedio >= 7:
            print(f"\nEl empleado {nombre} tiene un desempeño SATISFACTORIO. Promedio: {promedio:.2f}")
        else:
            print(f"\nEl empleado {nombre} puede mejorar su desempeño. Promedio: {promedio:.2f}")
    else:
        print("No se encontró al empleado.")


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
        evaluar_empleado()
    elif opcion == "4":
        print("¡Hasta pronto!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")