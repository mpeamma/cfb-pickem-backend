from dataclasses import dataclass
from typing import Optional
from dataclasses_json import DataClassJsonMixin, dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Selection(DataClassJsonMixin):
    team: str
    game_id: int
    game_set_id: str
    user_id: Optional[str] = None
    id: Optional[int] = None
