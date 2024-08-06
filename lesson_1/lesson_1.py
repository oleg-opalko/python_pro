class Product:
    def __init__(self, name: str, price: int | float, description: str):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f'Product: name:{self.name},price: {self.price},description: {self.description}'


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, product: Product, quantity: int):
        self.items[product] = self.items.get(product, 0) + quantity

    def calculate_total(self) -> float:
        total = 0.0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def __str__(self):
        cart_content = '\n'.join([f"{product.name}: {quantity} x ${product.price}" for product, quantity
                                  in self.items.items()])
        return f'Card: \n{cart_content}\nTotal: {self.calculate_total():.2f}'


cart = Cart()

product_1 = Product('Potatoes', 20, 'Potatoes from farms')
product_2 = Product('Tomatoes', 15, 'Ukrainian tomato')
product_3 = Product('Strawberries', 35, 'Carpathian strawberry')

cart.add_product(product_1, 1)
cart.add_product(product_2, 2)
cart.add_product(product_3, 3)

print(cart)
