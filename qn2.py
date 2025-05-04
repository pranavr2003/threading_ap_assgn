import threading
import time
import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    lesser = [x for x in arr[1:] if x < pivot]
    greater_equal = [x for x in arr[1:] if x >= pivot]
    return quicksort(lesser) + [pivot] + quicksort(greater_equal)

class QuickSortThread(threading.Thread):
    def __init__(self, arr, depth=0, max_depth=2):
        super().__init__()
        self.arr = arr
        self.result = None
        self.depth = depth
        self.max_depth = max_depth

    def run(self):
        if len(self.arr) <= 1:
            self.result = self.arr
            return

        pivot = self.arr[0]
        lesser = [x for x in self.arr[1:] if x < pivot]
        greater_equal = [x for x in self.arr[1:] if x >= pivot]

        if self.depth < self.max_depth:
            left_thread = QuickSortThread(lesser, self.depth + 1, self.max_depth)
            right_thread = QuickSortThread(greater_equal, self.depth + 1, self.max_depth)
            left_thread.start()
            right_thread.start()
            left_thread.join()
            right_thread.join()
            self.result = left_thread.result + [pivot] + right_thread.result
        else:
            left = quicksort(lesser)
            right = quicksort(greater_equal)
            self.result = left + [pivot] + right

def threaded_quicksort(arr):
    thread = QuickSortThread(arr)
    thread.start()
    thread.join()
    return thread.result

if __name__ == "__main__":
    size = 20000
    data = [random.randint(1, 100000) for _ in range(size)]

    # Single-threaded quicksort
    start = time.time()
    sorted_single = quicksort(data)
    print(f"Single-threaded time: {time.time() - start:.4f} seconds")

    # Multi-threaded quicksort
    start = time.time()
    sorted_multi = threaded_quicksort(data)
    print(f"Multi-threaded time: {time.time() - start:.4f} seconds")

    print("Output Correct:", sorted_single == sorted_multi)
