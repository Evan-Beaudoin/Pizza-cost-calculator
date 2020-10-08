#Created by: Evan
#Created on: Oct. 2020

#This program calculates the cost of making a pizza



diameter = float(input("Enter the diameter of the pizza you would like (inch): "))
LABOUR_COST = 0.75
RENT_COST = 1
HST = 1.13
MATERIALS =  0.5

subtotal_pizza_cost = (RENT_COST + LABOUR_COST+(MATERIALS * diameter)) * 1.13

total_pizza_cost = round(subtotal_pizza_cost, 2)

print("Your", diameter,"inch pizza costs $",total_pizza_cost) 