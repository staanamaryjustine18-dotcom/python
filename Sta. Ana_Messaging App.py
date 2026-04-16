def create_file():
    try: 
        # 'x' mode fails if file exists, effectively doing nothing
        with open('file.txt', 'x') as f:
            f.write('This is a new file.\n')    
        print("Message file created!")
    except FileExistsError:
        print("Message file already exists, skipping creation.")
        
def send_msg():
    msg = input("Enter your message: ")
    if msg.strip():
        try:
            with open("message.txt", "a") as f:
                f.write(msg + "\n")
            print("Message sent!")
        except Exception as e:
            print("Error: {e}")
    else: 
        print("Error: Cannot send empty message.")
        
def view_msg():
    try:
        with open("message.txt", "r") as f:
            messages = f.read()
            if messages.strip():
                print("\n---Messages---")
                print(messages)
            else:
                print("No messages found.")
    except FileNotFoundError:
        print("No message file found. Please send a message first.")
        
# --- Main Program Flow ---
print("Welcome to the Simple Messaging App")
create_file()

while True:
    print("\n1. Send message\n2. View messages\n3. Exit")
    choice = input("Choose an option: ")
    
    if choice == '1':
        send_msg()
    elif choice == '2':
        view_msg()
    elif choice == '3':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1, 2, or 3")