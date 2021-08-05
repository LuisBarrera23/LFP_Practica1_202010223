from tkinter import filedialog,Tk
#variables globales utilizadas
opcion=0
curso=""
alumnos=[]
alumnos2=[]
notas=[]
notas2=[]
reportes=[]
cantidad_alum=0

#FUNCION PARA GENERAR REPORTE DE LOS DATOS GUARDADOS AL LEER EL ARCHIVO
def reportelectura():
    global curso,alumnos,notas
    print("Curso: ",curso)
    print("Estudiantes incritos: ",cantidad_alum)
    for i in range(cantidad_alum):
        print("El estudiante: ",alumnos[i]," tiene una nota de: ",notas[i])


def cargararchivo():
    global curso,alumnos,alumnos2,notas,notas2,cantidad_alum

    Tk().withdraw()
    #GENERANDO VENTANA PARA ELEGIR ARCHIVO
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

    #CAPTURA DE LOS DATOS {DATOS}
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

    #COPIA DE LOS ARREGLOS ORIGINALES
    alumnos2=alumnos.copy()
    notas2=notas.copy()
    
    #LECTURA DE LOS PARAMETROS OTORGADOS
    solicitado=contenido[fin_datos+1:len(contenido)]
    cantidad_rep=solicitado.count(",")+1
    if cantidad_rep==0:
        reportes.append(solicitado.strip())
    if cantidad_rep>0:
        for i in range(cantidad_rep):
            coma=solicitado.find(",")
            reporte=(solicitado[0:coma]).strip()
            
            if i<cantidad_rep-1:
                solicitado=solicitado[coma+1:len(solicitado)]
                reportes.append(reporte)
            else:
                reportes.append(solicitado.strip())

    #GENERAR REPORTE DE LA LECTURA
    reportelectura()

    #PRUEBAS DE ORDENAMIENTO

    for i in range(1,len(notas2)):
        for j in range(0,len(notas2)-i):
            if(notas2[j+1]>notas2[j]):
                aux1=notas2[j]
                aux2=alumnos2[j]
                notas2[j]=notas2[j+1]
                alumnos2[j]=alumnos2[j+1]
                notas2[j+1]=aux1
                alumnos2[j+1]=aux2
    #print(alumnos2)
    #print(notas2)

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
