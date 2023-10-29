def generar_menu_stark():
    print("--------------------------STARK INDUSTRIES--------------------------")
    opcion = (input("\na). Mostrar listado de nombres de superheroes\
                     \nb). Mostrar listado de nombres y alturas de superheroes\
                     \nc). Mostrar nombre y altura de superheroe/s mas altos\
                     \nd). Mostrar nombre y altura de superheroe/s mas bajos\
                     \ne). Mostrar altura promedio de los superheroes\
                     \nf). Mostrar nombre y peso de superheroes mas y menos pesados\
                     \ng). Mostrar nombre de superheroes de genero masculino\
                     \nh). Mostrar nombre de superheroes de genero femenino\
                     \ni). Mostrar superheroe masculino mas alto\
                     \nj). Mostrar superheroe femenino mas alto\
                     \nk). Mostrar superheroe masculino mas bajo\
                     \nl). Mostrar superheroe femenino mas bajo\
                     \nm). Mostrar promedio de altura de heroes masculinos\
                     \nn). Mostrar promedio de altura de heroes femeninos\
                     \no). Mostrar cantidad de heroes por color de ojos\
                     \np). Mostrar cantidad de heroes por color de pelo\
                     \nq). Mostrar cantidad de heroes por tipo de inteligencia\
                     \nr). Salir\n\nElija una opcion: "))
    opcion = opcion.lower()
    return opcion
    

def separar_maximo (lista:list, clave:str, tipo_de_dato = float):
    maximo = 0
    bandera_primero = True
    for i in lista:
        maximo_lista = tipo_de_dato(i[clave])
        if maximo_lista > maximo or bandera_primero == True:
            maximo = maximo_lista
            bandera_primero = False
    
    return maximo

def separar_minimo (lista:list, clave:str, tipo_de_dato = float):
    minimo = 0
    bandera_primero = True
    for i in lista:
        minimo_lista = tipo_de_dato(i[clave])
        if minimo_lista < minimo or bandera_primero == True:
            minimo = minimo_lista
            bandera_primero = False
    
    return minimo

def calcular_promedio (lista:list, clave:str, tipo_de_dato = float):
    acumulador = 0

    for i in lista:
        valor = tipo_de_dato(i[clave])

        acumulador += valor

    return acumulador/len(lista)

def separar_maximo_condicional (lista:list, clave_1:str, clave_2:str, condicion:str, tipo_de_dato = float):
    maximo = 0
    for i in lista:
        maximo_lista = tipo_de_dato(i[clave_1])
        condicion_lista = i[clave_2]

        if maximo_lista > maximo and condicion_lista == condicion:
            maximo = maximo_lista
            
    return maximo

def separar_minimo_condicional (lista:list, clave_1:str, clave_2:str, condicion:str, tipo_de_dato = float):
    minimo = 0
    bandera_primero = True
    for i in lista:
        minimo_lista = tipo_de_dato(i[clave_1])
        condicion_lista = i[clave_2]

        if (minimo_lista < minimo and condicion_lista == condicion) or (bandera_primero == True and condicion_lista == condicion):
            minimo = minimo_lista
            bandera_primero = False
            
    return minimo

def calcular_promedio_condicional (lista:list, clave_1:str, clave_2:str, condicion:str, tipo_de_dato = float):
    acumulador = 0
    contador = 0

    for i in lista:
        valor = tipo_de_dato(i[clave_1])
        condicion_lista = i[clave_2]
        if condicion_lista == condicion:
            acumulador += valor
            contador += 1

    return acumulador/contador