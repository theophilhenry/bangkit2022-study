<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Managing Resources <hr/>
Sometimes the problem we face isn't that something `doesn't work`, but that it doesn't work `as well as it should`. This usually comes down to not making the best use of available resources.


## Memory Leaks and How to Prevent Them <hr/>
A chunk of `memory` that's no longer needed is `not released`<br>
When this happen, the program might start failing, and terminate processes to free up some memory (causes unrelated program to crash)<br>

Java, Python, Go sometimes can go wrong too. How those language works?
1. Request nescessary memory
2. Run a `Garbage Collector` : Freeing the memory that's no longer in use<br>
When you create a dict inside a function, and that function returns another var, that dict will be released.<br>
But, when it returns that dict, you could see the same effects of memory leak.

If you're OS that causes that memory leak, you need to full restart.

`Memory Profiler` : Figure out how memory is being used.<br>
```shell
~$ python3 -m memory_profiler script.py
```
- First column : Required memory when each line gets executed
- Second column : Increases in memory for each spesific line

<br>

## Managing Disk Space <hr/>
Programs may need disk space for diferent reasons :
- Installed binaries and libraries
- Data stored by the app
- Cached info
- Logs
- Temp files
- Backups

Just remember to delete overly generated logs.<br>
Deleted files can still take space because processes read/write it first when opening ,and actually delete it as it closes. So if the program is big, it might end up using a lot of space.

<br>

## Network Saturation <hr/>
Two most important factors of networking :
1. `Latency` : Delay between sending byte of data from one point, and receiving it on the other. This values affected by distance.
2. `Bandwidth` : How much data can be sent/retrieved in a second. Affected by the data capacity of the connection. 

`iftop` : Shows how much data each active connection is sending over the network. 

You can resrict how much each connection takes by using `Traffic Shaping` : Way of marking data packets sent over the network with different priorities. 

<br>

## Dealing with Memory Leaks <hr/>
We will run app with uxterm, added with <br>
`Scroll Buffer` : Feature that lets us scroll up and see the things that we executed and their output.
```shell
~$ od -cx /dev/urandom # Random hex and number
```
You can use `top` to check, and press `Shift + M` to order by memory.

About top,
- `RES` : Dynamic memory preserved for the spesific process
- `SHR` : Memory that's shared accross processes
- `VIRT` : lists all the virtual memory allocated for each process (process spesific memory, shared memory, and other shared resources that was stored on disk but maps into the memory of the process). 

`VIRT` is fine when high, `RES` is problem if it's high. 

<br>

### Example : 
```python
@profiler # This is called Decorator, it is to tell we want to analyze the memory consumption of it.
def main():
```
`Decorator` : Add extra behavior to functions without having to modify the code.

<br>

## More about Managing Resources <hr>

<ul><li><p><a href="https://realpython.com/python-concurrency/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://realpython.com/python-concurrency/</u></a></p></li><li><p><a href="https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32</u></a></p></li><li><p><a href="https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python</u></a></p></li><li><p><a href="https://www.linuxjournal.com/content/troubleshooting-network-problems" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://www.linuxjournal.com/content/troubleshooting-network-problems</u></a></p></li></ul>

Note :  `guppy module` :  tools to profile an entire Python application
