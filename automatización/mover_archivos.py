texto="archivo.txt"
nuevo="destino.txt"

#Lee el contenido del archivo origen y lo guarda en una variable
with open(texto,"r") as archivo:
    contenido = archivo.read()
    
#Escribe en el archivo destino el contenido del archivo origen
with open (nuevo,"w") as destino:
    destino.write(contenido)
    
    
"""
esto sirve para borrar la información dentro del archivo

with open(texto,"w") as archivo:
    contenido = archivo.truncate()
    
print("COntenido copiado y archivo de origen limpio")"""