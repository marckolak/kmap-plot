import matplotlib
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
import seaborn as sns

from kmapplot.kmap import Kmap

sns.set_style('whitegrid')

def plot_kmap_grid(ax: matplotlib.axes.Axes, kmap: list[list] | np.ndarray):
    rows_n, cols_n = len(kmap), len(kmap[0])
    for i in range(0, rows_n+1):
        ax.plot([0, cols_n], [i, i], color='k', linewidth=1)

    for i in range(0, cols_n+1):
        ax.plot([i, i], [0, rows_n], color='k', linewidth=1)


    ax.plot([-.8,0], [rows_n+.8, rows_n], color='k', linewidth=1)

    # ax.plot([0, 0], [0, rows+0.5], color='k', linewidth=2)
    # ax.plot([-0.5,cols], [rows, rows], color='k', linewidth=2)

    return ax

def fill_kmap_grid(ax: matplotlib.axes.Axes, kmap: list[list] | np.ndarray):
    rows_n, cols_n = len(kmap), len(kmap[0])
    for r in range(rows_n):
            for c in range(cols_n):
                ax.text(
                    c + 0.5,
                    rows_n-r-0.5,
                    str(kmap[r,c]),
                    ha="center",
                    va="center",
                    fontsize=16
                )

def variables_labels(ax, variable_names, row_var_n):
    rows = int(2**row_var_n)
    # variables
    ax.text(-0.6, rows + 0.3, ''.join(variable_names[:row_var_n]),
                fontsize=16, horizontalalignment='right')

    ax.text(-0.3, rows + 0.55, ''.join(variable_names[row_var_n:]),
                fontsize=16, horizontalalignment='left')

def gray_labels(ax, rows_n, gray_c, gray_r):
    
    for c, label in enumerate(gray_c):
        ax.text(c+0.5, rows_n+0.15, label,
                ha="center", fontsize=16)

    for r, label in enumerate(gray_r):
        ax.text(-0.2, rows_n-r-0.5, label,
                ha="right", va="center", fontsize=16)



def main():

    # with individual functions

    kmap = np.array([[0, 1, 1,1], [0, 0 , 0, 0], [1, '-', 0, '-'], ['-', '-', '-', '-']])
    variables = 'abcd'
    rows_n = 4
    gray_r = gray_c = ["00", "01", "11", "10"]


    fig, ax = plt.subplots(figsize=(5,5))

    plot_kmap_grid(ax = ax, kmap=kmap)
    fill_kmap_grid(ax=ax, kmap=kmap)
    variables_labels(ax=ax, variable_names=variables, row_var_n=2)
    gray_labels(ax=ax, rows_n=rows_n, gray_c=gray_c, gray_r=gray_r)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.title('y', fontsize=18)
    plt.show()

    # directly with the Kmap

    kmap = Kmap(kmap=[[0, 1, 1,1], [0, 0 , 0, 0], [1, '-', 0, '-'], ['-', '-', '-', '-']])
    kmap.plot()

if __name__ == "__main__":
    main()