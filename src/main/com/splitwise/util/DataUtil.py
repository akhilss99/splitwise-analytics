import pandas as pd

from src.main.com.splitwise.ingestion.SplitwiseExtraction import SplitwiseExtractUtil


class DataUtil:

    @staticmethod
    def write_as_csv(df: pd.DataFrame, path: str, sep: str):
        df.to_csv(path, sep=sep, index=False)

    @staticmethod
    def extract_expenses(extraction_util: SplitwiseExtractUtil) -> pd.DataFrame:
        expenses_list = map(lambda x: x.__dict__, extraction_util.get_expenses())
        return pd.DataFrame(expenses_list)

    @staticmethod
    def preprocess_expenses(expenses: pd.DataFrame) -> pd.DataFrame:
        expenses = expenses[["id", "description", "cost", "date"]].copy()
        expenses['cost'] = pd.to_numeric(expenses['cost'], downcast='signed')
        expenses['date'] = pd.to_datetime(expenses['date'], format='%Y-%m-%dT%H:%M:%SZ')
        expenses['pk'] = expenses['date'].dt.strftime('%B, %Y')
        expenses['month'] = expenses['date'].dt.strftime('%m')
        expenses['year'] = expenses['date'].dt.strftime('%Y')
        return expenses
