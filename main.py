from card.card import Cart
from discounts.discount import PercentageDiscount, FixedAmountDiscount
from exceptions.invalid_price_error import InvalidPriceError
from exceptions.invalid_quantity_error import InvalidQuantityError
from payment_processors.payment_processor import CreditCardProcessor, PayPalProcessor, BankTransferProcessor
from product.product import Product


def main():

    # Created test product
    try:
        product1 = Product("Laptop", 1500.00, "A high-end gaming laptop")
        product2 = Product("Mouse", 50.00, "A wireless mouse")
        product3 = Product("Keyboard", 100.00, "A mechanical keyboard")
        # product4 = Product("Headphones", -10.00, "Noise-cancelling headphones")
        # product5 = Product("Monitor", 0, "4K monitor")
    except (InvalidPriceError, TypeError, ValueError) as e:
        print(e)

    cart = Cart()

    try:
        cart.add_product(product1, 1)
        cart.add_product(product2, 2)
        cart.add_product(product3, 3)
        # cart.add_product(product4, -1)
        # cart.add_product(product5, 0)
    except (InvalidQuantityError, TypeError, ValueError) as e:
        print(e)

    print(cart)
    print(f'Total cost:{cart.total_cost()} $')

    try:
        # Applying different types of discounts
        percentage_discount = PercentageDiscount(10)
        fixed_amount_discount = FixedAmountDiscount(20)
    except TypeError as e:
        print(e)

    cart.apply_discount(percentage_discount)
    cart.log('Applied percentage discount to the cart')

    print(cart)
    print(f'Total cost after percentage discount: {cart.total_cost()} $')

    cart.apply_discount(fixed_amount_discount)
    cart.log('Applied fixed amount discount to the cart')
    print(cart)
    print(f'Total cost after fixed amount discount: {cart.total_cost()} $')

    # Using different payment systems
    credit_card_processor = CreditCardProcessor("1234-5678-9800-1111", "Oleh Opalko", "000", "12/26")
    paypal_processor = PayPalProcessor("oleh.opalko@gmail.com")
    bank_transfer_processor = BankTransferProcessor("123456789", "Oleh Opalko")

    cart.pay(credit_card_processor)
    cart.pay(paypal_processor)
    cart.pay(bank_transfer_processor)


if __name__ == "__main__":
    main()
