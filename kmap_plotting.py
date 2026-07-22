import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np

fig, ax = plt.subplots(figsize=(5,5))

rows = 4
cols = 4


for i in range(1, rows):
    ax.plot([0, cols], [i, i], color='k', linewidth=1)

for i in range(1, cols):
    ax.plot([i, i], [0, rows], color='k', linewidth=1)

ax.plot([0, 0], [0, rows+0.5], color='k', linewidth=2)
ax.plot([-0.5,cols], [rows, rows], color='k', linewidth=2)


kmap = np.array([[0, 1, 1,1], [0, 0 , 0, 0], [1, '-', 0, '-'], ['-', '-', '-', '-']])

for r in range(rows):
    for c in range(cols):
        ax.text(
            c + 0.5,
            rows-r-0.5,
            str(kmap[r,c]),
            ha="center",
            va="center",
            fontsize=16
        )

gray = ["00", "01", "11", "10"]

for c, label in enumerate(gray):
    ax.text(c+0.5, rows+0.15, label,
            ha="center", fontsize=16)

for r, label in enumerate(gray):
    ax.text(-0.2, rows-r-0.5, label,
            ha="right", va="center", fontsize=16)



ax.set_xlim(-1, cols+1)
ax.set_ylim(-1, rows+1)
ax.set_aspect("equal")
ax.axis("off")
plt.show()