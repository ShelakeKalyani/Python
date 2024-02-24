''' Program Name = Python Program to Generate a Random Number.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 19-08-2022 '''


import random   #To generate random number we want to import random package

start = int(input("Enter Start Range = "))
end = int(input("Enter End Range = "))

if(start>end):
    print("Start range should be less than End range.")
    exit()

rand = random.randint(start,end)      #This function will generate a random number

print(f"Generated Random Number is {rand}")

'''
OUTPUT:
Enter Start Range = 1
Enter End Range = 20
Generated Random Number is 4
'''
