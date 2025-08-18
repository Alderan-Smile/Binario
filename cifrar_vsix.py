import base64
import sys
import os

# Uso: python cifrar_vsix.py archivo.vsix

def cifrar_archivo(archivo_entrada):
    nombre = os.path.basename(archivo_entrada)
    archivo_salida = f"{nombre}.b64.txt"
    with open(archivo_entrada, 'rb') as f:
        datos = f.read()
    datos_b64 = base64.b64encode(datos).decode('utf-8')
    with open(archivo_salida, 'w', encoding='utf-8') as f:
        f.write(f"{nombre}\n")
        f.write(datos_b64)
    print(f"Archivo cifrado como base64 en: {archivo_salida}")

cifrar_archivo("sonarsource.sonarlint-vscode-3.11.0-win32-x64.vsix")
cifrar_archivo("sonarsource.sonarlint-vscode-3.12.0-win32-x64.vsix")
cifrar_archivo("sonarsource.sonarlint-vscode-4.2.2-win32-x64.vsix")
cifrar_archivo("sonarsource.sonarlint-vscode-4.27.0-win32-x64.vsix")
