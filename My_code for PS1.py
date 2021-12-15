# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 15:49:59 2021

@author: Abdullah Azhar
"""

#calculate when will you be able to save money for the downpayment in months 

total_cost = float(input("What is the cost of your dream home? :"))
portion_down_payment = (0.25)*total_cost

annual_salary = float(input("Enter your annual salary? :"))
monthly_salary = annual_salary/12


portion_saved = float(input('What is the portion of the monthly salary that you want to save? :'))
# print('monthly salary saved: ',portion_saved*monthly_salary)

monthly_savings = portion_saved*monthly_salary

r = 0.04 #return on investments 

current_savings = 0 #for the first month
months = 0;
    
while (current_savings < portion_down_payment):
    current_savings += (current_savings * r/12) + monthly_savings
    months = months+1

print(months)


# #User Inputs
# annual_salary = float(input('Enter your annual salary:​ ')) #Your salary for the whole year
# portion_saved = float(input('Enter the percent of your salary to save, as a decimal: ​')) #this is the percentage of what you wishes to save monthly
# total_cost = float(input('Enter the cost of your dream home: ​'))    #total cost of the dream home

# #Variables. All amounts in (#)
# current_savings = 0  #the amount that you have saved so far,starting from 0
# portion_down_payment = 0.25 * total_cost
# current_savings = 0  #the amount that you have saved so far,starting from 0
# r = 0.04 #annual rate
# annual_return = (current_savings * r) / 12
# monthly_salary = annual_salary / 12
# portion_saved = portion_saved * monthly_salary 
# time = 0

# #Iterations and Output
# while (current_savings <= portion_down_payment):
#     time += 1
#     current_savings += (current_savings * r / 12) + portion_saved    
# print('Number of months: %d'%time)