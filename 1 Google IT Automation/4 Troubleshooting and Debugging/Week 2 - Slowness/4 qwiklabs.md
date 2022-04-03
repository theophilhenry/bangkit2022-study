`rsync`(remote sync) is a utility for efficiently transferring and synchronizing files between a computer and an external hard drive and across networked computers by comparing the modification time and size of files. One of the important features of rsync is that it works on the delta transfer algorithm, which means it'll only sync or copy the changes from the source to the destination instead of copying the whole file. This ultimately reduces the amount of data sent over the network.

```shell
~$ rsync [Options] [Source-Files-Dir] [Destination]
```
https://www.linuxtechi.com/rsync-command-examples-linux/

### multisync.py
```python
#!/usr/bin/env python3
from multiprocessing import Pool
def run(task):
  # Do something with task here
    print("Handling {}".format(task))
if __name__ == "__main__":
  tasks = ['task1', 'task2', 'task3']
  # Create a pool of specific number of CPUs
  p = Pool(len(tasks))
  # Start each task within the pool
  p.map(run, tasks)
```

### dailysync.py
```python
#!/usr/bin/env python
import subprocess
src = "/data/prod/"
dest = "/data/prod_backup/"
subprocess.call(["rsync", "-arq", src, dest])
```

### Updated dailysync.py
```python

#!/usr/bin/env python
import subprocess
import os
from multiprocessing import Pool

src = "/data/prod/"
dest = "/data/prod_backup/"

def run(file):
  subprocess.call(["rsync", "-arq", os.getenv("HOME") + src + file, os.getenv("HOME") + dest])
  print("Processing {}".format(os.getenv("HOME") + src + file))

list_dir = os.listdir('./data/prod')
print(list_dir)
pool = Pool(len(list_dir))
pool.map(run, list_dir)
```