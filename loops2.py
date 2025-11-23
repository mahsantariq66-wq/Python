#SUM OF EVEN NUMBERS
n=int(input("Enter Range: "))
sum=0
for i in range(1,n+1,1):
    if i%2==0:
        print("even numbers are:",i)
        sum+=i

print(f"sum is : {sum}")

