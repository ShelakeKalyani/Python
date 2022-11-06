'''Program Name = Write a Python Program to Find the Sum of Natural Numbers in an Interval.
   Developer Name = Shelake Kalyani
   Language = Python
   Date = 20-08-2022'''

start = int(input("Enter starting of interval = "))
end = int(input("Enter ending of interval = "))

sum = 0
for i in range(start,end):
    sum = sum + i

print("Sum of natural numbers betweeen {} and {} = {}".format(start,end,sum))

'''
OUTPUT:
Enter starting of interval = 1
Enter ending of interval = 10
Sum of natural numbers betweeen 1 and 10 = 45
'''
