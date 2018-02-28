#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess




### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


from sklearn import svm
clf=svm.SVC(kernel='rbf', C=10000)
t0=time()

##Sliced the dataset to 1% of original
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

clf.fit(features_train,labels_train)
print "training time:",round(time()-t0,3),"s"

p1=time()
pred=clf.predict(features_test)
print "predicion time:", round(time()-p1,3), "s"

#print "pred[10]: ",pred[10]," pred[26]: ",pred[26]," pred[50]:",pred[50]
print "Chris Occurence:",list(pred).count(1)


accuracy=clf.score(features_test,labels_test)
print "accuracy:",accuracy

#########################################################
### your code goes here ###

#########################################################


