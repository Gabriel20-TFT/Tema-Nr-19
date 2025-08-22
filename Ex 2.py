# Lista personalizată ( __len__ și __getitem__ )
# Creează o clasă MyList care să conțină o listă internă.
# Implementează __len__ ca să returneze lungimea listei.
# Implementează __getitem__ pentru a permite accesul prin [].
# Implementează __contains__ ca să poți verifica if x in lista.

class MyList:
    def __init__(self, initial_list=None):
        if initial_list is None:
            self.data = []
        else:
            self.data = initial_list

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __contains__(self, item):
        return item in self.data

    def __repr__(self):
        return f"MyList({self.data})"

if __name__ == '__main__':
    # Testare
    my_list = MyList([10, 20, 30, 40])

    print(f"Lungimea listei: {len(my_list)}")
    print(f"Elementul de la indexul 2: {my_list[2]}")
    print(f"Verificare dacă 20 este în listă: {'da' if 20 in my_list else 'nu'}")
    print(f"Verificare dacă 50 este în listă: {'da' if 50 in my_list else 'nu'}")

    