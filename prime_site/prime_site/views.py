from django.shortcuts import render
import math

def index(req, count):
    count = int(count)
    primes = []
    i = 0
    current = 2
    while i < count:
        if _is_prime(current):
            primes.append(current)
            i += 1
        current += 1

    return render(req, 'prime_site/index.html', { 'primes': primes, 'n': count })

def _is_prime(n):
    for d in range(2, int(math.sqrt(n) + 1)):
        if n % d == 0:
            return False
    return True
