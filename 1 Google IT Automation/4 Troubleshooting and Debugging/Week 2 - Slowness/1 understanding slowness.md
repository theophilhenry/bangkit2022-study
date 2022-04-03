<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Slowness <hr/>
Slow is a relative term. Modern computer is more capable than decades ago.<br>
Closing tabs will free CPU, RAM and Memory.<br>
Maybe our computer is exhausted, it could be IO, Graphic Card, and others.<br>
`top` : Processes that using te most CPU time.<br>

But what about in MacOS?<br>
`Activity Monitor` : See what's using the most CPU, memory, energy, disk, or network.

Windows?<br>
`Resource Monitor` & `Performance Monitor`  : Analyze what's going on with different resources.

We can check those to monitor which causes a bottleneck and why.

<br>

## How Computers use Resources <hr/>
When an app access some data, the time spent retrieving that data, will depend where it's located.<br>
- If it's a variable that is being used in a function, the data is in CPU's internal memory, this can be retrieved really fast.<br>
- If the data related to our current running program, but not currently executing function, it would be likely on a RAM. This can be really fast aswell<br>
- If the data is in a file, our program will need to read it from disk, which is much slower than RAM. 
- If the data is on a network, it is much slower than file!

So, if you have a data on a network, you want want to do read once stored on a disk, then read it from disk!
Also, if you reading file regurarly in disk, you might want to put it directly into the proces memory.<br>
In other words, cache!

`Cache` : Stores data in a form that's faster to access than its original form.<br>
-  A web proxy is a form of cache. It stores wesites, images, or videos accessed often by users behind the proxy.<br>
- DNS also usually implement a local cache for the websites they resolve. 
- OS also use cache, A.K.A Cached in Memory to keep as much information as possible in RAM. Like the contents of files or library that are used often.<br>
Btw, what happen if you run out of RAM? 
    - OS will remove from RAM anything that's cached that is not necessary.
    - Still not enough RAM? the OS will put the parts of the memory that aren't currently in use onto hard drive in a space called `swap`.<br>
    Swap is slower than RAM, so when requested app want read/write, it will take long to loads.
    Swap happens maybe because of `Memory Leak` : Memory which is no longer needed is not getting released.

<br>

## Possible Casues of Slowness <hr/>
> When figuring out WHY computer is slow, first we need to know WHEN computer is slow

If it's slow when starting up, then probably there's too much app that gets booted up.<br>
If reboot do fine, it means there's a program keeping some state while running, keeping the computer to slow down.<br>

<br>

## Example : Slow Web Server <hr/>
`ab` : Apache Benchmark to see how slow site loads.
```shell
~$ ab -n 500 site.example.com/ # -n : Average timing of 500 request
```
Say you got 150ms on average.

Check on the web server : <br>
Appereantly there's a ffmpeg processes running for video encoding.<br>
How to fix it?<br>
We can change the `process priorities` in Linux. Typical range `0-19`, default 0. The lower the number, the higher the priority.
```shell
~$ nice # Starting a process with different priority
~$ renice [new_priority] [PID] # Changing priority of a process that's already running
```
We can do renice to each ffmpeg, but we can automate it!
`pidof`:  Recieves process name, and returns all the PIDs that have that name. 

Appereantly, it still takes too much CPU!! What can we do now?<br>
We need to run them on one after the other instead of running them at the same time (paralel). <br>
To do that, we need to find out how these processes got started. <br>
We can do that with
```shell
~$ ps ax | less # Then search with /ffmpeg
```
Say we know these ffmpeg processes are converting from webm to mp4. But where's the file are in our hard drive.
```shell
~$ locate static/001.webm # Output is /srv/deploy_videos/static/001.webm
```
Let's check the dir, and see which command uses ffmpeg
```shell
~$ grep ffmpeg * # We see deploy.sh file are using ffmpeg
```
`Daemonize` : Runs each program separately as if it were a daemon.<br>
Now we can delete that daemonize, and kill the current running processes.<br>
BUT STOP, don't kill it because the convertion will be incomplete. So we need to do 
```shell
~$ killall -STOP ffmpeg # Sends a stop signal but doesn't kill the processes completely
```
Now we want to continue it but 1 by 1 by sending -CONT command
```shell
~$ for pid in  $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done
```

<br>

### Monitoring Tools <hr>


https://docs.microsoft.com/en-us/sysinternals/downloads/procmon 

http://www.brendangregg.com/linuxperf.html

http://brendangregg.com/usemethod.html

Activity Monitor in Mac : https://support.apple.com/guide/activity-monitor/welcome/mac

Performance Monitor on Windows : https://www.windowscentral.com/how-use-performance-monitor-windows-10

https://www.digitalcitizen.life/how-use-resource-monitor-windows-7

https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer

https://en.wikipedia.org/wiki/Cache_(computing)

https://www.reddit.com/r/linux/comments/d7hx2c/why_nice_levels_are_a_placebo_and_have_been_for_a/

