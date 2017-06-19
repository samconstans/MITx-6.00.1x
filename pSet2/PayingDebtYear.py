# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 16:44:50 2017

@author: Анастасия
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

total_paid = 0.00
i=1
while(i <= 12):
    monthly_interest_rate = (annualInterestRate) / 12.0
    minimum_monthly_payment = (monthlyPaymentRate) * (balance)
    monthly_unpaid_balance = (balance) - (minimum_monthly_payment)
    balance = (monthly_unpaid_balance) + (monthly_interest_rate * monthly_unpaid_balance)
    
    total_paid += minimum_monthly_payment
    i+=1

print('Remaining balance: '+str(round(balance,2)))