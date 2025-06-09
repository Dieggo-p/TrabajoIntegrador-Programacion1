# Importamos la libreria necesaria para normalizar los strings
import unicodedata

# Funciones para manejo del arbol con listas 

def crear_opcion(nombre):
    return [nombre, [], []]

def insertar_izquierda(nodo, nueva_opcion):
    subarbol_izq = nodo[1]
    if subarbol_izq:
        nodo[1] = [nueva_opcion, subarbol_izq, []]
    else:
        nodo[1] = [nueva_opcion, [], []]

def insertar_derecha(nodo, nueva_opcion):
    subarbol_der = nodo[2]
    if subarbol_der:
        nodo[2] = [nueva_opcion, [], subarbol_der]
    else:
        nodo[2] = [nueva_opcion, [], []]
        
def imprimir_arbol(arbol, nivel=0):
    if arbol:
        imprimir_arbol(arbol[2], nivel + 1)
        print(' ' * nivel + str(arbol[0]))
        imprimir_arbol(arbol[1], nivel + 1)
        
def preorden(arbol):
    if arbol:
        print(arbol[0])
        preorden(arbol[1])
        preorden(arbol[2])

def inorden(arbol):
    if arbol:
        inorden(arbol[1])
        print(arbol[0])
        inorden(arbol[2])
        
def postorden(arbol):
    if arbol:
        postorden(arbol[1])
        postorden(arbol[2])
        print(arbol[0])

def normalizar(texto):  # Convierte el texto a minúsculas, elimina tildes y espacios innecesarios.
    texto = texto.strip().lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

def buscar_opcion(arbol, nombre):
    if not arbol:
        return None

    if normalizar(arbol[0]) == normalizar(nombre):
        return arbol

    encontrado = buscar_opcion(arbol[1], nombre)
    if encontrado:
        return encontrado
    return buscar_opcion(arbol[2], nombre)


# Interfaz de usuario

def menu_interactico():
    print('Inicializando menú raíz...')
    menu = crear_opcion('Menú Principal')
    
    while True:
        print('\n --- MENÚ INTERACTIVO --- ')
        print('1. Ver árbol completo')
        print('2. Recorrer árbol')
        print('3. Buscar una opción')
        print('4. Agregar una opción')
        print('5. Salir')
        opcion = input('\nSeleccione una opción: ')
        
        if opcion == '1':
            print('\nÁrbol rotado 90°:')
            imprimir_arbol(menu)
        
        elif opcion == '2':
            print('\nTipos de recorrido:')
            print('a. Preorden')
            print('b. Inorden')
            print('c. Postorden')
            tipo = input('\nElige el tipo de recorrido: (a/b/c): ')
            print('\nResultado:')
            if tipo == 'a':
                preorden(menu)
            elif tipo == 'b':
                inorden(menu)
            elif tipo == 'c':
                postorden(menu)
            else:
                print('Opción no válida.')
        
        elif opcion == '3':
            nombre = input('Ingrese el nombre de la opción a buscar: ')
            resultado = buscar_opcion(menu, nombre)
            if resultado:
                print('Opción encontrada:', resultado[0], '!')
            else:
                print('Opción no encontrada.')
                
        elif opcion == '4':
            padre = input('¿A qué nodo le querés agregar un hijo?: ')
            lado = input('¿Izquierda o derecha? (i/d): ').lower()
            nuevo_nombre = input('Nombre de la nueva opción: ')
            
            nodo_padre = buscar_opcion(menu, padre)
            if nodo_padre:
                if lado == 'i':
                    insertar_izquierda(nodo_padre, nuevo_nombre)
                    print('Opción agregada a la izquierda.')
                elif lado == 'd':
                    insertar_derecha(nodo_padre, nuevo_nombre)
                    print('Opción agregada a la derecha.')
                else:
                    print('Dirección inválida.')
            else: 
                print('No se encontró el nodo padre.')
        
        elif opcion == '5':
            print('Saliendo del programa...')
            break
        else:
            print('Opción no válida. Intente nuevamente.')

# Ejecutar el menú
menu_interactico()
