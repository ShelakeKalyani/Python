''' Program Name = Write a python program to print even length words in a string
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 10-09-2022 '''

str = input("Enter any string = ")
l = str.split()

print("Even length words in string are = ")
for i in l:
    length = len(i)
    if(length%2==0):
        print(i)


'''
OUTPUT:
Enter any string = Hello welcome in my home
Even length words in string are = 
in
my
home'''
