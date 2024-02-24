''' Program Name = Write a Python Program to Find the Factorial of a Number.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 19-08-2022 '''

num = int(input("Enter any number = "))

sum = 1
for i in range(1,num+1):
    sum = sum*i
    
print("Factorial of {} is = {}".format(num,sum))



'''
OUTPUT :
Enter any number = 4
Factorial of 4 is = 24
'''
