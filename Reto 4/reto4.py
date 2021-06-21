# Se Solicitan los datos al usuario:

num_lect = int(input("Digite cantidad de datos a Ingresar: "))  # Numero de datos a Ingresar por Altura y Profundidad
cont = 0                                                        # Contador limite por cada dato, Altura y Profundidad

cont_SuA = 0    #Contador Sumamente APTO
cont_MoA = 0    #Contador Moderadamente APTO
cont_MarA = 0   #Contador Marginalmente APTO
cont_NoA = 0    #Contador No APTO

SUM_Alt = 0                 #Acumulador Altura sobre el nivel de mar  -  Posible Borrar
SUM_Prof = 0                #Acumulador Profundidad efectiva del suelo  -  posible Borrar

MatrizAlt = []              # Matriz acumuladora para listas de entrada - Altura
MatrizProf = []             # Matriz acumuladora para listas de entrada - Profundidad

MatrizComp = []             # Matriz de comparacion
MatrizComp.append([])
ListaConteo = []            # Lista utilizada temporalmente para añadir las categorias de cada comparacion numerica, para posteriormente, añadir esta lista a la Matriz de Comparacion.

Lista_Salida_Altura = []    # Definicion lista final  -  Posible Borrar
Lista_Salida_Prof = []      # Definicion lista final  -  Posible Borrar

def List_Str_Int(lista):            # Funcion para convertir una lista con datos String a datos Integer
    b= [int(x) for x in lista]
    return b

def CreaLista(num_lect):
    L = []
    for i in range(k+1):
        L.append(0)
    return L
    

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


for ingrFilas in range(num_lect):
    MatrizAlt.append(List_Str_Int(input("Ingrese datos de Alturas: ").split(" ")))  # Este ciclo for hace lo mismo que en la linea 24


for ingrFilas in range(num_lect):
    MatrizProf.append(List_Str_Int(input("Ingrese datos de Profundidades: ").split(" ")))


for val1, val2, i in zip(MatrizAlt, MatrizProf, MatrizComp):
    MatrizComp.append([])
    i = 1
    for j in range(7):
        #print(val1[0], val2[0])
        MatrizComp[i][j].append(comparar_categoria(val1[0], val2[0]))
        #print(val1[1], val2[1])
        MatrizComp[i][j].append(comparar_categoria(val1[1], val2[1]))
        #print(val1[2], val2[2])
        MatrizComp[i][j].append(comparar_categoria(val1[2], val2[2]))
        #print(val1[3], val2[3])
        MatrizComp[i][j].append(comparar_categoria(val1[3], val2[3]))
        #print(val1[4], val2[4])
        MatrizComp[i][j].append(comparar_categoria(val1[4], val2[4]))
        #print(val1[5], val2[5])
        MatrizComp[i][j].append(comparar_categoria(val1[5], val2[5]))
        #print(val1[6], val2[6])
        MatrizComp[i][j].append(comparar_categoria(val1[6], val2[6]))
        j += 1

print(MatrizComp)
    




print(" ")
#print(MatrizComp)




"""

    print(val1[1], val2[1])
    print(val1[2], val2[2])
    print(val1[3], val2[3])
    print(val1[4], val2[4])
    print(val1[5], val2[5])
    print(val1[6], val2[6])

print(" ")
print(val1[0])
print(type(val1[0]))


"""

"""comparar_categoria(int(tupla[0][0]), int(tupla[1][0]))
    ListaConteo.append(str(comparar_categoria))


print(" ")
print(ListaConteo)
#print(MatrizComp)"""

