from typing import Any

from splitwise import Splitwise, Group, Expense

from src.main.com.splitwise.exceptions import GroupIdNotFoundError

MAX_LIMIT = 1e100000000000
GROUP_ID_KEY = 'GROUP_ID'
GROUP_ID_NOT_FOUND_ERR = 'Group Id is not provided.'


class SplitwiseExtractUtil:
    conf: dict[str, str]
    split_wise: Splitwise

    def __init__(self, split_wise: Splitwise, conf: dict[str, str]):
        self.split_wise = split_wise
        self.conf = conf

    def get_group(self, group_id: int = None) -> Group:
        group_id = self._validate(group_id, GROUP_ID_KEY, GroupIdNotFoundError(GROUP_ID_NOT_FOUND_ERR))
        return self.split_wise.getGroup(group_id)

    def get_expenses(self, group_id: int = None) -> list[Expense]:
        group_id = self._validate(group_id, GROUP_ID_KEY, GroupIdNotFoundError(GROUP_ID_NOT_FOUND_ERR))
        return self.split_wise.getExpenses(group_id=group_id, limit=MAX_LIMIT)

    def _validate(self, obj: Any, key: str, exception: Exception) -> Any:
        configured_obj = self.conf.get(key, None)
        if configured_obj is None and obj is not None:
            return obj
        elif configured_obj is not None:
            return configured_obj
        else:
            raise exception
