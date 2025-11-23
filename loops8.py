num=int(input("enter number: "))
is_Prime=True
if num>1:
    for i in range(2,num):
        if num%i==0:
            is_Prime=False
            break
print(f"Number is Prime: {is_Prime}")



