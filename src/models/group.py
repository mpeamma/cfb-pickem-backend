from dataclasses import dataclass
from typing import List
from dataclasses_json import DataClassJsonMixin, dataclass_json

@dataclass_json
@dataclass
class Group(DataClassJsonMixin):
    id: str
    name: str
    user_ids: List[str]
