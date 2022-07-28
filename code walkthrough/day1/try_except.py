# way for ur program to handle user input mistakes 

try: 
    number = int(input("Enter a number: " ))
    print(number)

# except ___ will catch certain types of input errors to specify when program "breaks"
except ZeroDivisionError: 
    print("Divided by zero")
except ValueError: 
    print("Invalid input")