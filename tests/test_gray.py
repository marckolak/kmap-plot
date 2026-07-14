from kmapplot.gray import gray_code

def test_gray_code():
    assert gray_code(1) == ['0', '1']
    assert gray_code(2) == ['00', '01', '11', '10']
    assert gray_code(3) == ['000', '001', '011', '010', '110', '111', '101', '100']