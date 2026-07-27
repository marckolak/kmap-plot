import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import seaborn as sns

sns.set_style('whitegrid')

def plot_kmap_grid(ax: matplotlib.axes.Axes, rows: int, cols: int, **kwargs):
    
    for i in range(0, rows+1):
        ax.plot([0, cols], [i, i], color='k', linewidth=1)

    for i in range(0, cols+1):
        ax.plot([i, i], [0, rows], color='k', linewidth=1)


    ax.plot([-.8,0], [rows+.8, rows], color='k', linewidth=1)

    # ax.plot([0, 0], [0, rows+0.5], color='k', linewidth=2)
    # ax.plot([-0.5,cols], [rows, rows], color='k', linewidth=2)

    return ax

def main():
    fig, ax = plt.subplots(figsize=(5,5))

    rows = 4
    cols = 4

    plot_kmap_grid(ax = ax, rows=rows, cols = cols)


    kmap = np.array([[0, 1, 1,1], [0, 0 , 0, 0], [1, '-', 0, '-'], ['-', '-', '-', '-']])
    variables = 'abcd'
    n_row_var = 2 
    n_col_var = 2


    ax.text(-0.6, rows + 0.3, ''.join(variables[:n_row_var]),
                fontsize=16, horizontalalignment='right')

    ax.text(-0.3, rows + 0.55, ''.join(variables[n_row_var:]),
                fontsize=16, horizontalalignment='left')

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




    # ax.set_xlim(-1, cols+1)
    # ax.set_ylim(-1, rows+1)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.title('y', fontsize=18)
    plt.show()

if __name__ == "__main__":
    main()