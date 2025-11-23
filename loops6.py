num=int(input("enter number: "))
fact=1
while num>0:
    fact*=num
    num=num-1
print(f"Factorial is: {fact}")