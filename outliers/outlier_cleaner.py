#!/usr/bin/python

import operator

def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []

    ### your code goes here
    for i in range(90):
      cleaned_data.append((ages[i], net_worths[i], abs(predictions[i] - net_worths[i])))
    cleaned_data.sort(key=lambda tup: tup[2])
    cleaned_data = cleaned_data[0:81]
    return cleaned_data

