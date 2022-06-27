# Se Solicitan los datos al usuario:

num_lect = int(input("Digite el numero de datos a ingresar: "))  # Numero de datos a Ingresar por Altura y Profundidad
cont = 0                                                         # Contador limite por cada dato, Altura y Profundidad

###############################  DEFINICION DE VARIALES, LISTAS Y MATRICES  ###########################

cont_SuA = 0    #Contador Sumamente APTO
cont_MoA = 0    #Contador Moderadamente APTO
cont_MarA = 0   #Contador Marginalmente APTO
cont_NoA = 0    #Contador No APTO

MatrizAlt = []          # Matriz acumuladora para listas de entrada - Altura
MatrizProf = []         # Matriz acumuladora para listas de entrada - Profundidad

MatrizComp = []             # Matriz de comparacion - De categorias
Conteo_Categ = []           # Matriz de conteo de (4) categorias (Columnas: 4) por zona (filas - Infinito)

Lista_Salida_Final1 = []    # Definicion lista final a IMPRIMIR  
Lista_Salida_Final2 = []    # Definicion lista final a IMPRIMIR  

#########################    Funcion para convertir una lista con datos String a una lista con datos Integer   ###########

def List_Str_Int(lista):         
    b = [int(x) for x in lista]
    return b

##################### Funcion para obtener el numero MAYOR de una lista y su respectivo INDICE. ##########################

def CatMasPresent(lista):
        may = max(lista)              
        ind = lista.index(may)
        if ind == 0 and lista[0] > 0:
            if lista[0] == lista[1]:
                Cat = "marginalmente"
            if lista[0] == lista[2]:
                Cat = "moderadamente"
            if lista[0] == lista[3]:
                Cat = "sumamente"
            else:
                Cat = "no apto"
            return Cat
            #print("El indice del numero mayor en la lista es: ", ind)
            #print("Su valor maximo es: ", may)
            #print("Categoria no apto")
        elif ind == 1 and lista[1] > 0:
            if lista[1] == lista[2]:
                Cat = "moderadamente"
            if lista[1] == lista[3]:
                Cat = "sumamente"
            else:
                Cat = "marginalmente"
            return Cat
            #print("El indice del numero mayor en la lista es: ", ind)
            #print("Su valor maximo es: ", may)
            #print("Categoria marginalmente alto")
        elif ind == 2 and lista[2] > 0:
            if lista[2] == lista[3]:
                Cat = "sumamente"
            else:
                Cat = "moderadamente"
            return Cat
            #print("El indice del numero mayor en la lista es: ", ind)
            #print("Su valor maximo es: ", may)
            #print("Categoria moderadamente alto")
        elif ind == 3 and lista[3] > 0:
            Cat = "sumamente"
            return Cat
            #print("El indice del numero mayor en la lista es: ", ind)
            #print("Su valor maximo es: ", may)
            #print("Categoria moderadamente alto")
        else:
            pass

##################### Funcion para obtener el numero MENOR de una lista y su respectivo INDICE. ##########################

def CatMenosPresent(lista):           
        Min = min(lista)              
        ind = lista.index(Min)
        if ind == 0 and lista[0] > 0:
            if lista[0] == lista[1]:
                Cat = "marginalmente"
            if lista[0] == lista[2]:
                Cat = "moderadamente"
            if lista[0] == lista[3]:
                Cat = "sumamente"
            else:
                Cat = "no apto"
            return Cat
            #print("El indice del numero menor en la lista es: ", ind)
            #print("Su valor minimo es: ", Min)
            #print("Categoria no apto")
        elif ind == 1 and lista[1] > 0:
            if lista[1] == lista[2]:
                Cat = "moderadamente"
            if lista[1] == lista[3]:
                Cat = "sumamente"
            else:
                Cat = "marginalmente"
            return Cat
            #print("El indice del numero mayor en la lista es: ", ind)
            #print("Su valor maximo es: ", may)
            #print("Categoria marginalmente alto")
        elif ind == 2 and lista[2] > 0:
            if lista[2] == lista[3]:
                Cat = "sumamente"
            else:
                Cat = "moderadamente"
            return Cat
            #print("El indice del numero mayor en la lista es: ", ind)
            #print("Su valor maximo es: ", may)
            #print("Categoria moderadamente alto")
        elif ind == 3 and lista[3] > 0:
            Cat = "sumamente"
            return Cat
            #print("El indice del numero mayor en la lista es: ", ind)
            #print("Su valor maximo es: ", may)
            #print("Categoria moderadamente alto")
        else:
            pass
        #return Cat

