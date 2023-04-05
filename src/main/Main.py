from com.splitwise.pipeline.AnalyticsPipeline import AnalyticsPipeline
from com.splitwise.util.DataUtil import DataUtil
from com.splitwise.util.ConfigUtil import ConfigUtil

if __name__ == '__main__':
    path = "D:\Projects\splitwise-analytics\src\main\\resources\splitwise-credentials.env"

    conf = ConfigUtil.get_conf(path)
    data_util = DataUtil(conf)

    pipeline = AnalyticsPipeline(conf, data_util)
    pipeline.execute()
