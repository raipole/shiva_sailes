
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from contourpy.util.data import random
from fontTools.merge.util import first
from pandas.core.interchange import column
from sklearn import linear_model
# from sklearn.externals.array_api_compat.cupy.linalg import pinv
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
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from xgboost import XGBRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold, cross_validate
from sklearn.feature_selection import VarianceThreshold
from rdkit.Chem import Descriptors
from sklearn.preprocessing import StandardScaler
from matplotlib.pyplot import plot
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV
from tkinter.constants import FIRST



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

print('No of Duplicates:',duplicate_smiles)

# i am removing id column

data_new=data.drop(['Molecule ChEMBL ID'],axis=1)
print(data_new.head())








# df = pd.read_csv("train.csv")

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
y=data_clean['pChEMBL Value']

# ============================================================
# FUNCTION TO IDENTIFY CHEMICAL FUNCTIONAL GROUP
# ============================================================

def identify_functional_group(molecule, atom_index, environment_radius):

    try:

        # Get atoms in Morgan environment
        bond_indices = Chem.FindAtomEnvironmentOfRadiusN(
            molecule,
            environment_radius,
            atom_index
        )

        atom_indices = {atom_index}

        for bond_index in bond_indices:

            bond = molecule.GetBondWithIdx(bond_index)

            atom_indices.add(bond.GetBeginAtomIdx())
            atom_indices.add(bond.GetEndAtomIdx())

        atoms = [
            molecule.GetAtomWithIdx(i)
            for i in atom_indices
        ]

        # ----------------------------------------------------
        # CHECK COMMON FUNCTIONAL GROUPS
        # ----------------------------------------------------

        # Carboxylic acid
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[CX3](=O)[OX2H1]")
        ):
            return "Carboxylic_acid"

        # Ester
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[CX3](=O)[OX2]")
        ):
            return "Ester"

        # Amide
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[CX3](=O)[NX3]")
        ):
            return "Amide"

        # Ketone
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[CX3](=O)[#6]")
        ):
            return "Ketone"

        # Aldehyde
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[CX3H1](=O)")
        ):
            return "Aldehyde"

        # Alcohol
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[OX2H][#6]")
        ):
            return "Alcohol"

        # Phenol
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[c][OX2H]")
        ):
            return "Phenol"

        # Ether
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[OD2]([#6])[#6]")
        ):
            return "Ether"

        # Primary amine
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[NX3;H2][#6]")
        ):
            return "Primary_amine"

        # Secondary amine
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[NX3;H1]([#6])[#6]")
        ):
            return "Secondary_amine"

        # Tertiary amine
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[NX3]([#6])([#6])[#6]")
        ):
            return "Tertiary_amine"

        # Nitrile
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[C]#[N]")
        ):
            return "Nitrile"

        # Nitro
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[N+](=O)[O-]")
        ):
            return "Nitro"

        # Thiol
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[SX2H]")
        ):
            return "Thiol"

        # Thioether
        if molecule.HasSubstructMatch(
                Chem.MolFromSmarts("[SX2]([#6])[#6]")
        ):
            return "Thioether"

        # Aromatic ring
        aromatic_atoms = sum(
            atom.GetIsAromatic()
            for atom in atoms
        )

        if aromatic_atoms >= 3:
            return "Aromatic_ring"

        # Heteroatom-containing ring
        hetero_atoms = sum(
            atom.GetAtomicNum() not in [6, 1]
            for atom in atoms
        )

        if hetero_atoms >= 1:
            return "Heterocycle"

        # Alkyl environment
        if all(
                atom.GetAtomicNum() in [6, 1]
                for atom in atoms
        ):
            return "Alkyl"

        return "Other"

    except:

        return "Unknown"


# ============================================================
# YOUR ORIGINAL MORGAN FINGERPRINT FUNCTION
# ============================================================

