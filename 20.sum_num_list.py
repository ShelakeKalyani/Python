''' Program Name = Write a Python function to sum all the numbers in list.
    Developer Name = Shelake Kalyani
    Language = Python
    Date = 05-09-2022 '''

L = [10,2,20,5,40,5]
print(L)

def sum_list(L):
    res = 0
    for i in L:
        res = res+i
    return res

print(f"Sum of all elements in list = {sum_list(L)}")

'''
OUTPUT :
[10, 2, 20, 5, 40, 5]
Sum of all elements in list = 82
'''
