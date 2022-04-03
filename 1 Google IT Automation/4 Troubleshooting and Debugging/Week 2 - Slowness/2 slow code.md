<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Writing Efficient Code <hr/>
We want our code to perform well!<br>

> We should always writes clear code that does what it should, <br>
> and only try to make it faster if we realize it's not fast enough.

Trying to optimize every second out of a script is probably not worth your time.<br>
If we want our code to finish faster, we need to make our computer do less work. <br>
Simple things like :
- Storing data that was already calculated, 
- Avoid calculating data again,
- Using the right data structure for the problem,
- Reorganizing the code so the computer can stay busy, while waiting for infrmation from slow sources,
    
### Tools to view resource usage for script
`profiles` : A tool that measures the resources that our code is using, giving us a better understanding of what's going on.<br>
It help us to see how the memory is allocated and how the time spent.<br>

Ex : `gprof` : C | `cProfile` : Python <br>
Also we can see which function are called by our program, how many times each function was called, and how much time our program spent on each of them.<br>

We also want to avoid `expensive action` that takes a long time to complete. For example : <br>
- parsing a file,
- reading data overt the network,
- and iterating through a whole list.

<br>

## Using the Right Data Structures <hr/>
We want to understand the performance of data structure under different conditions.<br>
List, Dict, Set, Tuples, which is faster?<br>

List is good, but finding value is slow<br>
Dict is better for finding spesific value, because you have the key.<br>
Then, double check if you really need a copy of a list vice versa.

<br>

## Expensive Loops <hr/>
How to deal with it?<br>
- See what operations that you can do just once outside the loop.<br>
- Remember to break out of loop when item you are looking for has founded.<br>

<br>

## Keeping Local Results <hr/>
What if parsing file is still slow even we do it outside the loop?<br>
If a data get access reguraly, it is common to create a local cache. <br>


But it's tricky. Wee need to think how often should we update the cache, and what happens if the data in the cache is out of date?<br>
- If we're looking from a long-term stats, once-a-day is fine.
- If the data is super important right NOW, either we can't use a cache, or it has to be short-lived. Like checking computer health, product stock, seing username exists.<br>

We need to know, how often the data change, how critical of using the latest data, how frequently the program will be executed. <br>
Once-per-minute is okay! 

<br>

## Slow Script with Expensive Loop <hr/>
`time` : Measure the script speed.
- Real : The amount of actual time that it took to execute the command (Wall-clock time).
- User : The time spent doing operations in the user space.
- Sys : The time spent doing system-level operations.

User + Sys won't be always like real because the computer might be busy with other processes.<br>
Let's use profiler to see resources use in pyrhon. <br>
```shell
~$ pprofile -f callgrind -o [name.out] [python_file] # -f use call_grind format, -o tell store output in a file
```
`kcachegrind` : See via GUI for callgrind file.<br>
We can see the times a function is called, and how long it spend there.<br>
Turns out, we need to break the loop, and better to use dict.
