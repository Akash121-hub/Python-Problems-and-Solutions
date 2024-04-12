def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# for i in range(2,int(n**0.5) + 1):
#         if n % i == 0:
#             return False
def generate_primes(count):
    primes = []
    num = 2
    while len(primes) <= count:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

# Generate the first 20 prime numbers
first_20_primes = generate_primes(20)
print("The first 20 prime numbers are:", (first_20_primes))