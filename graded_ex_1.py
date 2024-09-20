products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)

def validate_email(email):
    return "@" in email

def display_categories():
    print("Available Categories:")
    for i, category in enumerate(products.keys(), start=1):
        print(f"{i}. {category}")

def display_products(products_list):
    print("Available Products:")
    for i, (product, price) in enumerate(products_list, start=1):
        print(f"{i}. {product} - ${price:.2f}")

def display_sorted_products(products_list, sort_order):
    sorted_products = sorted(products_list, key=lambda item: item[1], reverse=(sort_order == 2))
    print("Sorted Products:")
    for i, (product, price) in enumerate(sorted_products, start=1):
        print(f"{i}. {product} - ${price:.2f}")
    return sorted_products

def add_to_cart(cart, product, quantity):
    cart.append((product, quantity))

def display_cart(cart):
    print("Your Cart:")
    if not cart:
        print("Your cart is empty.")
    else:
        for product, quantity in cart:
            print(f"{product} x {quantity}")

def generate_receipt(name, email, cart, total_cost, address):
    print("\n--- Receipt ---")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print("Products Purchased:")
    for product, quantity in cart:
        print(f"{product} x {quantity}")
    print(f"Total Cost: ${total_cost:.2f}")
    print(f"Delivery Address: {address}")
    print("Your items will be delivered in 3 days. Payment will be accepted after successful delivery.")

def main():
    name = input("Enter your full name (First Last): ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name.")
        name = input("Enter your full name (First Last): ")

    email = input("Enter your email address: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email address: ")

    cart = []

    while True:
        display_categories()
        category_choice = int(input("Select a category by number: "))
        category_list = list(products.keys())
        
        if 1 <= category_choice <= len(category_list):
            selected_category = category_list[category_choice - 1]
            display_products(products[selected_category])
            
            while True:
                print("\nOptions:")
                print("1. Select a product to buy")
                print("2. Sort the products by price")
                print("3. Go back to category selection")
                print("4. Finish shopping")
                option = int(input("Choose an option: "))

                if option == 1:  # Select a product to buy
                    product_choice = int(input("Enter the product number: "))
                    product_list = products[selected_category]
                    
                    if 1 <= product_choice <= len(product_list):
                        product_name, product_price = product_list[product_choice - 1]
                        
                        # Ensure quantity is a valid integer
                        while True:
                            try:
                                quantity = int(input(f"Enter quantity for {product_name}: "))
                                if quantity < 1:
                                    raise ValueError("Quantity must be at least 1.")
                                break
                            except ValueError as e:
                                print(f"Invalid input: {e}. Please enter a valid quantity.")

                        add_to_cart(cart, product_name, quantity)
                        print(f"Added {quantity} of {product_name} to cart.")
                    else:
                        print("Invalid product number.")

                elif option == 2:  # Sort products by price
                    sort_order = int(input("Sort by price: 1 for ascending, 2 for descending: "))
                    sorted_products = display_sorted_products(products[selected_category], sort_order)
                    # Display options again after sorting
                    print("\nOptions:")
                    print("1. Select a product to buy")
                    print("2. Sort the products by price")
                    print("3. Go back to category selection")
                    print("4. Finish shopping")

                elif option == 3:  # Go back to category selection
                    break

                elif option == 4:  # Finish shopping
                    display_cart(cart)
                    if cart:  # If cart is not empty
                        total_cost = sum(quantity * next(price for name, price in products[selected_category] if name == product) for product, quantity in cart)
                        address = input("Enter delivery address: ")
                        generate_receipt(name, email, cart, total_cost, address)
                    else:
                        print("Thank you for using our portal. Hope you buy something from us next time. Have a nice day.")
                    return

                else:
                    print("Invalid option.")

        else:
            print("Invalid category number.")

if __name__ == "__main__":
    main()