import tkinter as tk
from tkinter import filedialog
#variables globales utilizadas
opcion=0
curso=""
alumnos=[]
alumnos2=[]
notas=[]
notas2=[]
reportes=[]
cantidad_alum=0
promedio=0
aprobados=0
reprobados=0

def cargaprueba():
    global curso,alumnos,alumnos2,notas,notas2,cantidad_alum,reportes
    alumnos.clear(),alumnos2.clear(),notas.clear(),notas2.clear(),reportes.clear()

    #Tk().withdraw()
    #GENERANDO VENTANA PARA ELEGIR ARCHIVO
    root=tk.Tk()
    archivo=filedialog.askopenfilename(
        title="Selecciona un archivo en formato LFP",
        initialdir="./",
        filetypes=(("archivos LFP","*.lfp"),("Todos los archivos","*.*")),
    )
    print(archivo)
    lectura=open(archivo,"r",encoding='UTF-8')
    contenido=lectura.read()
    lectura.close()
    
    if contenido is not None:
        for c,caracter in enumerate(contenido):
            if contenido[c]=="=":
                curso=contenido[0:c]
                print(curso)
        datos=""
        inicio=False
        fin=0
        iterador=0
        for c in contenido:
            if c=="}":
                fin=iterador
            if c=="\n":
                continue
            if c=="\t":
                continue
            if c =="{":
                inicio=True
                continue
            if inicio==True:
                datos+=c
                iterador+=1
        datos2=""
        solicitado=""
                
        for c,caracter in enumerate(datos):
            if c<fin:
                datos2+=caracter
            if c>fin:
                solicitado+=caracter
        print(datos2)
        print(solicitado)


        estudiante=""
        inicio=False
        for i, caracter in enumerate(datos2):
            if (caracter=="\"") and estudiante=="":
                inicio=True
                continue
            if caracter=="\"":
                alumnos.append(estudiante)
                inicio=False
                estudiante=""
                continue
            if inicio==True:
                estudiante+=caracter

        inicio=False
        nota_c=""
        nota=0
        for c in datos2:
            if c==";":
                inicio=True
                continue
            if c==">":
                nota=float(nota_c)
                nota_c=""
                inicio=False
                notas.append(nota)
            if (inicio==True) and (c!=" "):
                nota_c+=c
        
        reporte=""
        for c in solicitado:
            if c==",":
                reportes.append(reporte)
                reporte=""
                continue
            if c!=" ":
                reporte+=c
        
        reportes.append(reporte)
            


        cantidad_alum=len(alumnos)
        alumnos2=alumnos.copy()
        notas2=notas.copy()
        print(reportes)

                
                


#FUNCION PARA GENERAR REPORTE DE LOS DATOS GUARDADOS AL LEER EL ARCHIVO
def reportelectura():
    global curso,alumnos,notas
    print("Curso: ",curso)
    print("Estudiantes incritos: ",cantidad_alum)
    for i in range(cantidad_alum):
        print("El estudiante: ",alumnos[i]," tiene una nota de: ",notas[i])

#Reporte ASC orden ascendente
def mostrarascendente():
    global alumnos2,notas2

    for i in range(1,len(notas2)):
        for j in range(0,len(notas2)-i):
            if(notas2[j+1]<notas2[j]):
                aux1=notas2[j]
                aux2=alumnos2[j]
                notas2[j]=notas2[j+1]
                alumnos2[j]=alumnos2[j+1]
                notas2[j+1]=aux1
                alumnos2[j+1]=aux2
    
    print("-----Listado de Estudiantes segun nota de forma ascendente-----")
    for i in range(len(alumnos2)):
        print("Estudiante: ",alumnos2[i],"\t Nota: ",notas2[i])
    print("\n")

#Reporte DESC orden descendente    
def mostrardescendente():
    global alumnos2,notas2

    for i in range(1,len(notas2)):
        for j in range(0,len(notas2)-i):
            if(notas2[j+1]>notas2[j]):
                aux1=notas2[j]
                aux2=alumnos2[j]
                notas2[j]=notas2[j+1]
                alumnos2[j]=alumnos2[j+1]
                notas2[j+1]=aux1
                alumnos2[j+1]=aux2
    
    print("-----Listado de Estudiantes segun nota de forma descendente-----")
    for i in range(len(alumnos2)):
        print("Estudiante: ",alumnos2[i],"\t Nota: ",notas2[i])
    print("\n")

#Reporte AVG calculo del promedio de notas de los estudiantes
def mostrarpromedio():
    global notas2,promedio
    promedio=0
    suma=0

    for i in range(len(notas2)):
        suma+=notas2[i]
    promedio=round(suma/len(notas2),2)
    print("-----\tEl promedio de los estudiantes del curso es: ",promedio,"\t-----")
    print("\n")


#Reporte MAX mostrar la nota mas alta
def mostrarMax():
    global alumnos2,notas2

    for i in range(1,len(notas2)):
        for j in range(0,len(notas2)-i):
            if(notas2[j+1]>notas2[j]):
                aux1=notas2[j]
                aux2=alumnos2[j]
                notas2[j]=notas2[j+1]
                alumnos2[j]=alumnos2[j+1]
                notas2[j+1]=aux1
                alumnos2[j+1]=aux2
    
    print("-----\tLa nota maxima es del estudiante: ",alumnos2[0]," con ", notas2[0],"\t-----")
    print("\n")


#Reporte MIN mostrar la nota mas baja
def mostrarMin():
    global alumnos2,notas2

    for i in range(1,len(notas2)):
        for j in range(0,len(notas2)-i):
            if(notas2[j+1]<notas2[j]):
                aux1=notas2[j]
                aux2=alumnos2[j]
                notas2[j]=notas2[j+1]
                alumnos2[j]=alumnos2[j+1]
                notas2[j+1]=aux1
                alumnos2[j+1]=aux2
    
    print("-----\tLa nota minima es del estudiante: ",alumnos2[0]," con ", notas2[0],"\t-----")
    print("\n")

#Reporte APR mostrar estudiantes aprobados
def mostrarAprobados():
    global notas2,aprobados
    aprobados=0

    for i in range(len(notas2)):
        if notas2[i]>=61:
            aprobados+=1
    
    print("-----\tEstudiantes aprobados en el curso: ",aprobados,"\t-----")
    print("\n")


#Reporte APR mostrar estudiantes reprobados
def mostrarReprobados():
    global notas2,reprobados
    reprobados=0

    for i in range(len(notas2)):
        if notas2[i]<61:
            reprobados+=1
    
    print("-----\tEstudiantes reprobados en el curso: ",reprobados,"\t-----")
    print("\n")
    



def menu():
    global opcion,reportes,curso,cantidad_alum
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
                #cargararchivo()
                cargaprueba()
            elif opcion==2:
                print("Curso: ",curso)
                print("Estudiantes inscritos: ",cantidad_alum)
                for i in range(len(reportes)):
                    if reportes[i]=="ASC":
                        mostrarascendente()
                    elif reportes[i]=="DESC":
                        mostrardescendente()
                    elif reportes[i]=="AVG":
                        mostrarpromedio()
                    elif reportes[i]=="MIN":
                        mostrarMin()
                    elif reportes[i]=="MAX":
                        mostrarMax()
                    elif reportes[i]=="APR":
                        mostrarAprobados()
                    elif reportes[i]=="REP":
                        mostrarReprobados()
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
