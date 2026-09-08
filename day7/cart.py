cart = {}


def add_product(product, price):
    cart[product] = price


def remove_product(product):
    if product in cart:
        del cart[product]
        return "Product removed successfully"

    return "Product not found"


def calculate_total():
    return sum(cart.values())


def display_cart():
    if not cart:
        print("Cart is empty")
    else:
        print("\n--- SHOPPING CART ---")

        for product, price in cart.items():
            print(product, ":", price)