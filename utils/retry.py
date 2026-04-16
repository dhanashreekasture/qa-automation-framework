import time
from utils.logger import Logger


def retry(func, retries=3):
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            Logger.error(f"Retry {i + 1} failed: {e}")
            if i == retries - 1:
                raise
            time.sleep(1)
