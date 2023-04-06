import duckdb
import pandas as pd

from src.main.com.splitwise.util.DataUtil import DataUtil
from src.main.com.splitwise.ingestion.SplitwiseExtraction import SplitwiseExtractUtil
from src.main.com.splitwise.warehouse.BigQueryClient import BigQueryLoader


class AnalyticsPipeline:
    def __init__(self, db_connection: duckdb.DuckDBPyConnection,
                 extraction_util: SplitwiseExtractUtil,
                 bq_loader: BigQueryLoader):
        self.conn = db_connection
        self.extraction_util = extraction_util
        self.loader = bq_loader

    def execute(self, query_dict: dict):
        self.conn.query("install httpfs; load httpfs;")
        # Extract & Pre-process
        expenses = DataUtil.extract_expenses(extraction_util=self.extraction_util)
        expenses = DataUtil.preprocess_expenses(expenses=expenses)
        # Transform
        result = self._transform(expenses, query_dict)
        # Load
        return self.loader.load_df_to_bq(result)

    def _transform(self, df: pd.DataFrame, query_dict: dict) -> pd.DataFrame:
        self.conn.register("expenses", df)
        self.conn.query(query_dict['instamart']).to_view("instamart")
        self.conn.query(query_dict['swiggy']).to_view("swiggy")
        self.conn.query(query_dict['supermarket']).to_view("supermarket")
        self.conn.query(query_dict['bigbasket']).to_view("bigbasket")
        result = self.conn.query(query_dict['result'])
        result.show()
        return result.df()
