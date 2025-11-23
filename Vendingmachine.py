# 1. Vending Machine Program
# Build a program that:
# Displays a list of snacks and drinks with item numbers and prices.
# Asks the user to choose items by number in a loop.
# Keeps track of selected items and their prices.
# Ends when the user types “done”.
# Finally prints a receipt showing:
# List of selected items with prices
# Total cost
# Skills practiced: loops, input(), conditionals, lists/dictionaries, sum(), print formatting



print("Welcome to Vending Machine! ")
menu = {
    1: {"name": "cookie", "price": 1.75},
    2: {"name": "energydrink", "price": 2.00},
    3: {"name": "candy", "price": 1.00},
    4: {"name": "water", "price": 2.00},
}
cart = []
# Display menu
print("\n====Menu=====")
for item_num, details in menu.items():
    print(f"{item_num}. {details['name']} - ${details['price']:.2f}")
print("========================\n")
while True:
    choice=input("Enter item number or done").lower()
    if choice == "done":
        break
    if choice.isdigit():
        item_num=int(choice)
        if item_num in menu: 
            cart.append(menu[item_num])
            # print(f" added{menu[item_num]['name'] - menu[item_num]['price']}to cart")
            print(f"added{menu[item_num]['name']} - ${menu[item_num]['price']:.2f} to cart")
        else: 
            print("invalid item number. please try again")
    else:
        print("invalid item number")
  
print("\n====RECEIPT=====")
total_sum = 0
if cart:
    for item in cart:
        print(f"{item['name']:15} ${item['price']:.2f}")
        total_sum += item['price']

    print("---------------------")
    print(f"{'TOTAL':15} ${total_sum:.2f}")
else:
    print("No item selected")
print("\n Thank you! ")