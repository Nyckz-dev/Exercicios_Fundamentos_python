import uuid
class Peoples:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.id = uuid.uuid4()
        self.AgeRange = None

