import re

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def is_valid_phone(phone):
    pattern = re.compile(r"^(?:\+?380|0)\d{9}$")
    return pattern.match(phone) is not None

def add_contact(args, contacts):
    name, phone = args
    if not is_valid_phone(phone):
        return('Invalid phone number')
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        return f"Contact with name {name} not found."
    if not is_valid_phone(phone):
        return('Invalid phone number')
    contacts[name] = phone
    return f"New phone number for contact {name} is changed for {phone}."

def show_phone(args, contacts):
    name = args[0]
    if name not in contacts:
        return f"Contact {name} not found."
    return f"Phone number for {name}: {contacts[name]}"

def show_all(contacts):
        if not contacts:
            return "No saved contacts"
        result = "List of contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    
    
def main():
    contacts = {}


    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            if len(args) == 2:
                print(add_contact(args, contacts))
            else:
                print("Command 'add' should have two arguments: name, phone.")
        elif command == "change":
            if len(args) == 2:
                print(change_contact(args, contacts))
            else:
                print("Command 'change' should have two arguments: name, phone.")
        elif command == "phone":
            if len(args) == 1:
                print(show_phone(args, contacts))
            else:
                print("Command 'change' should have two arguments: name.")
        elif command == "all":
            print(show_all(contacts))
        elif command in ["exit", "close"]:
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()