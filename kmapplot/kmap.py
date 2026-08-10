import string
from math import log2

from matplotlib import pyplot as plt

from kmapplot.gray import gray_code
from kmapplot.layout import KMapLayout
from kmapplot.plotting import fill_kmap_grid, gray_labels, plot_kmap_grid, variables_labels


class Kmap:

    def __init__(
            self,
            kmap: list[list] | None = None,
            variables_n: int | None = None,
            ones: list | None = None,
            dont_cares: list | None = None,
            variable_names: list | None = None
    ):

        if not (kmap or variables_n):
            raise TypeError("You must specify either the number of variables or a K-map itself")

        self.layout: KMapLayout | None = None

        # Kmap structure and values initialization
        if kmap:
            self.kmap = kmap
            self.col_vars_n = int(log2(len(self.kmap[0])))
            self.row_vars_n = int(log2(len(self.kmap)))
            self.variables_n = self.col_vars_n + self.row_vars_n
            self.layout = KMapLayout(self.variables_n, self.row_vars_n)

        elif variables_n:
            self.layout = KMapLayout(variables_n)
            self.kmap = [[0] * self.layout.cols_n for _ in range(self.layout.rows_n)]
            # print(self.kmap)
            # self.impl_mapping = self.implicant_mapping(self.n_rows, self.n_cols)
            if ones:
                for impl in ones:
                    self.kmap[0] = 1

        # Kmap labeling initialization
        if variable_names:
            self.variable_names = variable_names
        else:
            self.variable_names = [string.ascii_lowercase[i] for i in range(self.layout.variables_n)]


    def __getitem__(self, key):
        return self.kmap[key]

    def __eq__(self, value: object) -> bool:
        return self.kmap == value

    def __len__(self):
        return len(self.kmap)

    def __str__(self):

        max_col_len = max(len(self.layout.gray_cols[0]), len(''.join(self.variable_names + ['/'])))

        row_width = self.row_vars_n

        lines = []

        variable_names = ''.join(self.variable_names[:self.row_vars_n]) + ' \\ ' + ''.join(
            self.variable_names[self.row_vars_n:])
        top_row = variable_names + ' | ' + ' | '.join(self.layout.gray_cols)
        column_len = len(self.layout.gray_cols[0])

        lines.append(top_row)
        lines.append('-' * len(top_row))

        for row, g in zip(self.kmap, self.layout.gray_rows):
            row_str = f'{g:{''}^{len(variable_names)}}'
            lines.append(row_str + ' | ' + ' | '.join([f'{c:{''}^{column_len}}' for c in row]))
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

        plot_kmap_grid(ax=ax, kmap=self.kmap)
        fill_kmap_grid(ax=ax, kmap=self.kmap)
        variables_labels(ax=ax, variable_names=self.variable_names, row_var_n=self.row_vars_n)
        gray_labels(ax=ax, rows_n=len(self.kmap), gray_c=self.layout.gray_cols, gray_r=self.layout.gray_rows)
        ax.set_aspect("equal")
        ax.axis("off")
        ax.figure.suptitle('y', fontsize=18)

        if show:
            plt.show()
