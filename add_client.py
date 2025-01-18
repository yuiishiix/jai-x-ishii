clients = {}


def add_client():
    try:
        name = input("Enter your name: ")
        email = input("Enter Your Email: ")


        # Generate a unique account number
        client_id = len(clients) + 1001
        clients[client_id] = {"name": name, "email": email }
        print(f"Client added successfully! Your account number is {client_id}.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the balance.")

