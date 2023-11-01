import math
import matplotlib
import matplotlib.pyplot

def func(x):
    return math.sin(x) * math.cos(x)

data = [x for x in range(0, 50)]
results = [func(x) for x in data]

matplotlib.pyplot.plot(data,results)
matplotlib.pyplot.show()