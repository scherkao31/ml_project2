# Prediction of the effect of a mutation in an amido acid sequence


## Generate the Data files

### Main datasets
First, you need to download the file datasets/uniprot_fasta_sequences.csv contained in https://drive.google.com/drive/folders/19PUzDqEg_kl-8nWG_Z7C7NDC9BaZTwPw?usp=sharing and put it in the folder 'datasets' of the repo (or download the full folder 'datasets' in the drive and replace the repo one), since the file is too big to upload on git.

Due to limited computational power, we use the the train set provided by the lab, to create our train set, val set and test set.
We create one small set composed of sequences with a maximum length of 215 aminoa acids and another bigger one with sequences with a maximum length of 600 aminoa acids.
To create those datasets, make that the provided files'mut_effect_train.csv' and 'uniprot_fasta_sequences.csv' are contained in the dataset folder, and run the following :

```bash
mkdir data
```

```bash
python data_creation/create_data_sets.py
```

### Cut datasets
To do some deeper analysis on how our models perform, we create new cut datasets from the 215 ones.
We cut every sequence around the mutation, and keep X amount of amino acids.
To recreate this data, run the following :

```bash
mkdir data/cut
```

```bash
python data_creation/create_cut_data_sets.py
```

### Generate sequence features using ProtBert

N.B.: Generate sequence features using ProtBert is a very expensive and long process, we invite you to download directly the necessary features by downloading the 'data' folder contained in https://drive.google.com/drive/folders/19PUzDqEg_kl-8nWG_Z7C7NDC9BaZTwPw?usp=sharing and put it in the cloned repo.

Generating sequence features using the ProtBert from amazon takes a long time, therefore we decided to create all features needed in on go and store them in csv files.

Due to limited computational power, we had to save the features for every 10 sequences, and couldn't create just one big files.
To recreate those files, you should run the following :

If the following folders are not already created :


```bash
mkdir data/data_bert_600 data/data_bert_215 data/cut/cut_bert
```

```bash
mkdir data/data_bert_600/train data/data_bert_600/val data/data_bert_215/train data/data_bert_215/val data/cut/cut_bert/cut_5 data/cut/cut_bert/cut_10 data/cut/cut_bert/cut_20 cut/cut_bert/cut_50
```

Then run :

```bash
python3 sequence_to_bert_features.py
```
## Recreate our results

To use our models and recreate our results, you should follow the notebook FINAL which is already quite self-explenatory.


## Requirements

Make sure that following library are installed :

pytorch, pandas, sklearn, re, csv, numpy, seaborn, matplotlib
