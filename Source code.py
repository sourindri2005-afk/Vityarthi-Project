# Humanized Clothes Store Inventory System

import datetime

# --- 1. THE INVENTORY DATA ---
# FIX: Standardized the key 'name' to be all lowercase for consistency
Inventory = {
    101: {"name": "Women's Jeans", "price": 600, "stock": 75},
    102: {"name": "Men's Jeans", "price": 700, "stock": 50},
    103: {"name": "Women's Top", "price": 200, "stock": 65}
}

last_checked = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- 2. THE MAIN PROGRAM LOOP ---
end = False

print("\n👋 Welcome to the Retail Manager Assistant!")
print(f"Inventory was last checked on: {last_checked}")

while end == False:
    # Display the menu of available operations
    print("\n" + "🌟" * 4 + " What would you like to do? " + "🌟" * 4)
    print("1. Add a **NEW** item to the shelf.")
    print("2. Check an item's **AVAILABILITY**.")
    print("3. Check an item's **PRICE**.")
    print("4. **UPDATE** the stock level.")
    print("5. **REMOVE** an item completely.")
    print("6. **VIEW** all items and details.")
    print("7. **CLEAR** the entire inventory (DANGER!).")
    print("0. **EXIT** the system.")
    print("=" * 35)

    try:
        # Get user input and handle non-numeric input gracefully
        choice = int(input(">> Please enter your choice (0-7): "))
    except ValueError:
        print("🚨 Oops! That wasn't a number. Please try again with a single digit (0-7).\n")
        continue 
    
    print("\n")

    # --- 3. EXECUTION BLOCKS ---
    if choice == 0:
        # EXIT
        end = True
        print("👋 Thank you for managing the inventory! See you next time.")

    elif choice == 1:
        # ADD NEW ITEM
        try:
            clothes_id = int(input("Enter new Item ID (e.g., 104): "))
            if clothes_id in Inventory:
                print(f"⚠️ Error: Item ID {clothes_id} already exists! Use Option 4 to update stock.")
                continue
            name = input("Enter Item Name (e.g., Summer Dress): ")
            price = float(input("Enter Item Price ($): "))
            stock = int(input("Enter Starting Stock Quantity: "))
            
            Inventory[clothes_id] = {"name": name, "price": price, "stock": stock}
            print(f"\n✅ Success! **{name}** (ID: {clothes_id}) has been added to the inventory.")
        except ValueError:
            print("🚨 Invalid input for ID, Price, or Stock. Please use numbers.")

    elif choice == 2:
        # CHECK AVAILABILITY
        try:
            clothes_id = int(input("Enter Item ID to check stock for: "))
            if clothes_id in Inventory:
                item = Inventory[clothes_id]
                stock_level = item['stock']
                if stock_level > 10:
                    status = f"Plenty in stock! ({stock_level} units)"
                elif stock_level > 0:
                    status = f"Running low! Only {stock_level} units left."
                else:
                    status = "SOLD OUT!"
                
                print(f"🔎 Status for **{item['name']}** (ID {clothes_id}): {status}")
            else:
                print("❌ Item not found. Please double-check the ID.")
        except ValueError:
            print("🚨 Invalid input. Please enter a numerical ID.")

    elif choice == 3:
        # RETRIEVE PRICE
        try:
            clothes_id = int(input("Enter Item ID to check the price: "))
            if clothes_id in Inventory:
                item = Inventory[clothes_id]
                print(f"💰 The price for **{item['name']}** is **${item['price']:.2f}**.")
            else:
                print("❌ Item ID not found.")
        except ValueError:
            print("🚨 Invalid input. Please enter a numerical ID.")

    elif choice == 4:
        # UPDATE STOCK
        try:
            clothes_id = int(input("Enter Item ID to adjust stock: "))
            if clothes_id in Inventory:
                print("1. Received new delivery (Increase Stock).")
                print("2. Sold items (Decrease Stock).")
                opt = int(input("Enter choice (1 or 2): "))
                qty = int(input("Enter Quantity to change: "))
                
                item_name = Inventory[clothes_id]['name']
                
                if opt == 1:
                    Inventory[clothes_id]["stock"] += qty
                    print(f"✅ Stock for **{item_name}** increased by {qty}. **New Stock: {Inventory[clothes_id]['stock']}**.")
                elif opt == 2:
                    current_stock = Inventory[clothes_id]["stock"]
                    if current_stock >= qty:
                        Inventory[clothes_id]["stock"] -= qty
                        print(f"✅ Stock for **{item_name}** decreased by {qty}. **New Stock: {Inventory[clothes_id]['stock']}**.")
                    else:
                        print(f"❌ Error: Cannot sell {qty} units. Only {current_stock} available.")
                else:
                    print("Invalid stock operation choice.")
            else:
                print("❌ Item not found.")
        except ValueError:
            print("🚨 Invalid input. Please use numbers for ID, choice, and quantity.")

    elif choice == 5:
        # REMOVE ITEM
        try:
            clothes_id = int(input("Enter Item ID to permanently REMOVE: "))
            if Inventory.pop(clothes_id, None):
                print(f"🗑️ Item ID **{clothes_id}** was successfully removed from the inventory
