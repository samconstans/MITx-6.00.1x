# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:49:05 2017

@author: Анастасия
"""

balance = 320000
annualInterestRate = 0.2

min_month_payment = 0
monthly_unpaid_balance = 0
monthly_interest_rate =  annualInterestRate / 12.0
low_bal = balance / 12.0
high_bal = (balance * (1 + monthly_interest_rate) ** 12 ) / 12.0
min_month_payment = (low_bal + high_bal) / 2.0
while(True):
    rem_balance = balance
    for i in range(0,12):
        monthly_unpaid_balance = rem_balance - min_month_payment
        rem_balance =  monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance) 
    if(rem_balance <= 0 and rem_balance >= -0.01):
        break
    else:
        if(rem_balance > 0):
            low_bal = min_month_payment
        else:
            high_bal = min_month_payment
    min_month_payment = (low_bal + high_bal) / 2.0           
print('Lowest Payment: '+str(round(min_month_payment,2)))