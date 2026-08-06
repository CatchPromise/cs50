class Vault:
    def __init__(self, euros=0, dollar=0, naira=0):
        self.euros = euros
        self.dollar = dollar
        self.naira = naira



    def __str__(self):
        return f"{self.euros} Euros, {self.dollar} Dollar, {self.naira} Naira"

    def __add__(self, other):
        euros = self.euros + other.euros
        dollar = self.dollar + other.dollar
        naira = self.naira + other.naira
        return Vault(euros, dollar, naira)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter + weasley
print(total)