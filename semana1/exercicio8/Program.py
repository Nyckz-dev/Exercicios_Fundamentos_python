from GuessingGame import GuessingGame

class Program:
 @staticmethod
 def main():
  while True:
     game = GuessingGame()
     try:
      print("\nWelcome to Guessing game!")
      print("1-Start")
      print("2-Exit")
      choice = int(input("Choose an option:"))
     except ValueError:
       print("Enter a valid number!")
       continue
       
     if choice == 1:
      print("\nSelect level")
      print("1-Easy")
      print("2-Hard")
      print("3-impossible")
      try:
       level = int(input("Choose an level: "))
      except ValueError:
        print("Enter a valid number!\n")
        continue
      
      if level == 1:
       max_attempts = 5
       attempt = 0
       
       while attempt < max_attempts:
        try:
         guess = int(input("\nChoose a number from 1 to 25: "))
         attempt += 1
        except ValueError:
         print("Enter a valid number!")
         continue

        result, message = game.EasyLevel(guess, max_attempts, attempt)
        print(message)
          
        if result:
          break

        print("a) Try again")
        print("b) exit")
        
        try:
         choice = input("Choose an option: ")
        except ValueError:
          print("Choose a valid option!")
          continue


        if choice == "a":
          continue
        else:
          break
        
       if not result:
          print(f"Game over! The secret number was {game.easy}.")

      if level == 2: 
       
       max_attempts = 3
       attempt = 0
       
       while attempt < max_attempts:
        
        try:
         guess = int(input("\nChoose a number from 1 to 50: "))
         attempt += 1
        except ValueError:
          print("Enter a valid number!")
          continue

        result, message = game.HardLevel(guess, max_attempts, attempt)
        print(message)
          
        if result:
          break

        print("a) Try again")
        print("b) exit")
        
        try:
         choice = input("Choose an option: ")
        except ValueError:
          print("Choose a valid option!")
          continue

        if choice == "a":
          continue
        else:
          break
       if not result:
        print(f"Game over! The secret number was {game.hard}.") 
      
      if level == 3:
       max_attempts = 2
       attempt = 0
       
       while attempt < max_attempts:

        try:  
         guess = int(input("\nChoose a number from 1 to 100: "))
         attempt += 1
        except ValueError:
          print("Enter a valid number!")
          continue

        result, message = game.ImpossibleLevel(guess, max_attempts, attempt)
        print(message)
          
        if result:
          break

        print("a) Try again")
        print("b) exit")

        try:
         choice = input("Choose an option: ")
        except ValueError:
          print("Choose a valid option!")
          continue

        if choice == "a":
          continue
        else:
          break
       if not result:
        print(f"Game over! The secret number was {game.impossible}.") 

     else:
      print("Exiting...")
      break
          
if __name__ == "__main__":
    Program().main()