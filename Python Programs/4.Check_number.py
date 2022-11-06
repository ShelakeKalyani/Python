''' Program Name = Write a Python Program to Check if a Number is Positive, Negative or Zero.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 19-08-2022 '''


number = int(input("Enter a number = "))

if(number >0):
    print(f"{number} is positive number.")
elif (number<0):
    print(f"{number} is negative number.")
else:
    print(f"{number} is equal to zero.")


'''
OUTPUT 1:
Enter a number = 76
76 is positive number.

OUTPUT 2:
Enter a number = -87
-87 is negative number.

OUTPUT 3:
Enter a number = 0
0 is equal to zero.
'''
