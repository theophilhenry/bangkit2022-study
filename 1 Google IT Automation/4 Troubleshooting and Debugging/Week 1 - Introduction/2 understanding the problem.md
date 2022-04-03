<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Question to ASK  <hr/>
- What were you trying to do?
- What steps did you follow?
- What was the expected result?
- What was the actual result?

### Checking system resources
`top` : See which processes use the most CPU. The load average says 40. <br>
Load average : how much time a processur is busy in a given minute. 1 means it's busy for a whole minute.<br>
Normally, this amount shouldn't be above the amout of processors in the computer (overloaded).<br>


You also see most of the CPU Time spent in waiting. This means processes are stuck waiting for the OS to return from system calls.<br>
This usually happens when the processes get stuck gathering data from the hard drive or the network.

You finally see that the problem is the backup system keeps updating. use KILL -STOP, to stop it!!

<br>

## Creating a Reproduction Case  <hr/>
A way to verify if the problem is present or not. Reproduce the bug!


Sometimes the reproduction is complex. 
It could be the environment or app version.

How to read system logs
- Linux : 
    - /var/log/syslog : System error
    -x.session-errors : User spesific error 
- MacOS : 
    - /Library/Logs : System error
- Windows :
    - Event Viewer : Go through the event logs

<br>

## Finding the Root Cause  <hr/>
Sometimes when you know the reproduction case, it is not always the root cause of the problem.
> Understanding the root cause is important for long-term remediation

To find a root problem you need a hypotesis, if not true, then do another!

Whenever possible, check that hypothesis in a tst environment, 
<br>instead of the production environment that our user are working with.<br>
Even though it might seem like the users environment fault, we should always check first in test env!

Maybe there's a backup error, but what causes it? You can do the command below :

### Checking Input Output (I/O)
`iotop` : check if too much disk I/O usage, see which processes are using the most I/O.<br>
`iostat/vmstat` : shows statistic of thje I/O operations and virtual memory operations.<br>
`ionice` : if the processes generaate too much I/O, to make out backup system reduce its prority to access the dist, and let the services use it too.

### Checking the Network
`iftop` : Current traffic on the network interface. <br>
`rsync` : Backing up data, includes -bwlimit to limit the bandwidth.<br>
`Trickle` : Program to limit the bandhwidth that is being used.

### Checking the Compression Algorithms is too Aggresive
`nice` : Reduce the proirity of process and accessing the CPU.

<br>

## Dealing with Intermittent Issues  <hr/>
Dealing with problem that happened only occasionally.<br>
To deal with that, you need to be more involved. Understands when it happens and not.<br>
If we maintain the code, modify it to log information related to the problem.<br>
Depending on the problem, you might need to look into these :
- The load on the computer
- The processes running at the same time
- The usage of the network
- ... so on

`Heisenbug` : A type of bug that dissapears when we debug -_-
> __Observer Effect__ <br>
> Observing a phenomenon, alters the phenomenon<br>
> \- Werner Heisenberg \-

This bugs usually point to bad resource management. <br>
Maybe the memory was wrongly allocated, network connection weren't correctly initialized, or file weren't properly handled.

`Restart` : Type of bug that works on restart.<br>
Restarting can fix bug! It means cleaning all alocated memory, deleting temporary files, reset the state, re-establish network connections, closing open files, and more!<br>
But.. if you find that's the reason, do a long-term remediation!<br>

<br>


