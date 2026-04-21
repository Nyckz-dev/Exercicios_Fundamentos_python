from ClassificationEnum import ClassificationEnum
class Verification:
    def validate_age(self, age):
        if not isinstance(age, int):
            raise ValueError("Age must be a integer number.")
        if age <= 0: 
            raise ValueError("Age must be greater than zero.")
        if age > 130:
            raise ValueError("Age must be less than 130.") 
        return True
    
    def classify(self, age):
        self.validate_age(age)

        if age < 12:
            return ClassificationEnum.child
        if age >= 12 and age < 18:
            return ClassificationEnum.teenager
        if age >= 18:
            return ClassificationEnum.adult
        

            
            
        
    

    