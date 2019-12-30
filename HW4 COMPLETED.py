import pandas as pd
import numpy as np
#I uploaded the data
data = pd.read_csv("Plaza Coffee.csv", sep=";")
#With i.loc, I selected the first columns of the dataframe (df)
Company_column_data = data.iloc[:,0]
Order_column_data = data.iloc[:,0]
Quantity_column_data = data.iloc[:,0]
Payment_column_data = data.iloc[:,0]
#
KPMG_data = data[data.Company == "KPMG"]
EY_data = data[data.Company == "EY"]
Deloitte_data = data[data.Company == "Deloite & Touche"]
PWC_data = data[data.Company == "PWC"]
#I began with Deloitte and Touche(Cash & Credit)
Deloitte_cash_data = Deloitte_data[(Deloitte_data.Payment == "Cash")]
Deloitte_cash_buyer_number = 0 
for i in Deloitte_cash_data.Quantity:
    Deloitte_cash_buyer_number += i
    Deloitte_credit_data = Deloitte_data[(Deloitte_data.Payment == "Credit")]
    Deloitte_credit_buyer_number = 0 
    for i in Deloitte_credit_data.Quantity:
        Deloitte_credit_buyer_number += i
#I continued with KPMG (Cash & Credit)
KPMG_cash_data = KPMG_data[(KPMG_data.Payment == "Cash")]
KPMG_cash_buyer_number = 0
for i in KPMG_cash_data.Quantity:
    KPMG_cash_buyer_number += i
    KPMG_credit_data = KPMG_data[(KPMG_data.Payment == "Credit")]
    KPMG_credit_buyer_number = 0 
    for i in KPMG_credit_data.Quantity:
        KPMG_credit_buyer_number += i
#I continued with PWC (Cash&Credit)
    PWC_cash_data = PWC_data[(PWC_data.Payment == "Cash")]
PWC_cash_buyer_number = 0
for i in PWC_cash_data.Quantity:
    PWC_cash_buyer_number += i
    PWC_credit_data = PWC_data[(PWC_data.Payment == "Credit")]
    PWC_credit_buyer_number = 0 
    for i in PWC_credit_data.Quantity:
        PWC_credit_buyer_number += i
    
#I finished sorting with company Ernst&Young (Cash&Credit)
EY_cash_data = EY_data[(EY_data.Payment == "Cash")]
EY_cash_buyer_number = 0 
for i in EY_cash_data.Quantity:
    EY_cash_buyer_number += i
    EY_credit_data = EY_data[(EY_data.Payment == "Credit")]
    EY_credit_buyer_number = 0 
    for i in EY_credit_data.Quantity:
        EY_credit_buyer_number += i
#With these all steps, I managed to sort and analyse data due to its Cash or Credit checks.
#In the final step, I printed the early arranged sentences can change with my the sortings such as company names, the order quantity, the payment styles.
    #I printed sentences in string.
print("From KPMG "+str(KPMG_cash_buyer_number)+" people have bought stuff on discount and paid in cash, also assistants got "+str(KPMG_credit_buyer_number)+" serving of coffee on credit.")
print("From PWC "+str(PWC_cash_buyer_number)+" people have bought stuff on discount and paid in cash, also assistants got "+str(PWC_credit_buyer_number)+" serving of coffee on credit.")
print("From EY "+str(EY_cash_buyer_number)+" people have bought stuff on discount and paid in cash, also assistants got "+str(EY_credit_buyer_number)+" serving of coffee on credit.")
print("From Deloite & Touche "+str(Deloitte_cash_buyer_number)+" people have bought stuff on discount and paid in cash, also assistants got "+str(Deloitte_credit_buyer_number)+" serving of coffee on credit.")

#ÖYKÜ ZÜMRÜTDAL -2149607
