<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Definition <hr/>
`web app` : app you can interact over HTTP

Browser send HTTP req -> web serverr. Web server passes -> web app decide which info to show. 

Web app also have API known as `web service`. Part of program that listen for API call is `API endpoint`

<br>

## Data Seralization <hr/>
What to send?

`Data Serialization` : Process taking an in-memory dat astructure, turning it into something that can be stored on a disk, or transmitted accross network. It can be read and turn back into an object by using deserialization.

Using this kind of data structure (instead of CSV), let's one person have many phones. 
```python
people = [
    {
        "name": "Sabrina Green",
        "username": "sgreen",
        "phone": {
            "office": "802-867-5309",
            "cell": "802-867-5310"
        },
        "department": "IT Infrastructure",
        "role": "Systems Administrator"
    },
    {
        "name": "Eli Jones",
        "username": "ejones",
        "phone": {
            "office": "684-348-1127"
        },
        "department": "IT Infrastructure",
        "role": "IT Specialist"
    },
]
```

<br>

## Data Serialization Format <hr>
There are lots of way to serialize data. Here are the most common ones :
- `JSON`

```python
import json

with open('people.json', 'w') as people_json:
    json.dump(people, people_json, indent=2) # Writes our people dict to a people_json file
```

```JSON
[
  {
    "name": "Sabrina Green",
    "username": "sgreen",
    "phone": {
      "office": "802-867-5309",
      "cell": "802-867-5310"
    },
    "department": "IT Infrastructure",
    "role": "Systems Administrator"
  },
  {
    "name": "Eli Jones",
    "username": "ejones",
    "phone": {
      "office": "684-348-1127"
    },
    "department": "IT Infrastructure",
    "role": "IT Specialist"
  },
]

```

- `YAML`

```python
import yaml

with open('people.yaml', 'w') as people_yaml:
    yaml.safe_dump(people, people_yaml)
```

```YAML
- department: IT Infrastructure
  name: Sabrina Green
  phone:
    cell: 802-867-5310
    office: 802-867-5309
  role: Systems Administrator
  username: sgreen
- department: IT Infrastructure
  name: Eli Jones
  phone:
    office: 684-348-1127
  role: IT Specialist
  username: ejones
```

### YAML VS JSON
SON is used frequently for transmitting data between web services, while YAML is used the most for storing configuration values.

We also have Python pickle, Protocol Buffers, or the eXtensible Markup Language (XML).

<br>

## More about JSON <hr>
Type : "string", 20, {"object", "value"}, ["array"]

You can use json.dumps, that will return a string, instead of writing directly to a file.
```python
people_json = json.dumps(people)
print(people_json)
```

- `json.load()`, deserializes JSON file to Python objects. 
- `json.loads()` parses string instead of file.

```python
>>> import json
>>> with open('people.json', 'r') as people_json:
...     people = json.load(people_json)
```