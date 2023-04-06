import os

from src.main.com.splitwise.util.ConfigLoad import ConfigUtil

CONSUMER_KEY = os.environ['SPLITWISE.CONSUMER_KEY']
CONSUMER_SECRET = os.environ['SPLITWISE.CONSUMER_SECRET']
API_KEY = os.environ['SPLITWISE.API_KEY']

CONFIGS = ConfigUtil.load_json("config.json")
QUERIES = ConfigUtil.get_queries("queries.yaml")
