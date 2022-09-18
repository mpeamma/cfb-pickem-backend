from dataclasses import dataclass
from typing import List
from dataclasses_json import DataClassJsonMixin, dataclass_json

@dataclass_json
@dataclass
class GameSet(DataClassJsonMixin):
    id: int
    games: List[int]
    group_id: int
    year: int
    week: int
