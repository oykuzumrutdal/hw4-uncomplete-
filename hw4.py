import pandas as pd
import numpy as np
import os

df = os.getcwd() + "/Plaza_Coffee.csv"
df = pd.read_csv(df, sep=';')

companyNames = ["KPMG", "EY", "Deloite & Touche", "PWC"]
companyTuple = tuple(df['Company'])
paymenttuple = tuple(df['Payment'])
ordertuple = tuple(df['Order'])
quantitytuple = tuple(df['Quantity'])


for X_Company in companyNames:
    dessertcash = 0
    dessertcredit = 0
    dailycash = 0
    dailycredit = 0
    coffeecash = 0
    coffeecredit = 0
        if(company == X_Company):
            if(order == 'Dessert' and payment == "Cash"):
                dessertcash += quantity
            if(order == 'Dessert' and payment == "Credit"):
                dessertcredit += quantity
            if(order == 'Daily Menu' and payment == "Cash"):
                dailycash += quantity
            if(order == 'Daily Menu' and payment == "Credit"):
                dailycredit += quantity
            if(order == 'Coffee' and payment == "Cash"):
                coffeecash += quantity
            if(order == 'Coffee' and payment == "Credit"):
                coffeecredit += quantity
   
   
