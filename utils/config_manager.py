import json
import os
from dotenv import load_dotenv

load_dotenv()


class ConfigManager:

    def __init__(self, env):
        with open("config/config.json") as f:
            config = json.load(f)

        env_config = config[env]

        self.base_url = env_config["base_url"]
        self.ui_url = env_config["ui_url"]

        self.db_config = {
            "host": os.getenv(env_config["db"]["host"]),
            "database": os.getenv(env_config["db"]["database"]),
            "user": os.getenv(env_config["db"]["user"]),
            "password": os.getenv(env_config["db"]["password"]),
        }

    def get_base_url(self):
        return self.base_url

    def get_ui_url(self):
        return self.ui_url

    def get_db_config(self):
        return self.db_config