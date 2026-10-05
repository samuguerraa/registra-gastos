import math
import re

gastos = []
def registrar_gasto():

    categoria = obtener_categoria()
    descripcion = obtener_descripcion()
    valor = obtener_valor()
            

    gasto = {   
        "categoria": categoria,
        "descripcion": descripcion,
        "valor": valor
    }

    return gasto

def obtener_categoria(): 
    categorias = ["Transporte", "Alimentacion / Restaurantes", "Entretenimiento / Ocio", "Salud", "Educacion", "Ropa / Calzado", "Supermercado", "Viajes", "Servicios",
              "Compras", "Otros"]

    categoria = -1
    while True:
        try:
            print("Seleccione la categoria correspondiente al gasto a registrar:\n\n")
            for indice, nombre_categoria in enumerate(categorias, start=1):
                print(f"{indice}. {nombre_categoria}")
            categoria = int(input("\nIngrese el numero según la opción deseada: "))

        except ValueError:
            print("Opcion invalida. Intente nuevamente\n")
        else:
            if categoria not in range (1, 12):
                print("Opcion invalida. Intente nuevamente\n")
            else: 
                break
    return categorias[categoria - 1]
    
def obtener_descripcion():
    descripcion = ''
    while True:
        descripcion = input("Ingrese descripción: ")
        cantidad_letras = 0
        for i in descripcion:
            if i.isalpha():
                cantidad_letras += 1
            if cantidad_letras >= 2:
                break
        if cantidad_letras < 2:
            print("La descripcion es muy corta o inválida. Intente nuevamente\n")
        else:
            break        

    return descripcion.strip()

def obtener_valor():
    while True:
        valor = input("Ingrese valor en COP: ")
        if re.fullmatch(r"\d{1,3}([.,]\d{3})*|\d+", valor):
            valor.strip() = valor.replace(',', '')
            valor.strip() = valor.replace('.', '')
            valor_numerico = int(valor.strip())
            if valor_numerico > 0:
                return valor_numerico
            else:
                print("El valor debe ser mayor a cero. Intente nuevamente\n")
                continue
        else:
            print("Entrada o formato invalido. Intente nuevamente.\n")
            
        
    

def mostrar_gastos():
    if not gastos:
        print("No hay gastos registrados")
    else:
        for indice, gasto in enumerate(gastos, start=1):
            print(f"Gasto #{indice}:\nCategoria: {gasto['categoria']}\nDescripción: {gasto['descripcion']}\nValor: {gasto['valor']}\n")

def calcular_total_gastado():
    total_gastos = 0
    for gasto in gastos:
        total_gastos += gasto['valor']
    return total_gastos
        
def menu_principal():
    while True:
        try:
            opcion = int(input("Seleccione la opcion deseada ingresando el numero correspondiente:\n\n1. Registrar gasto\n2. Mostrar gastos\n3. Ver total gastado\n4. Salir\n\nIngrese la opcion deseada a continuacion: "))
        except ValueError:
          print("Opcion invalida. Intente nuevamente\n")
        else:
            if opcion in range(1,5):
                break
            else:
                print("Opcion invalida. Intente nuevamente\n") 
    return opcion

print("Bienvenido al registra-gastos v1.3\n")

opcion = menu_principal()
while opcion != 4:
    match opcion:
        case 1:
            gastos.append(registrar_gasto())
            print("Gasto agregado correctamente.\n")

        case 2:
            mostrar_gastos()

        case 3:
          print(f"Su total gastado es de: ${calcular_total_gastado()} COP")

        case _:
             print("Opcion no encontrada. Intente nuevamente")

    opcion = menu_principal()