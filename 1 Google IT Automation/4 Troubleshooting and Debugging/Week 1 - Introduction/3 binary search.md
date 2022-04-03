<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Binary Search <hr/>
First we need to know Linear Search, it is searching from top to bottom, for BIG data slow process isn't it?<br>
Binary Search, we can do half of the list that you want to search. But the list must be sorted!<br>
For searching just one element.. well just do linear instead bothering sorting the data first (if it haven't).

```python
def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1
```

<br>

## Applying Binary Search in Troubleshooting <hr/>
`Bisecting` : Dividing the problem by finding it half by half.
Say there's 1 in 9 files that causes crash. Find half, half, half, until 1 script that causes it founded.
`bisect` : There's this command on git to let us find bug in version control.

Example :<br>
We have a program in CSV file, it will import it to the database. <br>
What if one of the users tells us that the file they're trying to import fails. <br>
First we try to reproduce it, using a test server. If also failed, <br>
then check the lines to see how long the contact are with wc -l contacts.csv<br>
There's 100 contact list, which is a lot. We can try to halfen up the contact to see which contact are faulty. <br>
We can use head and tail to get the first half or last half. And pass it to the tails.
```shell
~$ head -50 contracts.csv | tail -25 | tail -12 | ... | ./import.py --server test
```

