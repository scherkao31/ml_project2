import torch
import pickle
import re

import pandas as pd  

# PLEASE CREATE A CUT FOLDER BEFORE RUNNING THIS FILE AND MAKE SURE OF ALL THE DIRECTORIES

train_set = torch.load('datasets/train_set_215.csv')
val_set = torch.load('datasets/val_set_215.csv')

def cut_len(data, len_seq):
    
    seqs = []
    seqs_mut = []
    seqs_mask = []
    labels = []
    amino_infos = []

    idx_tensor = 0
    when_save = 40
    save_ = False
    for i in data['Y'].keys():
        #print(i)
        #print(data['sequence'][i])
        seq = list(data['sequence'][i])
        seq_mask = list(data['sequence'][i])
        seq_mut = list(data['sequence_mutated'][i])
        label = data['Y'][i]
        amino_info = data['amino_info'][i]
        #print(seq, seq_mask, seq_mut, label)
        position_mutation = amino_info[2] - 1

        part_1 = seq[position_mutation - len_seq:position_mutation]
        part_2 = seq[position_mutation : position_mutation + len_seq]
        seq = part_1 + part_2

        part_1 = seq_mut[position_mutation - len_seq:position_mutation]
        part_2 = seq_mut[position_mutation : position_mutation + len_seq]
        seq_mut = part_1 + part_2

        seq_mask[position_mutation] = '?'
        part_1 = seq_mask[position_mutation - len_seq:position_mutation]
        part_2 = seq_mask[position_mutation : position_mutation + len_seq]
        seq_mask = part_1 + part_2


        seq = ''.join(seq)
        seq_mut = ''.join(seq_mut)
        seq_mask = ''.join(seq_mask)


        seqs += [seq]
        seqs_mut += [seq_mut]
        seqs_mask += [seq_mask]

        labels += [label]
        amino_infos += [amino_info]
        
    data_frame = {'sequence': seqs, 'sequence_mutated': seqs_mut, 'sequence_mask': seqs_mask,  'Y': labels, 'amino_info': amino_infos}  
    df = pd.DataFrame(data_frame)
    
    return df


df_train_10 = cut_len(train_set, 10)
df_val_10 = cut_len(val_set, 10)

torch.save(df_train_10, 'data/cut/train_set_215_cut_10.csv')
torch.save(df_val_10, 'data/cut/val_set_215_cut_10.csv')

df_train_5 = cut_len(train_set, 5)
df_val_5 = cut_len(val_set, 5)

torch.save(df_train_5, 'data/cut/train_set_215_cut_5.csv')
torch.save(df_val_5, 'data/cut/val_set_215_cut_5.csv')

df_train_20 = cut_len(train_set, 20)
df_val_20 = cut_len(val_set, 20)

torch.save(df_train_20, 'data/cut/train_set_215_cut_20.csv')
torch.save(df_val_20, 'data/cut/val_set_215_cut_20.csv')

df_train_50 = cut_len(train_set, 50)
df_val_50 = cut_len(val_set, 50)

torch.save(df_train_50, 'data/cut/train_set_215_cut_50.csv')
torch.save(df_val_50, 'data/cut/val_set_215_cut_50.csv')
