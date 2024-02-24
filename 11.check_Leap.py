'''Program Name = Write a Python Program to Check Leap Year.
   Developer Name = Shelake Kalyani
   Language = Python
   Date = 19-08-2022'''


year = int(input("Enter any year = "))

if((year%100==0 and year%400==0) or (year%100!=0 and year%4==0)):
    print(f"{year} is leap year.")
else:
    print(f"{year} is not leap year.")

'''
OUTPUT:
Enter any year = 2022
2022 is not leap year.
'''
