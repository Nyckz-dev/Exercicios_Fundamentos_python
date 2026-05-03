class PrimeNumber:
    def calculation(value):
        print(f"All prime numbers in range {value}")
        for i in range(2, value + 1):
         if PrimeNumber.is_prime(i):
            print(i)

    def is_prime(n):
       if n < 2:
          return False
       for div in range(2, int(n**0.5) + 1):
          if n % div == 0:
           return False
       return True 