''' Program Name = Write a Python Program to Check Armstrong Number.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 19-08-2022 '''


# Armstrong number =
#            Ex.        num = 153
#                       total digits = 3
#                       sum = (1^3)+(5^3)+(3^3) = 153                  where, power 3 = total digits and 1,5,3 are digits in given number
#                       here num = sum,                                 hence 153 is armstrong number


number = int(input("Enter any number = "))      # Accept number from user
temp = number
temp1 = number

ans = 0
cnt = 0
while number>0:
    cnt = cnt+1                                 
    number = int(number/10)

while temp>0:
    digit = temp%10
    ans = ans + (digit**cnt)
    temp = int(temp/10)

if(temp1==ans):
    print(f"{temp1} is armstrong number.")
else:
    print(f"{temp1} is not armstrong number.")


'''
OUTPUT :
Enter any number = 153
153 is armstrong number.
'''
