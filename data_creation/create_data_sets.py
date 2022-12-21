import re
import torch
import torch.nn as nnx
import torch.nn.functional as F
import torch.optim as optim

torch.manual_seed(1)

import random

import csv
import pandas as pd
import numpy as np

import sklearn.metrics

        
def to_data_frame(data):
    seqs = []
    seqs_mut = []
    seqs_mask = []
    labels = []
    amino_infos = []
    for a, b, c, d, e in data:
        seqs += [a]
        seqs_mut += [b]
        seqs_mask += [c]

        labels += [d]
        amino_infos += [e]
        
    data_frame = {'sequence': seqs, 'sequence_mutated': seqs_mut, 'sequence_mask': seqs_mask,  'Y': labels, 'amino_info': amino_infos}  
    df = pd.DataFrame(data_frame)
    
    return df
        
        
def create_data_set(data, max_len = 600, false_set_max = 3000, true_set_max = 3000):
    max_len = 600
    training = []
    training_set_size = 0
    true_num = 0
    false_num = 0
    idx_tensor = 0
    save_ = False
    for i, uniprot in enumerate(data['uniprot']):
        label = data['no effect'][i]
        if label and true_num < true_set_max:
            
            if data['length'][i] < max_len and data['pos'][i] < data['length'][i] and (len(data['var_res'][i]) == 1): #some mutation are out of range and some are multiple

                position_mutation = data['pos'][i] - 1
                var_mutation = data['var_res'][i]
                seq = list(seq_dict[uniprot])

                seq_mutated = list(seq_dict[uniprot])
                seq_mask = list(seq_dict[uniprot])

                seq_mutated[position_mutation] = var_mutation
                seq_mask[position_mutation] = '?'

                seq_mut = "".join(seq_mutated)
                seq_mask = "".join(seq_mask)

                seq = seq_dict[uniprot]
                seq_mut = ''.join(seq_mutated)
                #seq_mask = ' '.join(seq_mask)

                triplet = (data['ori_res'][i], data['var_res'][i], data['pos'][i])


                training += [(seq, seq_mut, seq_mask, int(label), triplet)]

                true_num += 1
                save_ = True
                training_set_size += 1

        if (not label) and false_num < false_set_max:
            if data['length'][i] < max_len and data['pos'][i] < data['length'][i] and (len(data['var_res'][i]) == 1): #some mutation are out of range

                position_mutation = data['pos'][i] - 1
                var_mutation = data['var_res'][i]
                seq = list(seq_dict[uniprot])
                seq_mutated = list(seq_dict[uniprot])
                seq_mask = list(seq_dict[uniprot])

                seq_mutated[position_mutation] = var_mutation
                seq_mask[position_mutation] = '?'

                seq_mut = "".join(seq_mutated)
                seq_mask = "".join(seq_mask)

                seq = seq_dict[uniprot]
                seq_mut = ''.join(seq_mutated)

                triplet = (data['ori_res'][i], data['var_res'][i], data['pos'][i])


                training += [(seq, seq_mut, seq_mask, int(label), triplet)]

                false_num += 1
                save_ = True
                training_set_size += 1

        if idx_tensor > 200:
            when_save = 5
        else:
            when_save = 10 

        if (training_set_size  % when_save == 0) and save_ and (training_set_size > 0):
            idx_tensor += 1
            #training = []
            save_ = False
            
            
    return training

data= pd.read_csv("../mut_effect_train.csv")

seqs = pd.read_csv("../uniprot_fasta_sequences.csv")

num_values = 20
seq_dict = {}
for i, uniprot in enumerate(seqs['uniprot']):
    seq = seqs['sequence'][i]
    if type(seq) == str:
        seq_dict[uniprot] = seq
        
training_600 = create_data_set(data, max_len = 600, false_set_max = 3000, true_set_max = 3000)
random.shuffle(training_600)

train_set_600 = training_600[:4500]
val_set_600 = training_600[4500:]

train_set_frame_600 = to_data_frame(train_set_600)
val_set_frame_600 = to_data_frame(val_set_600)

torch.save(train_set_frame_600, 'train_set_600.csv')
torch.save(val_set_frame_600, 'val_set_600.csv')



training_215 = create_data_set(data, max_len = 215, false_set_max = 500, true_set_max = 500)
random.shuffle(training_215)

train_set_215= training_215[:800]
val_set_215 = training_215[800:]

train_set_frame_215 = to_data_frame(train_set_215)
val_set_frame_215 = to_data_frame(val_set_215)

torch.save(train_set_frame_215, 'train_set_215.csv')
torch.save(val_set_frame_215, 'val_set_215.csv')
