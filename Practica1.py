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
    archivo=filedialog.askopenfilename(
        title="Selecciona un archivo en formato LFP",
        initialdir="./",
        filetypes=(("archivos LFP","*.lfp"),("Todos los archivos","*.*")),
    )
    #print(archivo)
    lectura=open(archivo,"r",encoding='UTF-8')
    contenido=lectura.read()
    lectura.close()
    
    if contenido is not None:
        for c,caracter in enumerate(contenido):
            if contenido[c]=="=":
                curso=contenido[0:c]
                #print(curso)
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
        #print(datos2)
        #print(solicitado)


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
        #print(reportes)
        reportelectura()

                
                


#FUNCION PARA GENERAR REPORTE DE LOS DATOS GUARDADOS AL LEER EL ARCHIVO
def reportelectura():
    global curso,alumnos,notas
    print("Curso: ",curso)
    print("Estudiantes incritos: ",cantidad_alum)
    for i in range(cantidad_alum):
        print("El estudiante: ",alumnos[i]," tiene una nota de: ",notas[i])


#Funcion para la generación de HTML 
def generarReporteHTML():
    print("hola")
    global curso,cantidad_alum,alumnos2,notas2,reportes,promedio,alumnos,notas
    f=open("Reporte.html","w",encoding='UTF-8')
    inicio="""
    <!doctype html>
    <html lang="en">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">

    <title>Reporte Practica 1</title>
    </head>
    <style>
    .titulo{
        text-align: center;
        background-color: aqua;
        padding: 8px;
    }
    .cuerpo{
        background-color: white;
    }
    .contenido{
        color: white;
    }
    .inscritos{
        color:white;
        background-color: teal;
        padding: 8px;
    }
    .tabla{
        width:80%; 
        text-align: center; 
        margin-right: auto; 
        margin-left: auto;
        padding: 15px;
    }
    h1,h2{
        text-align:center;
        padding:8px;
    }
    button{
        margin-right: auto; 
        margin-left: auto;
        text-align: center;
        padding: 5px;
        margin-bottom: 15px;
        width: 200px;
    }
    </style>
    <body class="cuerpo">
    <div class="titulo">
    <h1>"""
    inicio+=curso+"</h1></div>"
    inicio+="<div class=\"inscritos\"><h2>Estudiantes incritos en el curso: "+str(cantidad_alum)+"</h2></div>"

    inicio+="<div><h2>Listado Original</h2>"

    inicio+="<div class=\"tabla\"><table class=\"table table-dark table-hover\">"
    inicio+="""<thead><tr>
    <th scope="col">No.</th>
    <th scope="col">NOMBRE</th>
    <th scope="col">NOTA</th>
    </tr></thead><tbody>"""
            
    for i in range(len(alumnos)):
        inicio+="<tr>"
        inicio+="<th scope=\"row\">"+str(i+1)+"</th>"
        inicio+="<td>"+alumnos[i]+"</td>"
        if notas2[i]>=61:
            inicio+="<td style=\"color:#033CF6;\">"+str(notas[i])+"</td>"
        else:
            inicio+="<td style=\"color:red;\">"+str(notas[i])+"</td>"
        inicio+="</tr>"
            
    inicio+="</tbody></table></div></div>"


    contenido=""
    for i in range(len(reportes)):
        if reportes[i]=="ASC":
            for i in range(1,len(notas2)):
                for j in range(0,len(notas2)-i):
                    if(notas2[j+1]<notas2[j]):
                        aux1=notas2[j]
                        aux2=alumnos2[j]
                        notas2[j]=notas2[j+1]
                        alumnos2[j]=alumnos2[j+1]
                        notas2[j+1]=aux1
                        alumnos2[j+1]=aux2

            contenido+="<h2>Listado de Estudiantes según nota de forma ascendente</h2>"
            contenido+="<div class=\"tabla\"><table class=\"table table-dark table-hover\">"
            contenido+="""<thead><tr>
            <th scope="col">No.</th>
            <th scope="col">NOMBRE</th>
            <th scope="col">NOTA</th>
            </tr></thead><tbody>"""
            
            for i in range(len(alumnos2)):
                contenido+="<tr>"
                contenido+="<th scope=\"row\">"+str(i+1)+"</th>"
                contenido+="<td>"+alumnos2[i]+"</td>"
                if notas2[i]>=61:
                    contenido+="<td style=\"color:#033CF6;\">"+str(notas2[i])+"</td>"
                else:
                    contenido+="<td style=\"color:red;\">"+str(notas2[i])+"</td>"
                contenido+="</tr>"
            
            contenido+="</tbody></table></div>"
        
        elif reportes[i]=="DESC":
            for i in range(1,len(notas2)):
                for j in range(0,len(notas2)-i):
                    if(notas2[j+1]>notas2[j]):
                        aux1=notas2[j]
                        aux2=alumnos2[j]
                        notas2[j]=notas2[j+1]
                        alumnos2[j]=alumnos2[j+1]
                        notas2[j+1]=aux1
                        alumnos2[j+1]=aux2

            contenido+="<h2>Listado de Estudiantes según nota de forma Descendente</h2>"
            contenido+="<div class=\"tabla\"><table class=\"table table-dark table-hover\">"
            contenido+="""<thead><tr>
            <th scope="col">No.</th>
            <th scope="col">NOMBRE</th>
            <th scope="col">NOTA</th>
            </tr></thead><tbody>"""
            
            for i in range(len(alumnos2)):
                contenido+="<tr>"
                contenido+="<th scope=\"row\">"+str(i+1)+"</th>"
                contenido+="<td>"+alumnos2[i]+"</td>"
                if notas2[i]>=61:
                    contenido+="<td style=\"color:#033CF6;\">"+str(notas2[i])+"</td>"
                else:
                    contenido+="<td style=\"color:red;\">"+str(notas2[i])+"</td>"
                contenido+="</tr>"
            
            contenido+="</tbody></table></div>"
            
        elif reportes[i]=="AVG":
            contenido+="<h2>El promedio de los estudiantes del curso es: </h2>"
            suma=0
            for i in range(len(notas2)):
                suma+=notas2[i]
            promedio=round(suma/len(notas2),2)
            if promedio>=61:
                contenido+="<center><button type=\"button\" class=\"btn btn-outline-primary\">"+str(promedio)+"</button></center>"
            else:
                contenido+="<center><button type=\"button\" class=\"btn btn-outline-danger\">"+str(promedio)+"</button></center>"
            

        elif reportes[i]=="MIN":

            for i in range(1,len(notas2)):
                for j in range(0,len(notas2)-i):
                    if(notas2[j+1]<notas2[j]):
                        aux1=notas2[j]
                        aux2=alumnos2[j]
                        notas2[j]=notas2[j+1]
                        alumnos2[j]=alumnos2[j+1]
                        notas2[j+1]=aux1
                        alumnos2[j+1]=aux2
            
            contenido+="<h2>La nota mínima reportada en el curso: </h2>"

            contenido+="<div class=\"tabla\"><table class=\"table table-dark table-hover\">"
            contenido+="""<thead><tr>
            <th scope="col">No.</th>
            <th scope="col">NOMBRE</th>
            <th scope="col">NOTA</th>
            </tr></thead><tbody>"""

            for i in range(len(notas2)):
                if notas2[i]==notas2[0]:
                    contenido+="<tr>"
                    contenido+="<th scope=\"row\">"+str(i+1)+"</th>"
                    contenido+="<td>"+alumnos2[i]+"</td>"
                    if notas2[i]>=61:
                        contenido+="<td style=\"color:#033CF6;\">"+str(notas2[i])+"</td>"
                    else:
                        contenido+="<td style=\"color:red;\">"+str(notas2[i])+"</td>"
                    contenido+="</tr>"
            
            contenido+="</tbody></table></div>"

        elif reportes[i]=="MAX":

            for i in range(1,len(notas2)):
                for j in range(0,len(notas2)-i):
                    if(notas2[j+1]>notas2[j]):
                        aux1=notas2[j]
                        aux2=alumnos2[j]
                        notas2[j]=notas2[j+1]
                        alumnos2[j]=alumnos2[j+1]
                        notas2[j+1]=aux1
                        alumnos2[j+1]=aux2
            
            contenido+="<h2>La nota máxima reportada en el curso: </h2>"

            contenido+="<div class=\"tabla\"><table class=\"table table-dark table-hover\">"
            contenido+="""<thead><tr>
            <th scope="col">No.</th>
            <th scope="col">NOMBRE</th>
            <th scope="col">NOTA</th>
            </tr></thead><tbody>"""

            for i in range(len(notas2)):
                if notas2[i]==notas2[0]:
                    contenido+="<tr>"
                    contenido+="<th scope=\"row\">"+str(i+1)+"</th>"
                    contenido+="<td>"+alumnos2[i]+"</td>"
                    if notas2[i]>=61:
                        contenido+="<td style=\"color:#033CF6;\">"+str(notas2[i])+"</td>"
                    else:
                        contenido+="<td style=\"color:red;\">"+str(notas2[i])+"</td>"
                    contenido+="</tr>"
            
            contenido+="</tbody></table></div>"

        elif reportes[i]=="APR":
            contenido+="<h2>El número de estudiantes aprobados en el curso: </h2>"
            suma=0
            for i in range(len(notas2)):
                if notas2[i]>=61:
                    suma+=1
            
            contenido+="<center><button type=\"button\" class=\"btn btn-outline-success\">"+str(suma)+"</button></center>"

        elif reportes[i]=="REP":
            contenido+="<h2>El número de estudiantes reprobados en el curso: </h2>"
            suma=0
            for i in range(len(notas2)):
                if notas2[i]<61:
                    suma+=1
            
            contenido+="<center><button type=\"button\" class=\"btn btn-outline-danger\">"+str(suma)+"</button></center>"

            



    fin="""
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.bundle.min.js" integrity="sha384-U1DAWAznBHeqEIlVSCgzq+c9gqGAJn5c/t99JyeKa9xxaYpSvHU5awsuZVVFIhvj" crossorigin="anonymous"></script>
    </body>
    </html>"""
    f.write(inicio+contenido+fin)
    f.close()


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
    
    for i in range(len(notas2)):
        if notas2[i]==notas2[0]:
            print("-----\tLa nota maxima es del estudiante: ",alumnos2[i]," con ", notas2[i],"\t-----")

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
    
    for i in range(len(notas2)):
        if notas2[i]==notas2[0]:
            print("-----\tLa nota minima es del estudiante: ",alumnos2[i]," con ", notas2[i],"\t-----")
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
                if curso!="":
                    generarReporteHTML()
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
