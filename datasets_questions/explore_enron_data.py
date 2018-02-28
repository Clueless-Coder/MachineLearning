#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Size of dataset:",len(enron_data)

print "No. of Features:",len(enron_data.values()[0])

count=0
for key in enron_data:
    if enron_data[key]['poi']==1:
        count=count+1

"""
print "No. of POIs:",count

with open("../final_project/poi_names.txt") as f:
    print "POI Compiled by Catie:",(sum(1 for _ in f)-2)

print "Stocks of James Prentice:",enron_data["Prentice James".upper()]['total_stock_value']

print "Email from Wesley Colwell to persons of interest:",enron_data["Colwell Wesley".upper()]['from_this_person_to_poi']

print "value of stock options exercised by Jeffrey K Skilling",enron_data["Skilling Jeffrey K".upper()]['exercised_stock_options']

print "JEFF",enron_data["Skilling Jeffrey K".upper()]
print "KEN",enron_data["Lay Kenneth L".upper()]
print "ANDY",enron_data["Fastow Andrew S".upper()]




sal,email=0,0
for key in enron_data:
    if enron_data[key]['salary']!='NaN':
        sal=sal+1
    if enron_data[key]['email_address']!='NaN':
        email=email+1

print "Salaries:",sal,"Emails:",email

"""

print enron_data.values()
payment=0
for key in enron_data:
    if enron_data[key]['total_payments']=='NaN':
        payment=payment+1

print "% of NaN for total payment=",payment*100/len(enron_data)



