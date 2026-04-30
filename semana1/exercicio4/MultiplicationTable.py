class MultiplicationTable:
 def calculation(self, start, max, limit):
  result = []
  for n in range(start, limit + 1):
    result.append(f"\nMultiplication Table {n}")
    for i in range(1, max + 1):
     result.append(f"{n} x {i} = {n * i}")
  return result