import random
import time
import matplotlib.pyplot as plt
from merge_sort import mergesort


def generate_random_data(size):
    """Generates a list of random integers of specified size."""
    return random.sample(range(1, size + 1), size)

def generate_sorted_data(size):
    """Generates a sorted list of integers of specified size."""
    return list(range(1, size + 1))

def generate_reversed_data(size):
    """Generates a reversed list of integers of specified size."""
    return list(range(size, 0, -1))

def measure_time(func, data):
    """Measures the execution time of a function for a given data."""
    start_time = time.time()
    func(data, 0, len(data) - 1)  
    end_time = time.time()
    return end_time - start_time

def plot_execution_time(data_sizes, mergesort_times, title):
    plt.plot(data_sizes, mergesort_times, label='Merge Sort')
    plt.xlabel('Input Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.show()

# Test Cases (Best, Average, Worst Cases)
data_sizes = [100, 1000, 10000, 100000]

# Best Case (Already Sorted Data)
mergesort_times = []
for size in data_sizes:
    data = generate_sorted_data(size)
    mergesort_times.append(measure_time(mergesort, data))

# Average Case (Random Data)
average_mergesort_times = []
for size in data_sizes:
    data = generate_random_data(size)
    average_mergesort_times.append(measure_time(mergesort, data))

# Worst Case (Reversed Data)
worst_mergesort_times = []
for size in data_sizes:
    data = generate_reversed_data(size)
    worst_mergesort_times.append(measure_time(mergesort, data))

# Plot the results for all cases (Best, Average, Worst)
plot_execution_time(data_sizes, mergesort_times, 'Best Case Execution Time')
plot_execution_time(data_sizes, average_mergesort_times, 'Average Case Execution Time')
plot_execution_time(data_sizes, worst_mergesort_times, 'Worst Case Execution Time')
