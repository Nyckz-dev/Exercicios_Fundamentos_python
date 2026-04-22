from Calculation import Calculation
class Program:
 @staticmethod
 def main():
  while True:
   print("\nTemperature converter")
   print("1. Celsius to Fahrenheit")
   print("2. Fahrenheit to Celsius")
   print("3. Exit")
   
   try:
    n = int(input("Choose an option: "))
   except ValueError:
    print("Invalid input. Please enter a valid number.")
    continue

   if n == 1:
    try: 
      print("Enter the temperature in Celsius: ")
      celsius = float(input())
      print(f"The temperature in Fahrenheit: {Calculation(celsius, 0).celsiusConverter(): .2f}")
    except ValueError:
      print("Invalid input. Please enter a valid number.")

   elif n == 2:
    try:
      print("Enter the temperature in Fahrenheit: ")
      fahrenheit = float(input())
      print(f"The temperature in Celsius: {Calculation(0, fahrenheit).fahrenheitConverter(): .2f}")
    except ValueError:
      print("Invalid input. Please enter a valid number.")

   elif n == 3:
    print("Exiting...")
    break
   else:
    print("Invalid option. Please choose a valid option.") 

if __name__ == "__main__":
 Program.main()