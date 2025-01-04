def save_message_to_file():
    """
    Prompts the user for a message and a filename,
    then saves the message to the specified file without any validation.
    """
    message = input("Enter the message you want to save: ")
    filename = input("Enter the filename (e.g., message.txt): ")
    
    with open(filename, 'w') as file:
        file.write(message)
    
    print(f"Message saved to {filename}")

if __name__ == "__main__":
    save_message_to_file()
