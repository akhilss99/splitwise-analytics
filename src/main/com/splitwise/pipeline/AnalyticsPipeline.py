import duckdb
import pandas as pd

from src.main.com.splitwise.util.DataUtil import DataUtil
from src.main.com.splitwise.util.DateUtil import DateUtil


class AnalyticsPipeline:
    def __init__(self, conf: dict, data_util: DataUtil):
        self.conf = conf
        self.data_util = data_util

    def execute(self, query_dict: dict):
        expenses = self.data_util.get_expenses(int(self.conf.get("GROUP_ID")))
        data = pd.DataFrame([expense.__dict__ for expense in expenses])
        required_data = data[["id", "description", "cost", "date"]]
        required_data['month'] = required_data.apply(lambda x: DateUtil.extract_month(x['date']), axis=1)
        duckdb.query(query_dict['instamart']).to_view("instamart")
        duckdb.query(query_dict['swiggy']).to_view("swiggy")
        duckdb.query(query_dict['supermarket']).to_view("supermarket")
        duckdb.query(query_dict['bigbasket']).to_view("bigbasket")
        print(duckdb.query(query_dict['aggregation']).explain())