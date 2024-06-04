


#Ingreso del primer dato. En este importe de la biblioteca 're' que junto a la expresion re.match(r'^[a-zA-Z\s]+$', texto) te permite evaluar si lo ingresado es texto ya sea minusculas o mayusculas, teniendo en cuenta los espacios.

def solicitar_nombre_apellido():
    import re
    while True:
        entrada = input("Ingrese nombre y apellido: ")
        if re.match(r'^[a-zA-Z\s]+$', entrada):
            entrada = entrada.strip()
            
            return entrada
            
        else:
            print("¡Error! Debes ingresar solo texto.")


entrada_final = solicitar_nombre_apellido()

#print(entrada_final)
