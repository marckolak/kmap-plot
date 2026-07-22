from kmapplot.kmap import Kmap


kmap = Kmap(kmap=[[0,1, 1, 0], [1,0, 1, 1]])
kmap.print()


kmap = Kmap(kmap=[[0,1], [1,0]])
kmap.print()

kmap = Kmap(variables_n=5)
kmap.print()


kmap = Kmap(variables_n=6)
kmap.print()