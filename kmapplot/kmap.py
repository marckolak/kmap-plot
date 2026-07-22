from kmapplot.gray import gray_code
from math import log2
import string

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

        # Kmap structure and values initialization
        if kmap:
            self.kmap = kmap
            self.col_vars_n = int(log2(len(self.kmap[0])))
            self.row_vars_n = int(log2(len(self.kmap)))
            self.variables_n = self.col_vars_n + self.row_vars_n


        elif variables_n:
            self.variables_n = variables_n
            self.row_vars_n = variables_n //2
            self.col_vars_n = variables_n - self.row_vars_n

            n_cols = 2**self.col_vars_n
            n_rows = 2**self.row_vars_n 

            self.kmap = [[0] * n_cols for _ in range(n_rows)]
            # print(self.kmap)
            # self.impl_mapping = self.implicant_mapping(self.n_rows, self.n_cols)
            if ones:
                for impl in ones:
                    self.kmap[0] = 1


        # Kmap labeling initialization
        if variable_names:
            self.variable_names = variable_names
        else:
            self.variable_names = [string.ascii_lowercase[i] for i in range(self.variables_n)]

        self.gray_rows = gray_code(self.row_vars_n)
        self.gray_cols = gray_code(self.col_vars_n)
        

    def __getitem__(self, key):
        return self.kmap[key]

    def __eq__(self, value: object) -> bool:
        return self.kmap == value

    def __len__(self):
        return len(self.kmap)

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


    def print(self):

        max_col_len = max(len(self.gray_cols[0]), len(''.join(self.variable_names+['/'])))

        row_width = self.row_vars_n


        variable_names = ''.join(self.variable_names[:self.row_vars_n]) + ' \\ ' + ''.join(self.variable_names[self.row_vars_n:])
        top_row = variable_names + ' | ' + ' | '.join(self.gray_cols)
        column_len = len(self.gray_cols[0])

        print(top_row)
        print('-'*len(top_row))

        for row, g in zip(self.kmap, self.gray_rows):
            row_str = f'{g:{''}^{len(variable_names)}}'
            print(row_str + ' | ' + ' | '.join([f'{c:{''}^{column_len}}' for c in row]))
            print('-'*len(top_row))

          

        pass


