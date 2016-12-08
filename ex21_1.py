def add(a, b):
    print "Adding: %d + %d\n" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting: %d - %d\n" % (a, b)
    return a - b

def multiply(a, b): 
    print "Mulitlying: %d * %d\n" % (a, b)
    return a * b

def divide(a, b): 
    print "Dividing: %d / %d\n" % (a, b)
    return a / b

problem = raw_input("Enter in a math problem: ").split()

#print (float(problem[0]) - 2)

if problem[1] == "+" :
    answer = add(float(problem[0]), float(problem[2]))
    print (answer)
elif problem[1] == "-":
    answer = subtract(float(problem[0]), float(problem[2]))
    print (answer)
elif problem[1] == "*":
    answer = multiply(float(problem[0]), float(problem[2]))
    print (answer)
elif problem[1] == "/":
    answer = divide(float(problem[0]), float(problem[2]))
    print (answer)
else:
    print "Error: Invaled Input!!"

       