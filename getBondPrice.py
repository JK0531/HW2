import numpy as np

def getBondPrice(y,face,couponRate,m,ppy=1):
    pv = (1 + y / ppy) ** -np.arange(1, m + 1)
    bondPrice = (np.sum(pv) * couponRate / ppy + pv[-1]) * face
    return(round(bondPrice, 2))

# test
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
result = getBondPrice(y,face,couponRate,m)
print(result)

m = 20
ppy = 2
result = getBondPrice(y,face,couponRate,m, ppy)
print(result)