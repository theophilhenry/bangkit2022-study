<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Accesing Invalid Memory <hr/>
Common reason for crashes is when system trying to access `invalid memory`.<br>
Each `processes` asks a chunk of `memory` from the `OS`.<br>

The OS keeps `mapping table`, of which process assigned to which portion of the memory. <br>
They weren't allowed to access the other memory.<br>
> Accessing `invalid memory` means that the process tried to access a portion of the system's memory that wasn't assigned to it.

### How does it happens?<br>
Programming errors might lead to it. When this happens, the OS will raise an error like :<br>
- `Segmentation Fault` or `General Protection Fault` : Happens with low-level languages (C/C++). Where the programmers need to take care of requesting the memory that the program is going to use, and then releasing it.<br>

    `Pointers` : Variables that store memory adddresses. It is mutable like other variables.<br>
    So, if pointer is set to a value outside of the valid memory range for that process, this causes crash.

Common programming errors that leads to Segfault :
- Forgeting to initialize variable
- Trying to access element list outside of the valid range
- Trying to access the memory after releasing it
- Trying to write more data than requested portion of memory can hold

How to avoid common mistakes above? Use `debugger`!<br>
If that's not enough, you'll need your program compiled with `debugging symbols`.<br>
It will give more information on top of the binary code, like the name of the variables, and functions being used. These name usually stripped to make the code smaller.

You can `download` the `debugging symbols` from the provider of the software if they're available.<br>

Linux Distributions like `Debian` / `Ubuntu` ships separate packages with debugging symbols. <br>

### Debugging Symbols Workcycle
Debug segfault app? Download `debugging symbol` for that app, attach `debugger`, see where the fault occurs. If the library error, you need to download debugging symbol for that library. It is repetitive task. 

`Microsoft compilers` can generate debugging symbols in a `PDB` file. Some windows software providers let user download PDB files correspond to their binaries to let them properly debug failures.

### Understand the problems related to Handling Invalid Memory
`Valgrid` : tells us the code is doing invalid operations, no matter if it crashes or not. It is on Linux/Mac OS.

`Dr. Memory` : Similiar tools to Valgrind, but available on Windows and Linux.

<br>

## Unhandled Errors and Exceptions <hr/>
Handling memory is hard, that's why Java, Python, Ruby do it for us.<br>
When these language come accross unexpected condition, it triggers errors/exceptions.<br>

The program will outputs the line that error, and the traceback.<br>
`Traceback` : The line of the different functions that were being executed when the problem happened.

Sometimes when Traceback isn't enough, you can use `PBD interactive debugger`.<br>
It can execute line one-by-one and see how variable value changes.

`Printf debugging` : Display the error by printing the var, or other things.<br>
Let's take printf debugging to another level!<br>
You easily enabled/disabled print with `logging` module. <br>
You can either pick :
- All Debug Messages
- Info Only
- Warning Only
- Error Only

<br>

## Fixing Someone Else's Code <hr/>
- Starts with reading the documentation.
- Write the comments yourself to take notes.
- Running test
- Add the test ourselves
- Trace the error from function to function. Don't read the whole code.

<br>

## Debugging a Segmentation Fault (C app) <hr/>
When debugging app crashes like this, it is useful to have a `core file`.<br>
`Core File` : Store all the information related to the crash so that we or someone else can debug what's going on.<br>
We can tell the OS to generate those Core Files by running 
```shell
~$ ulimit -c unlimited # We want core files of any size.
~$ ./example # We can try running our program again
Segmentation fault (core dumped)
~$ ls -l core
```
This file contains all information of what was going on with the program when it crashed. We can pass it to `gdb` debugger
```shell
~$ gdb -c core ./example # "example" to tell it where the executable that crashed is located
.. outputs ..
(gdb) backtrace
#0 I was called last
#1 I am the one who called 0
#2 I m the one who called 1
(gdb) up
More details of #1
(gdb) list

```
`backtrace` : See from top to bottom,

`up` : move to the calling function in the backtrace, checkout the line in the "#1" function that causes the crash.

`list` : Shows the line around the current one. For example around #1. 

`print i` : Print the variables i, when the programs crashes, this is the value of i. <br>
`0x7fffcef4e32c` ? This is hexadecimal numbers to show addresses in memory where data is stored. <br>
`0x0` is a `NULL` pointer. So if it points to 0, it means it points to invalid memory addresses. <br>
With that our program could have `off-by-one` error.

<br>

## Debugging Python Crash <hr/>
```shell
~$ pdb3 update_products.py new_products.csv
-> import argparse # First line of our script
(pdb)
```
`next` : run one-by-one
`continue` : continue the program until it finishes or crashes

We find that there's something in our Dictionary<br>
('\ufeffproduct_code', 'NAM-101'), instead of 'product_code'. What is that?<br>
It represent Byte Order Mark `BOM` : Used in UTF-16 to tell the difference between file stored using Little-endian and Big-endian. <br>
Since our file is in UTF-8, no need for BOM! How to fix it?<br>
`utf-8-sig` : Special value that we can set as the encoding parameter of the open function. Settng this encoding, means python will get rid of BOM. 

There are a ton more debugging features like setting
- `breakpoints` : Run until certain line of codes , 
- `watchpoints` : Run until Variables/Expressions changes.

<br>

### Resources for Debugging Crashes

Check out the following links for more information :

<ul><li><p><a href="https://realpython.com/python-concurrency/" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://realpython.com/python-concurrency/</u></a></p></li><li><p><a href="https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://hackernoon.com/threaded-asynchronous-magic-and-how-to-wield-it-bba9ed602c32</u></a></p></li><li><p><a href="https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://stackoverflow.com/questions/33047452/definitive-list-of-common-reasons-for-segmentation-faults</u></a></p></li><li><p><a href="https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/debugging-segmentation-faults" title="Debugging Segmentation Faults" target="_blank" rel="noopener nofollow" aria-label="Debugging Segmentation Faults">https://sites.google.com/a/case.edu/hpcc/home/important-notes-for-new-users/debugging-segmentation-faults</a></p></li></ul>

Readable Python code on GitHub : 

<ul><li><p><a href="https://github.com/fogleman/Minecraft" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://github.com/fogleman/Minecraft</u></a></p></li><li><p><a href="https://github.com/cherrypy/cherrypy" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://github.com/cherrypy/cherrypy</u></a></p></li><li><p><a href="https://github.com/pallets/flask" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://github.com/pallets/flask</u></a></p></li><li><p><a href="https://github.com/tornadoweb/tornado" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://github.com/tornadoweb/tornado</u></a></p></li><li><p><a href="https://github.com/gleitz/howdoi" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://github.com/gleitz/howdoi</u></a></p></li><li><p><a href="https://github.com/bottlepy/bottle/blob/master/bottle.py" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://github.com/bottlepy/bottle/blob/master/bottle.py</u></a></p></li><li><p><a href="https://github.com/sqlalchemy/sqlalchemy" title="" target="_blank" rel="noopener nofollow" aria-label=""><u>https://github.com/sqlalchemy/sqlalchemy</u></a></p></li></ul>
