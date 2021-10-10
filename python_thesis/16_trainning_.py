import matplotlib.pyplot as plt
import numpy as np

ann_nom_train = np.load('early/ann_nom_train.npy')
ann_nom_val = np.load('early/ann_nom_val.npy')
ann_ord_train = np.load('early/ann_ord_train.npy')
ann_ord_val = np.load('early/ann_ord_val.npy')
dlnn_ord_train = np.load('early/dlnn_ord_train.npy')
dlnn_ord_val = np.load('early/dlnn_ord_val.npy')

epochs = range(1, 201)
n=100
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
ax1.plot(epochs[:n], ann_nom_train[:n], 'k--', label='Entrenamiento')
ax1.plot(epochs[:n], ann_nom_val[:n], 'k', label='Validación')
ax1.set_title('DL-NOM')
ax1.set_ylabel('función de costo')
ax1.set_xlabel('número de pasadas')
ax1.legend()

ax2.plot(epochs[:n], ann_ord_train[:n], 'k--', label='Entrenamiento')
ax2.plot(epochs[:n], ann_ord_val[:n], 'k', label='Validación')
ax2.set_title('DL1-ORD')
ax2.set_ylabel('función de costo')
ax2.set_xlabel('número de pasadas')
ax2.legend()

ax3.plot(epochs[:n], dlnn_ord_train[:n], 'k--', label='Entrenamiento')
ax3.plot(epochs[:n], dlnn_ord_val[:n], 'k', label='Validación')
ax3.set_title('DL2-ORD')
ax3.set_ylabel('función de costo')
ax3.set_xlabel('número de pasadas')
ax3.legend()

plt.show()
