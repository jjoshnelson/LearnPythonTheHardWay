from fractions import gcd
from random import randint

# Defines the function 'cheese_and_crackers'
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count                 # The '%d' makes the variable an integer (digit)
    print "You have %d boxes of crackers!" % boxes_of_crackers
    cheese_to_cracker_ratio(cheese_count, boxes_of_crackers)
    print "Man that's enough for a party"
    print "Get a blanket.\n"        # The '\n' creates a line break

# Finds the gcd of 'amount_of_cheese' & 'amount_of_crackers' and then mulitplies each variable by that to find a simplified fraction
def cheese_to_cracker_ratio(cheese_count, boxes_of_crackers):
    greatestcd = gcd(cheese_count, boxes_of_crackers)
    print "Your cheese to cracker ratio is %d / %d." % (cheese_count/greatestcd, boxes_of_crackers/greatestcd)

amount_of_cheese = int(raw_input("How many cheeses do you have?: "))
amount_of_crackers = int(raw_input("How many crackers do you have?: "))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)         # Directly enters values for 'cheese_count' & 'boxes_of_crackers'


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
#cheese_to_cracker_ratio(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)
#cheese_to_cracker_ratio(10+20, 5+6)

print "And we can combine the two, Variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print "We can have a random number of cheese and crackers"
cheese_and_crackers(randint(1, 100), randint(1, 100))

#cheese_to_cracker_ratio(amount_of_cheese + 100, amount_of_crackers + 1000) 
