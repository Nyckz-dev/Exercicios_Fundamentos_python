from Calculator import Calculator

class Program:
 @staticmethod 
 def main():
   try:
    print("==Menu==")
    print("1-Max sum")
    print("2-Average")
    print("3-Multply")
    choice = int(input("Choose an option: "))
   except ValueError: 
    print("Insert a valid number!\n") 
    return
   
   calc = Calculator() 
   print("\nPress 0 for stop!")
   if choice == 1:
     while True:
      try:
       values = list(map(float, input("Values: ").split()))
      except ValueError: 
       print("Enter a valid number!")
       continue
    
      if any(v == 0 for v in values):
       print("Exiting...")
       break
      else:
       calc.add(values)
       print(calc.sum_values())
      
   elif choice == 2:
    while True:
     try:
      values = list(map(float, input("Values: ").split()))
     except ValueError:
      print("Enter a valid number!")

     if any(v == 0 for v in values):
       print("Exiting...")
       break
     else:
      calc.add(values)
     print(f"{calc.average():.2f}")
   
   elif choice == 3:
    while True:
     try:
      values = list(map(float, input("Values: ").split()))
     except ValueError:
      print("Enter a valid number!")

     if any(v == 0 for v in values):
      print("Exiting...")
      break
     else:
      calc.add(values)
     print(calc.multiplication())
   

if __name__ == "__main__":
 Program().main()