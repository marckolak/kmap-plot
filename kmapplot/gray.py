
def gray_code(n_bits):
    if n_bits <1:
        print(f"Gray code generation error. The number of bits must be >=1. Supplied number: {n_bits}")    
        return []

    code = ['0', '1']
    for i in range(1, n_bits):
        code = ['0' + e for e in code] + ['1' + e for e in code[::-1]]

    return code