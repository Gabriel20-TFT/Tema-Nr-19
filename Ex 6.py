# Generator de ID-uri
# Creează o clasă IDGenerator.
# Atribute de clasă: un contor.
# Metodă statică next_id() care returnează un ID unic de fiecare dată când e apelată.

class IDGenerator:
    _counter = 0

    @staticmethod
    def next_id():
        """Generează un ID unic."""
        IDGenerator._counter += 1
        return IDGenerator._counter

# Exemplu de utilizare
if __name__ == "__main__":
    print(IDGenerator.next_id())
    print(IDGenerator.next_id())
    print(IDGenerator.next_id())