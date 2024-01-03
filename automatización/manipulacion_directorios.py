import os

mi_directorio = "nuevo_directorio"

if not os.path.exists(mi_directorio):
    os.makedirs(mi_directorio)
    print(f"Se creó el directorio '{mi_directorio}'.")
else:
    print(f"El diretorio '{mi_directorio}' ya existe.")