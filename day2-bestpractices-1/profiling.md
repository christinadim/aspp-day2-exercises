3.Profiling (answers to exercise based on results that can be found in the log files)

a. Investigate the performance of the matmult.py
Running cProfile on the given matmult.py script, we see that it takes 5.785 seconds. The tottime is max for line 2 when importing the module random.

Next step is to modify the script into matmult_edit.py so that it includes functions. Then line_profiler and memory_profiler can be used after decorating the functions with the @profile decorator.
First, we run line_profiler. The second function takes more time, especially lines 23 and 24 where the matrix multiplication is performed.
Then, we run memory_profiler. Again lines 19, 21-24 corresponding to matrix multiplication use 37.930 MiB.

b. Investigate the performance of the euler72.py
First comment out the @profile decorator and run cProfile. It takes 0.062 seconds and the tottime is max for line 22 (factorize). However, it is a very efficient scirpt.
Then while using the decorator, we run line_profiler. The third function takes more time than the other two, especially for line 52 where the factorize function is used.
Running the memory_profiler, we see that all lines take the same memory usage, 35.676 MiB.

c. Improve the performance of the matmult.py
As stated before, the script was modified to include functions. Running cProfile on the edited script we see that it takes 3.931 seconds, compared to 5.785 seconds which took in the beginning. This is still an improvement even without using NumPy.

-----------------
All the above are results of profiling from the command line. Next, I tried profiling using interactive python (jupyter notebook). Personally, I found it easier to do it in jupyter, however I noticed some differences in the numbers. For example, the same lines took longer time and bigger memory. Results can be found in profiling_jupyter.ipynb
