from tkinter import filedialog,Tk
opcion=0
curso=""
alumnos=[]
notas=[]



def cargararchivo():
    global curso,alumnos,notas

    print('cargararchivo')
    Tk().withdraw()
    archivo=filedialog.askopenfile(
        title="Selecciona un archivo en formato LFP",
        initialdir="./",
        filetypes=(("archivos LFP","*.lfp"),("Todos los archivos","*.*"))
    )
    contenido=archivo.read()
    separador=contenido.find("=")
    curso=(contenido[0:separador]).strip()
    inicio_datos=contenido.find("{")
    fin_datos=contenido.find("}")
    datos=(contenido[inicio_datos+1:fin_datos]).strip()
    cantidad_alum=datos.count(",")+1
    print(cantidad_alum)
    for i in range(cantidad_alum):
        pos_coma=datos.find(",")
        alumno=(datos[0:pos_coma]).strip()
        alumno=alumno.strip(' <>')
        pos_puntocoma=alumno.find(";")
        nota=int((alumno[pos_puntocoma+1:len(alumno)]).strip())
        alumno=(alumno[0:pos_puntocoma]).strip(' "')
        datos=datos[pos_coma+1:len(datos)]
        alumnos.append(alumno)
        notas.append(nota)
        print("Nombre del alumno: ",alumno," su nota es: ",nota)
    print(alumnos)
    print(notas)

def menu():
    global opcion
    while True:
        print('--------------------MENU PRINCIPAL--------------------')
        print('1. Cargar archivo')
        print('2. Mostrar reporte en consola')
        print('3. Exportar reporte')
        print('4. Salir')
        print('------------------------------------------------------')
        try:
            opcion=int(input('Ingrese el numero de opción deseada: \n'))
            if opcion==1:
                cargararchivo()
            elif opcion==2:
                for i in range(3):
                    print(i)
                print("Mostrar reporte")
            elif opcion==3:
                print("Exportar Reporte")
            elif opcion==4:
                print("Saliendo del programa")
                exit(0)
            else:
                print("Opcion no encontrada")
        except:
            if opcion==4:
                exit(0)
            print('Error, vuelva a intentarlo.')


if __name__=='__main__':
    menu()
