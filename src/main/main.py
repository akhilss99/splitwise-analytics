import duckdb
import functions_framework
from splitwise import Splitwise

from com.splitwise.pipeline.AnalyticsPipeline import AnalyticsPipeline
from src.main import CONSUMER_KEY, CONSUMER_SECRET, API_KEY, CONFIGS, QUERIES, LOGGER
from src.main.com.splitwise.ingestion.SplitwiseExtraction import SplitwiseExtractUtil
from src.main.com.splitwise.warehouse.BigQueryClient import BigQueryLoader

SPLITWISE_CONFIG = CONFIGS.get("splitwise", {})
BIGQUERY_CONFIG = CONFIGS.get("bigquery", {})

if __name__ == '__main__':
    @functions_framework.http
    def main(request):
        splitwise = Splitwise(consumer_key=CONSUMER_KEY,
                              consumer_secret=CONSUMER_SECRET,
                              api_key=API_KEY)
        ingestion_util = SplitwiseExtractUtil(splitwise, SPLITWISE_CONFIG)

        loader = BigQueryLoader(BIGQUERY_CONFIG)

        conn = duckdb.connect()

        pipeline = AnalyticsPipeline(db_connection=conn,
                                     extraction_util=ingestion_util,
                                     bq_loader=loader)
        result = pipeline.execute(query_dict=QUERIES)
        LOGGER.info(result)
        return result
