''' Program Name = Write a Python Program to Check Prime Number.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 19-08-2022 '''



# Prime number = The number which is divisible by only 1 and itself having no other factors.


number = int(input("Enter any number = "))      # Accept number from user

if(number==1):
    print("1 is neither prime not composit number")
    exit()
    
flag = False

for i in range(2,number):                       # Travel loop from 2 to number-1
    if(number%i==0):                            # Check condition for prime number
        flag = True                             
        break                                   # If we are in loop then it means it have some factors that is entered number is not prime number


if flag==True:
    print(f"{number} is not prime number")
else:
    print(f"{number} is prime number")


'''
OUTPUT :
Enter any number = 3
3 is prime number
'''
