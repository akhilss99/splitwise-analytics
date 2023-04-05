from datetime import datetime


class DateUtil:

    @staticmethod
    def extract_date(date_time: str):
        date_time_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%SZ')
        return date_time_obj.strftime('%Y-%m-%d')

    @staticmethod
    def extract_month(date_time: str):
        date_time_obj = datetime.strptime(date_time, '%Y-%m-%dT%H:%M:%SZ')
        return date_time_obj.strftime("%B, %Y")
