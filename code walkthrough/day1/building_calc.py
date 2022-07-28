#int() or float() --> converts to integer data type

def calc(n1, operator, n2):
    if (operator == "+"): 
        return n1 + n2 
    elif(operator == "-"): 
        return n1 - n2
    elif(operator == "*"):
        return n1 * n2 
    elif(operator == "/"): 
        return n1/n2 
    else: 
        return(print("Invalid input. Try again!"))


num1 = float(input("Enter first number: "))
op = input("Enter operation: ")
num2 = float(input("Enter second number: ")) 

print(calc(num1, op, num2))

