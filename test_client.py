import unittest
from pyactiveresource.connection import Connection

# https://github.com/Shopify/pyactiveresource/blob/master/pyactiveresource/connection.py#L304
class ClientTest(unittest.TestCase):

    def test_success(self):
        connection = Connection("https://httpbin.org")
        response = connection.get("/delay/5")
        print(response)

if __name__ == "__main__":
    unittest.main()
