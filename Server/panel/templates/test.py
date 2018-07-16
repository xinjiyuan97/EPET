import math

 

def sieve(size):
    sieve = [True] * size
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(size)) + 1):
        k = i * 2
        while k < size:
            sieve[k] = False
            k += i
    return sum(1 for x in sieve if x)


if __name__ == "__main__":
    print(sieve(10000000000))