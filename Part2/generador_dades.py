# generador_dades.py
import numpy as np
from scipy.ndimage import gaussian_filter

def generar_humitat(mida, num_llacs):
    humitat = np.random.randint(0, 6, size=(mida, mida)).astype(float)

    for _ in range(num_llacs):
        i0, j0 = np.random.randint(0, mida), np.random.randint(0, mida)
        humitat[i0, j0] = np.inf
        llac = [(i0, j0)]
        for _ in range(np.random.randint(300, 500)):
            i, j = llac[np.random.randint(len(llac))]
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < mida and 0 <= nj < mida and humitat[ni, nj] != np.inf:
                        humitat[ni, nj] = np.inf
                        llac.append((ni, nj))

    for i in range(mida):
        for j in range(mida):
            if not np.isinf(humitat[i, j]):
                llacs = np.argwhere(humitat == np.inf)
                if llacs.size > 0:
                    dist = np.min([np.sqrt((i - x)**2 + (j - y)**2) for x, y in llacs])
                    p = min(1, 2 / (dist + 1))
                    if np.random.rand() < p:
                        humitat[i, j] = np.random.randint(3, 6)
    return humitat

def generar_vegetacio(mida):
    base = np.random.rand(mida, mida)
    suavitzat = gaussian_filter(base, sigma=1.2)
    norm = (suavitzat - suavitzat.min()) / (suavitzat.max() - suavitzat.min())
    vegetacio = np.round(1 + 9 * norm).astype(int)
    return vegetacio
