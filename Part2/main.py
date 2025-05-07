# simulador_incendi.py

from generador_dades import generar_humitat, generar_vegetacio
from lectura_idrisi import guardar_fitxer_idrisi, llegir_fitxers_idrisi
from simulacio import inicialitzar_incendi, simular_incendi
from visualitzacio import visualitzar_estat
import numpy as np
import matplotlib.pyplot as plt
import random


SEED = 1111  # Canviar aquest valor per fer diferents experiments
random.seed(SEED)
np.random.seed(SEED)

# Paràmetres inicials
dimensio_mapa = 80
num_llacs = 1
num_focs = 1
direccio_vent = None  # 'nord', 'sud', 'est', 'oest' o None

# Generació de dades
humitat = generar_humitat(dimensio_mapa, num_llacs)
vegetacio = generar_vegetacio(dimensio_mapa)

guardar_fitxer_idrisi('humitat', humitat, 'Mapa de humitat')
guardar_fitxer_idrisi('vegetacio', vegetacio, 'Mapa de vegetació')

# Inicialització de l'incendi
estat_incendi = inicialitzar_incendi(dimensio_mapa, humitat, num_focs)
guardar_fitxer_idrisi('estat_incendi', estat_incendi, 'Estat inicial del foc')

# Bucle de simulació
fig = plt.figure(figsize=(15, 5))
pas = 0
while plt.fignum_exists(fig.number):
    visualitzar_estat(humitat, vegetacio, estat_incendi, pas)
    humitat, vegetacio, estat_incendi, foc_apagat = simular_incendi(
        humitat, vegetacio, estat_incendi, dimensio_mapa, direccio_vent
    )
    pas += 1
    if foc_apagat:
        print("\nL'incendi s'ha extingit completament.")
        print(f"Ha durat {pas} hores.")
        break

plt.show()
