import psycopg2
from utils.logger import Logger


class DBClient:

    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        self.conn = psycopg2.connect(**self.config)
        Logger.info("DB Connected")

    def fetch_order(self, order_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM orders WHERE order_id=%s", (order_id,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def close(self):
        if self.conn:
            self.conn.close()