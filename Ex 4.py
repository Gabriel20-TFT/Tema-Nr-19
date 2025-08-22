# Fracții ( __add__, __mul__, __truediv__ )
# Creează o clasă Fraction cu numărător și numitor.
# Suprascrie operatorii +, *, /.

from math import gcd

class Fraction:
    def __init__(self, numarator, numitor):
        if numitor == 0:
            raise ValueError("Numitorul nu poate fi zero")
        self.numarator = numarator
        self.numitor = numitor
        self._reduce()

    def _reduce(self):
        """Reduc fracția la forma sa cea mai simplă."""
        common_divisor = gcd(self.numarator, self.numitor)
        self.numarator //= common_divisor
        self.numitor //= common_divisor

    def __add__(self, other):
        if isinstance(other, Fraction):
            numarator = self.numarator * other.numitor + other.numarator * self.numitor
            numitor = self.numitor * other.numitor
            return Fraction(numarator, numitor)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Fraction):
            numarator = self.numarator * other.numarator
            numitor = self.numitor * other.numitor
            return Fraction(numarator, numitor)
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Fraction):
            if other.numarator == 0:
                raise ZeroDivisionError("Împărțirea la zero")
            numarator = self.numarator * other.numitor
            numitor = self.numitor * other.numarator
            return Fraction(numarator, numitor)
        return NotImplemented

    def __repr__(self):
        return f"{self.numarator}/{self.numitor}"

if __name__ == '__main__':
    # Exemple de utilizare
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)

    suma = f1 + f2
    produs = f1 * f2
    impartire = f1 / f2

    print(f"{f1} + {f2} = {suma}")
    print(f"{f1} * {f2} = {produs}")
    print(f"{f1} / {f2} = {impartire}")