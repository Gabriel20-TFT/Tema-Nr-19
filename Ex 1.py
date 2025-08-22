# Vectori ( __add__ și __sub__ )
# Creează o clasă Vector2D cu coordonatele x și y.
# Suprascrie __add__ pentru a aduna doi vectori.
# Suprascrie __sub__ pentru a scădea doi vectori.
# Testează cu câțiva vectori.

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        raise TypeError("Operandul trebuie să fie de tip Vector2D")

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        raise TypeError("Operandul trebuie să fie de tip Vector2D")

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

if __name__ == '__main__':
    # Testare
    v1 = Vector2D(3, 4)
    v2 = Vector2D(1, 2)

    adunare = v1 + v2
    scadere = v1 - v2

    print(f"Vectorul 1: {v1}")
    print(f"Vectorul 2: {v2}")
    print(f"Adunarea: {adunare}")
    print(f"Scăderea: {scadere}")

