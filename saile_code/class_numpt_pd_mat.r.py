import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys

def numpyops():
    ### The basics

    ## An example
    a = np.arange(15)
    a = a.reshape(3, 5)
    print(a.shape)
    print(a.ndim)
    print(a.size)
    print(a.itemsize) # Length of one array element in bytes
    print(a.dtype.name)
    print(type(a))

    a = np.array([2, 3, 4])
    print(type(a))
    b = np.array([(1.5, 2, 3), (4, 5, 6)])
    print(type(b))

numpyops()