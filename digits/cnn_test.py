from sklearn.metrics.cluster import supervised
import scipy.io as sio
from scipy.optimize import linear_sum_assignment
import numpy as np
import csv
import os

digits_train = sio.loadmat('digits-train.mat')
labels_true = digits_train['labels_train']

labels_pred = []
with open('labels_pred.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        labels_pred.append([int(row[0])])

labels_true, labels_pred = supervised.check_clusterings(labels_true, labels_pred)
# labels_true : int array with ground truth labels, shape = [n_samples]
# labels_pred : int array with estimated labels, shape = [n_samples]
value = supervised.contingency_matrix(labels_true, labels_pred)
# value : array of shape [n, n] whose (i, j)-th entry is the number of samples in true class i and in predicted class j
[r, c] = linear_sum_assignment(-value)
accr = value[r, c].sum() / len(labels_true)