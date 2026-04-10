class peoplesManager:
    def __init__(self):
        # initialize an empty list to store the people
        self._items = []

    def add(self, peoples):
        # add a new people to the list
        self._items.append(peoples)
    
    def remove_By_Id(self, person_id):
        # remove a people from the list by id
        for people in self._items:
            if people.id == person_id:
                self._items.remove(people)
                return people
        return False
    
    def List_all(self):
        # return all the people in the list
        return list(self._items)
    
    def find_By_Id(self, person_id):
        # find a people by id and return it, if not found return None
        for people in self._items:
            if people.id == person_id:
                return people
        return None
    
