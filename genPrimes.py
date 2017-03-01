def genPrimes():
    prime_numbers = []
    num = 1
    while True:
        num += 1
        for i in prime_numbers:
            if num % i == 0:
                break
            else:
                prime_numbers.append(num)
                yield num
    print(prime_numbers)            
