import base64
import sys
import os

# Uso: python decifrar_vsix.py archivo_base64.txt

def decifrar_archivo(archivo_entrada):
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        lineas = f.readlines()
    nombre = lineas[0].strip()
    datos_b64 = ''.join(lineas[1:])
    datos = base64.b64decode(datos_b64)
    with open(nombre, 'wb') as f:
        f.write(datos)
    print(f"Archivo decifrado: {nombre}")

decifrar_archivo("sonarsource.sonarlint-vscode-3.11.0-win32-x64.vsix.b64.txt")
decifrar_archivo("sonarsource.sonarlint-vscode-3.12.0-win32-x64.vsix.b64.txt")
decifrar_archivo("sonarsource.sonarlint-vscode-4.2.2-win32-x64.vsix.b64.txt")
decifrar_archivo("sonarsource.sonarlint-vscode-4.27.0-win32-x64.vsix.b64.txt")
