
import pandas as pd
import numpy as np
import os

from rdkit import Chem
from rdkit.Chem import AllChem, Draw


# ============================================================
# 1. LOAD DATA
# ============================================================

data = pd.read_csv(
    '/home/sails/shiva_sailes/saile_code/ML_file/'
    'ml-driven-qsar-modeling-for-large-scale-bioactivity-predictions (2)/train.csv'
)

smiles = data.Smiles
# ============================================================
# 2. TOP 20 FEATURES
# ============================================================

important_bits = [
    337, 496, 164, 494, 488,
    252, 183, 489, 68, 445,
    491, 162, 490, 419, 242,
    495, 449, 270, 70, 79
]


# ============================================================
# 3. FUNCTION TO RETRIEVE MORGAN STRUCTURAL INFORMATION
# ============================================================

def get_bit_information(smiles,bit_number,radius=2,nBits=1024):

    # Make sure we received ONE SMILES, not a pandas Series
    if isinstance(smiles, pd.Series):
        return None

    if pd.isna(smiles):
        return None

    smiles = str(smiles).strip()

    # Ignore invalid values
    if smiles in ["", "0", "1", "None", "nan"]:
        return None

    # Convert SMILES to RDKit molecule
    molecule = Chem.MolFromSmiles(smiles)

    if molecule is None:
        return None

    # Morgan fingerprint + bit information
    bit_info = {}

    fingerprint = AllChem.GetMorganFingerprintAsBitVect(molecule,radius,nBits=nBits,bitInfo=bit_info)

    # Does this bit occur in this molecule?
    if bit_number not in bit_info:
        return None

    results = []

    # A bit can have more than one environment
    for atom_index, environment_radius in bit_info[bit_number]:

        # Find bonds in Morgan environment
        bond_indices = Chem.FindAtomEnvironmentOfRadiusN(
            molecule,
            environment_radius,
            atom_index
        )

        # Find atoms in environment
        atom_indices = {atom_index}

        for bond_index in bond_indices:

            bond = molecule.GetBondWithIdx(bond_index)

            atom_indices.add(bond.GetBeginAtomIdx())

            atom_indices.add(bond.GetEndAtomIdx())

        atom_indices = sorted(atom_indices)

        # Get fragment SMILES
        if len(bond_indices) > 0:

            fragment_mol = Chem.PathToSubmol(molecule,bond_indices)

            fragment_smiles = Chem.MolToSmiles(fragment_mol)

        else:

            fragment_smiles = (molecule.GetAtomWithIdx(atom_index).GetSymbol())

        # Store information
        results.append({

            "Feature_Bit": bit_number,

            "Morgan_Radius":
                environment_radius,

            "Central_Atom_Index":
                atom_index,

            "Central_Atom":
                molecule
                .GetAtomWithIdx(atom_index)
                .GetSymbol(),

            "Environment_Atoms":",".join(map(str, atom_indices)),

            "Fragment_SMILES":fragment_smiles,

            "Full_SMILES":smiles})

    return results


# ============================================================
# 4. SEARCH DATASET FOR ALL 20 FEATURES
# ============================================================

all_results = []


for bit_number in important_bits:

    print("\n======================================")
    print("Searching Feature:", bit_number)
    print("======================================")

    found = False

    # IMPORTANT:
    # row["Smiles"] gives ONE SMILES string
    for index, row in data.iterrows():

        smiles = row["Smiles"]

        result = get_bit_information(smiles=smiles,bit_number=bit_number,radius=2,nBits=1024)

        if result is not None:

            for item in result:

                item["Dataset_Row"] = index

                # ChEMBL ID
                if "Molecule ChEMBL ID" in data.columns: item["ChEMBL_ID"] = (row["Molecule ChEMBL ID"])

                # Activity
                if "pChEMBL Value" in data.columns:

                    item["pChEMBL_Value"] = ( row["pChEMBL Value"])

                all_results.append(item)

            print("FOUND Feature:",bit_number)

            print("SMILES:",smiles)

            print("Fragment:",result[0]["Fragment_SMILES"])

            found = True

            # Use first representative molecule
            break

    if not found:

        print(
            "Feature",bit_number,"NOT FOUND")


# ============================================================
# 5. CREATE RESULTS DATAFRAME
# ============================================================

results_df = pd.DataFrame( all_results)


# ============================================================
# 6. SAVE EXCEL FILE
# ============================================================

output_file = ("Morgan_Top20_Feature_Structural_Information.xlsx")

results_df.to_excel(output_file,index=False)


# ============================================================
# 7. PRINT RESULTS
# ============================================================


print("Excel file:",output_file)

if len(results_df) > 0:

    print( results_df[["Feature_Bit","Morgan_Radius","Central_Atom","Environment_Atoms","Fragment_SMILES","ChEMBL_ID","pChEMBL_Value"]].to_string(index=False))

else:

    print("No features were found.")


# ============================================================
# 8. CREATE STRUCTURE IMAGES
# ============================================================

image_folder = "Morgan_Top20_Structures"

os.makedirs(image_folder,exist_ok=True)


for bit_number in important_bits:

    bit_rows = results_df[results_df["Feature_Bit"] == bit_number]

    if len(bit_rows) == 0:
        continue

    row = bit_rows.iloc[0]

    smiles = row["Full_SMILES"]

    molecule = Chem.MolFromSmiles(smiles)

    if molecule is None:
        continue

    atom_index = int(row["Central_Atom_Index"])

    radius = int(row["Morgan_Radius"])

    # Find environment
    bond_indices = Chem.FindAtomEnvironmentOfRadiusN(molecule,radius,atom_index)

    atom_indices = {atom_index}

    for bond_index in bond_indices:

        bond = molecule.GetBondWithIdx(bond_index)

        atom_indices.add(bond.GetBeginAtomIdx())

        atom_indices.add(bond.GetEndAtomIdx())

    # Draw molecule with highlighted Morgan environment
    image = Draw.MolToImage(
        molecule,
        size=(600, 500),
        highlightAtoms=list(atom_indices),
        highlightBonds=list(bond_indices))

    image.save(os.path.join(image_folder,f"Feature_{bit_number}.png"))

    print("Structure saved:",bit_number)


print("\nAll structure images saved in:")
print(image_folder)