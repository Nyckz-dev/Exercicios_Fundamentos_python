from PrimeNumber import PrimeNumber
class Program:
 @staticmethod
 def main():
  while True:
   try:
    value = int(input("Enter range of prime number you want: "))
    PrimeNumber.calculation(value)
   except ValueError:
    print("Enter a valid number!")
   
   print("\n1.Repeat")
   print("2.Exit")
   choose = int(input("Choose an option: "))

   if choose == 2:
    print("Exiting...")
    break
   elif choose == 1:
    continue
   
  
if __name__ == "__main__":
 Program().main()