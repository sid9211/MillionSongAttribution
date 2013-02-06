import csv_io
import numpy as np
from sklearn import cross_validation
from sklearn import grid_search
from sklearn import svm
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn.metrics import metrics
from sklearn.grid_search import GridSearchCV
import sys

def main(inputFile):
    #read in  data, parse into training and target sets
    data = csv_io.read_data(inputFile)
    target = np.array( [x[0] for x in data] )
    train = np.array( [x[1:] for x in data] )
    train_scaled = preprocessing.scale(train)

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(train_scaled, target, test_size = 0.5, random_state = 0)
    
    tuned_parameters = [{'kernel': ['rbf'],'gamma': [ 1e-3, 1e-4 ],
                        'C':[1, 10, 100, 1000]},
                       {'kernel': ['linear'], 'C':[1, 10,100, 1000]}]

    scores = [
           ('precision', metrics.precision_score),
    ]
  
    for score_name, score_func in scores:
        print "Tuning hyper-parameters for %s" % score_name
        print
        clf  = GridSearchCV(SVC(C=1), tuned_parameters, score_func=score_func)
        clf.fit(X_train, y_train, cv = 5)

        print "Best Parameters set found on development set:"
        print 
        print clf.best_estimator_
        print
        print "Grid scores on development set:"
        print
        for params, mean_score, scores in clf.grid_scores_:
            print "%0.3f (+/-%0.03f) for %r" % (
            mean_score, scores.std() / 2, params)
        print

    
        
        print "Detailed classification report:"
        print
        print "The model is trained on the full development set."
        print "The scores are computed on the full evaluation set."
        print
        y_true, y_pred = y_test, clf.predict(X_test)
        print metrics.classification_report(y_true, y_pred)
        print

if __name__=="__main__":
    inputfilename = sys.argv[-1]
    main(inputfilename)



     
