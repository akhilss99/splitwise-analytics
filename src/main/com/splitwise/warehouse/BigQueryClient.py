import pandas as pd
from google.cloud import bigquery

from src.main.com.splitwise.exceptions import TableIdNotFoundError


class BigQueryLoader:
    conf: dict
    client: bigquery.Client
    job_config: bigquery.LoadJobConfig

    def __init__(self, conf: dict):
        self.conf = conf
        self.client = bigquery.Client()
        self.job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")

    def load_df_to_bq(self, df: pd.DataFrame, table_id: str = None) -> bigquery.LoadJob:
        table_id = self.__validate_table_id(table_id)
        job = self.client.load_table_from_dataframe(df, table_id, job_config=self.job_config)
        return job.result()

    def __validate_table_id(self, table_id: str):
        configured_table_id = self.conf.get('TABLE_ID', None)
        if configured_table_id is None and table_id is not None:
            return table_id
        elif configured_table_id is not None:
            return configured_table_id
        else:
            raise TableIdNotFoundError("Table Id for loading the table onto BigQuery not found.")
