# lectura_idrisi.py
import numpy as np
import re
import os

def guardar_fitxer_idrisi(nom, matriu, descripcio, carpeta='Arxius_idrisi'):
    os.makedirs(carpeta, exist_ok=True)

    with open(f"{carpeta}/{nom}.img", 'w') as f:
        for valor in matriu.flatten():
            f.write(f"{valor}\n")

    header = f"""file title  : {descripcio}
data type   : integer
file type   : ascii
columns     : {matriu.shape[1]}
rows        : {matriu.shape[0]}
ref.system  : plane
ref.units   : m
unit dist.  : 15
min. X      : 0
max. X      : 2
min. Y      : 0
max. Y      : 2
pos 'n error: unknown
resolution  : 30
min. value  : {np.min(matriu)}
max. value  : {np.max(matriu)}
Value units : unspecified
Value Error : unknown
flag Value  : none
flag def 'n : none
legend cats : 0
"""
    with open(f"{carpeta}/{nom}.doc", 'w') as f:
        f.write(header)

def llegir_fitxer_idrisi(nom, carpeta='Arxius_idrisi'):
    with open(f"{carpeta}/{nom}.doc", 'r') as f:
        contingut = f.read()
        cols = int(re.search(r'columns\s*:\s*(\d+)', contingut).group(1))
        rows = int(re.search(r'rows\s*:\s*(\d+)', contingut).group(1))

    with open(f"{carpeta}/{nom}.img", 'r') as f:
        dades = [float(line.strip()) for line in f if line.strip()]
    matriu = np.array(dades).reshape((rows, cols))
    return matriu

def llegir_fitxers_idrisi(nom_humitat, nom_vegetacio, carpeta='Arxius_idrisi'):
    humitat = llegir_fitxer_idrisi(nom_humitat, carpeta)
    vegetacio = llegir_fitxer_idrisi(nom_vegetacio, carpeta)
    return humitat, vegetacio
