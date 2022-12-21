# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tqdm import tqdm
import numpy as np
from keras.utils import to_categorical
import tensorflow as tf

codes = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
         'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

def create_dict(codes):
    char_dict = {}
    for index, val in enumerate(codes):
        char_dict[val] = index+1

    return char_dict


def integer_encoding(seq, char_dict):
    """
    - Encodes code sequence to integer values.
    - 20 common amino acids are taken into consideration
    and rest 4 are categorized as 0.
    """
    
    seq_encode = []
    #if type(seq) == str:
    for code in seq:
        seq_encode.append(char_dict.get(code, 0))
    #else:
    #    seq_encode.append(np.nan)
    return seq_encode


def get_ohe_batch(data, MAX_SEQUENCE, batch_size, batch_k, char_dict):
    labels=[]
    # iterate over a single batch
    for i in range(batch_k*batch_size, batch_size*(batch_k+1)) : 

        # origin shape: [n, 2, 800, 21] = 1, 2, 800, 21
        # input_layer: 3 input channels, 6 output channels, 5 kernel size
        images = np.zeros((batch_size, 2, MAX_SEQUENCE, 21))
        
        # encode into the right shape
        encoded_image_0 = tf.keras.utils.to_categorical(integer_encoding(data.iloc[i][:2].values[0], char_dict), num_classes=21, dtype=np.int64)
        encoded_image_1 = tf.keras.utils.to_categorical(integer_encoding(data.iloc[i][:2].values[1], char_dict), num_classes=21, dtype=np.int64)
        labels.append(data.iloc[i][2])

        # pad it
        padding_0 = int((MAX_SEQUENCE - encoded_image_0.shape[0])/2)

        # center the padding
        if((MAX_SEQUENCE - encoded_image_0.shape[0])%2==1):
            padding_1 = int((MAX_SEQUENCE - encoded_image_0.shape[0])/2)+1
        else :
            padding_1 = padding_0

        try :
            images[i%batch_size, 0,:,:] = np.pad(encoded_image_0, ((padding_0, padding_1), (0, 0)), 'constant', constant_values=(np.int64(0)))
            images[i%batch_size, 1,:,:] = np.pad(encoded_image_1, ((padding_0, padding_1), (0, 0)), 'constant', constant_values=(np.int64(0)))
        except ValueError:
            print("Problem with shapes of the two images at iteration : %d" %i)

    return images, labels


def get_ohe_i(data, MAX_SEQUENCE, i, char_dict):

    # origin shape: [n, 2, 800, 21] = 1, 2, 800, 21
    # input_layer: 3 input channels, 6 output channels, 5 kernel size
    images = np.zeros((2, MAX_SEQUENCE, 21))
    
    # encode into the right shape
    encoded_image_0 = tf.keras.utils.to_categorical(integer_encoding(data.iloc[i][:2].values[0], char_dict), num_classes=21, dtype=np.int64)
    encoded_image_1 = tf.keras.utils.to_categorical(integer_encoding(data.iloc[i][:2].values[1], char_dict), num_classes=21, dtype=np.int64)
    label = data.iloc[i][2]

    # pad it
    padding_0 = int((MAX_SEQUENCE - encoded_image_0.shape[0])/2)

    # center the padding
    if((MAX_SEQUENCE - encoded_image_0.shape[0])%2==1):
        padding_1 = int((MAX_SEQUENCE - encoded_image_0.shape[0])/2)+1
    else :
        padding_1 = padding_0

    try :
        images[0,:,:] = np.pad(encoded_image_0, ((padding_0, padding_1), (0, 0)), 'constant', constant_values=(np.int64(0)))
        images[1,:,:] = np.pad(encoded_image_1, ((padding_0, padding_1), (0, 0)), 'constant', constant_values=(np.int64(0)))
    except ValueError:
        print("Problem with shapes of the two images at iteration : %d" %i)

    return images, label



def create_dataset(data, MAX_SEQUENCE, char_dict):

    data_len = data.shape[0]

    images = np.zeros((data_len, 2, MAX_SEQUENCE, 21))
    labels = np.zeros(data_len)

    for i in tqdm(range(data_len)):
        
        images[i], labels[i] = get_ohe_i(data, MAX_SEQUENCE, i, char_dict)
    
    return images, labels


    