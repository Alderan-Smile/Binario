
import base64
import sys
import os
import zlib
import glob

# Uso: python decifrar_vsix.py nombre_base_vsix

def decifrar_archivo(nombre_base):
    # Buscar todas las partes correspondientes
    patron = f"{nombre_base}.b64.txt.part*"
    partes = sorted(glob.glob(patron), key=lambda x: int(x.split('.part')[-1]))
    if not partes:
        print(f"No se encontraron partes para: {nombre_base}")
        sys.exit(1)
    # Unir todas las partes
    datos_total = b''
    for parte in partes:
        with open(parte, 'rb') as f:
            datos_total += f.read()
    # Decodificar como texto
    datos_total = datos_total.decode('utf-8')
    lineas = datos_total.splitlines()
    nombre = lineas[0].strip()
    datos_b64 = ''.join(lineas[1:])
    datos_comprimidos = base64.b64decode(datos_b64)
    datos = zlib.decompress(datos_comprimidos)
    with open(nombre, 'wb') as f:
        f.write(datos)
    print(f"Archivo decifrado y descomprimido: {nombre}")

decifrar_archivo("sonarsource.sonarlint-vscode-3.11.0-win32-x64.vsix")
decifrar_archivo("sonarsource.sonarlint-vscode-3.12.0-win32-x64.vsix")
decifrar_archivo("sonarsource.sonarlint-vscode-4.2.2-win32-x64.vsix")
decifrar_archivo("sonarsource.sonarlint-vscode-4.27.0-win32-x64.vsix")
