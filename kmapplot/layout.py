from kmapplot.gray import gray_code


class KMapLayout:
    """
    KMapLayout contains information on the K-map layout  - how many columns and rows
    """

    def __init__(self, variables_n, row_vars_n=None):
        self.variables_n = variables_n

        self.row_vars_n = variables_n // 2 if row_vars_n is None else row_vars_n
        self.col_vars_n = variables_n - self.row_vars_n

        self.cols_n = 2 ** self.col_vars_n
        self.rows_n = 2 ** self.row_vars_n

        self.gray_rows = gray_code(self.row_vars_n)
        self.gray_cols = gray_code(self.col_vars_n)

    def minterm_to_grid(self, minterm: int) -> tuple[int, int]:
        if not 0 <= minterm <= (1 << self.variables_n) -1:
            raise ValueError(f"Minterm {minterm} is out of range for a {self.variables_n}-varialbe K-map.")

        bit_str = f"{minterm:0{self.variables_n}b}"
        row_bits = bit_str[:self.row_vars_n]
        col_bits = bit_str[self.row_vars_n:]

        # Use 0 for dimensions with 0 variables (e.g. 1D K-maps)
        row_idx = self.gray_rows.index(row_bits) if row_bits else 0
        col_idx = self.gray_cols.index(col_bits) if col_bits else 0

        return row_idx, col_idx

        return 0, 0

    def grid_to_minterm(self, row, col) -> int:
        """Get the minterm for row and col"""
        bit_str = self.gray_rows[row] + self.gray_cols[col]
        return int(bit_str, 2)
