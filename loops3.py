table_number=int(input("enter table number: "))
for i in range(1,10+1,1):
    if i==5:
        continue
    else:
        print(f"{table_number}X{i}={table_number*i}")