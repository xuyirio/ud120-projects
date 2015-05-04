#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people %d " % len(enron_data)  # 146
print "Number of features per people %d " % len(enron_data[0]) # 21

print "James\'s Stock %d " % enron_data["PRENTICE JAMES"]["total_stock_value"]  # 1095040

print "Wesley emailed %d to poi " % enron_data["COLWELL WESLEY"]["from_this_person_to_poi"] # 11

print "Jeffrey exercised stock options %d " % enron_data["SKILLING JEFFREY K"]["exercised_stock_options"] # 19250000

print "Lay: %d " % enron_data["LAY KENNETH L"]["total_payments"]  # 103559793
print "Skilling: %d " % enron_data["SKILLING JEFFREY K"]["total_payments"]  # 8682716
print "Fastow: %d " % enron_data["FASTOW ANDREW S"]["total_payments"] # 2424083

count_poi = 0
count_has_salary = 0
count_has_email = 0
count_has_total_payments = 0
poi_has_total_payments = 0
for people, features in enron_data.iteritems():
  if features["poi"]:
    count_poi += 1
    if features["total_payments"] != "NaN":
      poi_has_total_payments += 1
  if features["salary"] != "NaN":
    count_has_salary += 1
  if features["email_address"] != "NaN":
    count_has_email += 1
  if features["total_payments"] != "NaN":
    count_has_total_payments += 1
print "Number of people of interest %d " % count_poi  # 18
print "Number of people having salary %d " % count_has_salary #95
print "Number of people having email %d " % count_has_email # 111
print "Number of people having total payments %d " % count_has_total_payments #125
print "Number of poi having total payments %d " % poi_has_total_payments  # 18
