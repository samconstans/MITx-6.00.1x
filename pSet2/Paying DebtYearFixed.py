# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:47:36 2017

@author: Анастасия
"""

balance = 3329
annualInterestRate = 0.2

min_month_payment = 0
monthly_unpaid_balance = 0
rem_balance = balance
while(True):
    min_month_payment += 10
    for i in range(0,12):
        monthly_interest_rate =  annualInterestRate / 12.0
        monthly_unpaid_balance = rem_balance - min_month_payment
        rem_balance =  monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance) 
    if(rem_balance <= 0):
        break    
    else:
        rem_balance = balance            
print('Lowest Payment: '+str(min_month_payment))