<style>hr{opacity: 20%; height: 1px!important; margin-bottom:0px!important</style>

## Python Requests Library <hr/>
Easy to write program that send and receive HTTP.
```python
import requests
response = requests.get('https://www.google.com') # returns requests.Response
print(response.text[:300]) # Print the first 300 words
```

You can look the first bytes of raw message
```python
>>> response = requests.get('https://www.google.com', stream=True)
>>> print(response.raw.read()[:100])
b'\x1f\x8b\x08\x00\x00\x00\x00\x00\x02\xff\xc5Z\xdbz\x9b\xc8\x96\xbe\xcfS`\xf2\xb5-\xc6X\x02$t\xc28\xe3v\xdc\xdd\xee\xce\xa9\xb7\xdd;\xe9\x9d\xce\xf6W@\t\x88\x11`@>D\xd6\x9b\xce\xe5<\xc3\\\xcd\xc5\xfc\xab8\x08\xc9Nz\x1f.&\x8e1U\xb5j\xd5:\xfc\xb5jU\x15\x87;^\xe2\x16\xf7)\x97\x82b\x1e\x1d\x1d\xd2S'
```
The responses was compressed with `gzip`. So it had to be decompressed, but Requests library handles it.

The requests.Response object also contains the exact request that was created for us. 

```python
# Check the header to see Requests Module told the web server that it's was okay to compress the content
>>> response.request.headers['Accept-Encoding']
'gzip, deflate'
# Then the server told us that the content had actually been compressed
>>> response.headers['Content-Encoding']
'gzip'
```

<br>

## Python Requests Operations <hr/>
```python
>>> response.ok # Returns True/False
>>> response.status_code # Returns Status Code (200/404)
>>> response.request.body # Get the body attr to see GET/POST parameters

>>> response = requests.get(url)
>>> response.raise_for_status() # Raise an error, if the Request Failed
```

<br>

## GET and POST Methods <hr/>
### GET parameters in Python
```python
>>> p = {"search": "grey kitten",
...      "max_results": 15}
>>> response = requests.get("https://example.com/path/to/api", params=p)
>>> response.request.url
'https://example.com/path/to/api?search=grey+kitten&max_results=15'
```
### POST parameters in Python
```python
>>> p = {"description": "white kitten",
...      "name": "Snowball",
...      "age_months": 6}
>>> response = requests.post("https://example.com/path/to/api", data=p)
```

It is so common to use `JSON` as a parameter, so Requests module can convert directly for us.
```python
>>> response = requests.post("https://example.com/path/to/api", json=p)
>>> response.request.url
'https://example.com/path/to/api'
>>> response.request.body
b'{"description": "white kitten", "name": "Snowball", "age_months": 6}' 
```
