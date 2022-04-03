<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Troubleshooting Concepts  <hr/>
We'll take a look at different approach understanding root cause of issues. For example using Binary Search to troubleshoots problem.

`Troubleshootng` : The process of identifying, analyzing, and solving any kinds of problems.

`Debugging`: The process of identifying, analyzing, and removing bugs in a system.

> Troubleshooting is fixing the system that runs the app, Debugging is fixing the app itself.

There are lot's of system that we can use to get information about system :
- tcpdump and Wireshark can troubleshoot ongoing network connections.
- ps, top, free, shows our system's resource information.
- strace to look at the system calls made by a program
- ltrace to look at library calls made by a software

`Debugger` : Follow the code line by line, inspect changing variable, interrupt when spesific condition is met.

<br>

## Problem Solving Steps  <hr/>
1. Getting Information<br>
Gather info about current state of things through documentation or other sources.<br>
What the issue is? When it happens? What the consequences are?<br>
One important resource is `Reproduction Case` : A clear description of how and when the problem appears.
2. Finding the root cause<br>
3. Performing the necessary remediation<br>
Depending on the problem, it can be an immediate remediation to fix right now, and then a medium or long-term remediation.

> It is important do DOCUMENT what we do.

<br>

## Silent Crash  <hr/>
Say we have a python program, that runs silently and has no error messages.<br>
Here we'll try to use `strace` to look system calls made by the program to the running kernel.<br>
```shell
~$ strace -o failure.strace ./our_code.py # -o is to output the file 
~$ less failure.strace # Use shift+G to move at the end of file 
```



