import numpy as np

def getBondDuration(y, face, couponRate, m, ppy=1):
    pv = (1 + y / ppy) ** -np.arange(1, m + 1)
    cf = np.where(np.arange(1, m + 1) != m, face * couponRate, face + face * couponRate)
    pvcf = pv * cf
    pvcft = np.sum((np.arange(m) + 1) * pvcf)
    pvcfs = np.sum(pvcf)
    bondDuration = pvcft / pvcfs
    return(round(bondDuration, 2))

# test
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

result = getBondDuration(y, face, couponRate, m, ppy)
print(result)