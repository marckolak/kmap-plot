def gray_code(n_bits):
    """Generate the Gray's code for n_bits"""
    if n_bits < 1:
        raise ValueError(f"Gray code generation error. The number of bits must be >=1. Supplied number: {n_bits}")

    return [f"{i ^ (i >> 1):0{n_bits}b}" for i in range(1 << n_bits)]
