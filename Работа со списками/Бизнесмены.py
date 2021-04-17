biznes = "20000$ акции: apple "
biznes1 = "50000$ акции: tesla "
biznes2 = "35000$ акции: EPAM "
biznes3 = "36000$ акции: telegram "
c = biznes.split(" ")
c1 = biznes1.split(" ")
c2 = biznes2.split(" ")
c3 = biznes3.split(" ")
c4 = c, c1, c2, c3
c4 = sorted(c4, reverse=False)
print(c4)

