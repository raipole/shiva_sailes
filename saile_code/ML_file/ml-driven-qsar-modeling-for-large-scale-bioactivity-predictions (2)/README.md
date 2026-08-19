# Interpretable Machine Learning for QSAR Bioactivity Prediction

A comparative regression and classification study using Morgan fingerprints and
SHAP-based feature attribution.

Seven regression algorithms and six classifiers were trained on a curated
ChEMBL-derived bioactivity dataset, across nine representation and
feature-selection configurations, with SHAP attribution used to recover which
substructures the fitted models rely on.

**Author** Shivananda Reddy Kasula (Register No. 39958)
**Supervisor** Shyam Rajagopalan
**Programme** Syngene–IBAB Certification Program in Artificial Intelligence in
Life Sciences, Institute of Bioinformatics and Applied Biotechnology & Biocon
Academy, Bengaluru

---

## Results at a glance

| | |
|---|---|
| Compounds (supplied / after deduplication) | 2,700 / ~2,350 |
| Train / test split | 1,645 / 705 (70:30, seed 7) |
| Representation | Morgan fingerprint, radius 2, 1024 bits |
| Best cross-validated R² | **0.664** (Random Forest, untuned baseline) |
| Best R² across all configurations | 0.685 (2048 bits + variance threshold) |
| RMSE | 0.655 log units ≈ 4.5-fold in predicted potency |
| Cross-validation standard deviation | ~0.04 |
| Top SHAP feature | Aromatic amide (F_337), 18.7% of total attribution |
| Best classification F1 | 0.984 ± 0.003 (Random Forest) |
| Best classification ROC-AUC | 0.921 ± 0.029 (Logistic Regression) |

Three findings are worth stating plainly:

1. **Tree ensembles win as a class, not individually.** Random Forest (0.664),
   XGBoost (0.653) and Bagging (0.634) all fall within one cross-validation
   standard deviation of each other. No single winner is claimed.
2. **Neither feature selection nor grid search beat the untuned baseline by a
   meaningful margin.** The best configuration improved R² by 0.021 against a
   fold-to-fold SD of ~0.04. Signal is distributed across the representation
   rather than concentrated in a few bits — all 497 retained features carry
   non-zero attribution, and the top 20 hold only 54% of it.
