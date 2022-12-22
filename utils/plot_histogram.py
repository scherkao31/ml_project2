import seaborn as sns
import matplotlib.pylab as plt

import numpy as np



def plot_histogram(data_with_pred, max_mut = 0):

    all_mutations_dict_ = {}
    all_mutations_dict_true = {}
    all_mutations_dict_pred_acc = {}
    char_dict = {}
    index = 0
    for idx, seq in enumerate(data_with_pred):
        #print(seq[5])
        label = seq[3]#[0]
        pred = seq[4]
        position_mutation = seq[5][2]

        var_original = seq[5][0]
        var_mutation = seq[5][1]

        key = var_original + '-->' + var_mutation
        #print(label)
        if len(var_mutation) == 1 and len(var_original):
            num_ = all_mutations_dict_.get(key, 0)
            all_mutations_dict_[key] = num_ + 1

            if label:
                trues_ = all_mutations_dict_true.get(key, 0) + 1
            else:
                trues_ = all_mutations_dict_true.get(key, 0)

            if pred == label:
                trues_pred = all_mutations_dict_pred_acc.get(key, 0) + 1
            else:
                trues_pred = all_mutations_dict_pred_acc.get(key, 0)

            all_mutations_dict_true[key] = trues_
            all_mutations_dict_pred_acc[key] = trues_pred
            
    for key in all_mutations_dict_.keys():
        acc = all_mutations_dict_pred_acc[key] / all_mutations_dict_[key]
        #print(acc)
        all_mutations_dict_pred_acc[key] = acc
    
    #print(all_mutations_dict_true)
    #print(all_mutations_dict_pred_acc)
    list_key = []
    list_value = []
    list_value_true = []
    list_value_pred_acc = []
    for key in all_mutations_dict_:
        value = all_mutations_dict_[key]
        value_true = all_mutations_dict_true[key]
        value_pred_acc = all_mutations_dict_pred_acc[key]

        if value > max_mut:
            list_key += [key]
            list_value += [value]
            list_value_true += [value_true]
            list_value_pred_acc += [value_pred_acc]
            
    a = list_key#[:10]
    b = list_value#[:10]
    c = list_value_true#[10:20]
    d = list_value_pred_acc
    
    
    the_range = list(range(len(a)))
    plt.rcParams["figure.figsize"] = (20,3)
    plt.bar(the_range, b, label = 'Total', color = 'lightblue', ec = 'lightcoral')
    plt.bar(the_range, c, label = 'No effect', color = 'lightcoral')
    #plt.bar(the_range, d, label = 'No effect: pred', color = 'g')
    #plt.bar(range(len(c)), b)
    plt.title("Types of mutations")
    plt.ylabel("Amount of the mutation")
    plt.xticks(range(len(a)), a)
    plt.legend()
    plt.show()
    
    the_range = list(range(len(a)))
    plt.rcParams["figure.figsize"] = (20,3)
    #plt.bar(the_range, b, label = 'Total', color = 'b')
    #plt.bar(the_range, c, label = 'No effect', color = 'r')
    plt.bar(the_range, d, label = 'No effect: pred', color = 'lightgreen', ec = 'darkgreen')
    #plt.bar(range(len(c)), b)
    plt.title("Accuracy of the model's predictions for every type of mutation")
    plt.ylabel("Accuracy")
    plt.xticks(range(len(a)), a)
    plt.legend()
    plt.show()



