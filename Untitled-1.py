

def facto(n):
    if n == 0 or n == 1:#base case : 0! and 1! are both 1
        return 1
    else: 
        return n * facto(n - 1) #recurseive call:3
#input from user
num = int(input("enter a number: "))
#check if the  number is negative
if num < 0:
    print("facto doesnot exist for neg numbers.")
else:
    print(f"the facto of {num} is {facto(num)}")

#fahhhhhhhhh