"""
#Se Evalua la categoria a la que pertenece altura de cada fila y columna (dato a dato, 1 x 1) ingresada:
for fila in MatrizAlt:
    for colum_Alt in fila:
        if colum_Alt >= 400 and colum_Alt <= 800:
            Cat_Alt = "SUM_APTO"
        elif (colum_Alt < 400) or (colum_Alt > 800 and colum_Alt <= 999):
            Cat_Alt = "MOD_APTO"
        elif colum_Alt > 999 and colum_Alt <= 1200:
            Cat_Alt = "MAR_APTO"
        elif colum_Alt > 1200:
            Cat_Alt = "NO_APTO"
        print(Cat_Alt, end=', ')
    print(' ')

#Se Evalua la categoria a la que pertenecen los datos de profundidad ingresados por cada fila y columna (dato a dato, 1 x 1) ingresada:
for fila in MatrizProf:
    for colum_Prof in fila:
        if colum_Prof > 100:
            Cat_Prof = "SUM_APTO"
        elif colum_Prof > 50 and colum_Prof <= 100:
            Cat_Prof = "MOD_APTO"
        elif colum_Prof >= 25 and colum_Prof <= 50:
            Cat_Prof = "MAR_APTO"
        elif colum_Prof < 25:
            Cat_Prof = "NO_APTO"
        print(Cat_Prof, end=', ')
    print(' ')


"""



#print(column, end= ' ')
        #Se Evalua la categoria a la que pertenece la altura ingresada:
""" if Prom_Alt >= 400 and Prom_Alt <= 800:
            Cat_Alt = "SUM_APTO"
        elif (Prom_Alt < 400) or (Prom_Alt > 800 and Prom_Alt <= 999):
            Cat_Alt = "MOD_APTO"
        elif Prom_Alt > 999 and Prom_Alt <= 1200:
            Cat_Alt = "MAR_APTO"
        elif Prom_Alt > 1200:
            Cat_Alt = "NO_APTO"
        print(' ')"""













"""print('\n')
valor = MatrizAlt[0][1]
print(valor)"""



    



"""while cont < num_lect:                                            # Limite de ingreso de datos de Profundidad
    profund = input("Ingrese datos de Profundidad: ").split(" ")  # Solicitud e ingreso de datos de profundidad, ingresa como texto en una lista
    Prof = List_Str_Int(profund)
    MatrizProf.append(Prof)
    cont += 1
cont = 0
print(MatrizProf)
print(len(MatrizProf[0]))"""

    
# for i in altura.split(", "):  # La funcion split toma ese ingreso y lo convierte en una lista, con los datos separados por espacio, dicha lista es asignada a la variable "i" del for.
    #    datos_altura = int(i)   # Se convierte la lista en datos enteros y se asigna a la variable datos_altura
        
    #long_Alt = len(altura)      # Se lee la longitud de la lista en la variable "altura" y se asigna el dato numerico a la varible "long_Alt"
        
    # for j in profund.split(", "):
    #    datos_profund = int(j)

    #long_Prof = len(profund)    # Se lee la longitud de la lista en la variable "profund" y se asigna el dato numerico a la varible "long_Prof"

    #SUM_Alt = sum(List_Str_Int(altura)) # Se toma la variable altura que posee una lista en Str, se pasa por la funcion, para convertirla en lista de Int, sumo los datos con la funcion Sum() y el resultado se le asigna a la variable SUM_Alt..........
    #SUM_Prof = sum(List_Str_Int(profund)) 
    
    #Prom_Alt = SUM_Alt / long_Alt         # Promedio de la Altura del Vector
    #Prom_Prof = SUM_Prof / long_Prof      # Promedio de la Profundidad del Vectot

    #Se Evalua la categoria a la que pertenece la altura ingresada:
