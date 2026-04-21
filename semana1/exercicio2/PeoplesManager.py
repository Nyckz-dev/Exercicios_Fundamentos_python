from Peoples import Peoples
from Verification import Verification
class PeoplesManager:
    def __init__(self, verifier):
        # initialize an empty list to store the people
        self._items = []
        self._verifier = verifier


    def add(self, people):
        # add a new people to the list
        people.AgeRange = self._verifier.classify(people.age)
        self._items.append(people)
    
    def remove_By_Id(self, people_id):
        # remove a people from the list by id
        for people in self._items:
            if people.id == people_id:
                self._items.remove(people)
                return people
        return None
    
    def List_all(self):
        # return all the people in the list
        return list(self._items)
    
    def find_By_Id(self, Peoples_id):
        # find a people by id and return it, if not found return None
        for people in self._items:
            if people.id == Peoples_id:
                return people
        return None
    
