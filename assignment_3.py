#Write a program to implement a Configurable Payment Processing System Using Strategy Pattern

from abc import ABC, abstractmethod


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass



class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Debit Card.")


class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ₹{amount} using PayPal.")


class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("No payment method selected.")
        else:
            self.strategy.pay(amount)

processor = PaymentProcessor()


processor.set_strategy(CreditCardPayment())
processor.process_payment(1500)


processor.set_strategy(UPIPayment())
processor.process_payment(750)


processor.set_strategy(PayPalPayment())
processor.process_payment(3000)


processor.set_strategy(DebitCardPayment())
processor.process_payment(1200)
        