"""if Prom_Alt >= 400 and Prom_Alt <= 800:
        Cat_Alt = "SUM_APTO"
    elif (Prom_Alt < 400) or (Prom_Alt > 800 and Prom_Alt <= 999):
        Cat_Alt = "MOD_APTO"
    elif Prom_Alt > 999 and Prom_Alt <= 1200:
        Cat_Alt = "MAR_APTO"
    elif Prom_Alt > 1200:
        Cat_Alt = "NO_APTO"

    #Se Evalua la categoria a la que pertenece la profundidad ingresada:
    if Prom_Prof > 100:
        Cat_Prof = "SUM_APTO"
    elif Prom_Prof > 50 and Prom_Prof <= 100:
        Cat_Prof = "MOD_APTO"
    elif Prom_Prof >= 25 and Prom_Prof <= 50:
        Cat_Prof = "MAR_APTO"
    elif Prom_Prof < 25:
        Cat_Prof = "NO_APTO"

    #Se Evalua las categorias uno a uno, es decir, uno contra uno y logicamente 
    # se le ordena a la maquina, que hacer exactamente cuando evalue las comparaciones.
    if Cat_Alt == "SUM_APTO" and Cat_Prof == "SUM_APTO":
        cont_SuA += 1   #Sumamente APTO
    elif Cat_Alt == "SUM_APTO" and Cat_Prof == "MOD_APTO":
        cont_MoA += 1   #Moderadamente APTO
    elif Cat_Alt == "SUM_APTO" and Cat_Prof == "MAR_APTO":
        cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "SUM_APTO" and Cat_Prof == "NO_APTO":
        cont_NoA += 1   #No APTO
    elif Cat_Alt == "MOD_APTO" and Cat_Prof == "SUM_APTO":
        cont_MoA += 1 #Moderadamente APTO
    elif Cat_Alt == "MOD_APTO" and Cat_Prof == "MOD_APTO":
        cont_MoA += 1   #Moderadamente APTO
    elif Cat_Alt == "MOD_APTO" and Cat_Prof == "MAR_APTO":
        cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "MOD_APTO" and Cat_Prof == "NO_APTO":
        cont_NoA += 1   #No APTO
    elif Cat_Alt == "MAR_APTO" and Cat_Prof == "SUM_APTO":
        cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "MAR_APTO" and Cat_Prof == "MOD_APTO":
        cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "MAR_APTO" and Cat_Prof == "MAR_APTO":
        cont_MarA += 1  #Marginalmente APTO
    elif Cat_Alt == "MAR_APTO" and Cat_Prof == "NO_APTO":
        cont_NoA += 1   #No APTO
    elif Cat_Alt == "NO_APTO" and Cat_Prof == "SUM_APTO":
        cont_NoA += 1   #No APTO
    elif Cat_Alt == "NO_APTO" and Cat_Prof == "MOD_APTO":
        cont_NoA += 1   #No APTO
    elif Cat_Alt == "NO_APTO" and Cat_Prof == "MAR_APTO":
        cont_NoA += 1   #No APTO
    elif Cat_Alt == "NO_APTO" and Cat_Prof == "NO_APTO":
        cont_NoA += 1   #No APTO

    Decimal_Alt = ("{0:.2f}".format(Prom_Alt))   #Se formatea la impresion a dos decimales para la Altura
    Decimal_Prof = ("{0:.2f}".format(Prom_Prof))  #Se formatea la impresion a dos decimales para la Profundidad

    Lista_Salida_Altura.append(Decimal_Alt)        #Se van añadiendo los resultados finales al vector de salida
    Lista_Salida_Prof.append(Decimal_Prof)         #Se van añadiendo los resultados finales al vector de salida

    cont += 1    # Contador limite de lecturas o ingresos de listas - Vectores


print()  ############################      Area de Impresion      #################################



print(" ".join(Lista_Salida_Altura))    # Impresion resultado final - los codigos: " ".join(lista) realiza una separacion de espacio entre cada dato de la lista.
print()
print(" ".join(Lista_Salida_Prof))      # Impresion resultado final
print()
print("sumamente apto", cont_SuA)       # Contador Final Sumamente APTO
print()
print("moderadamente apto", cont_MoA)   # Contador Final Moderadamente APTO
print()
print("marginalmente apto", cont_MarA)  # Contador Final Marginalmente APTO
print()
print("no apto", cont_NoA)              # Contador Final No APTO

print()

"""




