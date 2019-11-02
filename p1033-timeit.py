import timeit
import sys

range_size = 1000
count = 1000
setup_statement = "l = [(str()x, x) for x in range(1000)]; d = {} "