class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def eat_lunch(self):
        if self.balance > 2.6:
            self.balance -= 2.6

    def eat_special(self):
        if self.balance > 4.6:
            self.balance -= 4.6

    def deposit_money(self, deposit: int):
        if deposit > 0:
            self.balance += deposit
        else:
            raise ValueError(
                "You cannot deposit an amount of money less than zero")

    def __str__(self):
        return f"The balance is {self.balance:.1f} euros"


def main():
    peters_card = LunchCard(20)
    graces_card = LunchCard(30)
    peters_card.eat_special()
    graces_card.eat_lunch()
    print("Peter:", peters_card)
    print("Grace:", graces_card)
    peters_card.deposit_money(20)
    graces_card.eat_special()
    print("Peter:", peters_card)
    print("Grace:", graces_card)
    peters_card.eat_lunch()
    peters_card.eat_lunch()
    graces_card.deposit_money(50)
    print("Peter:", peters_card)
    print("Grace:", graces_card)


main()
