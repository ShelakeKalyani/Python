''' Program Name = Python Program to check string is symmetric/palindrome or not.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 05-09-2022 '''

str1 = input("Enter  any string = ")

rev = str1[::-1]

print(rev)

if(rev==str1):
    print("'{}' is palindrome string.".format(str1))
else:
    print("'{}' is not palindrome string.".format(str1))

'''
OUTPUT 1:
Enter  any string = baba
abab
'baba' is not palindrome string.

OUTPUT 2:
Enter  any string = ababa
ababa
'ababa' is palindrome string.
'''