def smile_to_morganprint(smiles, radius=2, n_Bits=1024):

    finger_prints = []

    # Store chemical functional names
    feature_names = {}

    for i in smiles:

        try:

            count = +1

            # i am going to convert string smile to chemical object
            if i is not None:

                molecule = Chem.MolFromSmiles(str(i))

                # ------------------------------------------------
                # BIT INFORMATION
                # ------------------------------------------------

                bit_info = {}

                # i am going to convert each molecule
                # morgan fingerprints

                morgan_finger = AllChem.GetMorganFingerprintAsBitVect(
                    molecule,
                    radius,
                    nBits=n_Bits,
                    bitInfo=bit_info
                )

                # i am creating an empty arr

                empty_arr = np.zeros(
                    (0,),
                    np.int8
                )

                # i am going to convert morgan fingerprint
                # to array

                Chem.DataStructs.ConvertToNumpyArray(
                    morgan_finger,
                    empty_arr
                )

                # storing values in finger_prints

                finger_prints.append(empty_arr)

                # =================================================
                # GET CHEMICAL FUNCTIONAL NAME
                # =================================================

                for bit, environments in bit_info.items():

                    atom_index, environment_radius = environments[0]

                    functional_name = identify_functional_group(
                        molecule,
                        atom_index,
                        environment_radius
                    )

                    # Store feature name
                    if bit not in feature_names:

                        feature_names[bit] = (
                            f"FP_{bit}_{functional_name}"
                        )

            else:

                arr = np.zeros(
                    (n_Bits,),
                    np.int8
                )

                finger_prints.append(arr)

        except:

            arr = np.zeros(
                (n_Bits,),
                np.int8
            )

            finger_prints.append(arr)

    print(
        np.array(finger_prints).shape
    )

    # ============================================================
    # CREATE FINAL COLUMN NAMES
    # ============================================================

    final_feature_names = []

    for bit in range(n_Bits):

        if bit in feature_names:

            final_feature_names.append(
                feature_names[bit]
            )

        else:

            final_feature_names.append(
                f"FP_{bit}_Unknown"
            )

    # ============================================================
    # PRINT EXAMPLE
    # ============================================================

    print("\nMorgan fingerprint chemical functional names:")

    for name in final_feature_names[:20]:

        print(name)

    return (
        np.array(finger_prints),
        final_feature_names
    )



# X_train=smile_to_morganprint(X_train['Smiles'],radius=2,n_Bits=1024)
# X_test=smile_to_morganprint(X_test['Smiles'],radius=2,n_Bits=1024)
x_features=smile_to_morganprint(data_clean['Smiles'],radius=2,n_Bits=1024)
# x_features = pd.concat([x_features, descriptor_scaled], axis=1)




print(X_features)

# print('X_train morganfeatures prints:',X_train)
# print('X_test morganfinger prints',X_test)
# #
# models = {
#     "LinearRegression": LinearRegression(),
#     "Ridge": Ridge(),
#     "Lasso": Lasso(),
#     "RandomForest": RandomForestRegressor(random_state=42),
#     "GradientBoosting": GradientBoostingRegressor(random_state=42),
#     "Bagging": BaggingRegressor(random_state=42),
#     "XGBoost": XGBRegressor(random_state=42)}
#
# tree_based_model=[models["RandomForest"],models["GradientBoosting"],models['XGBoost'],models['GradientBoosting']]
#
# linear_model=[models['LinearRegression'],models['Ridge'],models['Lasso']]
#
#
# ################## KFold cross validation for generalization of model and model selection ######################
#
# # initialization of 10-kfold cross validation
#
# kfold=KFold(n_splits=10,shuffle=True)
#
# Kfold_result={}
#
# result=[]
#
# for name,model in models.items():
#
#
#
#     cv_score=cross_validate(model,x_features,y,cv=kfold,scoring={'r2': 'r2','mse': 'neg_mean_squared_error'})
#
#     r2_score=cv_score['test_r2']
#     r2_mean=np.mean(cv_score['test_r2'])
#     r2_std=np.std(cv_score['test_r2'])
#     print(f'r_cores of moedl{name}:',r2_score)
#     print(f'mean of r_score of {name}:',r2_mean)
#     print(f'std of r_score of {name}:',r2_std)
#
#
#     neg_score=-cv_score['test_mse']
#     mean_rmse = np.sqrt(neg_score)
#     mean_rmse_mean = mean_rmse.mean()
#     mean_rmse_std = mean_rmse.std()
#
#     print(f'mse_cores of moedl{name}:',-cv_score['test_mse'])
#     print(f'mean of mse_score of {name}:',(-cv_score['test_mse']).mean())
#     print(f'std of mse_score of {name}:',(-cv_score['test_mse']).std())
#     result.append({
#         "Model": name,"R2 Score":   r2_mean,"RMSE":mean_rmse_mean,'std_r2': r2_std})
#
#     results_df = pd.DataFrame(result)
#
#     results_df = results_df.sort_values(
#         by="R2 Score",
#         ascending=False
#     )