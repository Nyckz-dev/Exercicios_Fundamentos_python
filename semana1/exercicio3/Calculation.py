class Calculation: 
    def __init__(self, celsius, fahrenheit):
        self.celsius = celsius
        self.fahrenheit = fahrenheit
    
    def celsiusConverter(self):
        return (self.celsius * 9/5) + 32

    def fahrenheitConverter(self):
        return (self.fahrenheit - 32) * 5/9

