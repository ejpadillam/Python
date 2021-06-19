# Se Solicitan los datos al usuario:

num_lect = int(input())     # Numero de datos a Ingresar
cont = 0                    # Contador limite

cont_SuA = 0    #Contador Sumamente APTO
cont_MoA = 0    #Contador Moderadamente APTO
cont_MarA = 0   #Contador Marginalmente APTO
cont_NoA = 0    #Contador No APTO
SUM_Alt = 0                 #Acumulador Altura sobre el nivel de mar
SUM_Prof = 0                #Acumulador Profundidad efectiva del suelo
Lista_Salida_Altura = []    # Definicion lista final
Lista_Salida_Prof = []      # Definicion lista final

def List_Str_Int(lista):            # Funcion para convertir una lista con datos String a datos Integer
    b= [int(x) for x in lista]
    return b

while cont < num_lect:

    altura = input().split(" ")        # Solicitud e ingreso de datos de altura, ingresa como texto en una lista
    profund = input().split(" ")  # Solicitud e ingreso de datos de profuncidad, ingresa como texto en una lista
    
    # for i in altura.split(", "):  # La funcion split toma ese ingreso y lo convierte en una lista, con los datos separados por espacio, dicha lista es asignada a la variable "i" del for.
    #    datos_altura = int(i)   # Se convierte la lista en datos enteros y se asigna a la variable datos_altura
        
    long_Alt = len(altura)      # Se lee la longitud de la lista en la variable "altura" y se asigna el dato numerico a la varible "long_Alt"
        
    # for j in profund.split(", "):
    #    datos_profund = int(j)

    long_Prof = len(profund)    # Se lee la longitud de la lista en la variable "profund" y se asigna el dato numerico a la varible "long_Prof"

    SUM_Alt = sum(List_Str_Int(altura)) # Se toma la variable altura que posee una lista en Str, se pasa por la funcion, para convertirla en lista de Int, sumo los datos con la funcion Sum() y el resultado se le asigna a la variable SUM_Alt..........
    SUM_Prof = sum(List_Str_Int(profund)) 
    
    Prom_Alt = SUM_Alt / long_Alt         # Promedio de la Altura del Vector
    Prom_Prof = SUM_Prof / long_Prof      # Promedio de la Profundidad del Vectot

    #Se Evalua la categoria a la que pertenece la altura ingresada:
    if Prom_Alt >= 400 and Prom_Alt <= 800:
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






