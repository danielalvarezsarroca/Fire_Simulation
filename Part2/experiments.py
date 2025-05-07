# experiments_seeds.py

import numpy as np
import matplotlib.pyplot as plt
from generador_dades import generar_humitat, generar_vegetacio
from lectura_idrisi import guardar_fitxer_idrisi
from simulacio import inicialitzar_incendi, simular_incendi

# Paràmetres globals de l'experiment
graella_size = 80
num_llacs = 0
num_focs = 1
direccio_vent = None  # o None

resultats = []

for seed in range(1111, 7778, 1111):
    np.random.seed(seed)

    humitat = generar_humitat(graella_size, num_llacs)
    vegetacio = generar_vegetacio(graella_size)
    estat_incendi = inicialitzar_incendi(graella_size, humitat, num_focs)

    pas = 0
    foc_apagat = False
    while not foc_apagat:
        humitat, vegetacio, estat_incendi, foc_apagat = simular_incendi(
            humitat, vegetacio, estat_incendi, graella_size, direccio_vent
        )
        pas += 1

    print(f"Seed {seed} -> L'incendi s'ha apagat en {pas} hores.")

print("\nTots els experiments han finalitzat.")


