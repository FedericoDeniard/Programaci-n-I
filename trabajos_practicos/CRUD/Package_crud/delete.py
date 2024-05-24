from trabajos_practicos.CRUD.Package_crud.read import *


def delete_employee(employees: list):
    id = get_int("Ingrese el ID del empleado a eliminar: ")
    id_valid = check_id(employees,id)
    if id_valid != None:
        print("El siguiente empleado será elminado")
        show_employee(employees[id_valid])
        if get_confirm():
            employees.pop(id_valid)
            print("Empleado elminado.")
            input("Presione una tecla para continuar...")
            clear_screen()
        else:
            print("Eliminación cancelada.")
            input("Presione una tecla para continuar...")
            clear_screen()