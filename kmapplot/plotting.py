"""
Plotting helper functions
"""
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import numpy as np

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
                    str(kmap[r][c]),
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