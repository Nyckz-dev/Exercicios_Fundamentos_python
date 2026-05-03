from PrimeNumber import PrimeNumber
class Program:
 @staticmethod
 def main():
  value = int(input("Enter a number: "))
  PrimeNumber.calculation(value)
  
if __name__ == "__main__":
 Program().main()