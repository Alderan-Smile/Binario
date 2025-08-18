
import base64
import sys
import os
import zlib

# Uso: python cifrar_vsix.py archivo.vsix

def cifrar_archivo(archivo_entrada):
    nombre = os.path.basename(archivo_entrada)
    archivo_salida = f"{nombre}.b64.txt"
    with open(archivo_entrada, 'rb') as f:
        datos = f.read()
    datos_comprimidos = zlib.compress(datos)
    datos_b64 = base64.b64encode(datos_comprimidos).decode('utf-8')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(f"{nombre}\n")
        f.write(datos_b64)
    print(f"Archivo cifrado y comprimido como base64 en: {archivo_salida}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python cifrar_vsix.py <archivo_entrada>")
        sys.exit(1)
    cifrar_archivo(sys.argv[1])
