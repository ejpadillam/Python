''' LactoCaribe Ltda. usa 5 camiones para la distribución de leche a sus 10 puntos de distribución.
La empresa se encuentra interesada en medir la eficiencia de c/u de los 5 camiones. Por este motivo, LactoCaribe te solicita crear un sistema que dada una matriz de asignación con los siguientes campos: 
•	Punto de distribución
•	Identificación de camión
•	Cantidad de litros asignados
•	Tiempo de despacho asignado
y una matriz de registro con los siguientes campos: 
•	Punto de distribución
•	Identificación de camión
•	Cantidad de litros despachados
•	Tiempo de despacho registrado
Calcule los siguientes indicadores de desempeño para cada camión:
1.	Eficiencia en tiempos de despacho = (Tiempo de despacho asignado - Tiempo de despacho registrado) / Tiempo de despacho asignado x 100
2.	Tasa de entrega (Lt/min) = Cantidad de litros despachados / Tiempo total de despacho x100
3.	Nivel de Cumplimiento de los despachos = Litros despachados / Total de litros asignados x 100

Actividad
Usando los conceptos aprendidos dentro del curso:
1.	Diseña la solución al problema presentado
2.	Codifica la solución
3.	Durante la etapa de pruebas, el usuario requiere que modifiques la solución para incluir las siguientes validaciones
i.	Que los valores de litros y tiempos asignados no sean 0 o negativos.
ii.	Que los valores de litros y tiempos de despacho no sean 0 o negativos.
iii.	Si una de las condiciones no se cumple, el valor incluido para ese punto de distribución y para ese camión deberá ser ignorado en el cálculo.

4.	Durante la revisión del entregable que fue aprobado, LactoCaribe Ltda. manifiesta que requiere conocer un nuevo indicador de desempeño para cada camión:  

a.	Entregas a tiempo = Nº de entregas a tiempo / Nº total de entregas realizadas x 100 

Entendiendo que las “entregas a tiempo” excluyen a aquellas que registraron retraso.
 
Entendiendo que una entrega registra retraso, cuando el tiempo registrado es mayor al tiempo asignado '''



import os
#matrices[ptodistrib,idcamion,cantlitros,tiempo]
#           0           1       2         3

