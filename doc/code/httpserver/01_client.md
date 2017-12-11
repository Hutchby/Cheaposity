# HTTP Client

This file describes the way to implement an HTTP client that will be
compatible with the server implementation described in the HTTP Server
documentation.

The client needs to communicate with the server using only GET or POST requests.
These requests need to contain a JSON payload that will enable the request
handler of the server to call the desired method with the appropriate
behavior.

## Example:

```python
#!/usr/bin/python

import requests

if __name__ == "__main__":
    # This request is supposed to work well with the server
    post_data = {'print': 'Test message'}
    r = requests.post("http://0.0.0.0:8888", data=post_data)
    print(r.text)
```
