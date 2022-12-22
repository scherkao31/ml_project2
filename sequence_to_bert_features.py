import torch
import pickle
import re
from transformers import BertModel, BertTokenizer, AdamW

# PLEASE MAKE SUR TO CREATE THE NECCESARY FOLDERS

MAX_LEN = 512

PRE_TRAINED_MODEL_NAME = 'Rostlab/prot_bert_bfd_localization'
bert = BertModel.from_pretrained(PRE_TRAINED_MODEL_NAME)

tokenizer = BertTokenizer.from_pretrained(PRE_TRAINED_MODEL_NAME, do_lower_case=False)

def save_features_tensors(data, path, when_save = 10):
    training = []
    idx_tensor = 0
    #when_save = 10
    for i in data['Y'].keys():

        seq = data['sequence'][i]
        seq_mut = data['sequence_mutated'][i]
        seq_mask = data['sequence_mask'][i]
        label = data['Y'][i]
        amino_info = data['amino_info'] [i]
        #print(seq_mut)

        seq = ' '.join(seq)
        seq_mut = ' '.join(seq_mut)
        seq_mask = ' '.join(seq_mask)

        sequence_Example = re.sub(r"[UZOB]", "X", seq)
        encoded_input = tokenizer(sequence_Example, return_tensors='pt')
        bert_og = bert(**encoded_input)['pooler_output']

        sequence_Example = re.sub(r"[UZOB]", "X", seq_mut)
        encoded_input = tokenizer(sequence_Example, return_tensors='pt')
        bert_mut = bert(**encoded_input)['pooler_output']

        seq_mask = re.sub(r"[?]", "[MASK]", seq_mask)
        sequence_Example = re.sub(r"[UZOB]", "X", seq_mask)
        encoded_input = tokenizer(sequence_Example, return_tensors='pt')
        bert_mask = bert(**encoded_input)['pooler_output']

        training += [(bert_og, bert_mut, bert_mask, label, amino_info)]

        if (i  % when_save == 0) :
            name = path + '/tensor' + str(idx_tensor) +'.csv'
            print('Saving tensor number', idx_tensor, ': ', name )
            torch.save(training, name)
            idx_tensor += 1
            training = []

train_set = torch.load('train_set_600.csv')
load_data_tensors(train_set, 'data_bert_600/train')

val_set = torch.load('val_set_600.csv')
load_data_tensors(val_set, 'data_bert_600/val')

train_set = torch.load('train_set_215.csv')
load_data_tensors(train_set, 'data_bert_215/train')

val_set = torch.load('val_set_215.csv')
load_data_tensors(val_set, 'data_bert_215/val')

val_set_cut_5 = torch.load('cut/val_set_215_cut_5.csv')
load_data_tensors(val_set_cut_5, 'cut/cut_bert/cut_5')

val_set_cut_10 = torch.load('cut/val_set_215_cut_10.csv')
load_data_tensors(val_set_cut_10, 'cut/cut_bert/cut_10')

val_set_cut_20 = torch.load('cut/val_set_215_cut_20.csv')
load_data_tensors(val_set_cut_20, 'cut/cut_bert/cut_20')

val_set_cut_50 = torch.load('cut/val_set_215_cut_50.csv')
load_data_tensors(val_set_cut_50, 'cut/cut_bert/cut_50')

