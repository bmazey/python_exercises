import pyprimes
from challenges.interview.src.fizzbuzz import FizzBuzz

# each number between 1 and 100 is evaluated
for prime in range(1, 100):
    # if the number is divided by three and has a remainder of 0, then it is a multiple of 3
    if (prime % 3) == 0:



def test_fizzbuzz():
    prime = pyprimes.primes_above(5)
    assert FizzBuzz.fizzbuzz(i=next(prime) * 3) == 'fizz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 5) == 'buzz'
    assert FizzBuzz.fizzbuzz(i=next(prime) * 15) == 'fizzbuzz'
