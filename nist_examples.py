# -*- coding: utf-8 -*-
"""Nist-Examples.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ol3o97L-28pLBnaKYJIqrHrIgUJHhaZu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Simple, incredibly accurate SVM on NIST dataset.

# SVM

from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split

nist = datasets.load_digits()

X = nist.data
y = nist.target

clf = svm.SVC()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, shuffle=True) # split data
clf.fit(X_train, y_train)

predicted = clf.predict(X_test)
print(predicted)

print(f"Classification report for classifier {clf}:\n", f"{metrics.classification_report(y_test, predicted)}\n")