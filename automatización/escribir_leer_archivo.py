text= 'archivo.txt'

with open (text, "w") as archivo:
    archivo.write("Esto es una prueba\n")
    archivo.write("Hola Mundo\n")
    
    
with open(text,"r") as archivo:
    contenido = archivo.read()
    

print("Contenido del Archivo")
print(contenido)