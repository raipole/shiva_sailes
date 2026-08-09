

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from contourpy.util.data import random
from fontTools.merge.util import first
from pandas.core.interchange import column
from sklearn import linear_model
# from sklearn.externals.array_api_compat.cupy.linalg import pinv
from sklearn.linear_model import LogisticRegression
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
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Lasso
from sklearn.linear_model import RidgeClassifier
from xgboost import XGBClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold, cross_validate
from sklearn.feature_selection import VarianceThreshold
from rdkit.Chem import Descriptors
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import BaggingClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
from sklearn.metrics import log_loss
from sklearn.metrics import recall_score
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import StratifiedKFold, cross_validate

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier


########################## i am loading the data ############################


data=pd.read_csv('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/train.csv')


#################################### Explanatory data analysis ########################################


print(data.head())

print(data.describe())

print(data.info())
print('total number of null values:',data.isnull().sum())

print(data.shape)
print(data.columns)


duplicates = data[data.duplicated(subset='Smiles', keep=False)]

print('Duplicate:',duplicates)

print('sum of duplicate:',data.duplicated().sum())
duplicate_smiles = data[data.duplicated(subset=["Smiles"], keep=False)]

print('d',duplicate_smiles)
# i am removing id column

data_new=data.drop(['Molecule ChEMBL ID'],axis=1)
print(data_new.head())




duplicates = data[data.duplicated(subset=["Smiles"], keep=False)]

print(duplicates)
print('sum of duplicate:',data.duplicated().sum())

####################### Data preprocessing #########################


# Removing duplicate occurrences

data_clean = data.drop_duplicates(subset='Smiles', keep='first')
print(data_clean.head())
print(data_clean.shape)
print('sum of duplicate:',data_clean.duplicated().sum())

X=data_clean[['Smiles']]
print('shape',X.shape)
# y=data_clean['pChEMBL Value']

# converting continues values of target features into binary values to classification

data_clean["Activity"] = np.select([data_clean["pChEMBL Value"] < 5,(data_clean["pChEMBL Value"] >= 5)],[0, 1])

y=data_clean["Activity"]
print(y)
print(y.value_counts())


# splitting data into train and test

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=7)


print(X_train.shape)
print(y_train.shape)


def smile_to_morganprint(smiles,radius=2,n_Bits=1024):
    finger_prints=[]

    for  i in smiles:
        try:
            # i am going to convert string  smile to chemical object
            if i is not None :

                molecule=Chem.MolFromSmiles(str(i))

                # i am going to convert each molecule morganfingerprints

                morgan_finger=AllChem.GetMorganFingerprintAsBitVect(molecule,radius,n_Bits)

                # i am creating a emtpy arr

                empty_arr=np.zeros((0,),np.int8)

                # i am going to convert morganfingerprint to array

                Chem.DataStructs.ConvertToNumpyArray(morgan_finger,empty_arr)

                # now i am taking storing these values in  finger_prints

                finger_prints.append(empty_arr)

            else:
                arr=np.zeros((n_Bits,),np.int8)
                finger_prints.append(arr)

        except:
            arr=np.zeros((n_Bits,),np.int8)
            finger_prints.append(arr)

    print(np.array(finger_prints).shape)

    return np.array(finger_prints)

# converting smiles strings into morganfinger prints x_train and x_test


X_train=smile_to_morganprint(X_train['Smiles'],radius=2,n_Bits=1024)
X_test=smile_to_morganprint(X_test['Smiles'],radius=2,n_Bits=1024)
x_features=smile_to_morganprint(data_clean['Smiles'],radius=2,n_Bits=1024)

#
models = {
    "Logistic": LogisticRegression(max_iter=1000,random_state=42),
    "Ridge": RidgeClassifier(),

    "RandomForest":RandomForestClassifier(),
    "Lightboot": LGBMClassifier(),
    "Bagging":  BaggingClassifier(),
    "XGBoost": XGBClassifier()}
#----------------------------------------------------
#X = Features
#y = Target (0/1)
#----------------------------------------------------

cv = StratifiedKFold(n_splits=10,shuffle=True,random_state=42)


scoring = {'Accuracy':'accuracy','Precision':'precision','Recall':'recall','F1':'f1','ROC_AUC':'roc_auc'}

summary = []

for name, model in models.items():

    scores = cross_validate(model,x_features,y,cv=cv,scoring=scoring,return_train_score=False)

    summary.append({

        'Model':name,

        'Accuracy Mean':scores['test_Accuracy'].mean(),
        'Accuracy Std':scores['test_Accuracy'].std(),

        'Precision Mean':scores['test_Precision'].mean(),
        'Precision Std':scores['test_Precision'].std(),

        'Recall Mean':scores['test_Recall'].mean(),
        'Recall Std':scores['test_Recall'].std(),

        'F1 Mean':scores['test_F1'].mean(),
        'F1 Std':scores['test_F1'].std(),

        'ROC AUC Mean':scores['test_ROC_AUC'].mean(),
        'ROC AUC Std':scores['test_ROC_AUC'].std()

    })

results = pd.DataFrame(summary)

print(results)

results.to_excel('/home/sails/shiva_sailes/saile_code/ML_file/ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/QSAR bioactivity classification results/Classification_10Fold_Comparison.xlsx')

