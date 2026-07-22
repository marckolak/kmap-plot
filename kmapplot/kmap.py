from kmapplot.gray import gray_code
from math import log2


class Kmap:

    def __init__(
        self,
        kmap: list[list] | None = None,
        variables_n: int | None = None,
        ones: list | None = None,
        dont_cares: list | None = None,
    ):

        if kmap:
            self.kmap = kmap

        if variables_n:
            self.n_cols = 2**variables_n // 2
            self.n_rows = variables_n - self.n_cols
            print(self.n_cols, self.n_rows)
            self.kmap = [[0] * 2**self.n_cols for _ in range(self.n_rows)]
            self.impl_mapping = self.implicant_mapping(self.n_rows, self.n_cols)
            if ones:
                for impl in ones:
                    self.kmap[0] = 1

    def __getitem__(self, key):
        return self.kmap[key]

    def __eq__(self, value: object) -> bool:
        return self.kmap == value

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
