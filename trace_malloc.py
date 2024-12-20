import tracemalloc

tracemalloc.start()

def my_function():
    a = [1] * (10**6)
    b = [2] * (10**7)
    return a, b

my_function()

snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics('lineno'):
    print(stat)
