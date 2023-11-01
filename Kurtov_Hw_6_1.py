import math
import matplotlib
import matplotlib.pyplot

def func(x):
    return math.sin(x) * math.cos(x)

def func2(x):
    return math.log(x) + math.cos(x)

data = [x for x in range(1, 50)]
results = [func2(x) for x in data]

matplotlib.pyplot.plot(data,results)
matplotlib.pyplot.show()