
# función leer_líneas
# Esta función nos permite
# leer todas las líneas de
# un archivo especificado

def leer_lineas(arch_txt):
    objeto = open(arch_txt, "r")    
    for linea in objeto:
        print(linea.rstrip())
    objeto.close()

# función agregar
# Esta función permite agregar una
# línea a un texto ya existente

def agregar_linea(arch_txt, texto_nuevo_renglon):    
     objeto = open(arch_txt,'a')
     objeto.write('\n' + texto_nuevo_renglon)
     objeto.close()
     leer_lineas(arch_txt)  


# menú creado en clase
accion="segui adentro"
while accion != 'CHAU':

    print("ORDENES: CHAU, LEER, AGREGAR")
    accion = (input("ORDEN --> ")).upper()
    if accion == "LEER":
        archivo_a_leer = input('ARCHIVO: ')
        leer_lineas(archivo_a_leer)
    if accion == "AGREGAR":
        archivo_a_leer = input('ARCHIVO: ')
        texto_del_renglon = input('TEXTO DEL RENGLON: ')
        agregar_linea(archivo_a_leer, texto_del_renglon)
        leer_lineas(archivo_a_leer)
    


print('Nos vemos !')
    
# from asyncore import loop

# def escribir_lineas(arch_txt):
#         arch_obj = open(arch_txt, "r")    
#         for renglon in arch_obj:
#             print(renglon.rstrip())
#         arch_obj.close()
  
# def leer_lineas(arch_txt):
#     f = open(arch_txt, "r")    
#     for linea in f:
#         print(linea.rstrip())
#     f.close()

# def leer_lineas_numeradas(arch_txt):
#     f = open(arch_txt, "r")
#     item = 0    
#     for linea in f:
#         item += 1   
#         print(str(item)+" : "+linea.rstrip())
#     f.close()
  
# def leer_caracteres(arch_txt):
#     handler = open(arch_txt, "r")
#     caracter = handler.read(1)
#     contador = 0
    
#     while caracter != '':
#         contador += 1 
#         caracter = handler.read(1)
#     handler.close()
#     print(f'Cantidad de Caracteres {contador}')
  
    
 
    
# def nuevo(archivo,texto):
#     handler = open(archivo, 'w')
#     handler.write(texto)
#     handler.close()
#     leer_lineas(archivo)
    
# def existe():    
#     nombre_archivo = input('Nombre del archivo: ')
#     try:
#         handler = open(nombre_archivo)
#         handler.close()
#         print(f'Si existe el archivo {nombre_archivo} !')
        
#     except FileNotFoundError:
#         print(f'No existe el archivo {nombre_archivo} !')
#         #exit()
    
# accion = 'nada'

# while accion.upper() != 'ADIOS':
    
#     print(" ")
#     print(" ")
#     print('-- COMANDOS PARA OPERAR CON ARCHIVOS DE TEXTO---------------------------------------')
#     print(" ")
#     print('ADIOS - SALE DE LA APLICACION')
#     print('CREAR - CREA UN NUEVO ARCHIVO DE TEXTO')
#     print('LEER_LINEAS - LEE LINEA POR LINEA EL ARCHIVO DE TEXTO')
#     print('LEER_LINEAS_NUMERADAS - LEE LINEA POR LINEA EL ARCHIVO DE TEXTO Y LAS NUMERA')
#     print('LEER_CARACTERES - LEE UNO POR UNO LOS CARACTERES DEL ARCHIVO Y LOS CUENTA')
#     print('AGREGAR UNA LINEA AL ARCHIVO EXISTENTE')
#     print('EXISTE VERIFICA SI EXISTE EL ARCHIVO')
#     print('ESCRIBIR_LINEAS AGREGA VARIAS LINEAS AL ARCHIVO INDICADO')
#     print('RECORDAR_TABLA, RECUERDA LA TABLA DE UN NUMERO')
#     print(" ")
#     print('------------------------------------------------------------------------------------')
#     accion = (input("COMANDO --> ")).upper()

#     if accion == "RECORDAR_TABLA":
#         nombre_archivo = input('Nombre del archivo: ')
#         numero = int(input('Ingrese la tabla de que numero: '))
#         handler = open(nombre_archivo,"w")
#         for i in range(11):
#             handler.write(str(numero)+" * "+str(i)+" = "+str(numero*i)+"\n")
#         handler.close()
#         leer_lineas(nombre_archivo)
#         loop

#     if accion == "LEER_LINEAS":
#         nombre_archivo = input('Nombre del archivo: ')
#         leer_lineas(nombre_archivo)
#         loop

#     if accion == "LEER_LINEAS_NUMERADAS":
#         nombre_archivo = input('Nombre del archivo: ')
#         leer_lineas_numeradas(nombre_archivo)
#         loop

#     if accion == "ESCRIBIR_LINEAS":
#         nombre_archivo = input('Nombre del archivo: ')
#         handler = open(nombre_archivo,"w")
#         seguir = 's'
#         while seguir.upper() == 'S':
#             entrada = input("INGRESE TEXTO: ")
#             handler.write(f"{entrada}\n")  
#             seguir = input("Desea continuar (S/N)")
#         handler.close()
#         leer_lineas(nombre_archivo)
#         loop

#     if accion == "LEER_CARACTERES":
#         nombre_archivo = input('Nombre del archivo: ')
#         leer_caracteres(nombre_archivo)
#         loop

#     if accion == "AGREGAR":
#         nombre_archivo = input('NOMBRE ARCHIVO: ')
#         texto_archivo = input("TEXTO: ")
#         agregar(nombre_archivo, texto_archivo)
#         loop

#     if accion == "EXISTE":
#         existe()
#         loop

#     if accion == "CREAR":
#         nombre_archivo = input('NOMBRE ARCHIVO: ')
#         texto_archivo = input("TEXTO: ")
#         nuevo(nombre_archivo, texto_archivo)
#         leer_lineas(nombre_archivo)
#         loop
        

# print('------------------------------------------------------------------------------------')
# print('ACABA DE FINALIZAR LA APLICACION, ADIOS...')
