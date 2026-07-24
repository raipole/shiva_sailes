import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
#importing data file

data = pd.read_parquet('/home/sails/shiva_sailes/open-problems-single-cell-perturbationsde_train.parquet')
# print(data)