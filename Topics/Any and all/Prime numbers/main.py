prime_numbers = [x for x in range(2,1001) if all([x % y != 0 for y in range(2,x)])]
#print(prime_numbers)
