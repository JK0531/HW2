import numpy as np

def FizzBuzz(start = 1, finish = 15+1):
    # start = 1
    # finish = 15+1
    numvec = np.arange(start,finish)
    objvec = np.array(numvec,dtype=object)
    objvec = np.where((numvec % 3 == 0) & (numvec % 5 == 0), "fizzbuzz",np.where(numvec % 3 == 0, "fizz",np.where(numvec % 5 == 0, "buzz", numvec)))
    return(objvec)
    
# test
print(FizzBuzz())
print(FizzBuzz(40, 45))