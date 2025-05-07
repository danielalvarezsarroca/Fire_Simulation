# simulacio.py
import numpy as np

def inicialitzar_incendi(mida, humitat, num_focs):
    estat = np.zeros((mida, mida), dtype=int)
    for _ in range(num_focs):
        i, j = np.random.randint(0, mida), np.random.randint(0, mida)
        while humitat[i, j] == np.inf:
            i, j = np.random.randint(0, mida), np.random.randint(0, mida)
        estat[i, j] = 1  # Encesa inicial
    return estat

def simular_incendi(humitat, vegetacio, estat, mida, direccio_vent=None):
    nou_estat = estat.copy()
    foc_actiu = False

    for i in range(mida):
        for j in range(mida):
            if estat[i, j] == 1:
                foc_actiu = True
                if vegetacio[i, j] > 0:
                    vegetacio[i, j] -= 1
                else:
                    nou_estat[i, j] = 2

                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < mida and 0 <= nj < mida:
                            if humitat[ni, nj] > 0 and not np.isinf(humitat[ni, nj]):
                                humitat[ni, nj] -= 1

                if direccio_vent:
                    di, dj = {'nord': (-2,0), 'sud': (2,0), 'est': (0,2), 'oest': (0,-2)}.get(direccio_vent, (0,0))
                    ni, nj = i + di, j + dj
                    if 0 <= ni < mida and 0 <= nj < mida:
                        if estat[ni, nj] == 0 and humitat[ni, nj] == 0:
                            nou_estat[ni, nj] = 1

            elif estat[i, j] == 0:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < mida and 0 <= nj < mida:
                            if estat[ni, nj] == 1 and humitat[i, j] == 0:
                                nou_estat[i, j] = 1
                                break

    foc_apagat = not foc_actiu
    return humitat, vegetacio, nou_estat, foc_apagat
