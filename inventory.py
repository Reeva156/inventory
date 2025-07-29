def inventory_list_analyzer():
    inventory = []

    print("Welcome to Inventory List Analyzer!")

    while True:
        name = input("Enter item name: ")
        category = input("Enter category: ")
        quantity = int(input("Enter quantity: "))

        inventory.append({
            'name': name,
            'category': category,
            'quantity': quantity
        })

        more = input("Do you want to add more items? (y/n): ")
        if more != 'y':
            break

    print("\n----------------------INVENTORY SUMMARY------------------")

  
    total_items = len(inventory)
    item_names = [item['name'] for item in inventory]
    print(f"Total Different Items: {total_items}")
    print(f"Explanation: You entered {total_items} different items: {', '.join(item_names)}.")


    quantity = sum(item['quantity'] for item in inventory)
    print(f"\nTotal Quantity in Stock: {quantity}")
    quantities = ' + '.join(str(item['quantity']) for item in inventory)
    print(f"Explanation: Sum of all quantities: {quantities} = {total_quantity}")


    average_quantity = quantity / total_items
    print(f"\nAverage Quantity per Item: {average_quantity:.2f}")
    print(f"Explanation: Average = {quantity} total / {total_items} items")

   
    most = max(inventory, key=lambda x: x['quantity'])
    least = min(inventory, key=lambda x: x['quantity'])
    print(f"\nMost Stocked Item: {most['name']} ({most['quantity']} units)")
    print(f"Explanation: {most['name']} has the highest quantity among all items.")

    print(f"\nLeast Stocked Item: {least['name']} ({least['quantity']} units)")
    print(f"Explanation: {least['name']} has the lowest quantity.")


    unique = sorted(set(item['category'] for item in inventory))
    print("\n-------------------------------------------")
    print(" Items Sorted by Quantity (High to Low):")
    sorted = sorted(inventory, key=lambda x: x['quantity'], reverse=True)
    for i, item in enumerate(sorted, start=1):
        print(f"{i}. {item['name']} - {item['quantity']} units")
    print("Explanation: Items are sorted using the quantity field from highest to lowest.")

    print("\n Categories in Alphabetical Order:")
    for i, cat in enumerate(unique, start=1):
        print(f"{i}. {cat}")
    print("Explanation: The set of unique categories was sorted alphabetically for display.")

    print("\n=========== END OF REPORT ===========")


inventory_list_analyzer()