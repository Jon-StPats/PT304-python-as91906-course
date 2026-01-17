"""03 — Menu-based programs

Goal: Build the core pattern used in BOTH AS91906 project options.
"""

def show_menu() -> None:
    print("\n=== MENU ===")
    print("1. Add item")
    print("2. View items")
    print("3. Exit")

items = []

while True:
    show_menu()
    choice = input("Choose: ").strip()

    if choice == "1":
        # TODO: add an item
        pass
    elif choice == "2":
        # TODO: view items
        pass
    elif choice == "3":
        break
    else:
        print("Invalid option")

# EXTENSION:
# Add an option 4 that removes an item.
