import http.client



conn = http.client.HTTPConnection('localhost', 8080)

conn.request("POST", "/", "toto\n")
response = conn.getresponse()
if response:
    print(response.status, response.reason)
#conn.request("GET", "/")
