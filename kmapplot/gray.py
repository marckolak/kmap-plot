
def gray_code(n_bits):
    assert n_bits > 0

    code = ['0', '1']
    for i in range(1, n_bits):
        code = ['0' + e for e in code] + ['1' + e for e in code[::-1]]

    return code