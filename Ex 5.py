# Conversii de temperatură
# Creează o clasă TemperatureConverter.
# Metode statice:
# celsius_to_fahrenheit(c)
# fahrenheit_to_celsius(f)
# Testează conversiile cu câteva valori

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        """Conversie din Celsius în Fahrenheit."""
        return c * 9/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        """Conversie din Fahrenheit în Celsius."""
        return (f - 32) * 5/9

# Testarea conversiilor
if __name__ == "__main__":
    valori_celsius = [5, 23, 37, 100]
    valori_fahrenheit = [32, 68, 98.6, 212]

    print("Conversii Celsius -> Fahrenheit:")
    for c in valori_celsius:
        print(f"{c}°C = {TemperatureConverter.celsius_to_fahrenheit(c):.2f}°F")

    print("\nConversii Fahrenheit -> Celsius:")
    for f in valori_fahrenheit:
        print(f"{f}°F = {TemperatureConverter.fahrenheit_to_celsius(f):.2f}°C")
