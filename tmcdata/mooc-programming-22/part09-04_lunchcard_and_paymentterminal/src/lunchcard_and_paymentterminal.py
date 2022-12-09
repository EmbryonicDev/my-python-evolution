# WRITE YOUR SOLUTION HERE:

class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        # The amount should be subtracted from the balance only if there is enough money on the card
        # If the payment is successful, the method returns True, and otherwise it returns False
        payment_possible = amount <= self.balance
        if payment_possible:
            self.balance -= amount
        return payment_possible


class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    def eat_lunch(self, payment: float):
        # A regular lunch costs 2.50 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of lunches sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        cost = 2.5
        change = payment
        if payment >= cost:
            self.funds += cost
            self.lunches += 1
            change -= cost
        return change

    def eat_special(self, payment: float):
        # A special lunch costs 4.30 euros.
        # Increase the value of the funds at the terminal by the price of the lunch,
        # increase the number of specials sold, and return the appropriate change.
        # If the payment passed as an argument is not large enough to cover the price,
        # the lunch is not sold, and the entire sum is returned.
        cost = 4.3
        change = payment
        if payment >= cost:
            self.funds += cost
            self.specials += 1
            change -= cost
        return change

    def eat_lunch_lunchcard(self, card: LunchCard):
        # A regular lunch costs 2.50 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        cost = 2.5
        payment_possible = card.balance >= cost
        if payment_possible:
            self.lunches += 1
            card.balance -= cost
        return payment_possible

    def eat_special_lunchcard(self, card: LunchCard):
        # A special lunch costs 4.30 euros.
        # If there is enough money on the card, subtract the price of the lunch from the balance
        # and return True. If not, return False.
        cost = 4.3
        payment_possible = card.balance >= cost
        if payment_possible:
            self.specials += 1
            card.balance -= cost
        return payment_possible

    def deposit_money_on_card(self, card: LunchCard, amount: float):
        card.balance += amount
        self.funds += amount


if __name__ == "__main__":
    print('\nPart 1')
    card = LunchCard(10)
    print("Balance", card.balance)
    result = card.subtract_from_balance(8)
    print("Payment successful:", result)
    print("Balance", card.balance)
    result = card.subtract_from_balance(4)
    print("Payment successful:", result)
    print("Balance", card.balance)

    print('\nPart 2')
    exactum = PaymentTerminal()
    change = exactum.eat_lunch(10)
    print("The change returned was", change)
    change = exactum.eat_lunch(5)
    print("The change returned was", change)
    change = exactum.eat_special(4.3)
    print("The change returned was", change)
    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    print('\nPart 3')
    exactum = PaymentTerminal()
    change = exactum.eat_lunch(10)
    print("The change returned was", change)
    card = LunchCard(7)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    result = exactum.eat_lunch_lunchcard(card)
    print("Payment successful:", result)
    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)

    print('\nPart 4')
    exactum = PaymentTerminal()
    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")
    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)
