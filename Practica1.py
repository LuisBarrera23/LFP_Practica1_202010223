def cargararchivo():
    print('cargararchivo')

while True:
    print('--------------------MENU PRINCIPAL--------------------')
    print('1. Cargar archivo')
    print('2. Mostrar reporte en consola')
    print('3. Exportar reporte')
    print('4. Salir')
    print('------------------------------------------------------')
    try:
        opcion=int(input('Ingrese el numero de opción deseada'))
        #if opcion==1:cargararchivo()
        if opcion==(1 or 2 or 3 or 4):
            print('Opción ingresada no valida')
    except:
        print('Error, vuelva a intentarlo.')
