#############################
## FUNCIONES DE VALIDACION ##
#############################
def validar_nombre(nombre):
  return nombre.strip() != ""

def validar_edad(edad):
  return edad > 0

def validar_nota(nota):
  return (nota >= 1.0) and (nota <= 7.0)

###########################
## FUNCIONES PRINCIPALES ##
###########################
def agregar_estudiante(lista):
  ## INGRESO DE DATOS ##
  nombre = input("Ingrese el nombre del estudiante: ")
  while True:
    try:
      edad = int(input("Ingrese su edad: "))
      break
    except ValueError:
      print("ERROR: Debe ingresar un numero entero")
  while True:
    try:
      nota = float(input("Ingrese su nota: "))
      break
    except ValueError:
      print("ERROR: Debe ingresar un numero decimal")
  ## VALIDACION DE DATOS ##
  if not validar_nombre(nombre):
    print("--- El nombre no puede ser un campo vacio ---")
    return
  if not validar_edad(edad):
    print("--- La edad debe ser mayor que cero ---")
    return
  if not validar_nota(nota):
    print("--- La nota debe estar en un rango entre 1.0 y 7.0 ---")
    return
  ## INGRESO DE DATOS A LA LISTA ##
  estudiante = {
    "nombre": nombre,
    "edad": edad,
    "nota": nota,
    "aprobado": False
  }
  lista.append(estudiante)
  print("--- ESTUDIANTE REGISTRADO EXITOSAMENTE ---")

def buscar_estudiante(lista, nombre):
  for indice in range(len(lista)):
    if lista[indice]["nombre"] == nombre:
      return indice
  return -1

def actualizar_estado(lista):
  for estudiante in lista:
    if estudiante["nota"] >= 4.0:
      estudiante["aprobado"] = True

def mostrar_opciones():
  print("====== MENU PRINCIPAL ======")
  print("1. Agregar estudiante")
  print("2. Buscar estudiante")
  print("3. Eliminar estudiante")
  print("4. Actualizar estados")
  print("5. Mostrar estudiantes")
  print("6. Salir")
  
def seleccionar_opcion():
  while True:
    try:
      opcion_seleccionada = int(input("Seleccione una opcion: "))
      break
    except ValueError:
      print("ERROR: Debe ingresar un numero entero")
  return opcion_seleccionada

####################
## MENU PRINCIPAL ##
####################
estudiantes = [] 
while True:
  mostrar_opciones()
  opcion = seleccionar_opcion()
  ## OPCIONES DEL MENU ##
  if opcion == 1:
    agregar_estudiante(estudiantes)
  elif opcion == 2:
    if estudiantes:
      estudiante_buscado = input("Ingrese el nombre del estudiante: ")
      posicion = buscar_estudiante(estudiantes, estudiante_buscado)
      if posicion != -1:
        print(f"Posicion: {posicion}")
        print(f"Nombre: {estudiantes[posicion]['nombre']}")
        print(f"Edad: {estudiantes[posicion]['edad']}")
        print(f"Nota: {estudiantes[posicion]['nota']}")
        print(f"Estado: {estudiantes[posicion]['aprobado']}")
      else:
        print(f"El estudiante '{estudiante_buscado}' no se encuentra registrado")
    else:
      print("|-- Aun no hay estudiantes registrados --|")
  elif opcion == 3:
    if estudiantes:
      nombre_estudiante = input("Ingrese el nombre del estudiante: ")
      posicion = buscar_estudiante(estudiantes, nombre_estudiante)
      if posicion != -1:
        del estudiantes[posicion]
        print("|-- Estudiante eliminado exitosamente --|")
      else:
        print(f"El estudiante '{nombre_estudiante}' no se encuentra registrado")
    else:
      print("|-- Aun no hay estudiantes registrados --|")
  elif opcion == 4:
    actualizar_estado(estudiantes)
    print("|-- Estado actualizado correctamente --|")
  elif opcion == 5:
    if estudiantes:
      print("=== LISTA DE ESTUDIANTES ===")
      actualizar_estado(estudiantes)
      for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota: {estudiante['nota']}")
        if estudiante["aprobado"]:
          print("Estado: APROBADO")
        else:
          print("Estado: REPROBADO")
        print("*" * 30)
    else:
      print("|-- Aun no hay estudiantes registrados --|")
  elif opcion == 6:
    print("|-- Gracias por usar el sistema. Vuelva Pronto --|")
    break
  else:
    print("|-- La opcion seleccionada no existe --|")