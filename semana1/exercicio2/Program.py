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
    
    for _ in range(n):
        name = input("Whats your name? ")
        age = int(input("Whats your age? "))
        people = Peoples(name, age)
        manager.add(people)
      
    print("List of all people: ")
    for people in manager.List_all():
        print(f"Name: {people.name}\nAge: {people.age}\nAge Range: {people.AgeRange.value}\nid: {people.id}\n")

if __name__ == "__main__":
    Program.main()