#movie Ticket Price
age=int(input("enter your age: "))
day=(input("enter day: "))
if age>=18:
    ticket_price=12
    if day=="wednesday" or day=="WEDNESDAY":
        Discount=2
        final_price=ticket_price-Discount
        print(f"Ticket Price : {final_price}$")
    else:
        print(f"Ticket Price: {ticket_price}$")
elif age<18:
    ticket_price=8
    if day=="wednesday" or day=="WEDNESDAY":
        Discount=2
        final_price=ticket_price-Discount
        print(f"Ticket Price : {final_price}$")
    else:
        print(f"Ticket Price: {ticket_price}$")
    
    