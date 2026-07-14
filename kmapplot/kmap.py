class Kmap:

    def __init__(self, variables_n: int, ones: list, dont_cares: list):
        self.N = variables_n //2
        self.M = variables_n - self.N

        self.kmap = [[0]*2**self.M for _ in range(self.N)] 

    def __getitem__(self, key):
        return self.kmap[key]
    
    def __eq__(self, value: object) -> bool:
        return self.kmap == value
    
    