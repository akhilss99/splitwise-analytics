import duckdb
import pandas as pd

from src.main.com.splitwise.util.DataUtil import DataUtil
from src.main.com.splitwise.util.DateUtil import DateUtil


class AnalyticsPipeline:
    def __init__(self, conf: dict, data_util: DataUtil):
        self.conf = conf
        self.data_util = data_util

    def execute(self):
        expenses = self.data_util.get_expenses(int(self.conf.get("GROUP_ID")))
        data = pd.DataFrame([expense.__dict__ for expense in expenses])
        required_data = data[["id", "description", "cost", "date"]]
        required_data['month'] = required_data.apply(lambda x: DateUtil.extract_month(x['date']), axis=1)
        instamart = duckdb.query("select * from required_data where description ilike '%instamart%'")
        swiggy = duckdb.query(
            "select * from required_data where description not ilike '%instamart%' and description ilike '%swiggy%'")
        supermarket = duckdb.query("select * from required_data where description ilike '%supermarket%'")
        bigbasket = duckdb.query(
            "select * from required_data where description ilike '%big%' or description ilike '%basket%'")
        query = """
        with data as 
        (
        select id, month, 'instamart' as description, cast(cost as float) as cost from instamart
        union all
        select id, month, 'swiggy' as description, cast(cost as float) as cost from swiggy
        union all
        select id, month, 'supermarket' as description, cast(cost as float) as cost from supermarket
        union all
        select id, month, 'big basket' as description, cast(cost as float) as cost from bigbasket
        )
    
        select 
        month,
        sum(case when description='instamart' then cost end) as 'Instamart',
        count(case when description='instamart' then id end) as 'Count',
        sum(case when description='swiggy' then cost end) as 'Swiggy',
        count(case when description='swiggy' then id end) as 'Count',
        sum(case when description='supermarket' then cost end) as 'Supermarket',
        count(case when description='supermarket' then id end) as 'Count',
        sum(case when description='big basket' then cost end) as 'Big Basket',
        count(case when description='big basket' then id end) as 'Count',
        sum(cost) as 'Total'
        from data
        group by month
     """
        duckdb.query(query).show()
