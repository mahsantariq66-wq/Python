fruits=["apple","banana","orange","apple","grapes"]
unique_item=set()
for i in fruits:
    if i in unique_item:
        print("duplicate found")
        break
    unique_item.add(i)
