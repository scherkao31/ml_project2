# Prediction of the effect of a mutation in an amido acid sequence

## Requirements

```bash
mkdir data figure
```

## Generate the Data files

Due to limited computational power, we use the the train set provided by the lab, to create our train set, val set and test set.
We create one small set composed of sequences with a maximum length of 215 aminoa acids and another bigger one with sequences with a maximum length of 600 aminoa acids.
To create those datasets, make that the provided files'mut_effect_train.csv' and 'uniprot_fasta_sequences.csv' are contained in the dataset folder, and run the following :

```bash
python create_data_sets.py
```

## Requirements

To install requirements:

```bash
pip3 install -r requirements.txt
```
