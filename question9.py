#LEAP YEAR CHECK

year=int(input("enter year to check it is LEAP or not: "))
if year%4==0 and year%100!=100 or year%400==0:
    print(f"Leap Year: {year}")
else:
    print(f"Not A Leat Year: {year}")