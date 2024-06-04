#Convertidor de Datos

def ingreso(): 
    """Pide datos al operador y luego muestra el tipo de dato que es"""
    while True:
        ingreso_del_usuario = input("Ingresa el dato que quieras: ")

        # isdigit(): Este método devuelve True si todos los caracteres de una cadena son dígitos y 
        # hay al menos un carácter, de lo contrario devuelve False.

        if ingreso_del_usuario.isdigit():
            ingreso_del_usuario = int(ingreso_del_usuario)

        # isalpha(): Devuelve True si todos los caracteres de una cadena son letras (alfabéticas)
        # y hay al menos un carácter, de lo contrario devuelve False.

        elif ingreso_del_usuario.isalpha():
            ingreso_del_usuario = str(ingreso_del_usuario)

        # count(): Este método cuenta cuántas veces aparece un determinado subcadena en una cadena. 
        # replace(): Este método devuelve una copia de una cadena donde se reemplazan 
        # todas las ocurrencias de una subcadena con otra subcadena.

        elif ingreso_del_usuario.count(".") == 1 and ingreso_del_usuario.replace(".", "").isdigit():
            ingreso_del_usuario = float(ingreso_del_usuario)

        # split(): Este método divide una cadena en una lista de subcadenas, 
        # utilizando un separador especificado.

        elif " " in ingreso_del_usuario:
            ingreso_del_usuario = ingreso_del_usuario.split()

        # isalnum(): Devuelve True si todos los caracteres de una cadena son alfanuméricos
        # (letras o números) y hay al menos un carácter, de lo contrario devuelve False.

        elif ingreso_del_usuario.isalnum():
            ingreso_del_usuario = str(ingreso_del_usuario)
            print("El string ingresado es alfanumérico.")
            print("El dato que ingresaste es ", ingreso_del_usuario)
            print("El tipo de dato que ingresaste es ", type(ingreso_del_usuario))
            return ingreso_del_usuario
            dato = ingreso_del_usuario
            break
        
        print("El dato que ingresaste es ", ingreso_del_usuario)
        print("El tipo de dato que ingresaste es ", type(ingreso_del_usuario))

        # isinstance(): Esta función se utiliza para verificar si un objeto es una instancia de una clase específica.
        # Toma dos argumentos: el objeto que se va a verificar y la clase que se desea verificar.
        # Devuelve True si el objeto es una instancia de la clase especificada, de lo contrario devuelve False

        if isinstance(ingreso_del_usuario, (float, int, str, list)):
            return ingreso_del_usuario
            dato = ingreso_del_usuario
            break


def respuesta_valida(si_no):
    """Verifica que las respuestas de los usuarios sean Si o No"""

    if si_no == "si":
        ingreso()

    elif si_no == "no":
        print("¡Gracias por ejecutar el programa!")
    
    else:
        while si_no != "si" and si_no != "no":
            si_no = input("La opcion ingresa no es valida, porfavor ingrese Si o No : ").lower()

        if si_no == "si":
            ingreso()


def convertidor(ingreso_del_usuario): 
    """Convierte el de dato que ingrese el usuario en otro tipo de dato"""

    if isinstance(ingreso_del_usuario, str):
        return list(ingreso_del_usuario)
    
    elif isinstance(ingreso_del_usuario, int):
        dato = ingreso_del_usuario
        return float(ingreso_del_usuario)

    elif isinstance(ingreso_del_usuario, float):
        dato = ingreso_del_usuario
        return int(ingreso_del_usuario)
    
    elif isinstance(ingreso_del_usuario, list):
        while True:
            preguntar = input("¿En que te gustaria convertir tu lista? Opcion 1: Conjunto, Opcion 2: Tupla. Ingresar 1 o 2 : ")

            if preguntar == "1":
                return set(ingreso_del_usuario)
                

            elif preguntar == "2":
                return tuple(ingreso_del_usuario)
                
            else:
                preguntar = input("La opcion ingresada no existe, porfavor ingresar 1 para Conjunto o 2 para tupla : ")

                if preguntar == "1":
                    return set(ingreso_del_usuario)
                    
                elif preguntar == "2":
                    return tuple(ingreso_del_usuario)
                    


#Comienzo de programa

print("Hola! Bienvenido al Convertidor de Datos")

si_no = input("¿Desea utilizar el convertidor? Responder Si/No: ").lower()
respuesta_valida(si_no)

cambiar_dato = input("¿Quieres ingresar un dato que se convertira en otro tipo de dato? Responder Si/No : ").lower()

if cambiar_dato == "si":
    dato = ingreso()
    convertido = convertidor(dato)
    print("El dato se convirtió en: ", convertido, "que es de tipo ", type(convertido))

    while True:
        si_no = input("¿Deseas volver a ingresar otro dato? Responder Si/No : ").lower()
        respuesta_valida(si_no)



        if si_no == "no":
            cambiar_dato = input("¿Quieres ingresar un dato que se convertira en otro tipo de dato? Responder Si/No : ").lower()

            if cambiar_dato == "si":
                dato = ingreso()
                convertido = convertidor(dato)
                print("El dato se convirtió en: ", convertido, "que es de tipo ", type(convertido))
            elif cambiar_dato == "no":
                print("¡Hasta luego Willi!")
                break

elif cambiar_dato == "no":
    print("¡Adios!")

    while si_no != "no":
        si_no = input("¿Desea volver a usar el convertidor? Responder Si/No : ")
        respuesta_valida(si_no)
        print("¡Hasta pronto!")
        break

else:
    while cambiar_dato != "si" and "no":
        cambiar_dato = input("La opcion ingresada no es valida. Porfavor ingresar Si o No :")

