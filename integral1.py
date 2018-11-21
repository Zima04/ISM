from math import *
import numpy as np

data = [(21, 10), (20001, 10), (20001, 1000), (2000001, 1000), (2000001, 10000)]
print("Right answer is something about 0.00036866")
for (n, ranges) in data:
    h = (ranges * 2) / (n - 1)
    nodes = [i for i in np.arange(4, ranges + h, h)]
    answer = sum([exp(-(x)) /(x *(1 + x ** 3) ** (1 / 2)) for x in nodes]) * (ranges * 2 / n)
    print("Answer: {0}, ranges = (4, {1}), number of nodes = {2}".format(answer, ranges, n))