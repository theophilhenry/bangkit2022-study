<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## API <hr/>
API help different pieces of software talk to each other

An API is sort of like a `promise`. Even if the library's `internal` code `changes`, you expect the function to keep accepting the same parameters and returning the `same` `results`. That provides a `stable` interface to write your code with.

Any new extreme update must follow these rules https://semver.org/#summary

API names are descriptive, and follow patterns+naming conventions.

Python Imaging Library `PIL` : Transform and Converting Images<br>
The original hasn't been updated since 2009. But new fork called Pillow support Py3.<br>
You need to install pillow first, and import it as PIL.

```python
from PIL import Image
im = Image.open("bride.jpg")
im.rotate(45).show()
```

<br>

### Using PIL

we wanted to resize an image and save the new image with a new name,
```python
from PIL import Image
im = Image("example.jpg")
new_im = im.resize((640,480))
# new_im = im.rotate(90)
new_im.save("example_resized.jpg")

# im = Image("example.jpg")
# im.rotate(180).resize((640,480)).save("flipped_and_resized.jpg")
```

