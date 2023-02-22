"""Chef's Kiss

    You are making a digital menu to order food.
    The menu is stored as a list of items.

    Your program needs to take the index of the item as input and output the item name.
    In case the index is not valid, you should output "Item not found".
    In case the index is valid and the item name is output successfully, you should output "Thanks for your order".

    Sample Input
    2

    Sample Output
    Cheeseburger
    Thanks for your order
"""

menu = ['Fries', 'Sandwich', 'Cheeseburger', 'Coffee', 'Soda']

food = int(input("Input a menu item: "))

try:
    if food not in range(len(menu)):
        raise Exception("Item not found")

except Exception as e:
    print(e)

else:
    print(menu[food])
    print("Thanks for your order")
