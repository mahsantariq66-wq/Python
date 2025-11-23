#Transportaion Mode Selection
distance=int(input("enter distance: "))
if distance<=3:
    print("WALK")
elif distance>3 and distance<16:
    print("BIKE")
elif distance>16:
    print("CAR")
