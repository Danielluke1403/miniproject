#code for cafe system
#welcome message
#new text

print("hello welcome to the resteraunt")
#displaying menu
menu={
    'pizza':60,
    'pasta':30,
    'burger':60,
    'salad':70,
    'coffee':80
}
print( "pizza:60\npasta:30\nburger:60\nsalad:70\ncoffee:80")
order_total=0
item1=input("enter item for order: ")
if item1 in menu:
    order_total+= menu[item1]
    print(f"your {item1} has been added to your order")
else:
    print("its not available")
another_order=input("do you want to add another item")
if another_order=="yes" :
    item2=input("enter item: ")
    if item2 in menu:
        order_total+=menu[item2]
        print (f"{item2} has been added")
    else:
        print("not available")
print (f"the total amount to pay is {order_total}")

