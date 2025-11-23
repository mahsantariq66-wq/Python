password=input("enter password: ")
if len(password)<6:
    print("WEAK!")
elif len(password)>6 and len(password)<=10:
    print("MEDIUM")
elif len(password)>10:
    print("STRONG!")

       
