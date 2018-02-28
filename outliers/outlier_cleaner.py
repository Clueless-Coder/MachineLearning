#!/usr/bin/python

import numpy as np
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    import math
    cleaned_data = []
    error=[]
    ### your code goes here
    for i in range(len(predictions)):
        error.append(abs(net_worths[i]-predictions[i]))
    
    clip=int(math.ceil(len(predictions)/10))
    #print "clip=",clip
    #print error
    for i in range(clip):
        ind=(np.argmax(error))
        #print "maxerr=",error[ind],"ind=",ind
        
        error=np.delete(error,ind)
        ages=np.delete(ages,ind)
        net_worths=np.delete(net_worths,ind)
    #print error
    cleaned_data = zip(ages,net_worths,error)  
    #print cleaned_data
    return cleaned_data

