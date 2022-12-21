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

### Generate sequence features using ProtBert

Generating sequence features using the ProtBert from amazon takes a long time, therefore we decided to create all features needed in on go and store them in csv files.

Due to limited computational power, we had to save the features for every 10 sequences, and couldn't create just one big files.
To recreate those files, you should run the following :

If the following folders are not already created :

```bash
mkdir data_bert_600 data_bert_215 cut/cut_bert
```

```bash
mkdir data_bert_600/train data_bert_600/val data_bert_215/train data_bert_215/val cut/cut_bert/cut_5 cut/cut_bert/cut_10 cut/cut_bert/cut_20 cut/cut_bert/cut_50
```

Then run :

```bash
python3 sequence_to_bert_features.py
```

## Requirements

To install requirements:

```bash
pip3 install -r requirements.txt
```
