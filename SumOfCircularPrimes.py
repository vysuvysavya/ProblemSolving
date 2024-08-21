def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def get_rotations(n):
    s = str(n)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def is_circular_prime(n):
    for rotation in get_rotations(n):
        if not is_prime(rotation):
            return False
    return True

def circular_primes_below_n(n):
    circular_primes = []
    for i in range(2, n):
        if is_prime(i) and is_circular_prime(i):
            circular_primes.append(i)
    return sum(circular_primes)

n = int(input())
print(circular_primes_below_n(n))