from funciones import *

banderamenu= True
while banderamenu:
    limpiar_pantalla()
    menu_principal()
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            registrar_paciente()
        elif opcion == 2:
            atencion_paciente()
            
        elif opcion == 3:
            gestionar_paciente()
            
        elif opcion == 4:
            print("saliendo del programa...")
            banderamenu = False
            
    except:
        limpiar_pantalla()
        print("opcion no valida")
        time.sleep(2)
        