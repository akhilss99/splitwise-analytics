import pandas as pd
from splitwise import Splitwise, Expense
from splitwise.group import Group


class DataUtil:
    __max_val = 1e1000

    def __init__(self, conf: dict):
        self.split_wise: Splitwise = Splitwise(consumer_key=conf.get("consumer_key"),
                                               consumer_secret=conf.get("consumer_secret"),
                                               api_key=conf.get("api_key"))

    def get_groups(self) -> list[Group]:
        return self.split_wise.getGroups()

    def get_group(self, group_id: int) -> Group:
        return self.split_wise.getGroup(group_id)

    def get_expenses(self, group_id: int) -> list[Expense]:
        return self.split_wise.getExpenses(group_id=group_id, limit=self.__max_val)

    @staticmethod
    def write_as_csv(df: pd.DataFrame, path: str, sep: str):
        df.to_csv(path, sep=sep, index=False)
