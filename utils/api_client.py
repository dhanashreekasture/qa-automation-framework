import requests
import time
from utils.retry import retry
from utils.logger import Logger

class APIClient:

    @staticmethod
    @retry
    def request(method, url, payload=None):
        start = time.time()

        res = requests.request(method, url, json=payload, timeout=5)

        duration = (time.time() - start) * 1000
        Logger.info(f"{method} {url} took {duration:.2f} ms")

        assert duration < 3000, "API too slow"

        return res