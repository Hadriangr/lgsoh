from manipulacion_directorios import mi_directorio
import os

mi_directorio = "nuevo_directorio"

if os.path.exists(mi_directorio):
    archivos = os.listdir(mi_directorio)
    for archivo in archivos:
        print(archivo)
        
else:
    print(f"El directorio '{mi_directorio}' no existe")