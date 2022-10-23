from math import exp
number = int | float


def clamp(value: int | float, _min: int | float, _max: int | float) -> int | float:
    return max(min(value, _max), _min)


for i in range(100):
    round(.4/exp(i)-.4+1, 1)
