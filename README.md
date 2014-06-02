visualization_utils
===================

Some visualization utils mostly in Python

machine_learning_vis_utils.py:
------------------------------
Visualization utilities for machine learning in python.

vis_confusion_matrix:

Visualize the confusion matrix in Python.
  Input: Confusion matrix and the class list in the 
  same order as used in confusion matrix. To get the confusion matrix 
  elements in the same order as in class_list use this list to generate 
  the confusion matrix in scipy.
    
  ex:
  from sklearn.metrics import confusion_matrix
    
  cm = confusion_matrix(true_labels, pred_labels, class_list)
  
  vis_confusion_matrix(cm, class_list)
  
![Screenshot](/images/cm.png)
