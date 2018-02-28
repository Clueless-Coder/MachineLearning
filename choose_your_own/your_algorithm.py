#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################

from sklearn import neighbors
from time import time
from sklearn import model_selection

#print "datapoints:",len(features_train)

nbrs= filter( lambda x: x%2!=0, list(range(1,100)))

cv_scores=[]
##finding optimal K
for k in nbrs:
    clf=neighbors.KNeighborsClassifier()
    scores=model_selection.cross_val_score(clf,features_train[:200],labels_train[:200],cv=10,scoring='accuracy')
    cv_scores.append(scores.mean())


print "k_optimal=",k_optimal
k_optimal=nbrs[cv_scores.index(max(cv_scores))]
clf=neighbors.KNeighborsClassifier(n_neighbors=k_optimal)
t0=time()
clf.fit(features_train[200:],labels_train[200:])
print "Training Time:",round(time()-t0,3),"s"


p0=time()
pred=clf.predict(features_test)
print "Pred time:",round(time()-p0 ,3),"s"
print "Accuracy:",clf.score(features_test,labels_test)
### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary








try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
