import threading
import time
import random

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

class MergeSortThread(threading.Thread):
    def __init__(self, arr, depth=0, max_depth=2):
        super().__init__()
        self.arr = arr
        self.result = None
        self.depth = depth
        self.max_depth = max_depth

    def run(self):
        if len(self.arr) <= 1:
            self.result = self.arr
        else:
            mid = len(self.arr) // 2
            if self.depth < self.max_depth:
                left_thread = MergeSortThread(self.arr[:mid], self.depth + 1, self.max_depth)
                right_thread = MergeSortThread(self.arr[mid:], self.depth + 1, self.max_depth)
                left_thread.start()
                right_thread.start()
                left_thread.join()
                right_thread.join()
                self.result = merge(left_thread.result, right_thread.result)
            else:
                left = merge_sort(self.arr[:mid])
                right = merge_sort(self.arr[mid:])
                self.result = merge(left, right)

def threaded_merge_sort(arr):
    thread = MergeSortThread(arr)
    thread.start()
    thread.join()
    return thread.result

if __name__ == "__main__":
    size = 20000
    data = [random.randint(1, 100000) for _ in range(size)]

    # single-threaded
    start = time.time()
    sorted_single = merge_sort(data)
    print(f"Single-threaded time: {time.time() - start:.4f} seconds")

    # multi-threaded
    start = time.time()
    sorted_multi = threaded_merge_sort(data)
    print(f"Multi-threaded time: {time.time() - start:.4f} seconds")

    print("Output Correct:", sorted_single == sorted_multi)
