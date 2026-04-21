from Peoples import Peoples
from Verification import Verification
from PeoplesManager import PeoplesManager

class Program:
 @staticmethod
 def main():
    verifier = Verification()
    manager = PeoplesManager(verifier)
    
    print("Input the number of people you want to add: ")
    n = int(input())
    
    for i in range(1, n + 1):
        print(f"\nInput the data of the {i}º person: ")
        name = input("Whats your name? ")
        age = int(input("Whats your age? "))
        people = Peoples(name, age)
        manager.add(people)
      
    print("\nList of all people: ")
    for people in manager.List_all():
        print(f"Name: {people.name}\nAge: {people.age}\nAge Range: {people.AgeRange.value}\nid: {people.id}\n")

if __name__ == "__main__":
    Program.main()
    inout = input("Press enter to exit...")