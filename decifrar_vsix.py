
import base64
import sys
import os
import zlib

# Uso: python decifrar_vsix.py archivo_base64.txt

def decifrar_archivo(archivo_entrada):
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
    nombre = lineas[0].strip()
    datos_b64 = ''.join(lineas[1:])
    datos_comprimidos = base64.b64decode(datos_b64)
    datos = zlib.decompress(datos_comprimidos)
    with open(nombre, 'wb') as f:
        f.write(datos)
    print(f"Archivo decifrado y descomprimido: {nombre}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python decifrar_vsix.py <archivo_base64.b64.txt>")
        sys.exit(1)
    decifrar_archivo(sys.argv[1])