def comparar_categoria(Altura, Profund):
    if Altura >= 400 and Altura <= 800:
        Cat_Alt = "SUM_APTO"
    elif (Altura < 400) or (Altura > 800 and Altura <= 999):
        Cat_Alt = "MOD_APTO"
    elif Altura > 999 and Altura <= 1200:
        Cat_Alt = "MAR_APTO"
    elif Altura > 1200:
        Cat_Alt = "NO_APTO" ###################### Fin comparacion Dato de Altura
    if Profund > 100:
        Cat_Prof = "SUM_APTO"
    elif Profund > 50 and Profund <= 100:
        Cat_Prof = "MOD_APTO"
    elif Profund >= 25 and Profund <= 50:
        Cat_Prof = "MAR_APTO"
    elif Profund < 25:
        Cat_Prof = "NO_APTO"  ###################### Fin comparacion Dato de Profundidad
    if Cat_Alt == "SUM_APTO" and Cat_Prof == "SUM_APTO":
        return "Sumamente"
        #cont_SuA += 1   #Sumamente APTO
    elif Cat_Alt == "SUM_APTO" and Cat_Prof == "MOD_APTO":
        return "Moderadamente"
        #cont_MoA += 1   #Moderadamente APTO
    elif Cat_Alt == "SUM_APTO" and Cat_Prof == "MAR_APTO":
        return "Marginalmente"
        #cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "SUM_APTO" and Cat_Prof == "NO_APTO":
        return "NO"
        #cont_NoA += 1   #No APTO
    elif Cat_Alt == "MOD_APTO" and Cat_Prof == "SUM_APTO":
        return "Moderadamente"
        #cont_MoA += 1 #Moderadamente APTO
    elif Cat_Alt == "MOD_APTO" and Cat_Prof == "MOD_APTO":
        return "Moderadamente"
        #cont_MoA += 1   #Moderadamente APTO
    elif Cat_Alt == "MOD_APTO" and Cat_Prof == "MAR_APTO":
        return "Marginalmente"
        #cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "MOD_APTO" and Cat_Prof == "NO_APTO":
        return "NO"
        #cont_NoA += 1   #No APTO
    elif Cat_Alt == "MAR_APTO" and Cat_Prof == "SUM_APTO":
        return "Marginalmente"
        #cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "MAR_APTO" and Cat_Prof == "MOD_APTO":
        return "Marginalmente"
        #cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "MAR_APTO" and Cat_Prof == "MAR_APTO":
        return "Marginalmente"
        #cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "MAR_APTO" and Cat_Prof == "NO_APTO":
        return "NO"
        #cont_NoA += 1   #No APTO
    elif Cat_Alt == "NO_APTO" and Cat_Prof == "SUM_APTO":
        return "NO"
        #cont_NoA += 1   #No APTO
    elif Cat_Alt == "NO_APTO" and Cat_Prof == "MOD_APTO":
        return "NO"
        #cont_NoA += 1   #No APTO
    elif Cat_Alt == "NO_APTO" and Cat_Prof == "MAR_APTO":
        return "NO"
        #cont_NoA += 1   #No APTO
    elif Cat_Alt == "NO_APTO" and Cat_Prof == "NO_APTO":
        return "NO"
        #cont_NoA += 1   #No APTO

##################################################################################################################################
# FASE 1 - Ingreso de listas y guardadas en dos matrices distintas

for ingrFilas in range(num_lect):                      #  Rango de datos a ingresar por cada categoria de Altura
    MatrizAlt.append(List_Str_Int(input("Ingrese datos de altura: ").split(" ")))  # Se ingresan las listas tipo 'Str', seguido se convierten listas tipo 'Int' la cual es añadida como nueva fila a la Matriz de altura.


for ingrFilas in range(num_lect):                         #  Rango de datos a ingresar por cada categoria de Profundidad
    MatrizProf.append(List_Str_Int(input("Ingrese datos de profundidad: ").split(" ")))  # Se ingresa las lista tipo 'Str', seguido se convierten listas tipo 'Int' la cual es añadida como nueva fila a la Matriz de Profundidad

