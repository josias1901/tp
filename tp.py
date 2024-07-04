lista_estudiantes = []

def menu():
    print("1- agregar estudiantes")
    print("2- eliminar estudiantes")
    print("3- mostrar estudiantes")
    print("4- salir de la aplicacion")

def agregar(estudiantes):
    lista_estudiantes.append(agregar)

def eliminar(estudiantes):
    lista_estudiantes.remove(eliminar)

while True:
        print(lista_estudiantes)
        opcion = int(input("ingrese la opcion que desea ejecutar"))
        if opcion == 1:
            estudiantes = input("ingrese el estudiante que desea agregar a su lista")
            agregar(estudiantes)
            print(f"{agregar} fue agregada a la lista correctamente")

        elif opcion == 2:
             lista_estudiantes.sort()
             for i in lista_estudiantes:
                  print(i)
                  eliminar = input("ingrse al estudiante que desea eliminar")
                  eliminar(estudiantes)
                  print(f"{eliminar} fue eliminado de la lista")
             else:
                  print("estudiante no encontrado, vuelve a intentarlo")
        elif opcion == 3:
             print("a continuacion se mostrara al estudiante")
             for i in lista_estudiantes:
                  print(i)
                  print("lista de estudiantes", lista_estudiantes if lista_estudiantes else "vacia")
        elif opcion == 4:
             print("hasta pronto")
             break  
                  