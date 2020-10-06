#Created by: Evan
#Created on: Oct. 2020

#This program calculates the cost of making a pizza



diameter = float(input("Enter the diameter of the pizza you would like (inch): "))
LABOUR_COST = 0.75
RENT = 1
HST_ONTARIO_TAX = 1.13
materials=  0.5 * diameter

cost_of_pizza_1 = (materials + RENT + LABOUR_COST) * 1.13
cost_of_pizza_2 = round(cost_of_pizza_1, 2)

print("Your", diameter,"inch pizza costs $",cost_of_pizza_2) 