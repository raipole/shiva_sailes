#1. Data normalization - scale the values between 0 and 1. Implement code from scratch
import numpy as np


def normalization(X):

    min = np.min(X)

    max = np.max(X)

    X = (X - min) / (max - min)

    print(X)

    return X

normalization(X)


# Data standardization - scale the values such that mean of new dist = 0 and sd = 1.
#Implement code from scratch.

def data_standardization(X):

    mean = np.mean(X)

    std = np.std(X)

    data_standardized = X - mean/std

    print(data_standardized)

    return data_standardized

data_standardization(X)