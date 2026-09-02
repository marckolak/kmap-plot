class BooleanFunction:

    def __init__(
        self,
        variable_names: list[str],
        ones: set[int] | None = None,
        dont_cares: set[int] | None = None,
    ):

        self.variable_names = variable_names
        self.var_n = len(self.variable_names)
        self.ones = set(ones or ())
        self.dont_cares = set(dont_cares or ())

        self._truth_table = [0 for i in range(2**self.var_n)]

        self._validate()

        if ones:
            for ix in ones:
                self._truth_table[ix] = 1

        if dont_cares:
            for ix in dont_cares:
                self._truth_table[ix] = -1


    def value(self, minterm: int):
        self._validate_minterm(minterm)
        return self._truth_table[minterm]

    def value_from_bits(self, bits: str):
            minterm = int(bits, base=2)
            self._validate_minterm(minterm)
            return self._truth_table[minterm]
    

    def _validate_minterm(self, minterm: int):
        if not 0<= minterm < 2**self.var_n:
            raise ValueError(f"Minterm {minterm} out of range for {self.var_n} variables.")

    def _validate(self):
        minterms = self.ones | self.dont_cares

        # assert no repeats in ones and dont_cares
        if len(minterms) < len(self.ones) + len(self.dont_cares):
            raise ValueError("Minterm repeats accross ones and don't cares.")

        # validate minterms
        for m in minterms:
            self._validate_minterm(m)
