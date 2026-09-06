import numpy as np
from copy import deepcopy
from kmapplot.plotting import cell_group_patch


class Implicant:

    def __init__(
        self,
        term: set[int] | str,
        variable_names: list[str] | None = None,
        color: str = "red",
        label: str | None = None,
    ):
        self.color = color
        self.label = label or (term if isinstance(term, str) else None)
        self.variable_names = variable_names

        if isinstance(term, str):
            if not variable_names:
                raise ValueError(
                    "variable_names are required when defining an implicant from a string expression."
                )
            self.minterms = self._parse_string_term(term, variable_names)
            self.literal = self._get_literal()
        else:
            self.minterms = set(term)
            self.literal = self._get_literal()

    def _get_literal(self):
        literal = []
        if self.variable_names is not None:
            minterms_copy = deepcopy(self.minterms)
            m0 = minterms_copy.pop()
            bits = [b for b in f"{m0:0{len(self.variable_names)}b}"][::-1]
            for m in minterms_copy:
                xor = m0 ^ m
                i = 0
                while xor:
                    if xor & 1:
                        bits[i] = "-"
                    i += 1
                    xor = xor >> 1

            bits = bits[::-1]

            for i, b in enumerate(bits):
                if b == "0":
                    literal.append(f"{self.variable_names[i]}'")
                elif b == "1":
                    literal.append(self.variable_names[i])

        return "".join(literal)

    def _parse_string_term(self, term: str, variable_names: list[str]) -> set[int]:

        # Map variables to 0, 1 or -
        var_states = {}
        for var in variable_names:
            if f"{var}'" in term or f"~{var}" in term or f"!{var}" in term:
                var_states[var] = "0"
            elif var in term:
                var_states[var] = "1"
            else:
                var_states[var] = "-"

        # binary representation
        pattern = "".join(var_states[v] for v in variable_names)

        def expand_mask(mask: str) -> list[str]:
            if "-" not in mask:
                return [mask]
            return expand_mask(mask.replace("-", "0", 1)) + expand_mask(
                mask.replace("-", "1", 1)
            )

        binary_strings = expand_mask(pattern)
        return {int(b, 2) for b in binary_strings}

    def get_grid_cells(self, layout) -> set[tuple[int, int]]:
        return {layout.minterm_to_grid(m) for m in self.minterms}

    def _get_cell_groups(self, layout):
        cells = self.get_grid_cells(layout)
        groups = []

        cell = cells.pop()
        groups.append(set((cell,)))

        while len(cells):  # while there are unassigned cells left
            assigned = []
            for g in groups:
                for c in cells:
                    if min_manhattan_dist_from_group(g, c) == 1:
                        assigned.append(c)
                        g.add(c)

                for c in assigned:
                    cells.remove(c)

            if not assigned:
                groups.append(set((cells.pop(),)))

        return groups

    def plot(self, ax, layout):
        groups = self._get_cell_groups(layout)
        if not groups:
            raise ValueError("No cell groups in the implicant")
        for i, g in enumerate(groups):
            label = self.literal if i == 0 else "_nolegend_"
            patch = cell_group_patch(g, self.color, layout.rows_n, label=label)
            ax.add_patch(patch)


def manhattan_distance(c1: tuple[int, int], c2: tuple[int, int]):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def min_manhattan_dist_from_group(group, c):
    return min([manhattan_distance(cg, c) for cg in group])
