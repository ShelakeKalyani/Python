'''
    Program Name = Write a python program to reverse words in a given string.
    Progamming Language = Python
    Name = Shelake Kalyani Rajendra
    Date = 05-09-2021
'''

str1 = input("Enter any string = ")

str2 = str1.split()

new1 = ''
new3 = ''

#print(str2)

for i in str2:
    str3 = str(i[::-1])
    new1 = new1+" " +str3

print(new1)

'''
OUTPUT:
Enter any string = HELLO EVERYONE GOOD MORNING
 OLLEH ENOYREVE DOOG GNINROM
'''
