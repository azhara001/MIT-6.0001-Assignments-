# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:15:50 2021

@author: Abdullah Azhar
"""

#code for MIT OCW Problem Set1 Part C 

## Code for Problem Set-1 Part-A 
# total_cost = float(input("What is the cost of your dream home? :"))
# portion_down_payment = (0.25)*total_cost

# annual_salary = float(input("Enter your annual salary? :"))
# monthly_salary = annual_salary/12


# portion_saved = float(input('What is the portion of the monthly salary that you want to save? :'))
# # print('monthly salary saved: ',portion_saved*monthly_salary)

# monthly_savings = portion_saved*monthly_salary

# r = 0.04 #return on investments 

# current_savings = 0 #for the first month
# months = 0;
    
# while (current_savings < portion_down_payment):
#     current_savings += (current_savings * r/12) + monthly_savings
#     months = months+1

# print(months)

semi_annual_raise = 0.07 # 7 percent increase bi-annually
check_semi_annual_raise = 0 
r = 0.04 # 4% return on investments (per year)
total_cost = 1000000 # House of cost is USD 1 Million
down_payment_percentage = 0.25 # 25% of the total cost of the house 
portion_down_payment = int(total_cost*down_payment_percentage)
months = 36 # target months to achieve the savings = portion_down_payment (mentioned in the problem set)


Epsilon = 100 # abs(savings - portion_down_payment) <= Epsilon 

annual_salary = float(input("Enter your annual salary: "))
monthly_salary = annual_salary/12

portion_saved = 0 #initializing the variable that needs to be found 
steps = 0 #to count the number of steps it takes to reach the bisection search method 

low = int(0) # you save none of your monthly salary
high = int(10000) # you save all your monthly salary 
guess = (high+low)//2
guess_converted = guess/10000
current_savings = 0;

print('Initial value of guess_converted: ',guess_converted)
print('Initial value of monthly salary: ',monthly_salary)
print('downpayment is equal to: ',portion_down_payment)
monthly_savings = guess_converted*monthly_salary #Initializing the monthly savings 
print('Initial Value of monthly savings: ',monthly_savings)

looptest = 0
flag = 0

while flag !=1:
# while steps < 10:    
    for month in range(0,months+1):
        if check_semi_annual_raise == 6:
            monthly_salary += monthly_salary*semi_annual_raise
            check_semi_annual_raise = 0
        
        current_savings = current_savings + (current_savings*(r/12) + monthly_savings)
        check_semi_annual_raise += 1
        current_savings = int(current_savings)
    print('for savings: ',guess_converted, 'the current savings after 36 months are: ',current_savings)
    #print('In loop: ',guess_converted)    
    
    if current_savings < portion_down_payment:
        low = guess_converted*10000 
        #low = guess_converted
    elif current_savings > portion_down_payment:
        high = guess_converted*10000
         
    guess = (high+low)//2
    
    if guess >= 9999: 
        print ("It is not possible to pay the downpayment in 36 months")
        break
    print('value of int guess: ',guess)
    
    guess_converted = guess/10000
    
    if abs(current_savings - portion_down_payment) <= Epsilon:
        break
    
    monthly_salary = annual_salary/12 # Resetting the value of monthly_salary 
    monthly_savings = guess_converted*monthly_salary
    current_savings = 0; #resetting the value of current_savings
    
         
    steps += 1
    # print('guess_converted in loop: ',guess_converted)
    
    
print('loop has ended')
print('percentage you need to save: ', guess_converted)
print('total bisection steps: ',steps)
print(current_savings)
        
        