def max_num(num1, num2, num3):
    if (num1 >= num2) and (num1 >= num3):
        return num1
    elif (num2 >= num1) and (num2 >= num3):
        return num2 
    else:
        return num3

usernum1 = float(input("Enter first number: "))

usernum2 = float(input("Enter 2nd number: "))

usernum3 = float(input("Enter last number: ") )

print(max_num(usernum1, usernum2, usernum3))


