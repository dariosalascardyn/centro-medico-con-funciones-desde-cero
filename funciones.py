import os, time

pacientes = []
def limpiar_pantalla():
    os.system("cls")
    
def menu_principal():
    limpiar_pantalla()
    print("1.- registrar paciente")
    print("2.- atencion paciente")
    print("3.- gestionar paciente")
    print("4.- salir")
    
def obtener_rut():
    while True:
        rutS= input("ingrese rut\n")
        while not rutS:
            rutS = input("ingrese rut\n")
        try:
            rut = int(rutS)
            if rut < 5000000 or rut > 30000000:
                print("rut fuera de rango")
            else:
                return rut
        except:
            print("en el campo rut, solo se aceptan numeros")
            
def obtener_campo(campo):
    valor = input(f"ingrese {campo}\n")
    while not valor:
        valor = input(f"{campo} no puede venir vacio")
    return valor

def obtener_correo():
    correo = input("ingrese correo\n")
    while "@" not in correo:
        correo = input("ingrese correo, debe tener el @")
    return correo

def obtener_edad():
    while True:
        edadS = input("ingrese edad\n")
        while not edadS:
            edadS = input("ingrese edad\n")
        try:
            edad = int(edadS)
            if edad < 0 or edad > 110:
                print("edad no esta en los rangos admitidos")
            else:
                return edad
            
        except:
            print("campo edad solo acepta numeros")

def obtener_sexo():
    sexo = input("ingrese sexo\n").lower()
    while sexo != "f" and sexo != "m":
        sexo = input("ingrese sexo\n").lower()
    return sexo

def obtener_prevision():
    prevision = input("ingrese su prevision\n").lower()
    while prevision != "fonasa" and prevision!= "isapre":
        prevision = input("ingrese su prevision\n").lower()
    return prevision

def registrar_paciente():
    while True:
        limpiar_pantalla()
        print("registrar paciente")
        rut = obtener_rut()
        nombre = obtener_campo("nombre")
        direccion = obtener_campo("direccion")
        correo = obtener_correo()
        edad = obtener_edad()
        sexo = obtener_sexo()
        prevision = obtener_prevision()
        paciente = [rut, nombre, direccion, correo, edad, sexo, prevision]
        pacientes.append(paciente)
        if input("deseas agregar otro paciente?\n 1.- si\n 2.- no\n") != 1:
            break
        else: 
            continue
    print(pacientes)
    input("ingrese tecla para continar")
    
#opcion atencion paciente
def atencion_paciente():
    limpiar_pantalla()
    print("\t\tAtencion paciente")
    rutBuscar = int(input("ingrese rut de paciente\n"))
    for paciente in pacientes:
        if paciente[0] == rutBuscar:
            print("adelante", paciente[1])
            registro = input("ingrese motivo consulta\n")
            while not registro:
                registro = input("ingrese motivo consulta\n")
            paciente.append(registro)
            print(paciente)
            input("ingrese tecla para continar")
        else:
            print("paciente no existe")

#opcion gestionar paciente 
def gestionar_paciente():
    while True:
        limpiar_pantalla()
        print("\t\tGestionar datos paciente")
        print("1.- consultar datos paciente")
        print("2.- modificar datos paciente")
        print("3.- eliminar datos paciente")
        print("4.- regresar al menu principal")
        try:
            opcion2 = int(input("ingrese opcion\n"))
            if opcion2 == 1:
                consultar_datos()
            elif opcion2 == 2:
                print("")
            elif opcion2 == 3:
                print("")
            elif opcion2 == 4:
                print("saliendo al menu principal...")
                time.sleep(1)
                break
        except:
            print("opcion no valida")

#consultar datos
def consultar_datos():
    limpiar_pantalla()
    print("\t\tConsultar datos paciente")
    rutBuscar = int(input("ingrese rut de paciente a consultar\n0000000000"))
    for paciente in pacientes:
        if paciente[0] == rutBuscar:
            #paciente = [rut, nombre, direccion, correo, edad, sexo, prevision]
            print(f" rut: {paciente[0]}")
            print(f" nombre: {paciente[1]}")
            print(f" direccion: {paciente[2]}")
            print(f" correo: {paciente[3]}")
            print(f" edad: {paciente[4]}")
            print(f" sexo: {paciente[5]}")
            print(f" prevision: {paciente[6]}")
            print(f" registro: {paciente[7]}")
        else: 
            print("paciente no encontrado")
        input("ingrese tecla para continuar")    
        
            
            
            
            
            
            
            