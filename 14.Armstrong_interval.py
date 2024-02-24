'''Program Name = Write a Python Program to Find Armstrong Number in an Interval.
   Developer Name = Shelake Kalyani
   Language = Python
   Date = 20-08-2022'''

start = int(input("Enter starting of interval = "))
end = int(input("Enter ending of interval = "))
L = []

for i in range(start,end):
    cnt = 0
    num = i
    temp = i
    ans = 0
    while(i>0):
        cnt = cnt+1
        i = int(i/10)
    while num>0:
        digit = num%10
        ans = ans + (digit**cnt)
        num = int(num/10)
    if(ans==temp):
        print(temp)

'''
OUTPUT :
Enter starting of interval = 100
Enter ending of interval = 1000
153
370
371
407
'''
