string=input("enter string: ")
reverse_string=""
for char in string:
    reverse_string= char + reverse_string
print(f"Original String: {string}")
print(f"Reversed String: {reverse_string}")