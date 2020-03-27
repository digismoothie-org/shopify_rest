import unittest
from pyactiveresource.connection import Connection
import shopify
from concurrent.futures import ProcessPoolExecutor

import django_toolbox.shopify_limits_patch

def get_shop(item):
    print(item)
    session = shopify.Session(".myshopify.com", "2020-01", "TOKEN")
    shopify.ShopifyResource.activate_session(session)
    return shopify.Shop.current()

class ClientTest(unittest.TestCase):

    def test_httpbin(self):
        connection = Connection("https://httpbin.org")
        response = connection.get("/delay/5")
        print(response)

    def test_shopify_rate_limit(self):
        """
        Hit Shopify rate limiting by requesting shop resource 50 times in batches of 10 requests at once.
        """
        pool = ProcessPoolExecutor(max_workers=10)
        print(list(pool.map(get_shop, range(50))))


if __name__ == "__main__":
    unittest.main()
