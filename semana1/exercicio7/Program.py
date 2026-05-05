from Calculator import Calculator

class Program:
 @staticmethod 
 def main():
   try:
    print("==Menu==")
    print("1-Max sum")
    print("2-Average")
    print("3-Multply")
    print("4-Exit")
    choice = int(input("Choose an option: "))
   except ValueError: 
    print("Insert a valid number!\n") 
    return
   
   calc = Calculator() 
   print("\nPress 0 for stop!")
   if choice == 1:
     
     while True:
      values = list(map(float, input("Values: ").split()))
      if any(v == 0 for v in values):
        print("Exiting...")
        break
      else:
        calc.add(values)
      print(calc.sum_values())
      
   elif choice == 2:
    while True:
     values = list(map(float, input("Values: ").split()))
     if any(v == 0 for v in values):
      print("Exiting...")
      break
     else:
      calc.add(values)
     print(f"{calc.average():.2f}")
   #elif choice == 3:
   #else:
   

if __name__ == "__main__":
 Program().main()