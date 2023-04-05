from dotenv import load_dotenv
import os


class ConfigUtil:

    @staticmethod
    def get_conf(path: str):
        load_dotenv(path)
        return {
            "consumer_key": os.environ.get("consumer_key"),
            "consumer_secret": os.environ.get("consumer_secret"),
            "api_key": os.environ.get("api_key"),
            "GROUP_ID": os.environ.get("GROUP_ID")
        }
