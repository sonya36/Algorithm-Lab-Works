# import random
# import time
# import matplotlib.pyplot as plt
# from quicksort import quicksort

# # Data Generation Functions
# def generate_random_data(size):
#     """Generates a list of random integers of specified size."""
#     return random.sample(range(1, size + 1), size)

# def generate_sorted_data(size):
#     """Generates a sorted list of integers of specified size."""
#     return list(range(1, size + 1))

# def generate_reversed_data(size):
#     """Generates a reversed list of integers of specified size."""
#     return list(range(size, 0, -1))

# # Measurement Function
# def measure_time(func, data):
#     """Measures the execution time of a function for a given data."""
#     start_time = time.time()
#     func(data, 0, len(data) - 1)  # Pass the start and end indices
#     end_time = time.time()
#     return end_time - start_time

# # Plotting Function
# def plot_execution_time(data_sizes, quicksort_times, title):
#     plt.plot(data_sizes, quicksort_times, label='Quick Sort')
#     plt.xlabel('Input Size')
#     plt.ylabel('Execution Time (seconds)')
#     plt.title(title)
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# # Test Cases for Quick Sort
# # data_sizes = [100, 1000, 10000, 100000]
# data_sizes = [500, 1000]
# # Best Case (Already Sorted Data)
# best_quicksort_times = []
# for size in data_sizes:
#     data = generate_sorted_data(size)
#     best_quicksort_times.append(measure_time(quicksort, data))

# # Average Case (Random Data)
# average_quicksort_times = []
# for size in data_sizes:
#     data = generate_random_data(size)
#     average_quicksort_times.append(measure_time(quicksort, data))

# # Worst Case (Reversed Data)
# worst_quicksort_times = []
# for size in data_sizes:
#     data = generate_reversed_data(size)
#     worst_quicksort_times.append(measure_time(quicksort, data))

# # Plot the results for all cases (Best, Average, Worst)
# plot_execution_time(data_sizes, best_quicksort_times, 'Best Case Execution Time')
# plot_execution_time(data_sizes, average_quicksort_times, 'Average Case Execution Time')
# plot_execution_time(data_sizes, worst_quicksort_times, 'Worst Case Execution Time')
# import random
# import time
# import matplotlib.pyplot as plt
# from quicksort import quicksort
# import sys

# # Increase recursion limit
# sys.setrecursionlimit(10**6)



# def generate_random_input(size):
#     return [random.randint(1, 100000000) for _ in range(size)]

# def measure_execution_time(arr):
#     start_time = time.time()
#     quicksort(arr, 0, len(arr) - 1)
#     return time.time() - start_time

# def plot_graph(sizes, times):
#     plt.plot(sizes, times)
#     plt.xlabel('Input Size')
#     plt.ylabel('Execution Time (s)')
#     plt.title('Execution Time vs Input Size (Quicksort)')
#     plt.show()

# # sizes = [100, 500, 1000, 2000, 5000]
# sizes = [250000, 500000, 1000000, 5000000]  

# quicksort_times_best = []
# quicksort_times_worst = []

# for size in sizes:
#     data = generate_random_input(size)
#     # Best case for Quicksort: already sorted
#     quicksort_times_best.append(measure_execution_time(sorted(data)))
#     # Worst case for Quicksort: reverse sorted
#     quicksort_times_worst.append(measure_execution_time(sorted(data, reverse=True)))

# plot_graph(sizes, quicksort_times_best)
# plot_graph(sizes, quicksort_times_worst)
# plt.ion()  # Enable interactive mode

import random
import time
import matplotlib.pyplot as plt
from quicksort import quicksort
import sys

# Increase recursion limit
sys.setrecursionlimit(10**6)

def generate_random_input(size):
    return [random.randint(1, 100000000) for _ in range(size)]

def measure_execution_time(arr):
    start_time = time.time()
    quicksort(arr, 0, len(arr) - 1)
    return time.time() - start_time

def plot_graph(sizes, times):
    plt.plot(sizes, times)
    if(times == quicksort_times_best):
      plt.xlabel('Input Size')
      plt.ylabel('Execution Time (s)')
      plt.title('Best Case')
      plt.show()
    else :
     plt.xlabel('Input Size')
     plt.ylabel('Execution Time (s)')
     plt.title('Worst Case')
     plt.show()



sizes = [3000,5000,7000,9000,11000,13000, 15000, 17000, 19000,21000,23000 ]  

quicksort_times_best = []
quicksort_times_worst = []

for size in sizes:
    data = generate_random_input(size)
    print("Sorting dataset size:", size)
    quicksort_times_best.append(measure_execution_time(sorted(data)))
    quicksort_times_worst.append(measure_execution_time(sorted(data, reverse=True)))
    print((sorted(data, reverse=True)))

plot_graph(sizes, quicksort_times_best)
plot_graph(sizes, quicksort_times_worst)
plt.ion()  # Enable interactive mode


