
"""
This module contains all the algorithms code with metric capturing. 
Note: For the purposes of this project, the output of the algorithms does not matter.
"""
from itertools import permutations
import functools
from perfgraph.metrics_helper import Metrics

TRIAL_COUNT = 5
metrics = Metrics()

def capture_metrics(function):
    
    @functools.wraps(function)
    def wrapper(array):
        for _ in range(TRIAL_COUNT):
            with metrics.measure(function.__name__, labels={"nsize": len(array)}):
                function(array)
        return
    return wrapper

@capture_metrics
def constant_time(input_list: list[int]):
    element = input_list[0] + 1

@capture_metrics
def logn_time(input_list: list[int]):
    """
    It contains Binary Search code for logN execution. Although BinarySearch expects the array to
    be sorted in nature, but since we don't care about the output, the array content is irrelevant
    """
    def binary_search(input_list):
        target = input_list[0]
        low, high = 0, len(input_list) - 1
        while low <= high:
            mid = (low + high) // 2
            if input_list[mid] == target:
                return mid
            elif input_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
    
    binary_search(input_list)

@capture_metrics
def linear_time(input_list: list[int]):
    for elem in input_list:
        elem + 1

@capture_metrics
def nlogn_time(input_list: list[int]):
    """
    It contains HeapSort code for NlogN execution.
    """

    def heapify(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def heap_sort(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        return arr
    
    heap_sort(input_list)

@capture_metrics
def quadratic_time(input_list: list[int]):
    for i in range(len(input_list)):
        for j in range(i+1, len(input_list)):
            i + j

@capture_metrics
def factorial_time(input_list: list[int]):
    """
    Generate all permutations of the input list.
    """
    list(permutations(input_list))