import time
from StopWatch import StopWatch


class Program:
      def __init__(self, count):
       self.cd = StopWatch(count)
     
      def menu(self):
       while True:
        if not self.cd.running:  # só mostra menu se não estiver rodando
            print("\n=== MENU ===")
            print("1 - Start countdown")
            print("2 - Pause")
            print("3 - Reset")
            print("4 - Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.cd.start_countdown()
            elif choice == "2":
                self.cd.pause()
            elif choice == "3":
                self.cd.reset()
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid option, try again.")
        else:
            time.sleep(0.5)


if __name__ == "__main__":
    try:
     count = int(input("Start countdown in: "))
     Program = Program(count)
     Program.menu()
    except ValueError:
       print("Enter a valid number!")  