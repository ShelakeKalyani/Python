'''Program Name = Write a Python Program to Print all Prime Numbers in an Interval.
   Developer Name = Shelake Kalyani
   Language = Python
   Date = 20-08-2022'''


start = int(input("Enter starting of interval = "))
end = int(input("Enter ending of interval = "))
L = []

for i in range(start,end):
    flag = False
    if(i==1):
        print("1 is neither prime nor composite.")
        continue
    for j in range(2,i):
        if(i%j==0):
            flag = True
            break
    if(flag==False):
        L.append(i)

print(f"Prime numbers between {start} and {end} = {L}")

'''
OUTPUT :
Enter starting of interval = 10
Enter ending of interval = 20
Prime numbers between 10 and 20 = [11, 13, 17, 19]
'''
