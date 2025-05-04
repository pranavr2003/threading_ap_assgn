## Multithreading in Python

1. For small input sizes, multi-threading is slower due to thread overhead. The benefits appear with larger datasets. Obviously the extent matters. Eg. In a high-spec PC, the definition of what is called a 'large dataset' varies when compared to a realatively average one.      

The `threading` module can be used to sort the left and right halves of the array concurrently in different threads. However, due to Python’s GIL, true parallelism may not be achieved with CPU-bound tasks. Otherwise the base approach is the same as with the normal merge sort.

> Sample input (same as the one inside the main func):

```py   
size = 20000
data = [random.randint(1, 100000) for _ in range(size)]
```
> Sample Output:

```sh
gitpod /workspace/threading_ap_assgn (main) $ /home/gitpod/.pyenv/shims/python /workspace/threading_ap_assgn/qn1.py
Single-threaded time: 0.0528 seconds
Multi-threaded time: 0.0647 seconds
Output Correct: True
```

A large inpyt list was deliberately given in order to try and show multi-threading in action to the extent possible.

2. Here we create separate threads to sort the left and right partitions concurrently.We use a depth limit to avoid spawning too many threads. Same as before with small and large inputs. With large datasets, performace can improve depending on the thread depth. 

> Sample input: Same as before

> Sample output:

```sh
gitpod /workspace/threading_ap_assgn (main) $ /home/gitpod/.pyenv/shims/python /workspace/threading_ap_assgn/qn2.py       
Single-threaded time: 0.0307 seconds    
Multi-threaded time: 0.0351 seconds    
Output Correct: True      
```

3. Here, `concurrent.futures.ThreadPoolExecutor` was used. It uses ThreadPoolExecutor to limit the number of concurrent downloads and prints results as each file finishes downloading. 

> Sample input:

```sh
gitpod /workspace/threading_ap_assgn (main) $ /home/gitpod/.pyenv/shims/python /workspace/threading_ap_assgn/qn3.py
Enter space-separated URLs:
https://upload.wikimedia.org/wikipedia/commons/b/b8/Chinese_vase.jpg?download
Enter space-separated URLs:
https://www.gifcen.com/wp-content/uploads/2021/04/flower-gif-1.gif
```

> Sample output:

```sh
Starting sequential download...
Downloaded: https://upload.wikimedia.org/wikipedia/commons/b/b8/Chinese_vase.jpg?download
Sequential download time: 0.16 seconds

Starting sequential download...
Downloaded: https://www.gifcen.com/wp-content/uploads/2021/04/flower-gif-1.gif
Sequential download time: 1.51 seconds

Starting concurrent download with ThreadPoolExecutor...
Downloaded: https://upload.wikimedia.org/wikipedia/commons/b/b8/Chinese_vase.jpg?download
Concurrent download time: 0.16 seconds

Starting concurrent download with ThreadPoolExecutor...
Downloaded: https://www.gifcen.com/wp-content/uploads/2021/04/flower-gif-1.gif
Concurrent download time: 1.45 
```

As we can see, the concurrent download time here on the second image `flower-gif-1` is better than the sequential dowload time on the same second image by exactly 0.06 secs.