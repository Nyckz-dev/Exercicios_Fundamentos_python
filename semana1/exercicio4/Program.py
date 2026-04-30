from MultiplicationTable import MultiplicationTable
class Program:
  
  @staticmethod
  def main():
   while True:
    try:
     
     value = int(input("Enter the first multiplication table: "))
     limit = int(input("Enter the last multiplication tables: "))
     max = int(input("Enter langth of multiplication table: "))
     result = MultiplicationTable().calculation(value, max, limit)
     for line in result:
      print(line)
    
    except ValueError: 
     print("Invalid number, please type a valid number!\n")
     continue 

    while True:
     print("\n1-Start Over")
     print("2-Exit")
     choice = input("Choice: ")
  
     if choice == "1":
      break
     elif choice == "2":
      print("Exiting...")
      return
     else:
      print("Invalid option!")
     
if __name__ == "__main__":
  Program().main()
