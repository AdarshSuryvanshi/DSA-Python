from abc import ABC, abstractmethod

class Payment(ABC):  # Abstract Base Class
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} using Credit Card.")

class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid ${amount} using PayPal.")

# Usage
payment_method = CreditCardPayment()
payment_method.make_payment(100)

payment_method = PayPalPayment()
payment_method.make_payment(200)
