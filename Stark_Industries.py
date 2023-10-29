from data_stark import lista_personajes
from os import system
from funciones import*

while True:
    system("cls")
    respuesta = generar_menu_stark()

    match respuesta:
        
        case "a":
            print("\n---------NOMBRES DE SUPERHEROES---------\n")
            for superheroe in lista_personajes:
                nombre_heroe = superheroe["nombre"]

                print(f"{nombre_heroe:^40} ")
            print("\n")
          
        case "b":
            print("\n------NOMBRES-----------ALTURAS------\n")
            
            for superheroe in lista_personajes:
                nombre_heroe = superheroe["nombre"]
                altura_heroe = float(superheroe["altura"])

                print(f"{nombre_heroe:^20}   {altura_heroe:6.2f} cm")
            print("\n")

        case "c":
            print("\n------HEROE/S DE MAYOR ALTURA------")
            print("\n      NOMBRE    ALTURA\n")

            altura_maxima = separar_maximo(lista_personajes, "altura", float)

            for superheroe in lista_personajes:
                    altura_heroe = float(superheroe["altura"])
                    nombre_heroe = superheroe["nombre"]

                    if altura_heroe == altura_maxima:
                        print(f"    {nombre_heroe:^10}  {altura_heroe:6.2f} cm")
            print("\n")

        case "d":
            print("\n------HEROE/S DE MENOR ALTURA------")
            print("\n      NOMBRE        ALTURA\n")

            altura_minima = separar_minimo(lista_personajes, "altura", float)

            for superheroe in lista_personajes:
                    altura_heroe = float(superheroe["altura"])
                    nombre_heroe = superheroe["nombre"]
        

                    if altura_heroe == altura_minima:
                        print(f" {nombre_heroe:^10}  {altura_heroe:6.2f} cm")
            print("\n")

        case "e":
            print("\n----ALTURA PROMEDIO----")

            promedio = calcular_promedio(lista_personajes, "altura", float)

            print(f"{promedio:5.2f} cm")

            print("\n")

        case "f":
            peso_maximo = separar_maximo(lista_personajes, "peso")
            peso_minimo = separar_minimo(lista_personajes, "peso")

            print("\n----HEROE/S MAS PESADO----")
            for superheroe in lista_personajes:
                    peso_heroe = float(superheroe["peso"])
                    nombre_heroe = superheroe["nombre"]           
                    if peso_heroe == peso_maximo:
                        print(f" {nombre_heroe:10}  {peso_heroe:6.2f} kg")

            print("\n----HEROE/S MENOS PESADO----")
            for superheroe in lista_personajes:
                    peso_heroe = float(superheroe["peso"])
                    nombre_heroe = superheroe["nombre"]                           
                    if peso_heroe == peso_minimo:
                        print(f" {nombre_heroe:10}  {peso_heroe:6.2f} kg")

            print("\n")
        case "g":       
              print("\n--HEROES DE GENERO MASCULINO--\n")
            
              for superheroe in lista_personajes:
                nombre_heroe = superheroe["nombre"]
                genero_heroe = superheroe["genero"]

                if genero_heroe == "M":
                     print(f"     {nombre_heroe:^20}")

              print("\n")

        case "h":        
              print("\n--HEROES DE GENERO FEMENINO--\n")
            
              for superheroe in lista_personajes:
                nombre_heroe = superheroe["nombre"]
                genero_heroe = superheroe["genero"]

                if genero_heroe == "F":
                     print(f"     {nombre_heroe:^20}")

              print("\n")

        case "i":      
              print("\n--HEROE/S MASCULINO MAS ALTO--\n")
            
              altura_maxima = separar_maximo_condicional(lista_personajes, "altura", "genero", "M")

              for superheroe in lista_personajes:
                  nombre_heroe = superheroe["nombre"]
                  altura_heroe = float(superheroe["altura"])

                  if altura_heroe == altura_maxima:
                      print(f"{nombre_heroe:^20}")
            

              print("\n")

        case "j":          
              print("\n--HEROE/S FEMENINOS MAS ALTO--\n")
            
              altura_maxima = separar_maximo_condicional(lista_personajes, "altura", "genero", "F")

              for superheroe in lista_personajes:
                  nombre_heroe = superheroe["nombre"]
                  altura_heroe = float(superheroe["altura"])

                  if altura_heroe == altura_maxima:
                      print(f"{nombre_heroe:^20}")
            

              print("\n")

        case "k":        
              print("\n--HEROE/S MASCULINO MAS BAJO--\n")
            
              altura_minima = separar_minimo_condicional(lista_personajes, "altura", "genero", "M")

              for superheroe in lista_personajes:
                  nombre_heroe = superheroe["nombre"]
                  altura_heroe = float(superheroe["altura"])

                  if altura_heroe == altura_minima:
                      print(f"{nombre_heroe:^20}")
            

              print("\n")

        case "l":        
              print("\n--HEROE/S FEMENINO MAS BAJO--\n")
            
              altura_minima = separar_minimo_condicional(lista_personajes, "altura", "genero", "F")

              for superheroe in lista_personajes:
                  nombre_heroe = superheroe["nombre"]
                  altura_heroe = float(superheroe["altura"])

                  if altura_heroe == altura_minima:
                      print(f"{nombre_heroe:^20}")

              print("\n")

        case "m":        
              print("\n--PROMEDIO DE ALTURA DE HEROES MASCULINOS--\n")
             
              promedio = calcular_promedio_condicional(lista_personajes, "altura", "genero", "M")
              print(f"            {promedio:5.2f} cm")

              print("\n")

        case "n":        
              print("\n--PROMEDIO DE ALTURA DE HEROES FEMENINOS--\n")
            
              promedio = calcular_promedio_condicional(lista_personajes, "altura", "genero", "F")
              print(f"            {promedio:5.2f} cm")


              print("\n")

        case "o":        
              contador_azul = 0
              contador_amarillo = 0
              contador_verde = 0
              contador_plateado = 0
              contador_marron = 0
              contador_rojo = 0
              contador_avellana = 0

              print("CANTIDAD DE HEROES POR COLOR DE OJOS")
              for superheroe in lista_personajes:
                color_ojos_heroe = superheroe["color_ojos"]

                if color_ojos_heroe == "Blue":
                    contador_azul += 1
                if color_ojos_heroe == "Yellow" or color_ojos_heroe == "Yellow (without irises)":
                    contador_amarillo += 1
                if color_ojos_heroe == "Green":
                    contador_verde += 1
                if color_ojos_heroe == "Silver":
                    contador_plateado += 1
                if color_ojos_heroe == "Brown":
                    contador_marron += 1
                if color_ojos_heroe == "Red":
                    contador_rojo += 1
                if color_ojos_heroe == "Hazel":
                    contador_avellana += 1

        
              print(f"\nAZUL: {contador_azul}\
                      \nAMARILLO: {contador_amarillo}\
                      \nVERDE: {contador_verde}\
                      \nPLATEADO: {contador_plateado}\
                      \nMARRON: {contador_marron}\
                      \nROJO: {contador_rojo}\
                      \nAVELLANA: {contador_avellana}")
                      
              print("\n")

        case "p":        
              contador_negro = 0
              contador_no_tiene = 0
              contador_rubio = 0
              contador_colorado = 0
              contador_verde = 0
              contador_blanco = 0
              contador_marron = 0
              

              print("CANTIDAD DE HEROES POR COLOR DE PELO")
              for superheroe in lista_personajes:
                color_pelo_heroe = superheroe["color_pelo"]

                if color_pelo_heroe == "Black":
                    contador_negro += 1
                if color_pelo_heroe == "No Hair":
                    contador_no_tiene += 1
                if color_pelo_heroe == "Blond" or color_pelo_heroe == "Yellow":
                    contador_rubio += 1
                if color_pelo_heroe == "Red" or color_pelo_heroe == "Auburn" or color_pelo_heroe == "Red / Orange":
                    contador_colorado += 1
                if color_pelo_heroe == "Green":
                    contador_verde += 1
                if color_pelo_heroe == "White":
                    contador_blanco += 1
                if color_pelo_heroe == "Brown" or color_pelo_heroe == "Brown / White":
                    contador_marron += 1

        
              print(f"\nNEGRO: {contador_negro}\
                      \nRUBIO: {contador_rubio}\
                      \nVERDE: {contador_verde}\
                      \nCOLORADO: {contador_colorado}\
                      \nMARRON: {contador_marron}\
                      \nBLANCO: {contador_blanco}\
                      \nNO TIENE PELO: {contador_no_tiene}")
                      
              print("\n")

        case "q":        
              contador_inteligencia_alta = 0
              contador_no_tiene = 0
              contador_inteligencia_buena = 0
              contador_inteligencia_promedio = 0
            
              print("CANTIDAD DE HEROES POR TIPO DE INTELIGENCIA")
              for superheroe in lista_personajes:
                inteligencia_heroe = superheroe["inteligencia"]

                if inteligencia_heroe == "high":
                    contador_inteligencia_alta += 1
                if inteligencia_heroe == "No tiene":
                    contador_no_tiene += 1
                if inteligencia_heroe == "good":
                    contador_inteligencia_buena += 1
                if inteligencia_heroe == "average":
                    contador_inteligencia_promedio += 1
           

        
              print(f"\nALTA: {contador_inteligencia_alta}\
                      \nPROMEDIO: {contador_inteligencia_promedio}\
                      \nBUENA: {contador_inteligencia_buena}\
                      \nNO TIENE: {contador_no_tiene}")
                      
              print("\n")
             
        case "r":
            break

    system("pause")
    