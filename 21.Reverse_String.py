''' Program Name = Write a Python program to reverse a string.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 10-09-2022 '''

str = input("Enter any string = ")

def Reverse(str):
    rev = ""
    l = len(str)
    for i in range(l-1,-1,-1):
        rev = rev+str[i]
    return rev

rev_str = Reverse(str)
print(f"Reverse String = {rev_str}")


'''
OUTPUT :
Enter any string = kalyani
Reverse String = inaylak
'''
    
    
