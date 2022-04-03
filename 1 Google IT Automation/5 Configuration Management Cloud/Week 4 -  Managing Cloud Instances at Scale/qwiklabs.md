`systemctl` is a utility for controlling the systemd system and service manager. It comes with a long list of options for different functionality, including starting, stopping, restarting, or reloading a daemon.

This is the erorr message when we tried to restart apache2
```shell
Job for apache2.service failed because the control process exited with error code.
See "systemctl status apache2.service" and "journalctl -xe" for details.
```
The output of status said that port :80 is currently not available.

To find which processes are listening on which ports, we'll be using the `netstat` command, which returns network-related information. Here, we'll be using a combination of flags along with the `netstat` command to check which process is using a particular port:

```shell
~$ sudo netstat -nlp
```
You see PID 2190 which is python3 script uses :80.
Find that service using
```shell
~$ ps -ax | grep python3
```
It returns the location of the file which is `cat /usr/local/bin/jimmytest.py`
Check the file, then kill it using kill 2190

Then, 
```shell
~$ ps -ax | grep python3 # Outputs jimmy again!
~$ sudo systemctl --type=service | grep jimmy # Check all the available jimmy service!
```
