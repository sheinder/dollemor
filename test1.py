import math
from turtle import *

def heart(k):
    return 15 * math.sin(k) ** 3

def heart2(k):
    return (11.8 * math.cos(k) - 5 * math.cos(2 * k)
            - 2 * math.cos(3 * k) - math.cos(4 * k))

speed(0)
bgcolor("black")
color("red")

for i in range(10000):
    x = heart(i) * 20
    y = heart2(i) * 20
    goto(x, y)
    for j in range(3):
        goto(x, 0)


done()
