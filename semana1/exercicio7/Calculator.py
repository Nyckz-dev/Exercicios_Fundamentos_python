import math
class Calculator:
    values = []
    def __init__(self):
        self.values = []
    
    def add(self, numbers):
     if isinstance(numbers, list):
      self.values.extend(numbers)
     else:
        self.values.append(numbers)

    def sum_values(self):
        return sum(self.values) 

    def average(self):
       return sum(self.values) / len(self.values) if self.values else 0
    
    def multiplication(self):
       return math.prod(self.values)
      
     
        