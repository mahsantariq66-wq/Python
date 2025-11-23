string=input("enter string: ")
for char in string:
    print(char)
    if string.count(char)==1:
        print(f"Not Repeating:{char}")
        break
