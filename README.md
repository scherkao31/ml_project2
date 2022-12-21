# Prediction of the effect of a mutation in an amido acid sequence

## Requirements

```bash
mkdir data figure
```

## Generate the Data files

### Main datasets
Due to limited computational power, we use the the train set provided by the lab, to create our train set, val set and test set.
We create one small set composed of sequences with a maximum length of 215 aminoa acids and another bigger one with sequences with a maximum length of 600 aminoa acids.
To create those datasets, make that the provided files'mut_effect_train.csv' and 'uniprot_fasta_sequences.csv' are contained in the dataset folder, and run the following :

```bash
python data_creation/create_data_sets.py
```

### Cut datasets
To do some deeper analysis on how our models perform, we create new cut datasets from the 215 ones.
We cut every sequence around the mutation, and keep X amount of amino acids.
To recreate this data, run the following :

```bash
mkdir cut
```

```bash
python data_creation/create_cut_data_sets.py
```
## Requirements

To install requirements:

```bash
pip3 install -r requirements.txt
```