3. **The classification task is easier than it looks.** F1 scores cluster
   within 0.008 of one another while ROC-AUC standard deviations run twenty
   times larger than F1's, which is the signature of class imbalance. See
   [Known limitations](#known-limitations).

---

## Repository layout

```
├── QSAR_Bioactivity_Predictor.py    # main pipeline: EDA → fingerprints → CV → results
├── morgan_named_features.py         # Morgan bits → substructure names (importable module)
├── requirements.txt
├── data/
│   └── README.md                    # dataset access notes — data itself is NOT in this repo
├── outputs/
│   ├── morgan_bit_legend.csv        # bit → fragment mapping, generated at runtime
│   └── figures/
└── docs/
    └── project_report.pdf
```

---

## Data availability

**The dataset is not included in this repository and must not be committed to
it.** The bioactivity data were supplied in blinded form by the industrial
partner: molecule identifiers and pChEMBL values were retained, but the
biological target, assay types and therapeutic context were withheld. Redistributing
the file publicly would require the partner's permission.

If you have been given `train.csv`, place it in `data/` and point the script at
it. The file needs three columns:

| Column | Description |
|---|---|
| `Molecule ChEMBL ID` | Compound identifier (dropped before modelling) |
| `Smiles` | SMILES string encoding the structure |
| `pChEMBL Value` | Negative base-10 log of the molar activity concentration |

To reproduce the method on public data instead, any single-target activity set
exported from ChEMBL with these three columns will run unmodified.

---

## Installation

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>

python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

RDKit is the one dependency that can be awkward under `pip` on some platforms.
If it fails:

```bash
conda install -c conda-forge rdkit
```

### requirements.txt

```
pandas>=1.5
numpy>=1.23
scikit-learn>=1.2
xgboost>=1.7
lightgbm>=3.3
rdkit>=2023.3.1
shap>=0.42
matplotlib>=3.6
```

---

## Usage

The data path is currently hard-coded near the top of
`QSAR_Bioactivity_Predictor.py`. Edit this line before running:

```python
data = pd.read_csv('data/train.csv')
```

Then:

```bash
python QSAR_Bioactivity_Predictor.py
```

The script prints exploratory statistics, the fingerprint legend summary,
per-model cross-validation scores, and a ranked results table, and writes
`morgan_bit_legend.csv`.

### Named fingerprint features

A raw Morgan fingerprint yields anonymous columns — bit 314 is just "bit 314",
which makes a SHAP plot unreadable. `morgan_named_features.py` retains RDKit's
`bitInfo` map at generation time and reconstructs the atom environment behind
each bit, so columns arrive as `bit0337_c1ccccc1C(=O)N` rather than `337`.

```python
from morgan_named_features import build_legend, featurize, top_features_by_shap

legend = build_legend(data_clean['Smiles'], radius=2, n_bits=1024)
print(legend.summary())

X_train = featurize(train_smiles, legend)   # same legend for every split,
X_test  = featurize(test_smiles,  legend)   # so columns stay aligned

legend.to_frame().to_csv('outputs/morgan_bit_legend.csv', index=False)
```

Build the legend once on the full deduplicated set and reuse it. This is not
leakage: the fingerprint transform estimates no parameters from the data, so
the bit-to-fragment mapping is a property of the hash function and the
chemistry, identical whichever fold a molecule lands in.

Two behaviours worth knowing. Folding 2³² hash values into 1024 slots forces
collisions, so chemically distinct fragments share bits — colliding bits are
suffixed `_x3` and the full fragment list per bit is written to the legend CSV.
And feature names have square brackets substituted (`[nH]` → `{nH}`), because
XGBoost rejects `[`, `]` and `<` in feature names outright.

---

## Method

**Preprocessing.** Records deduplicated on the SMILES column keeping the first
occurrence. Compounds encoded as Morgan fingerprints (radius 2) at 1024 and
2048 bits, optionally concatenated with RDKit physicochemical descriptors.

**Regression task.** Continuous pChEMBL predicted by Linear Regression, Ridge,
Lasso, Random Forest, Gradient Boosting, Bagging and XGBoost. Validation by
70:30 hold-out plus 10-fold cross-validation; metrics R², RMSE, MAE.

**Classification task.** Compounds labelled active at pChEMBL ≥ 5 (10 µM) and
modelled by Logistic Regression, Ridge, Random Forest, LightGBM, Bagging and
XGBoost, with stratified 10-fold cross-validation; metrics accuracy,
precision, recall, F1, ROC-AUC.

**Feature selection.** Nine configurations compared: raw fingerprints at both
bit lengths, with and without descriptors, variance thresholding at 0.01
(reducing to 497 features), PCA at 95% retained variance, and SHAP-guided
selection of the top 50, 100, 150, 300 and 350 features.

**Interpretability.** TreeSHAP attributions computed for the fitted tree
ensembles, ranked by mean absolute SHAP value and compared across algorithms.

---

## Interpretability findings

The six highest-attribution features:

| Rank | Feature | Bit | mean \|SHAP\| |
|---|---|---|---|
| 1 | Aromatic amide | F_337 | 0.335 |
| 2 | Aniline | F_496 | 0.090 |
| 3 | Azole-like N-heterocycle | F_164 | 0.075 |
| 4 | Amine + N-heterocycle | F_494 | 0.061 |
| 5 | N-heterocycle + ethyl | F_488 | 0.052 |
| 6 | Acylated N-heterocycle | F_252 | 0.043 |

Four of the six contain a nitrogen heterocycle and four present a
hydrogen-bond donor and acceptor within one motif — a coherent chemical theme
rather than six unrelated bits. Twelve of the top twenty features are shared
between the Random Forest and Gradient Boosting rankings, two algorithms that
build ensembles by entirely different mechanisms, which suggests the
attribution reflects the data rather than one model's inductive bias.

These are hypotheses, not established structure–activity relationships. High
attribution means the model relies on a fragment; with the target blinded it
cannot be checked against a binding site, and the model may be keying on a
scaffold common to a well-represented compound series.

---

## Known limitations

Stated plainly, because they bound what the results support.

- **Random splitting.** Analogues of training compounds appear in the test set,
  so scores measure interpolation within known chemistry rather than
  prospective prediction. A Bemis–Murcko scaffold split or a time split would
  be the harder and more realistic test.
- **No external validation set and no applicability domain.** Every prediction
  is currently reported with equal confidence regardless of how unusual the
  compound is.
- **Bit collisions are not quantified.** Folding makes a bit index chemically
  ambiguous; the legend CSV now records collisions per bit, but the study's
  reported results predate that.
- **Assay noise floor unmeasured.** Public bioactivity data typically carries
  around 0.5 log units of inter-assay variability, so an RMSE of 0.655 may sit
  close to the irreducible floor — but this was not measured for this dataset.
- **Duplicated output files.** The two PCA runs and the Lasso-selection run
  produced identical output files and must be re-run. Conclusions that do not
  depend on those three configurations are unaffected.
- **Blinded target.** No target-specific literature comparison and no
  structural validation of the SHAP results were possible.

### Before this repository is presented as final

- [ ] Record the class balance and majority-class baseline F1, and state both
      alongside the classification results. F1 computed on a dominant active
      class is flattered by imbalance; MCC would be the more informative metric
      here.
- [ ] Confirm whether SHAP-guided feature selection was nested inside each
      cross-validation fold. If the ranking was computed once on the full
      dataset, held-out compounds influenced which features survived and those
      scores are optimistic.
- [ ] Set `random_state` on `KFold` so reported means and standard deviations
      are exactly reproducible.
- [ ] Record library version numbers from the working environment.

---

## Citation

```bibtex
@mastersthesis{kasula2026qsar,
  author = {Kasula, Shivananda Reddy},
  title  = {Interpretable Machine Learning for {QSAR} Bioactivity Prediction:
            A Comparative Regression and Classification Study Using Morgan
            Fingerprints and {SHAP}-Based Feature Attribution},
  school = {Institute of Bioinformatics and Applied Biotechnology and
            Biocon Academy},
  year   = {2026},
  type   = {Project Report},
  note   = {Syngene--IBAB Certification Program in Artificial Intelligence
            in Life Sciences}
}
```

## Key references

- Rogers, D., & Hahn, M. (2010). Extended-connectivity fingerprints. *Journal
  of Chemical Information and Modeling, 50*(5), 742–754.
- Lundberg, S. M., & Lee, S.-I. (2017). A unified approach to interpreting
  model predictions. *Advances in Neural Information Processing Systems, 30*.
- Lundberg, S. M., et al. (2020). From local explanations to global
  understanding with explainable AI for trees. *Nature Machine Intelligence,
  2*(1), 56–67.
- Cherkasov, A., et al. (2014). QSAR modeling: Where have you been? Where are
  you going to? *Journal of Medicinal Chemistry, 57*(12), 4977–5010.
- Tropsha, A. (2010). Best practices for QSAR model development, validation,
  and exploitation. *Molecular Informatics, 29*(6–7), 476–488.

## Acknowledgements

Carried out under the supervision of Shyam Rajagopalan at the Institute of
Bioinformatics and Applied Biotechnology, in partnership with Biocon Academy
and Syngene International.

## License

Code released under the MIT License — see `LICENSE`. The bioactivity dataset is
not covered by this license and is not distributed here.
