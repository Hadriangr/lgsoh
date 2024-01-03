miarchivo = "archivo.txt"

with open(miarchivo,"r") as archivo:
    contenido = archivo.read()
    palabras = contenido.split()
    
    

num_palabras = len(palabras)
mensaje = f"El archivo tiene {num_palabras} palabras."
print(mensaje)

with open(miarchivo,"a") as archivo:
    archivo.write("\n" + mensaje)