import random

def RA(N):
    a_arr = [random.randint(1, 10) for _ in range(N)]
    print(a_arr)

RA(10)