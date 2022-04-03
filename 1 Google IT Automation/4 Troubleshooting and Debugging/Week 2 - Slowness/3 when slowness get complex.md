<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Parallelizing Operations <hr/>
`Concurrency` : Field in Compuer Sicence, dedicated on how we write programs that do operation in parallel.<br>

Our OS handles many processes. If computer has many core, the OS can pick which processes get executed on which core. <br>
All of these processes will be executing in parallel. Each of them has its own memory allocation.<br>

When you have a processs that use a lot of network I/O, then another use disk I/O, and another is CPU, they all can run pararell without interfering with each other. These processes doesn't share any memory.

If we need some shared data, we'd use threads.<br>
`Thread` : Run parallel task inside a process. <br>
We need to modify our code if we want to do thread.

In Python, we can use `Threading` or `AsyncIO` module to do parallel thread.<br>
__Be careful__, depending on the language, it might happen that all threads get executed in the same CPU processor. If you want to use more processor, you need to split the code into fully separate process.<br>
`I/O bound` :  script is mostly just waiting on input or output. It might not matter if it's executed on one processor or eight.<br>
`CPU Bound` : Bottlenecked by the CPU. script that needs to run operations in parallel using all available CPU time.<br>
`I/O Bound` : program that often leaves our CPU with little to do as it waits on data from local disk and the internet.

> When doing parallel process, we need the right balance that let our computer stay busy, <br>without starving our system for resources.

<br>

## Slowly Growing in Complexity <hr/>
Once your program grew, you need to change from csv based to SQLite!<br>
Also, you might want to use Varnish for Caching, and Load Balancer, if you decide to publish your website<br>
Use the right solution for the problem.

<br>

## Dealing with Complex Slow Systems <hr/>
![complex_system](complex_system.png)

Imagine you are dealing with this kind of complex system for e-commerce.

You need to know where your system spends most of the time.<br>
Say you are getting the web pages is pretty slow.<br>
The web server is not overloaded. Instead, most of the time is spent waiting on network calls.<br>
And when you're looking at the Database Server, it is spending a lot of time on Disk I/O.<br>
This shows problem on how the data is being accessed in the database.<br>

- Is the indexes are present in the DB? It can do it much faster if it's present. But not too much (all index need to be updated then, causes slowness).<br>

- If it's not solved by indexing, and there are too many queries for the server to reply then, you want to consider caching it AKA `memcached`. And/Or distributing the data to separate Database Server.<br> 

- When you try to see why sevice is slow, you see that the CPU on the Web Server is saturated. <br>
first step is to check if the code of the service can be improved. If it's a dynamic, we might try adding caching. Also, you can do load distribution accross more compputers. You might need to reorganize the code for this. 

<br>

## Using Threads to Make Things Go Faster <hr/>
Say you want to migrate e-commerce system, you need to update the old photo to a new one. <br>
You also need to generate the thumbnail with a script. Say it took about 2 seconds for 1000 images.<br>
It might not seems that long, but there are tens of thousands images! You want to make it as fast as possible! <br>

We can make it to go faster using parallel process. <br>
We can import future sub module, which is part of the concurrent module. This gives us simple way using Python Threads.

To be able to run things in parallel, we'll need an executor.<br>
`Executor` : Process that's in charge of distributing work among the different workers.<br>
`Futures Module` : Provides couple of executors. One for using Threads, one for using Processes.


```python
from concurrent import futures

def main():
    process_options()
    executor = futures.ThreadPoolExecutor()

    # Now submit the function that does most of the work in an executor
    executor.submit([function_name], parameter 1, parameter 2, ...)

    print("Waiting for all threads to finish ... ")
    executor.shutdown() # This function waits until all the workers in the pool are done, and only then shut down the executor.
```

With the code above, the user time is higher than the realtime. Why? <br>
Because our script is making use of the different processors available in the computer. This value shows the time used on all processors combined.

What if we use processors (ProcessPoolExecutor), instead of thread (ThreadPoolExecutor).<br>
Wow, it is taking less than a second to finish. The user time has gone up even more! Why? <br>
By using processes, we're making even more use of the CPU. <br>
The difference is caused by the way threads and processes work in Python.

`Threads` : Use bunch of safety features to avoid having two threads that try to write to the same variable. So threads may take turn writing variable for a few milliseconds.

Refference about Concorencies

https://realpython.com/python-concurrency/

https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32

<br>

### Note
`Asyncio` : Module that lets you specify parts of the code to run as separate asynchronous events.