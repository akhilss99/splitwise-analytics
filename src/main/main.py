import duckdb

from com.splitwise.pipeline.AnalyticsPipeline import AnalyticsPipeline
from com.splitwise.util.DataUtil import DataUtil
from com.splitwise.util.ConfigUtil import ConfigUtil

if __name__ == '__main__':

    conf = ConfigUtil.get_conf("splitwise-credentials.env")
    data_util = DataUtil(conf)

    queries = ConfigUtil.get_queries("queries.yaml")

    conn = duckdb.connect()

    pipeline = AnalyticsPipeline(conn, conf, data_util)
    pipeline.execute(query_dict=queries)
