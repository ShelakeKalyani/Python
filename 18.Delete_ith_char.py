''' Program Name = Write a Python Program to remove i'th character from string in different ways.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 05-09-2022 '''

str1 = input("Enter any string = ")

L = str1.split()
print(L)

j = int(input("Enter which index you want to delete = ")) 

for i in range(0,len(str1)):
    if(i==j):
        str1.replace(str('i')," ")
        
print(str1)
    
