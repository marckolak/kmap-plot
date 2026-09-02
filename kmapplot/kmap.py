import string
from math import log2

from matplotlib import pyplot as plt

from kmapplot.boolfunc import BooleanFunction
from kmapplot.gray import gray_code
from kmapplot.layout import KMapLayout
from kmapplot.plotting import fill_kmap_grid, gray_labels, plot_kmap_grid, variables_labels


class Kmap:

    def __init__(
            self,
            function: BooleanFunction,
            rows_n: int | None = None
    ):

        self.function = function
        self.layout: KMapLayout = KMapLayout(variables_n=self.function.var_n, row_vars_n=rows_n)

       

        self.grid = [[0] * self.layout.cols_n for _ in range(self.layout.rows_n)]

        for minterm in function.ones:
            row, col = self.layout.minterm_to_grid(minterm)
            self.grid[row][col] = 1

        for minterm in function.dont_cares:
            row, col = self.layout.minterm_to_grid(minterm)
            self.grid[row][col] = "X"

    def __getitem__(self, key):
        return self.grid[key]

    def __eq__(self, value: object) -> bool:
        return self.grid == value

    def __len__(self):
        return len(self.grid)

    def __str__(self):

        lines = []

        variable_names = ''.join(self.function.variable_names[:self.layout.row_vars_n]) + ' \\ ' + ''.join(
            self.function.variable_names[self.layout.row_vars_n:])
        top_row = variable_names + ' | ' + ' | '.join(self.layout.gray_cols)
        column_len = len(self.layout.gray_cols[0])

        lines.append(top_row)
        lines.append('-' * len(top_row))

        for row, g in zip(self.grid, self.layout.gray_rows):
            row_str = f'{g:{''}^{len(variable_names)}}'
            lines.append(row_str + ' | ' + ' | '.join([f"{c:{''}^{column_len}}" for c in row]))
            lines.append('-' * len(top_row))

        return '\n'.join(lines)

    def __repr__(self):
        return self.__str__()

    def implicant_mapping(self, n_rows, n_cols) -> dict:
        gray_rows = gray_code(log2(n_rows))
        gray_cols = gray_code(log2(n_cols))

        mapping = [[0] * n_cols for _ in range(n_rows)]
        mapping_dict = {}
        for i in range(n_rows):
            for j in range(n_cols):
                bit_str = gray_rows[i] + gray_cols[j]
                mapping[i][j] = int(bit_str, 2)
                mapping_dict[int(bit_str, 2)] = (i, j)

        return mapping_dict

    def plot(self, ax=None, show=False):

        if not ax:
            fig, ax = plt.subplots(figsize=(5, 5))

        plot_kmap_grid(ax=ax, kmap=self.grid)
        fill_kmap_grid(ax=ax, kmap=self.grid)
        variables_labels(ax=ax, variable_names=self.function.variable_names, row_var_n=self.layout.row_vars_n)
        gray_labels(ax=ax, rows_n=len(self.grid), gray_c=self.layout.gray_cols, gray_r=self.layout.gray_rows)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.figure.suptitle('y', fontsize=18)

        if show:
            plt.show()
