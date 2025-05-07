# visualitzacio.py
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

def visualitzar_estat(humitat, vegetacio, estat, pas):
    import matplotlib.pyplot as plt
    import numpy as np
    from matplotlib.colors import ListedColormap

    plt.clf()

    # 1. Humitat
    plt.subplot(2, 2, 1)
    cmap_h = ListedColormap(['white', 'blue'])
    plt.imshow(humitat == np.inf, cmap=cmap_h)
    plt.imshow(humitat, cmap='Blues', alpha=0.6)
    plt.title('Humitat')
    plt.axis('off')

    # 2. Vegetació
    plt.subplot(2, 2, 2)
    plt.imshow(vegetacio, cmap='Greens', vmin=0, vmax=10)
    plt.title('Vegetació')
    plt.axis('off')

    # 3. Estat de l’incendi
    plt.subplot(2, 2, 3)
    cmap_e = ListedColormap(['white', 'red', 'black'])  # 0 = blanc, 1 = vermell, 2 = negre
    plt.imshow(estat, cmap=cmap_e, vmin=0, vmax=2)
    plt.title("Estat del foc")
    plt.axis('off')

    # 4. Combinat: vegetació (verd), humitat (blau), incendi (vermell i negre)
    plt.subplot(2, 2, 4)
    base = np.zeros((*vegetacio.shape, 3))

    # Vegetació (fons verd)
    norm_veg = vegetacio / vegetacio.max()
    base[..., 1] = norm_veg

    # Humitat (blau afegit)
    norm_hum = np.where(humitat == np.inf, 1, humitat / np.nanmax(humitat))
    base[..., 2] += 0.3 * norm_hum

    # Incendi per sobre
    for i in range(estat.shape[0]):
        for j in range(estat.shape[1]):
            if estat[i, j] == 1:
                base[i, j] = [1.0, 0.0, 0.0]  # Vermell per foc actiu
            elif estat[i, j] == 2:
                base[i, j] = [0.1, 0.1, 0.1]  # Negre per zona cremada

    plt.imshow(base)
    plt.title(f"Combinat – Pas {pas}")
    plt.axis('off')

    plt.tight_layout()
    plt.pause(0.001)
