''' Program Name = Write a Python function to find the Max of three numbers.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 05-09-2022 '''

def Max_num(num1,num2,num3):
    if(num1>num2 and num1>num3):
        print(f"{num1} is greater number.")
    elif(num2>num1 and num2>num3):
        print(f"{num2} is greater number.")
    else:
        print(f"{num3} is greater number.")


num1 = int(input("Enter first numbers = "))
num2 = int(input("Enter second numbers = "))
num3 = int(input("Enter third numbers = "))

Max_num(num1,num2,num3)


'''
OUTPUT :
Enter first numbers = 23
Enter second numbers = 89
Enter third numbers = 33
89 is greater number.
'''
