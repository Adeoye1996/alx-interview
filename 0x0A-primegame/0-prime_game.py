#!/usr/bin/python3
"""
Module for 0-prime_game.py
"""


def isPrime(num):
    """Determines the winner of a prime game session with `x` round
 """
    prime = []
    sieve = [True] * (num + 1)
    for p in range(2, num + 1):
        if (sieve[p]):
            prime.append(p)
            for i in range(p, num + 1, p):
                sieve[i] = False
    return prime


def isWinner(x, nums):
    """
    Determines winner of Prime Game
"""
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime = isPrime(nums[i])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
