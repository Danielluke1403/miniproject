def show_balance():
    print (f"your balance is{balance: .2f}")

def deposit():
    amount= float(input("enter your amount you want to deposit"))
    if balance <0:
        print("not a valid amount to be added")
        return 0
    else: 
        return amount
def withdraw():
    amount=float(input('enter the amount to be withdrawn'))
    if amount >balance:
        print("not possible")
    elif amount<0:
        print("amount must be a greater amount")
        return 0
    else:
        return amount
def main
balance=0
is_running = True

while is_running:
    print("banking program")
    print("1. Show Balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. Exit")
    

    choice =input("enter your choice(1_4): ")
    if choice =="1":
        show_balance()
    elif choice =='2':
        balance +=deposit()
    elif choice=='3':
        balance -= withdraw()
    elif choice =='4':
        is_running=False
    else:
        print("its not a valid thing")




print("have a nice day !!")

