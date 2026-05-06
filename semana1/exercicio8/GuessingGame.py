import random 
class GuessingGame:
    def __init__(self):
        self.easy = random.randint(1, 25)
        self.hard = random.randint(1, 50)
        self.impossible = random.randint(1, 100)
    
    def EasyLevel(self, guess, max_attempts, attempt):
        secret = self.easy
       
        if guess == secret:
           return True, f"Nailed it! You got it in {attempt}"
        
        elif guess < secret:
            return False, f"It's a larger number. You have {max_attempts - attempt} attempts"

           
        elif guess > secret:
            return False, f"It's a smaller number. You have {max_attempts - attempt} attempts"
            
    def HardLevel(self, guess, max_attempts, attempt):
        secret = self.hard
        
        if guess == secret:
           return True, f"Incredible! You got it in {attempt}"
        
        elif guess < secret:
            return False, f"It's a larger number. You have {max_attempts - attempt} attempts"
        
        elif guess > secret:
            return False, f"It's a smaller number. You have {max_attempts - attempt} attempts"
    
    def ImpossibleLevel(self, guess, max_attempts, attempt):
        secret = self.impossible

        if guess == secret:
           return True, f"A living legend! You got it in {attempt}"
       
        elif guess < secret:
            return False, f"It's a larger number. You have {max_attempts - attempt} attempts"
       
        elif guess > secret:
            return False, f"It's a smaller number. You have {max_attempts - attempt} attempts"