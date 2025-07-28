empleados = {}

class Contacto:
    def __init__(self, telefono, correo):
        self.telefono = telefono
        self.correo = correo

    def mostrar_contacto(self):
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")


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


class EmpleadoConContacto(Empleado):
    def __init__(self, codigo, nombre, departamento, trabajo, contacto):
        super().__init__(codigo, nombre, departamento, trabajo)
        self.contacto = contacto

    def mostrar_informacion(self):
        super().mostrar_informacion()
        self.contacto.mostrar_contacto()


class Evaluacion:
    def promediar_puntaje(self):
        codigo = input("Ingrese el código del empleado a evaluar: ")
        if codigo in empleados:
            print("Empleado encontrado... Evalue al empleado")
            puntualidad = int(input("Puntaje de puntualidad (0-10): "))
            trabajo_equipo = int(input("Puntaje de trabajo en equipo (0-10): "))
            productividad = int(input("Puntaje de productividad (0-10): "))

            suma = puntualidad + trabajo_equipo + productividad
            promedio = suma / 3
            empleado = empleados[codigo]

            if promedio >= 7:
                print(f"\nEl empleado {empleado.nombre} tiene un desempeño SATISFACTORIO. Promedio: {promedio:.2f}")
            else:
                print(f"\nEl empleado {empleado.nombre} puede mejorar su desempeño. Promedio: {promedio:.2f}")
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
            continue

        telefono = input("Teléfono de contacto: ")
        correo = input("Correo electrónico: ")

        contacto = Contacto(telefono, correo)
        empleado = EmpleadoConContacto(codigo, nombre, departamento, trabajo, contacto)
        empleados[codigo] = empleado
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
