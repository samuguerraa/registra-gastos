import datetime
import re

gastos = []
def registrar_gasto():

    fecha = obtener_fecha()
    categoria = obtener_categoria()
    descripcion = obtener_descripcion()
    valor = obtener_valor()
            

    gasto = {   
        "fecha": fecha,
        "categoria": categoria,
        "descripcion": descripcion,
        "valor": valor
    }

    return gasto

def obtener_fecha():
    fecha = datetime.date.today()
    return fecha

def obtener_categoria(): 
    categorias = ["Transporte", "Alimentacion / Restaurantes", "Entretenimiento / Ocio", "Salud", "Educacion", "Ropa / Calzado", "Supermercado", "Viajes", "Servicios",
              "Compras", "Otros"]

    categoria = -1
    while True:
        try:
            print("Seleccione la categoria correspondiente al gasto:\n\n")
            for indice, nombre_categoria in enumerate(categorias, start=1):
                print(f"{indice}. {nombre_categoria}")
            categoria = int(input("\nIngrese el numero según la opción deseada: "))

        except ValueError:
            print("Opcion invalida. Intente nuevamente\n")
        else:
            if categoria not in range (1, len(categorias) + 1):
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
            valor = valor.replace(',', '')
            valor = valor.replace('.', '')
            valor_numerico = int(valor)
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
        return False
    else:
        for indice, gasto in enumerate(gastos, start=1):
            print(f"Gasto #{indice}:\nFecha: {gasto['fecha']}\nCategoria: {gasto['categoria']}\nDescripción: {gasto['descripcion']}\nValor: {gasto['valor']}\n")

    return True

def calcular_total_gastado():
    total_gastos = 0
    for gasto in gastos:
        total_gastos += gasto['valor']
    return total_gastos

def obtener_indice_gasto():
    print("A continuacion se muestran los gastos encontrados. Introduzca el numero del gasto que desea editar o escriba 0 para volver:")
    if mostrar_gastos():
        while True:
            try:
                gasto_a_editar = int(input("\n\nIngrese el numero correspondiente al gasto deseado: "))
            except ValueError:
                print("Se debe ingresar un numero, intente nuevamente.")
            else: 
                indice = gasto_a_editar - 1
                if indice not in range(-1, len(gastos)):
                    print(f"No se encontro el gasto numero {gasto_a_editar}. Intente nuevamente.")
                else:
                    return indice
    else:
        return
    
def editar_gasto():
    indice = obtener_indice_gasto()
    if indice == -1:
        print("Operacion cancelada exitosamente. No se edito ningun gasto")
        return
    elif indice is None:
        return
    else:
        print("\n¿Que desea modificar? Seleccione el numero correspondiente a la opcion deseada:\n\n" 
            "1. Editar categoría\n"
            "2. Editar descripcion\n"
            "3. Editar valor\n"
            "4. Cancelar\n")
        while True:
            try:
                opcion_a_editar = int(input("\nIntroduzca el numero correspondiente a la opcion deseada: "))
            except ValueError:
                print("Se debe introducir un numero. Intente nuevamente.")
            else:
                if opcion_a_editar not in range(1, 5):
                    print("Opción inválida. Intente nuevamente")
                else:
                    break
        match opcion_a_editar:
            case 1:
                editar_categoria(indice)
            case 2:
                editar_descripcion(indice)
            case 3:
                editar_valor(indice)
            case 4:
                print("Operacion cancelada exitosamente. No se edito ningun gasto")
                return
            case _:
                print("Error al procesar la opcion. Intente nuevamente.")

def editar_categoria(indice):
    nueva_categoria = obtener_categoria()
    gastos[indice]['categoria'] = nueva_categoria
    print(f"Categoria actualizada con exito a {nueva_categoria}")

def editar_descripcion(indice):
    nueva_descripcion = obtener_descripcion()
    gastos[indice]['descripcion'] = nueva_descripcion
    print(f"Descripcion actualizada con exito a {nueva_descripcion}")

def editar_valor(indice):
    nuevo_valor = obtener_valor()
    gastos[indice]['valor'] = nuevo_valor
    print(f"Valor actualizado con éxito a {nuevo_valor}")
        
def menu_principal():
    opciones = ["Registrar", "Mostrar", "Total", "Editar", "Salir"]
    while True:
        try:
            opcion = int(input("Seleccione la opcion deseada ingresando el numero correspondiente:\n\n1. Registrar gasto\n2. Mostrar gastos\n3. Ver total gastado\n4. Editar un gasto\n5. Salir\n\nIngrese la opcion deseada a continuacion: "))
        except ValueError:
          print("Opcion invalida. Intente nuevamente\n")
        else:
            if opcion in range(1, len(opciones) + 1):
                break
            else:
                print("Opcion invalida. Intente nuevamente\n") 
    return opcion

print("Bienvenido al registra-gastos v1.5.1\n")

opcion = menu_principal()
while opcion != 5:
    match opcion:
        case 1:
            gastos.append(registrar_gasto())
            print("Gasto agregado correctamente.\n")

        case 2:
            mostrar_gastos()

        case 3:
          print(f"Su total gastado es de: ${calcular_total_gastado()} COP")

        case 4:
            editar_gasto()

        case _:
             print("Error al procesar la opcion. Intente nuevamente")

    opcion = menu_principal()