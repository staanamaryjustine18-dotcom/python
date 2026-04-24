contact_list = [] 
def display_contact(): 
    print("\nContacts:")
    if not contact_list: 
        print("No contacts yet.")
    else:
        for i, person in enumerate(contact_list, start=1):
            print(f"{i}. {person['name']} - {person['number']}")
            
def add_contact():
    name = input("Enter name: ")
    number = input("Enter number: ")
    contact_list.append({"name": name, "number": number})
    print(f"Added {name} to contacts.")
    
def remove_contact():
    display_contact()
    if not contact_list:
        return

    try:
        choice = int(input("Enter contact number to remove: "))
        # Subtract 1 because lists are 0-indexed
        removed = contact_list.pop(choice - 1)
        print(f"Removed {removed['name']} from contacts.")
    except (ValueError, IndexError):
        print("Invalid choice. Please enter a valid number from the list.")
        
def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. View Contacts")
        print("2. Add Contact")
        print("3. Remove Contact")
        print("4. Quit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            display_contact()
        elif choice == "2":
            add_contact()
        elif choice == "3":
            remove_contact()
        elif choice == "4":
            print("Goodbye!")
            break
        else: 
            print("Invalid choice.")

if __name__ == "__main__":
    main()