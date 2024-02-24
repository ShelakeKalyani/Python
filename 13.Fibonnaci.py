'''Program Name = Write a Python Program to Print the Fibonacci sequence.
   Developer Name = Shelake Kalyani
   Language = Python
   Date = 20-08-2022'''

num = int(input("Enter terms value = "))
a = 0
b = 1
count = 0

while(count < num):
    print(a)
    c = a +  b
    a = b
    b = c
    count +=1

'''
OUTPUT :
Enter terms value = 7
0
1
1
2
3
5
8
'''


