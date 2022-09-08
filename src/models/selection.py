from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin, dataclass_json, Undefined

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class Selection(DataClassJsonMixin):
    id: int
    team: str
    game_id: int
    game_set_id: int
    user_id: str
