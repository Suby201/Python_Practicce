def find_primes(a,b):
    primes = []
    for num in range(a, b+1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
