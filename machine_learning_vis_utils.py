#!/usr/bin/env python

"""visualize_cm.py: Visualizing confusion matrix ."""

__author__      = "Krishna Dubba"


import matplotlib.pyplot as plt
import numpy as np
    
def vis_confusion_matrix(conf_mat, class_list, out_file=None):
    """ Visualize the confusion matrix in Python.
    Input: Confusion matrix and the class list in the 
    same order as used in confusion matrix. To get the confusion matrix 
    elements in the same order as in class_list use this list to generate 
    the confusion matrix in scipy.
    
    ex:
    from sklearn.metrics import confusion_matrix
    
    cm = confusion_matrix(true_labels, pred_labels, class_list)
    vis_confusion_matrix(cm, class_list)
    """
    
    norm_conf = []
    for i in conf_mat:
        a = 0
        tmp_arr = []
        a = sum(i, 0)
        for j in i:
            tmp_arr.append(float(j)/float(a))
        norm_conf.append(tmp_arr)
    
    fig = plt.figure()
    plt.clf()
    ax = fig.add_subplot(111)
    #ax.set_aspect(1)
    res = ax.imshow(np.array(norm_conf), cmap=plt.cm.bone, 
                    interpolation='nearest')
    
    width = len(conf_mat)
    height = len(conf_mat[0])
    
    # Display recall in the diagonal
    for x in xrange(width):
        for y in xrange(height):
            ratio = float(conf_mat[x][y])/sum(conf_mat[x])
            ratio_str = '%0.2f' %ratio
            ax.annotate(ratio_str, xy=(y, x), 
                        horizontalalignment='center',
                        verticalalignment='center')
    
    cb = fig.colorbar(res)
    alphabet = class_list
    
    ax.xaxis.tick_top()    
    ax.xaxis.set_tick_params(labelsize=20)
    ax.yaxis.set_tick_params(labelsize=20)
    
    # Rotate the x ticks
    plt.xticks(range(width), class_list[:width], rotation=85)
    plt.yticks(range(height), class_list[:height])
    plt.tight_layout()
    if out_file == None:
        plt.show()
    else:    
        plt.savefig(out_file, format='png')
