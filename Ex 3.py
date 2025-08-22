# Cont bancar ( __eq__, __lt__ )
# Creează o clasă BankAccount cu nume și sold.
# Suprascrie __eq__ pentru a compara două conturi după sold.
# Suprascrie __lt__ pentru a permite sortarea conturilor după sold.
# Testează cu o listă de conturi și sorteaz-o.

class BankAccount:
    def __init__(self, nume, sold):
        self.nume = nume
        self.sold = sold

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.sold == other.sold
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, BankAccount):
            return self.sold < other.sold
        return NotImplemented

    def __repr__(self):
        return f"BankAccount(nume='{self.nume}', sold={self.sold})"

if __name__ == '__main__':
    # Creare liste de conturi
    conturi = [
        BankAccount("Andrei", 2400),
        BankAccount("Maria", 1500),
        BankAccount("Ionel", 847),
        BankAccount("Ana", 1500)
    ]

    # Sortare după sold
    conturi_sortate = sorted(conturi)

    # Afișare rezultate
    print("Conturi înainte de sortare:")
    for cont in conturi:
        print(cont)

    print("\nConturi după sortare (după sold):")
    for cont in conturi_sortate:
        print(cont)
