from dataclasses import dataclass
from typing import List, Optional
from dataclasses_json import DataClassJsonMixin, dataclass_json

@dataclass_json
@dataclass
class GameSet(DataClassJsonMixin):
    games: List[int]
    group_id: str
    year: int
    week: int
    id: Optional[int] = None