#################################################################################################################################
# FASE 2 y 3 = (fase 2: Comparacion de categorias y escoger la peor) - (fase 3: Guardar el resultado de la comparacion en una nueva matriz.)

i = 0                                                       # Contador de filas, de la matriz de comparacion (Infinito - numero de zonas ingresadas)
for val1, val2 in zip(MatrizAlt, MatrizProf):               # Se recorren las filas de ambas matrices (Altura y Profundidad) tomando sus indices de las filas (de arriba(0) hacia abajo(infinito)) (Al mismo tiempo) (Infinito - numero de datos(zonas) ingresados)
    MatrizComp.append(['0', '1', '2', '3', '4', '5', '6'])      # Se añade una nueva fila a la matriz de comparacion para que cuente con los indices de fila(0) y columna (0 a 6).
    for j in range(7):                                         # Se recorre cada columna de 0 a 6 (el 7 no se cuenta)
        MatrizComp[i][j] = comparar_categoria(val1[j], val2[j])  # Se recorren las columnas de ambas matrices (Altura y Profundidad) tomando sus indices de las columnas (de izquierda(0) hacia derecha(6)) (Al mismo tiempo) Se comparan ambos resultados con la funcion "Comparar" el cual devuelve un 'Str' y este mismo es asignado a las coordenadas de la nueva matriz...
    i += 1                                                          # Contador de filas, de la matriz de comparacion

########################################################################################################################
# FASE 4 y 5 = (fase 4: Contar las categorias por zona (filas - Infinito)) - (fase 5: El conteo resultante asignarlo a una nueva matriz por zona (filas - infinito))

c = 0               # Contador de filas, de la matriz de conteo de categorias(Infinito - numero de zonas ingresadas)
for i in range(num_lect):
    Conteo_Categ.append([0, 0, 0, 0])
    for j in range(7):
        valor = str(MatrizComp[i][j])
        if valor == "NO":
            cont_NoA += 1            
        elif valor == "Marginalmente":
            cont_MarA += 1
        elif valor == "Moderadamente":
            cont_MoA += 1
        else:
            cont_SuA += 1
    Conteo_Categ[c][0] += cont_NoA
    Conteo_Categ[c][1] += cont_MarA
    Conteo_Categ[c][2] += cont_MoA
    Conteo_Categ[c][3] += cont_SuA
    cont_NoA = 0
    cont_MarA = 0
    cont_MoA = 0
    cont_SuA = 0
    c += 1

##########################################################################################################
# Fase 6 y 7 = (fase 6: Se hace conteo de las categorias (por columnas) sin importar las zonas) - (fase 7: El resultado del conteo de las categorias, se asigna a la lista de impresion final)

for c in range(4):
    if c == 0:
        for f in range(num_lect):
            valor = int(Conteo_Categ[f][0])
            cont_NoA += valor
        Lista_Salida_Final1.append(str(cont_NoA))
    elif c == 1:
        for f in range(num_lect):
            valor = int(Conteo_Categ[f][1])
            cont_MarA += valor
        Lista_Salida_Final1.append(str(cont_MarA))
    elif c == 2:
        for f in range(num_lect):
            valor = int(Conteo_Categ[f][2])
            cont_MoA += valor
        Lista_Salida_Final1.append(str(cont_MoA))
    elif c == 3:
        for f in range(num_lect):
            valor = int(Conteo_Categ[f][3])
            cont_SuA += valor
        Lista_Salida_Final1.append(str(cont_SuA))

#print(MatrizComp)

#########################################################################################################################
# Fase 8 = Escoger la categoria que MAS se presentó por cada zona
print(" ")

for lista1 in Conteo_Categ:
    Lista_Salida_Final2.append(CatMasPresent(lista1))
    print(" ")

#########################################################################################################################
# Fase 9 = Escoger la categoria que MENOS se presentó por cada zona

for lista2 in Conteo_Categ:
    Lista_Salida_Final2.append(str(CatMenosPresent(lista2)))
    print(" ")

print(" ".join(Lista_Salida_Final1))
print(",".join(Lista_Salida_Final2))