def control(matrizAsig, matrizReg):     # Se reciben como Parametros (Matriz de Asignacion - Matriz de Registro)
    os.system("cls")
    mAsig=matrizAsig
    mReg=matrizReg
    print("------------------Matrices iniciales----------------")
    print(mAsig)
    print(mReg)
    print("-----------------------------------------------------")


    """ Modificaciones en la Etapa de Prueba """
    Regresar = False
    for i in range (len(mAsig)): 
        #i. Que los valores de LITROS asignados no sean 0 o negativos en Ambas Matrices. 
        if (mAsig[i][2]<= 0): 
            print(f"Error en litros asignados: Punto # {mAsig[i][0]} Camión {mAsig[i][1]}")
            Regresar = True
        if (mReg[i][2]<= 0):
            print(f"Error en litros registrados: Punto # {mReg[i][0]} Camión {mReg[i][1]}")
            Regresar = True

        #ii.Que los valores de TIEMPOS de despacho no sean 0 o negativos en Ambas Matrices.
        if (mAsig[i][3]<= 0): 
            print(f"Error en tiempo de despacho asignados: Punto # {mAsig[i][0]} Camión {mAsig[i][1]}")
            Regresar = True
        if (mReg[i][3]<= 0): 
            print(f"Error en tiempo de despacho registrados: Punto # {mReg[i][0]} Camión {mReg[i][1]}")
            Regresar = True
    if Regresar == True:
        print("Se encontrarosn tiempo de Despacho en 0 o Negativos.")
        return


    print(" *** Eficiencia en tiempo de Despacho ***")
    for f in range(1, 6) : # f=1     Hacer calculo por Camion
        tda=0               # Tiempo de despacho asignado
        tdr=0               # Tiempo de despacho registrado

        #Ciclo para sumar los Tiempo de Despacho Asignados por Camion en cad Punto de Distribuc (tda)
        for pto in range (len(mAsig)): #pto=0  Aqui sumará todos los tiempos en cada matriz / camión
            if (mAsig[pto][1] == f): #[0][1] == 1
                tda += mAsig[pto][3]

        #Ciclo para sumar los Tiempo de Despacho Registrados por Camion en cada Punto de Distribuc (tdr)
        for pto in range(len(mReg)):
            if (mReg[pto][1] == f):
                tdr += mReg[pto][3]
        print("Para Id camión #",f, "=", round((tda - tdr) / tda * 100, 1),"%" )
    print()


    print(" *** Tasa de entrega (Lt / min) ***")
    for f in range(1,6) :   # Hacer calculo por Camion
        cLtd=0              # Cant de Litros despachados
        ttd=0               # Tiempo total de despacho

        # Ciclo para calcular la Cant de Litros despachados
        for pto in range(len(mReg)): 
            if (mReg[pto][1] == f):
                cLtd += mReg[pto][2] #Aqui sumará todos los litros en matriz reg/camión

        # Ciclo para el Tiempo total de despacho
        for pto in range(len(mReg)):
            if (mReg[pto][1] == f):
                ttd += mReg[pto][3] #Aqui sumará todos los tiempos en matriz reg/camión
        print("Para Id camión #",f, "=", round(cLtd / ttd,1))
    print()

    print(" *** Nivel de cumplimiento de los Despachos ***")
    for f in range(1,6) :   # Hacer calculo por Camion
        tLrasg=0        #  Total de Litros asignados
        ltrdsp=0        #  Litros Despachados
        # Ciclo para calcular el Total de Litros Asignados
        for pto in range(len(mAsig)): 
            if (mAsig[pto][1] == f):
                tLrasg += mAsig[pto][2]  #Aqui sumará todos los litros en cada matriz/camión

        # Ciclo para calcular el Total de Litros Despachados
        for pto in range(len(mAsig)):
            if (mReg[pto][1] == f):
                ltrdsp += mReg[pto][2]
        print("Para Id camión #",f, "=", round((ltrdsp / tLrasg) * 100, 1),"%" )
    print()


    print(" *** Entregas a tiempo ***")
    for f in range(1,6) : #f=1      Hacer calculo por Camion
        entregasATiempo=[]
        listaTiempoAsig=[]
        listaTiempoReg=[]
        for i in range (len(mAsig)): #i=0 
            if f == mAsig[i][1]  and mAsig[i][2] > 0 and mAsig[i][3] > 0:
                listaTiempoAsig.append(mAsig[i][3])
            
            if f == mReg[i][1] and mReg[i][2] > 0 and mReg[i][3] > 0:
                listaTiempoReg.append(mReg[i][3])
        #print(listaTiempoAsig)
        #print(listaTiempoReg)
            
        for i in range(len(listaTiempoAsig)):
            if listaTiempoAsig[i]-listaTiempoReg[i] >= 0:
                entregasATiempo.append(listaTiempoAsig[i]-listaTiempoReg[i])
        #print(entregasATiempo)
        print("Para Id camión #",f, "=",round(len(entregasATiempo)/len(listaTiempoAsig)*100,1),"%" )
    print()

control([[1,5,1,10],        # Matriz de Asignacion
         [2,4,2,35],
         [3,1,1462,10],
         [4,3,1222,35],
         [5,2,2000,44],
         [6,3,1389,52],
         [7,1,1500,35],
         [8,1,1419,50],
         [9,5,1355,44],
         [10,4,1000,52]],

        [[1,5,1168,52],     # Matriz de Registro
         [2,4,1254,51],
         [3,1,1379,33],
         [4,3,1281,52],
         [5,2,1200,30],
         [6,3,1320,34],
         [7,1,1225,52],
         [8,1,1149,51],
         [9,5,1424,34],
         [10,4,1000,36]] )