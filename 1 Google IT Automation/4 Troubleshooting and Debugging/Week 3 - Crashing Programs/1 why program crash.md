<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## System that Crash <hr/>
Usually a system crashes when it met unexpected result that the developers didn't anticipate.<br>


## System that Crash <hr/>
Say there's an invoice problem. Start with the easiest and fastest actions to check!<br>
Then you findout the problem is hardware related. <br>
Giving a random crashes, one thing to check would be `RAM`. <br>
Memory chips deteriorate over time. The computer might something, but get totally different value when reading it back.<br>

`memtest86` : Check the health of a RAM. Run this on boot. <br>
If the RAM is fine, check overheating by looking at the sensor. <br>
If that also not, check external devices like graphic card, sound card. Plug and check. :D<br>

Say you put your hard drive in the separate computer, but you get `strange caches`?<br>
This means the problem is in the drive itself, or the OS installation.<br>
`S.M.A.R.T` tools : Help detect errors and try to anticipate it.

If hard-drive isn't the problem, look into the OS. BUT is it worth it..? Reinstalling the OS might be faster and simpler.

<br>

## Understanding Crash Applications <hr/>
`Debug Logging` : Enabling this makes debug easier for most app.

On windows, you have `Process Monitor` to take a peek inside what's going on inside a process on Windows.<br>
We want to see :
- Which system calls a program is doing
- What files and dir it's trying to open
- What network connections it's trying to make and what information.

Error can also becaused of different version. You can look up your update history if you use VCS.

> To find the root cause of a crashing application ,we'll want to look at all available logs, figure out what changed, trace the system or library calls the program makes, and create the smallest possible reproduction case.

<br>

## Can't fix the program? (Workaround) <hr/>
Say you figured out the issue was caused by spesific data input format that makes the app crash.<br>
The old ones require xml, now it requires yaml. <br>
- Write a script that preprocesses the data, 

If the problem causes by incompatible external service that the app uses
- Write a server with a proxy and make sure both sides send the correct requests and responses.<br>
`Wrapper` : Function or program that provides a compatibility layer between two functions or programs, so they can work well together.<br>

Say the overall system is not compatible, check the env that the app developers recommend. 
- You can use VM or Container.

Sometimes, we can't avoid crashes! So, we want to restart the service. 
- We can deploy `WatchDog` : Process that checks wether a program is running and, when it's not, start the program again. Do this when availability > running continously.

<br>

## Internal Server Error <hr/>
Say there's an "500" error from the webserver
```shell
~$ date
~$ cd /var/low/
~$ ls -lt | head # Sort the file by the last modified date.
```
But there's nothing there!

Now we need to find information about the web server software. You can do that by finding which app listens to port 80!<br>
`netstat` : Buncho info about network, depending on the flags passed. We need sudo to run this because it acceses buncho sockets that are restricted to root.<br>
- `-n` : Only print numerical addresses instead resolving host names,
- `-l` : Only check the sockets that are listening for connection,
- `-p` : Print the process ID and name to which each socket belongs.
Since we only care about port 80, we can pipeline it to grep :80.

Great, now we know the service is running with `nginx`.<br>
Configuration in linux are stored in `/etc/`. Let's check /etc/nginx/
```shell
~$ ls -l /etc/nginx
```
We are looking for configuration related to a spesific site. Let's look at sites-enabled.<br>
We see at the bottom "uwsgi_pass 127.0.0.1:3031;". It seems that this website isn't being served directly from nginx, <br>
instead, the software is passing the control of the connections to uWSGI <br>
`uWSGI` : common solution to connect a `Web server` to programs that generate `dynamic pages`.<br>

```shell
~$ ls -l /etc/uwsgi/
```
See the apps-enabled, and we've found the configuration for out sites.<br>
This file has a lot info, about the main dir, etc... <br>
Here find the location of the `log` file. You can see the log file has 0 in length. Weird!<br>
Check the script that runs by uwsgi! There's a convenient debug code, uncomment it and restart uwsgi using :<br>
```shell
~$ sudo service uwsgi reload
```
Now access the web again, and great! We have traceback, and it said permission denied.<br>
So, the error is, you need to give access to 'www-data' for site.log file! Because it is currently owned by root.

YES WE DI Immediate Remediation. But what about the long-term remediation?<br>
We suspect that there might be wrong with the log rotate configuration. <br>
`log rotate` : Additional file so the main isn't overloaded with logs.

<br><br>

Addition : <br>
```python
@bottle # A python module to generate dynamic web pages.
```

Reading Logs in OS

<ul><li><p><a href="https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>How to find logs on Windows 10</u></a> (Digital Masters Magazine)</p></li><li><p><a href="https://www.howtogeek.com/356942/how-to-view-the-system-log-on-a-mac/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>How to view the System Log on a Mac</u></a> (How-to Geek)</p></li><li><p><a href="https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>How to check system logs on Linux</u></a> (FOSS Linux)&nbsp;</p></li></ul>

OS Diagnose Problems

<ul><li><p><a href="https://docs.microsoft.com/en-us/sysinternals/downloads/procmon" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>Process Monitor</u></a> for Windows (Microsoft)</p></li><li><p><a href="https://www.howtoforge.com/linux-strace-command/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>Linux strace command tutorial for beginners</u></a> (HowtoForge)  </p></li><li><p><a href="https://etcnotes.com/posts/system-call/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>How to trace your system calls on Mac OS</u></a> (/etc/notes)</p></li></ul>