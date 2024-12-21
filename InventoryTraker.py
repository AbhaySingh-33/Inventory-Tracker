import json

class InventoryTracker:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] += quantity
        else:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} of {item_name} at ${price} each.")

    def remove_item(self, item_name, quantity):
        if item_name in self.inventory:
            if self.inventory[item_name]['quantity'] >= quantity:
                self.inventory[item_name]['quantity'] -= quantity
                print(f"Removed {quantity} of {item_name}.")
                if self.inventory[item_name]['quantity'] == 0:
                    del self.inventory[item_name]
            else:
                print(f"Error: Only {self.inventory[item_name]['quantity']} of {item_name} available.")
        else:
            print(f"Error: {item_name} not found in inventory.")

    def view_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
        else:
            print("Current Inventory:")
            for item_name, details in self.inventory.items():
                print(f"- {item_name}: {details['quantity']} units at ${details['price']} each")

    def save_inventory(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.inventory, file)
        print(f"Inventory saved to {filename}.")

    def load_inventory(self, filename):
        try:
            with open(filename, 'r') as file:
                self.inventory = json.load(file)
            print(f"Inventory loaded from {filename}.")
        except FileNotFoundError:
            print(f"Error: {filename} not found.")

# Example usage
if __name__ == "__main__":
    tracker = InventoryTracker()

    while True:
        print("\nOptions:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Save Inventory")
        print("5. Load Inventory")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            tracker.add_item(name, quantity, price)
        elif choice == "2":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            tracker.remove_item(name, quantity)
        elif choice == "3":
            tracker.view_inventory()
        elif choice == "4":
            filename = input("Enter filename to save inventory: ")
            tracker.save_inventory(filename)
        elif choice == "5":
            filename = input("Enter filename to load inventory: ")
            tracker.load_inventory(filename)
        elif choice == "6":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
