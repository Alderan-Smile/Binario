
import base64
import sys
import os
import zlib

# Uso: python cifrar_vsix.py archivo.vsix

def cifrar_archivo(archivo_entrada):
    ruta_entrada = os.path.join("resource", archivo_entrada)
    nombre = os.path.basename(ruta_entrada)
    with open(ruta_entrada, 'rb') as f:
        datos = f.read()
    datos_comprimidos = zlib.compress(datos)
    datos_b64 = base64.b64encode(datos_comprimidos).decode('utf-8')
    # Dividir en partes de hasta 100 MB (100*1024*1024 bytes)
    max_tamano = 100 * 1024 * 1024  # 100 MB
    encabezado = f"{nombre}\n"
    datos_total = encabezado + datos_b64
    num_partes = (len(datos_total.encode('utf-8')) + max_tamano - 1) // max_tamano
    inicio = 0
    for i in range(num_partes):
        parte_nombre = f"{nombre}.b64.txt.part{i+1}"
        # Calcular el rango de bytes para esta parte
        if i == 0:
            # La primera parte incluye el encabezado
            parte_datos = datos_total.encode('utf-8')[0:max_tamano]
        else:
            parte_datos = datos_total.encode('utf-8')[i*max_tamano:(i+1)*max_tamano]
        with open(parte_nombre, 'wb') as f:
            f.write(parte_datos)
        print(f"Parte {i+1} guardada como: {parte_nombre}")
    print(f"Archivo cifrado y comprimido dividido en {num_partes} parte(s).")

cifrar_archivo("sonarsource.sonarlint-vscode-3.11.0-win32-x64.vsix")
cifrar_archivo("sonarsource.sonarlint-vscode-3.12.0-win32-x64.vsix")
cifrar_archivo("sonarsource.sonarlint-vscode-4.2.2-win32-x64.vsix")
cifrar_archivo("sonarsource.sonarlint-vscode-4.27.0-win32-x64.vsix")
