import random
import numpy as np

from simple_benchmark import benchmark

def numpy_sum(it):
    return np.sum(it) < 10

def python_sum(it):
    return sum(it) < 10

def numpy_sum_method(arr):
    return arr.sum() < 10

def python_in(it):
    return 0 in it

def python_notin(it):
    return np.prod(it) == 0

b_array = benchmark(
    [numpy_sum, numpy_sum_method, python_sum, python_in, python_notin],
    arguments={2**i: np.random.randint(2, size=10) for i in range(2, 21)},
    argument_name='array size',
    function_aliases={numpy_sum: 'numpy.sum(<array>)', numpy_sum_method: '<array>.sum()', python_sum: "sum(<array>)"
    , python_in: 'pyin', python_notin: 'pynotin'}
)

b_list = benchmark(
    [numpy_sum, python_sum, python_in, python_notin],
    arguments={2**i: [random.randint(0, 1) for _ in range(10)] for i in range(2, 21)},
    argument_name='list size',
    function_aliases={numpy_sum: 'numpy.sum(<list>)', python_sum: "sum(<list>)", python_in: 'pyin', python_notin: 'pynotin'}
)
print(b_array)
print(b_list)