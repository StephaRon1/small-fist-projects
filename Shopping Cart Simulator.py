# Greetings + method
# explanations: 
# - being able to add items 
# - type "done" to checkout

# while not "done":
# - Item name(str)
# - Item price(int)
# - Item + price list: Apple: $2
# Add price to a total cost
# When typed "done":
# - Print all cart items, one per line
# - Total cost

user = str(input("Name: "))
print("\nHello, " + user)
print('''This is your shopping cart.\nYou can add items and its prices.\nType "Done" after you're done''')

item_price_list = []
total_cost = []

while True:    
    item = input("Item name: ")
    if item.lower() == "done":
        for items in item_price_list:
            print("-", items)

        t_c = sum(total_cost)
        print("Total price: $", t_c)

        exit()

    price = int(input("price: "))
    print(f"\n{item}: ${price}\n")

    item_price_list.append(f"{item}: ${price}")
    total_cost.append(price)
