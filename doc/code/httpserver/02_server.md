# Request Handler

The request handler provides the developper of the HTTP Server with a generic
way of implementing functionalities by calling appropriates methods based on
the JSON payload contained in the requests.

# HTTP Server

In this repository can be found an example server implementation in
server_base.py.
To add functionalities to the server and enable it to process correct JSON
payloads sent by a compatible client (see the HTTP Client documentation:
client.md), one need to implement **do_GET_method()** or **do_POST_method()**.
The data of the payload will be passed to the method through the kwargs
dictionnary with the key "data" and can be accessed with:

```python
def do_POST_method(self, *args, **kwargs):
  payload_data = kwargs['data']
```

## Example

If the client sends this json payload through a POST method:

```json
{'print': 'Test message'}
```

The request handler of the server will call the method **do_POST_print()**
with **kwargs['data'] = 'Test message'**.
