import duckdb
import pandas as pd

from src.main.com.splitwise.util.DataUtil import DataUtil


class AnalyticsPipeline:
    def __init__(self, conn: duckdb.DuckDBPyConnection, conf: dict, data_util: DataUtil):
        self.conn = conn
        self.conf = conf
        self.data_util = data_util

    def __extract_expenses(self) -> pd.DataFrame:
        expenses_list = map(lambda x: x.__dict__, self.data_util.get_expenses(int(self.conf.get("GROUP_ID"))))
        return pd.DataFrame(expenses_list)

    def __preprocess_expenses(self, expenses: pd.DataFrame) -> pd.DataFrame:
        expenses = expenses[["id", "description", "cost", "date"]]
        expenses['cost'] = pd.to_numeric(expenses['cost'], downcast='signed')
        expenses['date'] = pd.to_datetime(expenses['date'], format='%Y-%m-%dT%H:%M:%SZ')
        expenses['month'] = expenses['date'].dt.strftime('%m/%Y')
        return expenses

    def execute(self, query_dict: dict):
        expenses = self.__extract_expenses()
        expenses = self.__preprocess_expenses(expenses)
        self.conn.register("expenses", expenses)
        self.conn.query(query_dict['instamart']).to_view("instamart")
        self.conn.query(query_dict['swiggy']).to_view("swiggy")
        self.conn.query(query_dict['supermarket']).to_view("supermarket")
        self.conn.query(query_dict['bigbasket']).to_view("bigbasket")
        self.conn.query(query_dict['aggregation']).to_view("aggregation")
        self.conn.query(query_dict['pivot']).show()
        a = 0
