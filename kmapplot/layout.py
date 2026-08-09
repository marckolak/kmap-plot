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

    def minterm_to_cell(self, minterm: int) -> (int, int):


        return 0, 0
