import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.core.interchange import column
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split, KFold
from sklearn.metrics import r2_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import RidgeClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from rdkit.Chem import rdFingerprintGenerator

# i am loading data
data=pd.read_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/train.csv')

print(data.head())

print(data.describe())

print(data.info())
print('total number of null values:',data.isnull().sum())

print(data.shape)
print(data.columns)

# i am removing id column

data_new=data.drop(['Molecule ChEMBL ID'],axis=1)

print(data_new.head())


def smile_to_morganprint(smiles,radius=1,n_Bits=2048):
    finger_prints=[]


    for  i in smiles:
        try:
            count=+1


            # i am going to convert string  smile to chemical object
            if i is not None :


                molecule=Chem.MolFromSmiles(str(i))

                # i am going to save each chemical object to structure show in a file named called molicule.png
                file_name=f'structi_{count}.png'
                Draw.MolToFile(molecule,'file_name',size=(300,300))

                # i am going to convert each molecule morganfingerprints

                morgan_finger=AllChem.GetMorganFingerprintAsBitVect(molecule,radius,n_Bits)

                # i am creating a emtpy arr

                empty_arr=np.zeros((0,),np.int8)

                # i am going to convert morganfingerprint to array


                morgan_array= Chem.DataStructs.ConvertToNumpyArray(morgan_finger,empty_arr)


                # now i am taking storing these values in  finger_prints

                finger_prints.append(morgan_finger)

            else:
                arr=np.zeros((n_Bits,),np.int8)
                finger_prints.append(arr)

        except:
            arr=np.zeros((n_Bits,),np.int8)
            finger_prints.append(arr)

    print(np.array(finger_prints).shape)
    return np.array(finger_prints)


smiles=data['Smiles']
x_train=smile_to_morganprint(data['Smiles'],radius=1,n_Bits=2048)
print(x_train.shape)
print(x_train)
