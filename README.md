## Playground thing


```
.
----------------------------------------------------------------------
Ran 1 test in 1.676s

OK
➜  shopify_rest pipenv run python test_client.py
Response(code=200, body="b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {}, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.7", \n    "X-Amzn-Trace-Id": "Root=1-5e7c766e-3f7cce687e271270984d88a1"\n  }, \n  "origin": "78.80.27.128", \n  "url": "https://httpbin.org/delay/1"\n}\n'", headers={'Date': 'Thu, 26 Mar 2020 09:31:27 GMT', 'Content-Type': 'application/json', 'Content-Length': '324', 'Connection': 'close', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}, msg="OK")
.
----------------------------------------------------------------------
Ran 1 test in 1.539s

OK
➜  shopify_rest pipenv run python test_client.py
Response(code=200, body="b'{\n  "args": {}, \n  "data": "", \n  "files": {}, \n  "form": {}, \n  "headers": {\n    "Accept-Encoding": "identity", \n    "Host": "httpbin.org", \n    "User-Agent": "Python-urllib/3.7", \n    "X-Amzn-Trace-Id": "Root=1-5e7c767f-83adab5157e050239ff53904"\n  }, \n  "origin": "78.80.27.128", \n  "url": "https://httpbin.org/delay/5"\n}\n'", headers={'Date': 'Thu, 26 Mar 2020 09:31:48 GMT', 'Content-Type': 'application/json', 'Content-Length': '324', 'Connection': 'close', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}, msg="OK")
.
----------------------------------------------------------------------
Ran 1 test in 5.548s

OK
```