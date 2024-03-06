import time
import math


def delayed_square_root(number, delay_ms):
    time.sleep(delay_ms / 1000.0)
    sqrt_result = math.sqrt(number)
    return sqrt_result


number = int(input())
delay_ms = int(input())
sqrt_result = delayed_square_root(number, delay_ms)
print(f"Square root of {number} after {delay_ms} milliseconds is {sqrt_result}")
